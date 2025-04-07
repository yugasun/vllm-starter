from os.path import abspath, dirname, join
from yaml import load, Loader
from types import SimpleNamespace

current_dir = dirname(abspath(__file__))
config_path = join(current_dir, "../config.yaml")

# Load settings as a dictionary first
settings_dict = load(open(config_path, "r"), Loader=Loader)


# Convert dictionary to object with attribute access
def dict_to_namespace(d):
    if isinstance(d, dict):
        # Create a copy of the original dict to preserve it
        original_dict = d.copy()
        for key, value in d.items():
            d[key] = dict_to_namespace(value)
        ns = SimpleNamespace(**d)
        # Add dictionary-like methods
        ns.get = lambda key, default=None: getattr(ns, key, default)
        ns.items = lambda: original_dict.items()
        return ns
    elif isinstance(d, list):
        return [dict_to_namespace(item) for item in d]
    else:
        return d


# Convert the settings dictionary to a namespace object
settings = dict_to_namespace(settings_dict)

# Now you can use dot notation
print(settings.model)
