`galcheat` data files
=====================

The following document describes the parameters expected for the photometric surveys and their filters: how they should be computed, their units, etc.

Survey parameters
-----------------
### Units and types

| parameter name    | type  | units          |
| ----------------- | ----- | -------------- |
| name              | str   | –              |
| pixel_scale       | float | arcsec / pixel |
| gain              | float | e- / ADU       |
| mirror_diameter   | float | m         |
| obscuration       | float | dimensionless  |
| zeropoint_airmass | float | dimensionless  |

### Description

#### `name`

The classical name or abbreviation for the survey. Most often this is how the survey is referred to.
In case of an ambiguity, for instance when a survey has several instruments, the name of the instrument should be added as a suffix (e.g. `Euclid_VIS`).

#### `pixel_scale`

Size of a square pixel on the sky.

#### `gain`

Conversion factor between the photo-electrons received by the camera and the digital counts after the amplification of the electronics.

#### `mirror_diameter`

Primary mirror diameter, in meters.

#### `obscuration`

Proportion of the total area of the telescope that is obscured by the position of secondary mirrors, lenses, camera, etc.

This parameter is used to compute the effective area of the telescope.

#### `zeropoint_airmass`

Airmass value at which the zeropoint is computed.

Filter parameters
-----------------
### Units and types

| parameter name | type      | units          |
| -------------- | --------- | -------------- |
| name           | str       | –              |
| sky_brightness | float     | mag / arcsec^2 |
| exp_time       | int/float | s              |
| psf_fwhm       | float     | arcsec         |
| zeropoint      | float     | e- / s         |

### Description
#### `name`

Name of the filter

#### `sky_brightness`

Average sky brightness computed for the survey and this filter.

#### `exp_time`

Average exposure time of the filter on the same spot in the sky over the course of the survey.

#### `psf_fwhm`

Average full width at half-maximum (FWHM) of the point spread function (PSF) over the filter.

This parameter is traditionally computed with the [`speclite`][speclite] library.

#### `zeropoint`

Zero point magnitude for the filter, computed using the [`speclite`][speclite] library with a classical atmosphere, at the airmass indicated in the survey parameters: `zeropoint_airmass`


[speclite]: https://github.com/desihub/speclite

YAML file layout
----------------

The information for a given survey should be written in an individual YAML file, with a specific layout.

The survey information should appear first, with one parameter per line.

After these parameters, the list of filters should appear. YAML uses new lines and indentation to create lists.

An example for a survey called `Survey42` with two filters `a` and `b` is shown below.

```yaml
# Content of Survey42.yaml
name: Survey42
pixel_scale: 0.2
gain: 2.0
mirror_diameter: 4.2
obscuration: 0.2
zeropoint_airmass: 1.2
filters:
  a:
    name: "a"
    sky_brightness: 19.4
    exp_time: 500
    psf_fwhm: 1.1
    zeropoint: 26.90
  b:
    name: "b"
    sky_brightness: 18.6
    exp_time: 500
    psf_fwhm: 1.2
    zeropoint: 27.36
```
