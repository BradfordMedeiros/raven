import argparse

def handle_parse_error(x):
	raise Exception(x)

def parse_args(options):
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.error = handle_parse_error # this normally calls exit
	parser.add_argument('-d', '--data', dest='data', required=True, help='file from which to get data from')
	options = parser.parse_args(options)
	return options
