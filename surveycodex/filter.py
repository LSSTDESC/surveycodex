from dataclasses import dataclass
from typing import Optional

import astropy.units as u
from astropy.units import Quantity


@dataclass(frozen=True)
class Filter:
    """A dataclass containing the main filter parameters"""

    name: str
    "The filter name"
    psf_fwhm: Quantity
    "The full-width at half maximum of the PSF"
    zeropoint: Quantity
    "The zeropoint magnitude computed with the speclite library"
    sky_brightness: Quantity
    "Mean sky brightness"
    full_exposure_time: Quantity
    "Mean time spent on the sky on a random survey location"
    effective_wavelength: Optional[Quantity] = None
    "Filter effective wavelength computed from the complete throughput information"

    @classmethod
    def from_dict(cls, filter_info):
        """Constructor for the Filter dataclass

        Makes sure each of the filter attributes gets the appropriate units
        to improve definition and avoid confusion and conversion issues.

        Parameters
        ----------
        filter_info: dict
            Dictionary with the filter informations

        Returns
        -------
        Filter
            A Filter object filled with the given information

        """
        name = filter_info["name"]
        psf_fwhm = filter_info["psf_fwhm"] * u.arcsec
        zeropoint = filter_info["zeropoint"] * u.mag
        sky_brightness = filter_info["sky_brightness"] * (u.mag / u.arcsec**2)
        full_exposure_time = filter_info["full_exposure_time"] * u.s
        wavelength = filter_info.get("effective_wavelength")
        wavelength = wavelength if wavelength is None else wavelength * u.nm

        return cls(
            name,
            psf_fwhm,
            zeropoint,
            sky_brightness,
            full_exposure_time,
            wavelength,
        )

    def __str__(self):
        filter_repr = f"-= {self.name} filter =-\n"
        printed_params = [
            f"  {key:<20} = {val}"
            for key, val in self.__dict__.items()
            if key not in ("name",)
        ]
        filter_repr += "\n".join(printed_params)
        return filter_repr

    def __repr__(self):
        return f"Filter {self.name}"
