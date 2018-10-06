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

l = ['apple', 'go', 'bana']
predictors=[
	[ 0, 10, 24 ],
	[ 10, 10, 10]
] 
configData=[
	[ 20, 30, 30],
	[ 10, 11, 12]
]

knearest = algorithm(labels = l, predictors = predictors, configData = configData)
value = knearest.predict([[ 34, 41, 34 ]])
print('value: ', value)