import argparse
import sys
import csv 

from algorithms.testAlgorithm import main as testAlgorithm
from algorithms.knearest import knearest


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-a', '--algorithm', dest='algorithm', required=True, help='algorithm to use')
parser.add_argument('-d', '--data', dest='data', required=True, help='file from which to get data from')

options = parser.parse_args(sys.argv[1:])

algorithms = {
	'test': testAlgorithm,
	'knearest': knearest
}

if not options.algorithm in algorithms:
	print ('algorithm undefined')
	sys.exit(1)

algorithm = algorithms[options.algorithm]

labels = None
results = []

with open(options.data) as csvfile:
    reader = csv.reader(csvfile) 
    labels = next(reader)
    for row in reader: 
        results.append(row)


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
					print('warning: invalid file format?')
					exit(1)
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


data_map = None
try:
	data_map = read_data_map(options.data)
	print data_map
except:
	print 'error parsing map'


#l = ['apple', 'go', 'bana']
#predictors=[
#	[ 0, 10, 24 ],
#	[ 10, 10, 10]
#] 
#configData=[
#	[ 20, 30, 30],
#	[ 10, 11, 12]
#]

#{
#	temperature: {
#		values: [ 30, 23, 23, 34],
#		is_predictor: True,
#	}
#	humidity: [
#		values: [ 30, 23, 23, 34],
#		is_predictor: False
#	]
#	///
#}

#knearest = algorithm(labels = l, predictors = predictors, configData = configData)
#value = knearest.predict([[ 34, 41, 34 ]])
#print('value: ', value)