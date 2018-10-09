from sklearn.neighbors import NearestNeighbors

#	knearest algorithm
#	we get the k-nearest neighbors, and then we average the k-nearest nodes


class knearest():
	def __init__(self, labels, predictors, feature_labels, feature_values ):
		classifier = NearestNeighbors(n_neighbors=2)
		self.labels = labels
		self.predictors = predictors
		self.feature_labels = feature_labels
		self.feature_values = feature_values
		self.classifier = classifier.fit(predictors) 

	def _generate_map(self, values):
		if len(values) != len(self.labels):
			raise Exception('invalid sample size')
		arr = []
		for label in self.labels:
			value = values[label]
			arr.append(value)
		return [arr]

	def predict(self, values):
		nodes = self.classifier.kneighbors(self._generate_map(values))[1][0]
		matching_node_value = [self.feature_values[node] for node in nodes]
		prediction = { }
		for i in range(len(self.feature_labels)):
			value = map(lambda node: node[i], matching_node_value)
			prediction[self.feature_labels[i]] = sum(value) / len(value)  # using averaging function
		return prediction
	
#p = [[110,23],[34,43],[34,22]]
#labels = ['temp', 'humidity']
#feature_labels = ['somefeature']
#feature_values = [[30],[40],[20]]

#k = knearest(labels, p, feature_labels, feature_values)
#rr = k.predict({ 'temp': 20, 'humidity': 30 })  # want: { temp: 400, humidity: 50 }