#  config file looks like
#
#person,gender,,feeling
#doctor,male,,happy
#doctor,female,,happy
#engineer,male,,sad
#dentist,male,,sad
from .common.is_valid_map import is_valid_map

requirements = {
	'predictors': 'string',
	'features': 'string',
	'num_predictors_min': 1,
	'num_predictors_max': None,
	'num_features_min': 1,
	'num_features_max': 1,
}

def is_valid_data_map(data_map):
	return is_valid_map(data_map, requirements)

def get_requirements():
	return requirements

