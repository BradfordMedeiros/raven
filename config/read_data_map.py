import csv 

"""
{
	
	labels: ['temperature', 'humidity', 'growth'],
	is_predictor: [False, False, True]
	values: [
		[10, 30,0.4],   # should be numpy array
		[20, 43,1.2],
		[30,12,1.4],
	]
}

"""


def verify_dimensions(data_map):
 	all_same_length = len(data_map['labels']) == len(data_map['is_predictor']) == len(data_map['values'])
 	if not all_same_length:
 		return False

 	for arr in data_map['values']:
 		if len(arr) != len(data_map['labels']):
 			return False
 	return True


def read_data_map(file):
	data_map = { 
		'labels': [ ],
		'is_predictor': [],
		'values': [],
	}

	num_empty_spaces = 0
	with open(file) as csvfile:
		reader = csv.reader(csvfile)
		labels = next(reader)

		for label in labels:
			if label == '' :
				num_empty_spaces = num_empty_spaces + 1
				if num_empty_spaces > 1:
					raise Exception('too many empty spaces')
				continue
			data_map['labels'].append(label)
			data_map['is_predictor'].append(num_empty_spaces == 0)
		
		while True:
			next_data = next(reader, None)
			if next_data == None:
				break

			values = []
			for value in next_data:
				if value == '':
					continue
				
				try:
					value_as_num = float(value)
					values.append(value_as_num)
				except:
					values.append(value)

			data_map['values'].append(values)

			print('next data: ', next_data)


	return data_map
