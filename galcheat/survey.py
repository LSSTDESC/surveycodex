import math
from dataclasses import dataclass, field
from typing import Dict, List

import astropy.units as u
import yaml
from astropy.units import Quantity

from galcheat.filter import Filter


@dataclass(frozen=True)
class Survey:
    """A dataclass for storing the parameters of a survey"""

    name: str
    "The survey name"
    description: str
    "The survey description with telescope/instrument information"
    _filters: Dict[str, Filter]
    "A private dictionary containing the survey filters"
    pixel_scale: Quantity
    "The pixel scale of the survey"
    mirror_diameter: Quantity
    "The mirror diameter"
    gain: Quantity
    "The gain in electron/ADU"
    obscuration: Quantity
    "The total obscuration created by the instrument pieces"
    zeropoint_airmass: Quantity
    "The zeropoint airmass"
    available_filters: List[str] = field(init=False)
    "The list of survey filters"
    effective_area: Quantity = field(init=False)
    "The survey instrument effective area on the sky computed from the obscuration"
    references: Dict[str, Dict[str, str]]
    "Dictionary of references for each parameter specified in galcheat"

    @classmethod
    def from_yaml(cls, yaml_file: str):
        """Constructor for the Survey class

        Parameters
        ----------
        yaml_file: pathlike
            Filepath to YAML file containing the survey info

        Returns
        -------
        Survey
            A `Survey` instance filled with the information as attributes

        """
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        filters = Survey._construct_filter_dict(data)
        pixel_scale = data["pixel_scale"] * u.arcsec
        mirror_diameter = data["mirror_diameter"] * u.m
        gain = data["gain"] * u.electron / u.adu
        obscuration = data["obscuration"] * u.dimensionless_unscaled
        zeropoint_airmass = data["zeropoint_airmass"] * u.dimensionless_unscaled

        return cls(
            data["name"],
            data["description"],
            filters,
            pixel_scale,
            mirror_diameter,
            gain,
            obscuration,
            zeropoint_airmass,
            data["references"],
        )

    def __str__(self):
        n = len(self.name)
        survey_repr = "-" * (n + 4) + "\n"
        survey_repr += f"| {self.name} |"
        survey_repr += f" {self.description}\n"
        survey_repr += "-" * (n + 4) + "\n"
        printed_params = [
            f"  {key:<20} = {val}"
            for key, val in self.__dict__.items()
            if key not in ("name", "description", "_filters", "references")
        ]
        survey_repr += "\n".join(printed_params)
        return survey_repr

    def __repr__(self):
        return f"Survey {self.name}"

    @staticmethod
    def _construct_filter_dict(survey_dict):
        """Create a custom dictionary for the survey filters

        Parameters
        ----------
        survey_dict: dict
            Dictionnary of the survey parameters, including the definition of the filters

        Returns
        -------
        dict
            Dictionary of the survey Filter instances

        """
        return {
            fname: Filter.from_dict(fdict)
            for fname, fdict in survey_dict["filters"].items()
        }

    def __post_init__(self):
        """Set attributes computed after class is constructed"""
        available_filters = list(self._filters.keys())
        object.__setattr__(self, "available_filters", available_filters)

        total_area = math.pi * (self.mirror_diameter * 0.5) ** 2
        effective_area = total_area * (1 - self.obscuration)
        object.__setattr__(self, "effective_area", effective_area)

    def get_filter(self, filter_name):
        """Getter method to retrieve a Filter object

        Parameters
        ----------
        filter_name : str
            Name of a filter chosen among the `available_filters` attribute

        Returns
        -------
        Filter
            Corresponding `Filter` dataclass

        Raises
        ------
        ValueError
            The requested filter does not exist or is not available in galcheat

        """
        if filter_name not in self.available_filters:
            raise ValueError(
                "Please check the filter name. "
                f"The available filters for {self.name} "
                f"are {self.available_filters}"
            )

        return self._filters[filter_name]
