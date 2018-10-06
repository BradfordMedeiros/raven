from sklearn.neighbors import NearestNeighbors

#	knearest algorithm
#	we get the k-nearest neighbors, and then we average the k-nearest nodes

class knearest():
	def __init__(self, labels = None, predictors=None, configData=None):
		if not (len(configData[0]) == len(predictors[0])):
			raise Exception("labels and config data sample must be same length")
		self._train(labels, predictors, configData)

	def _train(self, labels, predictors, values):
		classifier = NearestNeighbors(n_neighbors=2)
		self.labels = labels
		self.predictors = predictors
		self.classifier = classifier.fit(predictors, values) 

	def predict(self, values):
		nodes = self.classifier.kneighbors(values)[1][0]
		values = [0 for x in self.predictors[0]]
		for node in nodes:
			for i in range(len(self.predictors[node])):
				node_value = self.predictors[node][i]
				values[i] = values[i] + node_value

		for i in range(len(values)):
			values[i] = values[i] / len(nodes)

		valueMap = {}
		for i in range(len(self.labels)):
			#values[self.labels[i]] = values[i]
			label = self.labels[i]
			valueMap[label] = values[i]

		return valueMap
	