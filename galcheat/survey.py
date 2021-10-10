from dataclasses import dataclass, field, make_dataclass
from typing import Any, List, Optional

import astropy.units as u
import yaml
from astropy.units import Quantity

from galcheat.filter import Filter


@dataclass
class Survey:
    name: str
    filters: Any
    pixel_scale: Quantity
    effective_area: Quantity
    mirror_diameter: Quantity
    airmass: Optional[Quantity] = None
    zeropoint_airmass: Optional[Quantity] = None
    available_filters: List[str] = field(init=False)

    @classmethod
    def from_yaml(cls, yaml_file):
        """Constructor for the Survey class

        Parameters
        ----------
        yaml_file: pathlike
            Filepath to YAML file containing the survey info

        Returns
        -------
        The Survey object filled with the info

        """
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        filters = Survey._construct_filter_list(data)
        pixel_scale = data["pixel_scale"] * u.arcsec
        effective_area = data["effective_area"] * u.m ** 2
        mirror_diameter = data["mirror_diameter"] * u.m
        airmass = data.get("airmass")
        airmass = airmass if airmass is None else airmass * u.dimensionless_unscaled
        zeropoint_airmass = data.get("zeropoint_airmass")
        zeropoint_airmass = (
            zeropoint_airmass
            if zeropoint_airmass is None
            else zeropoint_airmass * u.dimensionless_unscaled
        )

        return cls(
            data["name"],
            filters,
            pixel_scale,
            effective_area,
            mirror_diameter,
            airmass,
            zeropoint_airmass,
        )

    @staticmethod
    def _construct_filter_list(survey_dict):
        """Create a custom container for the survey filters

        Parameters
        ----------
        survey_dict: dict
            Dictionnary of the survey parameters, including the definition of the filters

        Returns
        -------
        Dynamically created dataclass whose attributes are the survey filters

        """
        filter_data = {
            fname: Filter.from_dict(fdict)
            for fname, fdict in survey_dict["filters"].items()
        }
        FList = make_dataclass(
            survey_dict["name"] + "FilterList",
            [(filter_name, Filter) for filter_name in filter_data.keys()],
            namespace={
                "__repr__": lambda self: "("
                + ", ".join([filt for filt in self.__dict__.keys()])
                + ")"
            },
        )

        return FList(**filter_data)

    def __post_init__(self):
        self.available_filters = list(self.filters.__dict__.keys())

    def get_filters(self):
        """Getter method to retrieve the filters as a dictionary"""
        return self.filters.__dict__

    def get_filter(self, filter_name):
        """Getter method to retrieve a Filter object"""
        if filter_name not in self.available_filters:
            raise ValueError(
                "Please check the filter name. "
                f"The available filters for {self.name} "
                f"are {self.available_filters}"
            )

        return self.filters.__dict__[filter_name]
