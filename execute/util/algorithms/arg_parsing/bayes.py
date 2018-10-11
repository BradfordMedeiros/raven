import argparse

def handle_parse_error(x):
	raise Exception(x)

def parse_args(options):
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.error = handle_parse_error # this normally calls exit
	parser.add_argument('-d', '--data', dest='data', required=True, help='file from which to get data from')
	parser.add_argument('-u', '--usage', default=False, action="store_true" , help="Flag to do something")
	parser.add_argument('-v', '--value', dest='value', required=True, help='value to predict')
	options = parser.parse_args(options)
	return vars(options)
