`galcheat` supported parameters
===============================

The following page describes the parameters of the photometric surveys and their filters exposed in galcheat, what type and unit they should be specified with.

Survey parameters
-----------------

### Input parameters

The following parameters are required in the YAML file describing any survey to build the `Survey` class in `galcheat`.

| parameter name    |   type    |     units      | description                                                                                                                                                                                                                                                   |
| ----------------- | :-------: | :------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name              |    str    |       –        | The classical name or abbreviation for the survey. Most often this is how the survey is referred to. In case of an ambiguity, for instance when a survey has several instruments, the name of the instrument should be added as a suffix (e.g. `Euclid_VIS`). |
| description       |    str    |       –        | A bit of context around the survey: on which telescope, with which instrument, wide survey or a specific deep field.                                                                                                                                          |
| pixel_scale       |   float   | arcsec / pixel | Size of a square pixel on the sky.                                                                                                                                                                                                                            |
| gain              |   float   |   e^-^ / ADU   | Conversion factor between the photo-electrons received by the camera and the digital counts after the amplification of the electronics.                                                                                                                       |
| mirror_diameter   |   float   |       m        | Primary mirror diameter, in meters.                                                                                                                                                                                                                           |
| obscuration       |   float   | dimensionless  | Proportion of the total area of the telescope that is obscured by the position of secondary mirrors, lenses, camera, etc. This parameter is used to compute the effective area of the telescope.                                                              |
| zeropoint_airmass |   float   | dimensionless  | Airmass value at which the zeropoint is computed. The airmass is commonly defined as the optical path length through the atmosphere relative to the zenith path length. For space surveys, this value is set to 0.0.                                          |
| references        | dict[str] |       –        | **mandatory but can be left as an empty string –** Source of each parameter value (survey or filter), specified as a link (to an article or website) and a comment string. See the bottom [the dummy YAML file](#example) for layout.                         |

### Computed parameters

The following parameters are computed after initialisation of the `Survey` class, from the [mandatory info](#input-parameters).

| parameter name    |   type    | units | description                                                                                               |
| ----------------- | :-------: | :---: | --------------------------------------------------------------------------------------------------------- |
| available_filters | list[str] |   –   | List of available filter names for the survey.                                                            |
| effective area    |   float   | m^2^  | Actual area receiving light after taking into account the size of the primary mirror and the obscuration. |

Filter parameters
-----------------

The following parameters are required in the YAML file describing any filter of a given survey, to build the `Filter` class in `galcheat`.

| parameter name       |   type    |      units      | description                                                                                                                                                                                                                                                                                   |
| -------------------- | :-------: | :-------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                 |    str    |        –        | Name of the filter                                                                                                                                                                                                                                                                            |
| sky_brightness       |   float   | mag / arcsec^2^ | Average sky brightness computed for the survey and this filter. The moon conditions under which this number was computed will be given as a comment in the yaml file.                                                                                                                         |
| full_exposure_time   | int/float |        s        | Average exposure time of the filter on the same spot in the sky over the course of the survey.                                                                                                                                                                                                |
| psf_fwhm             |   float   |     arcsec      | Average full width at half-maximum (FWHM) of the point spread function (PSF) over the filter.                                                                                                                                                                                                 |
| zeropoint            |   float   |       mag       | The zeropoint value for most surveys is a reference magnitude computed as the magnitude in the AB system (see [this reference][abmag_ref]) collected on the instrument effective area in one second. It takes into account the filter bandwidth and a classical atmosphere for ground based surveys, using the [`speclite`][speclite] library, at the airmass given by the survey `zeropoint_airmass`. For the remaining surveys it is extracted from corresponding the references (see `references` parameter).                          |
| effective_wavelength |   float   |       nm        | **optional –** Wavelength computed as a weighted average of the full passband throughput over the wavelength range. The throughput takes into account the transmission of the filter, the transmittance of the optics, the CCD efficiency as well as a standard atmospheric extinction model. |

[speclite]: https://github.com/desihub/speclite
[abmag_ref]: https://speclite.readthedocs.io/en/stable/api.html#convolutions

YAML file layout
----------------

### Directives

The information for a given survey should be provided as an individual YAML file, with the following layout.

- survey information first
- list of filters below
- references last
- one parameter per line
- strings should be quoted with `" "`
- indentation (2 spaces) means sub-list
- comments (starts with `#`) are put on new lines

### Example

An toy example for a dummy survey called `Survey42` with two filters `a` and `b` is shown below.

```yaml
# Content of Survey42.yaml
name: "Survey42"
description: "The Survey42 was done on the XXX telescope with the YYY instrument"
pixel_scale: 0.2
gain: 2.0
mirror_diameter: 4.2
obscuration: 0.2
zeropoint_airmass: 1.2
filters:
  a:
    name: "a"
    sky_brightness: 19.4
    full_exposure_time: 500
    zeropoint: 26.90
    psf_fwhm: 1.1
    effective_wavelength: 500.00
  b:
    name: "b"
    sky_brightness: 18.6
    full_exposure_time: 500
    zeropoint: 27.36
    psf_fwhm: 1.2
    effective_wavelength: 600.00
references:
  pixel_scale:
    link: "https://link-to-the-pixelscale-ref.com"
    comment: "See section 2.4"
  gain:
    link: "https://link-to-the-gain-info.org"
    comment: ""
  psf_fwhm:
    link: "https://link-to-filters-refs.org"
    comment: ""
# goal is to have a reference per parameter, survey or filter-wise...
```
