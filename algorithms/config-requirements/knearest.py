requirements = {
	'features': 'number',
	'predictors': 'number',
	'num_features_min': 1,
	'num_features_max': None,
	'num_predictors_min': 1,
	'num_predictors_max': None,
}



"""
	{
	   temperature: {
		  predictor: False,
		  values: [30,30,100]
	   },
	   humidity: {
		  predictor: False,
		  values: [120,30,50]
	   },
	   growth: {
		  predictor: True,
		  values: [0.4, 1.2, 1.0]
	   }
	}
"""
#
#
#
#
#
def is_valid_data_map(data_map):
	num_features = 0
	num_predictors = 0

	if requirements['num_features_max'] != None and num_features > requirements['num_features_max']:
		return False
	if requirements['num_features_min'] != None and num_features < requirements['num_features_min']:
		return False

	if requirements['num_predictors_max'] != None and num_predictors > requirements['num_predictors_max']:
		return False
	if requirements['num_predictors_min'] != None and num_predictors < requirements['num_predictors_min']
		return False

	return True

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
