#  config file looks like
#
#  temperature,humidity,,growth
#  10,20,,0.5
#  14,24,,0.9
#  25,24,,0.5
#  23,23,,40
#
#  ui:
#  features: list of numbers
#  predictors: list of numbers
#  how to enforce? 

from .common.is_valid_map import is_valid_map

requirements = {
	'predictors': 'number',
	'features': 'number',
	'num_predictors_min': 1,
	'num_predictors_max': None,
	'num_features_min': 1,
	'num_features_max': 1,
}

def is_valid_data_map(data_map):
	return is_valid_map(data_map, requirements)

def get_requirements():
	return requirements

