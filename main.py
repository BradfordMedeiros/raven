import sys
from algorithms.implementation.testAlgorithm import main as testAlgorithm
from algorithms.arg_parsing.knearest import parse_args
from config.read_data_map import read_data_map

moduleName = sys.argv[1]

modules = {
	'knearest': {
		'parse_args' : parse_args,
	}
}

module = modules[moduleName]
module_args = sys.argv[2:]

options = module['parse_args'](module_args)
print('options: ', options)


data_map = None
print ('using file: ', options.data)
data_map = read_data_map(options.data)



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