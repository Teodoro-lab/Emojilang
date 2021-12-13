import sys
import gramatica


def readfile(filename):
	"""
	The function returns the string without preprocessing and reads directly from a file
	with emojilang source code. It generates a fileNotFound error if the path is pass incorrectly
	:param filename:
	:return:
	"""
	if(filename[-2:] == '.🙂'):
		file = open(f'{filename}', 'r', encoding='utf-8')
		token = file.read()
		return token
	else:
		raise Exception("Use the correct file extension '🙂'")
		


def main():
	"""
	You can pass the name of the file to be compiled as a console argument
	by running:

	# python main.py hola
	"""
	consoleArguments = sys.argv
	if len(consoleArguments) < 2:
		raise Exception('Provide a file to be compiled')
	filename = consoleArguments.pop()
	programString = readfile(filename)
	gramatica.P(programString)


if __name__ == '__main__':
	main()
