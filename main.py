import sys
import json
from execute.util.config.read_data_map import read_data_map
import execute.data_map_manipulation as data_map_manipulation
from execute.execute_knearest import execute_knearest
from execute.util.algorithms.arg_parsing.knearest import parse_args as parse_k_args
from execute.util.algorithms.config_requirements.knearest import is_valid_data_map as is_valid_data_map_knearest
from execute.util.algorithms.config_requirements.bayes import is_valid_data_map as is_valid_data_map_bayes
from execute.util.algorithms.config_requirements.knearest import get_requirements as get_requirements_knearest

moduleName = sys.argv[1]
modules = {
	'knearest': {
		'parse_args' : parse_k_args,
		'valid_map': is_valid_data_map_knearest,
		'execute': execute_knearest,
	},
}

if moduleName == 'help' or moduleName == '-h':
	print('usage: ')
	print('raven <modulename> <extra options>\n')
	print('available modules:')
	print('knearest')
	exit(0)


module = modules[moduleName]
module_args = sys.argv[2:]
options = module['parse_args'](module_args)

if options.has_key('usage') and options['usage']:
	requirements = json.dumps(get_requirements_knearest())
	print requirements
	exit(0)

if not options.has_key('data'):
	print 'no data'
	exit(1)

data_map = read_data_map(options['data'])
valid_map = module['valid_map'](data_map)

if not valid_map:
	print('invalid config for knearest')
	exit(1)

result = module['execute'](data_map, json.loads(options['value']), data_map_manipulation)
print json.dumps(result)

"""
usage idea:

maybe can do things like
raven knearest -d trainingdata -q jsonquery

or 

raven shell knearest -d trainingdata
### this will do whatever knearest did originally
but then you have interactive shell where query you type in goes to predict

raven server -p 3000 knearest -d trainingdata
### this will do whatever knearest did originally
but then you have webserver where you can query 


raven -c someconfig 

port:someport
algorithms:
- type: knearest
  training-data: filepath
  route: baseroute
- type: bayes
  training-data: anotherfilepath
  route: anotheroute
"""