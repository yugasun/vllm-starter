from os.path import abspath, dirname, join
from dynaconf import Dynaconf


current_dir = dirname(abspath(__file__))
config_path = join(current_dir, "../config.yaml")

settings = Dynaconf(
    envvar_prefix=False,
    merge_enabled=True,
    settings_files=[config_path],
)