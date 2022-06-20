import importlib
import sys

from slackbotr.constants.paths import SLACKBOTS_DIR


def import_slackbot_endpoints() -> None:
    slackbot_modules = SLACKBOTS_DIR.glob('*.py')

    for module_filepath in slackbot_modules:
        # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
        spec = importlib.util.spec_from_file_location('*', str(module_filepath))
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_filepath.stem] = module
        spec.loader.exec_module(module)
