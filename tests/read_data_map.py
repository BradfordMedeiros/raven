from execute.util.config.read_data_map import read_data_map

def test_read_data_map():
	data_map = read_data_map('./data/knearest-sample.csv')
	expected = {
		'labels': ['temperature', 'humidity', 'goodness'],
		'is_predictor': [True,True,False],
		'values': [
			[50,20,0.5],
			[34,34,0.9],
			[32,324,0.9],
			[300,34,0.6],
			[400,30,0.98],
		],

	}
	assert(data_map['labels'] == expected['labels'])
	assert(data_map['is_predictor'] == expected['is_predictor'])
	assert(expected['values'] == data_map['values'])
