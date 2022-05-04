# Create Simple Galaxy with Galcheat

In this tutorial, we will see how we can use the survey parameters in galcheat
to create a simple galsim elliptical galaxy. Our galaxy will be convolved with
a optical+atmospheric component PSF, include background and noise, and use
the r-band filter of the LSST survey.

```python
import galsim
from galcheat import available_surveys
from galcheat import get_survey, get_filter
from galcheat.utilites import mag2counts, mean_sky_level

LSST = get_survey("LSST")
r_band = get_filter("r", "LSST")

# galaxy model parameters
mag = 19.0 # ab
e1 = 0.2
e2 = 0.2
hlr = 1.2 # arcsecs

# get flux from magnitude using galcheat for LSST r-band
total_flux = mag2counts(mag, LSST, r_band)

# get only value of flux in specific units.
total_flux = total_flux.to_value('electron')

# simple gaussian galaxy with ellipticity.
gal = galsim.Gaussian(flux=total_flux, half_light_radius=hlr)
gal = gal.shear(e1=e1, e2=e2)

# create psf
# get atmospheric component.
fwhm = r_band.psf_fwhm.to_value("arcsec")
atmospheric_psf_model = galsim.Kolmogorov(fwhm=fwhm)

# get optical component.
effective_wavelength = r_band.effective_wavelength.to_value("angstrom")
obscuration = LSST.obscuration.value
mirror_diameter = LSST.mirror_diameter.to_value("m")
lam_over_diam = 3600 * np.degrees(1e-10 * effective_wavelength / mirror_diameter)
optical_psf_model = galsim.Airy(
    lam_over_diam=lam_over_diam, obscuration=obscuration
)

# convolve each component
psf = galsim.Convolve(atmospheric_psf_model, optical_psf_model)

# convolve with galaxy
conv_gal = galsim.Convolve(gal, psf)

# get mean sky level with galcheat for LSST r-band
sky_level = mean_sky_level(LSST, r_band)

# add noise and background to image
pixel_scale = LSST.pixel_scale.to_value('arcsec')
generator = galsim.random.BaseDeviate(seed=seedseq_blend.generate_state(1))
noise = galsim.PoissonNoise(rng=generator, sky_level=mean_sky_level)
image = galsim.Image(nx=53, ny=53, scale=pixel_scale)
image.addNoise(noise)

# image.array can now be plotted.
```
