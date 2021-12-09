import sys
import gramatica


def readfile(filename):
	file = open(f'{filename}.🙂', 'r', encoding='utf-8')
	token = file.read()
	return token


def main():
	consoleArguments = sys.argv
	if len(consoleArguments) < 2:
		raise Exception('File doesn\'t found. Provide a file to be compiled')
	filename = consoleArguments.pop()
	gramatica.P(readfile(filename))


if __name__ == '__main__':
	main()
