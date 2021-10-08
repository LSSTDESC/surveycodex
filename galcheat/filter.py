from dataclasses import dataclass
from typing import Optional

import astropy.units as u
from astropy.units import Quantity


@dataclass
class Filter:
    name: str
    psf_fwhm: Quantity
    zeropoint: Quantity
    extinction: Quantity
    sky_brightness: Quantity
    exposure_time: Quantity
    central_wavelength: Optional[Quantity] = None

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
        A Filter object filled with the given information

        """
        name = filter_info["name"]
        psf_fwhm = filter_info["psf_fwhm"] * u.arcsec
        zeropoint = filter_info["zeropoint"] * u.mag
        extinction = filter_info["extinction"] * u.dimensionless_unscaled
        sky_brightness = filter_info["sky_brightness"] * (u.mag / u.arcsec ** 2)
        exposure_time = filter_info["exp_time"] * u.s
        wavelength = filter_info.get("central_wavelength")
        wavelength = wavelength if wavelength is None else wavelength * u.nm

        return cls(
            name,
            psf_fwhm,
            zeropoint,
            extinction,
            sky_brightness,
            exposure_time,
            wavelength,
        )
