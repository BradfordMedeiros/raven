import csv 

def verify_dimensions(data_map):
 	label_length = None
	for label in data_map:
		length = len(data_map[label]['values'])
		if label_length == None:
			label_length = length
			continue
		if label_length != length:
			return False

	return True

def read_data_map(file):
	data_map = { }

	with open(file) as csvfile:
		reader = csv.reader(csvfile)
		labels = next(reader)

		num_empty_spaces = 0

		indexToLabel = {}
		for i in range(len(labels)):
			label = labels[i]
			if label == '' :
				num_empty_spaces = num_empty_spaces + 1
				if num_empty_spaces > 1:
					raise Exception('too many empty spaces')
				continue

			indexToLabel[i] = label
			data_map[label] = {
				'is_predictor': num_empty_spaces == 0,
				'values': [ ],
			}

		while True:
			next_data = next(reader, None)
			if next_data == None:
				break
			for i in range(len(next_data)):
				element = next_data[i]
				if element == '':
					continue
				label = indexToLabel[i]
				data_map[label]['values'].append(element)

		is_valid = verify_dimensions(data_map)

		if not is_valid:
			raise Exception('invalid dimensions')
			
	return data_map