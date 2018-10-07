requirements = {
	'features': 'string',
	'predictors': 'string',
	'num_features_min': 1,
	'num_features_max': None,
	'num_predictors_min': 1,
	'num_predictors_max': None,
}

def is_valid_data_map(data_map):
	pass

# usages:
# raven knearest -c somefield -n numberfork
#
#
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