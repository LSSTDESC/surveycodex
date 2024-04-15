import textwrap

from galcheat.helpers import Survey, get_survey

_SATELLITE = "🛰️️ "
_TELESCOPE = "🔭️ "


def _rich_survey_name(survey):
    if survey.name in ["Euclid_VIS", "COSMOS"]:
        icon = _SATELLITE
    else:
        icon = _TELESCOPE

    return f"{icon} [b]{survey.name}[/b]"


def display_survey(survey):
    from rich.console import Group
    from rich.panel import Panel
    from rich.text import Text

    if not isinstance(survey, Survey):
        survey = get_survey(survey)

    survey_desc = Text(
        textwrap.fill(survey.description, 40), no_wrap=False, justify="left"
    )

    survey_info = _survey_table(survey)

    filters_info = [
        _filter_panel(survey.get_filter(filter)) for filter in survey.available_filters
    ]

    display_info = [
        survey_desc,
        "\n",
        survey_info,
        "\n",
        "[b]Filter info:",
    ] + filters_info

    return Panel(
        Group(*display_info),
        padding=1,
        expand=False,
        title=_rich_survey_name(survey),
        title_align="center",
    )


def _survey_table(survey):
    from rich.table import Table

    survey_info = Table.grid()
    survey_info.add_column(justify="left")
    survey_info.add_column(justify="left")

    survey_info.add_row("Pixel scale: ", f"{survey.pixel_scale:.3f}")
    survey_info.add_row("Mirror diameter: ", f"{survey.mirror_diameter:.2f}")
    survey_info.add_row("Effective area: ", f"{survey.effective_area:.2f}")
    survey_info.add_row("Obscuration: ", f"{survey.obscuration:.2f}")
    survey_info.add_row("Gain: ", f"{survey.gain:.2f}")
    survey_info.add_row("Zeropoint airmass: ", f"{survey.zeropoint_airmass:.1f}")
    survey_info.add_row("Available filters: ", ", ".join(survey.available_filters))

    return survey_info


def _filter_panel(filter):
    from rich.panel import Panel
    from rich.table import Table

    filter_info = Table.grid()
    filter_info.add_column(justify="left")
    filter_info.add_column(justify="left")

    filter_info.add_row("PSF FWHM: ", f"{filter.psf_fwhm:.2f}")
    filter_info.add_row("Zeropoint: ", f"{filter.zeropoint:.2f}")
    filter_info.add_row("Sky brightness: ", f"{filter.sky_brightness:.2f}")
    filter_info.add_row("Full exposure time: ", f"{filter.full_exposure_time:0.0f}")
    filter_info.add_row("Effective wavelength: ", f"{filter.effective_wavelength:.1f}")

    return Panel(
        filter_info,
        padding=0,
        expand=False,
        title=f"[b]{filter.name}[/]",
        title_align="left",
    )


def display_references(survey):
    from rich.box import HEAVY_HEAD
    from rich.table import Table

    if not isinstance(survey, Survey):
        survey = get_survey(survey)

    ref_table = Table(
        "Parameter",
        "Source",
        "Comments",
        title=f"[b]{survey.name} references[/]",
        # show_lines=True,
        box=HEAVY_HEAD,
    )
    for name, param in survey.references.items():
        link = param["link"]
        source = f"[u cyan link={link}]{link}"
        comment = textwrap.fill(param["comment"], 60)
        ref_table.add_row(name, source, comment)

    return ref_table
