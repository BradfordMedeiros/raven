
def is_valid_map(data_map, requirements):
	num_predictors = len([predictor for predictor in data_map['is_predictor'] if predictor == True])
	num_features = len([predictor for predictor in data_map['is_predictor'] if predictor == False])
	if requirements['num_features_max'] != None and num_features > requirements['num_features_max']:
		return False
	if requirements['num_features_min'] != None and num_features < requirements['num_features_min']:
		print('1')

		return False
	if requirements['num_predictors_max'] != None and num_predictors > requirements['num_predictors_max']:
		return False
	if requirements['num_predictors_min'] != None and num_predictors < requirements['num_predictors_min']:
		return False

	return True