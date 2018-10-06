import argparse
import sys
import csv 

from algorithms.testAlgorithm import main as testAlgorithm
from algorithms.knearest import knearest
from config.read_data_map import read_data_map

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


data_map = None
print ('using file: ', options.data)
try:
	data_map = read_data_map(options.data)
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