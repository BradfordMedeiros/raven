import sys
from config.read_data_map import read_data_map
from algorithms.arg_parsing.knearest import parse_args as parse_k_args
from algorithms.arg_parsing.bayes import parse_args as parse_bayes_args
from algorithms.implementation.testAlgorithm import main as testAlgorithm
from algorithms.config_requirements.knearest import is_valid_data_map as is_valid_data_map_knearest

moduleName = sys.argv[1]

def execute_knearest(data_map):
	print ('execute k-knearest success')

modules = {
	'knearest': {
		'parse_args' : parse_k_args,
		'valid_map': is_valid_data_map_knearest,
		'execute': execute_knearest,
	},
	'bayes': {
		'parse_args': parse_bayes_args
	},
}

if moduleName == 'help' or moduleName == '-h':
	print('usage: ')
	print('raven <modulename> <extra options>\n')
	print('available modules:')
	print('knearest, bayes')
	exit(0)


module = modules[moduleName]
module_args = sys.argv[2:]
options = module['parse_args'](module_args)
data_map = None

print 'parsing csv'
data_map = read_data_map(options.data)
print 'csv parse success'

print 'checking data validity'
valid_map = module['valid_map'](data_map)
if not valid_map:
	print('invalid config for knearest')
	exit(1)

print 'valid map'

print 'starting executing : ' , moduleName
module['execute'](data_map)



"""
def create_from_data_map(data_map):
	data = {
		'labels': data_map.keys()
	}

	predictors = [ ]
	
        all_values = []
        for label in data_map:
            values = data_map[label]['values']
            all_values.append(values)

        print ('| ', all_values)

	return data

k_form = create_from_data_map(data_map)
print('k-form: ', k_form)
"""


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
