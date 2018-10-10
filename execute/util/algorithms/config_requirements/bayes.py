#  config file looks like
#
# person,gender,,feeling
# doctor,male,,happy
# doctor,female,,happy
# engineer,male,,sad
# dentist,male,,sad
#
#  ui:
#  features: list of numbers
#  predictors: list of numbers
#  how to enforce? 

requirements = {
	'features': 'string',
	'predictors': 'string',
	'num_features_min': 1,
	'num_features_max': None,
	'num_predictors_min': 1,
	'num_predictors_max': 1
}

def is_valid_data_map(data_map):
	num_features = 0
	num_predictors = 0

	if requirements['num_features_max'] != None and num_features > requirements['num_features_max']:
		return False
	if requirements['num_features_min'] != None and num_features < requirements['num_features_min']:
		return False

	if requirements['num_predictors_max'] != None and num_predictors > requirements['num_predictors_max']:
		return False
	if requirements['num_predictors_min'] != None and num_predictors < requirements['num_predictors_min']:
		return False

	return True

"""
{
	   person: {
		  predictor: False,
		  values: ['doctor','doctor','engineer', 'dentist']
	   },
	   gender: {
		  predictor: False,
		  values: ['male','female','male','male']
	   },
	   feeling: {
		  predictor: True,
		  values: ['happy','happy','sad','sad']
	   }
	}
"""

