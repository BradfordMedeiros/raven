import numpy
from util.algorithms.implementation.bayes import bayes

def execute_bayes(data_map, query, data_map_manipulation):
	labels = data_map['labels']
	predictors = data_map['is_predictor']
	values = numpy.array(data_map['values'])

	predictors_v = filter(lambda (x,y): predictors[x], enumerate(labels))
	features_v = filter(lambda (x,y): not predictors[x], enumerate(labels))
	predictor_labels = [x[1] for x in predictors_v]
	feature_labels = [x[1] for x in features_v]
	predictor_length = len(predictor_labels)
	predictor_values = values[:, 0: predictor_length]
	features_values = values[:, predictor_length:]

	"""print 'predictor_labels'
	print predictor_labels
	print
	print 'feature labels'
	print feature_labels

	print
	print 'predictor values'
	print predictor_values

	print 
	print 'features values'
	print features_values
	"""
	model = bayes(predictor_labels, predictor_values, feature_labels, features_values)
	
	prediction =  model.predict(query)
	return prediction


