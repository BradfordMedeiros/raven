import argparse
import sys

from algorithms.testAlgorithm import main as testAlgorithm

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-a', '--algorithm', dest='algorithm', required=True, help='algorithm to use')
parser.add_argument('-d', '--data', dest='data', required=False, help='file from which to get data from')

options = parser.parse_args(sys.argv[1:])

algorithms = {
	'test': testAlgorithm
}



if not options.algorithm in algorithms:
	print ('algorithm undefined')
	sys.exit(1)

algorithm = algorithms[options.algorithm]
algorithm()