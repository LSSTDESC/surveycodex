from pathlib import Path

from galcheat.survey import Survey


_BASEDIR = Path(__file__).parent.resolve()

survey_info = {
    path.stem: Survey.from_yaml(path)
    for path in _BASEDIR.glob("data/*.yaml")
}
