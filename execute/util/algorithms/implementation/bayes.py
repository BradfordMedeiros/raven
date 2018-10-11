from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing

def get_label_encoder(predictors, feature_values):
	all_labels = set()

	for sample in predictors:
		for label in sample:
			all_labels.add(label)
	for sample in feature_values:
		for label in sample:
			all_labels.add(label)
	
	all_labels_as_list = list(all_labels)

	encoder = preprocessing.LabelEncoder()
	encoder.fit(all_labels_as_list)
	return encoder

def encode_predictors(encoder, predictors):
	pass

def encode_feature_values(encoder, feature_values):
	pass 

class bayes():
	def __init__(self, labels, predictors, feature_labels, feature_values ):
		classifier = DecisionTreeClassifier(random_state=0)

		print labels
		print feature_labels
		self.labels = labels
		self.predictors = predictors
		self.feature_labels = feature_labels
		self.feature_values = feature_values
		self.classifier = classifier

		encoder = get_label_encoder(predictors, feature_values)
		values = encoder.transform(["doctor", "doctor","male"]) 

		encoded_predictors = encode_predictors(encoder, predictors)
		encoded_feature_values = encode_feature_values(encoder, feature_values)

		print 'encoded values: ', values
		decoded_values = encoder.inverse_transform(values)
		print 'decoded values: ', decoded_values



	def predict(self, values):
		return None