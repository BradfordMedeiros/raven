import sys
import json
from execute.util.config.read_data_map import read_data_map
from execute.execute_knearest import execute_knearest
from execute.util.algorithms.arg_parsing.knearest import parse_args as parse_k_args
from execute.util.algorithms.config_requirements.knearest import is_valid_data_map as is_valid_data_map_knearest
from execute.util.algorithms.config_requirements.knearest import get_requirements as get_requirements_knearest
from execute.util.algorithms.arg_parsing.bayes import parse_args as parse_bayes_args
from execute.util.algorithms.implementation.testAlgorithm import main as testAlgorithm


moduleName = sys.argv[1]
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

if options.usage:
	requirements = json.dumps(get_requirements_knearest())
	print requirements
	exit(0)

data_map = read_data_map(options.data)
valid_map = module['valid_map'](data_map)

if not valid_map:
	print('invalid config for knearest')
	exit(1)

result = module['execute'](data_map, json.loads(options.value))
print json.dumps(result)