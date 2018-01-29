import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import re

def sandbox():
	lib.require("DeBiltTempMax.txt", "http://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMax.txt")
	lib.require("DeBiltTempMin.txt", "http://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMin.txt")


def before():
	try:
		import matplotlib
		matplotlib.use("Agg")
		import matplotlib.pyplot as plt
		plt.switch_backend("Agg")
		lib.neutralizeFunction(plt.pause)
	except ImportError:
		pass

def after():
	try:
		import matplotlib.pyplot as plt
		plt.switch_backend("TkAgg")
		importlib.reload(plt)
	except ImportError:
		pass


# Thanks to Vera Schild!

@t.test(10)
def correctHighestTemp(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '36.8')
	test.description = lambda : "print hoogste temperatuur"

@t.passed(correctHighestTemp)
@t.test(11)
def correctDateHighestTemp(test):
	def findline(outputOf):
		for line in outputOf.split("\n"):
			if assertlib.contains(line, '36.8'):
				return line
		return 0

	outputLine = findline(lib.outputOf(_fileName))

	tsts = ['6', 'juni', 'June']
	test.test = lambda : assertlib.contains(outputLine, '27') and\
			     sum([assertlib.contains(outputLine, tst) for tst in tsts])\
		             and assertlib.contains(outputLine, '1947')


	output = lib.outputOf(_fileName).split("\n")
	source = " ".join(lib.removeComments(lib.source(_fileName)).split("\n"))

	if re.compile(".*" + outputLine + ".*").match(source):
		test.description = lambda : "let op: deze output is hardcoded. Dit geldt voor deze en de bovenstaande test"
				
	else:
		test.description = lambda : "print datum hoogste temperatuur"


@t.test(20)
def correctLowestTemp(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '-24.8')
	test.description = lambda : "print laagste temperatuur"

@t.passed(correctLowestTemp)
@t.test(21)
def correctDateLowestTemp(test):
	def findline(outputOf):
		for line in outputOf.split("\n"):
			if assertlib.contains(line, '-24.8'):
				return line
		return 0

	outputLine = findline(lib.outputOf(_fileName))

	tsts = ['1', 'januari', 'January']
	test.test = lambda : assertlib.contains(outputLine, '27') and\
			     sum([assertlib.contains(outputLine, tst) for tst in tsts])\
		             and assertlib.contains(outputLine, '1942')

	output = lib.outputOf(_fileName).split("\n")
	source = " ".join(lib.removeComments(lib.source(_fileName)).split("\n"))

	if re.compile(".*" + outputLine + ".*").match(source):
		test.description = lambda : "Let op: deze output is hardcoded. Dit geldt voor deze en de bovenstaande test"

	else:
		test.description = lambda : "print datum laagste temperatuur"


@t.test(30)
def correctLongestFreezing(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '21')
	test.description = lambda : "print de langste periode dat het aaneengesloten heeft gevroren"

@t.passed(correctLongestFreezing)
@t.test(31)
def correctDateLongestFreezingp(test):
	def findline(outputOf):
		for line in outputOf.split("\n"):
			if assertlib.contains(line, '21'):
				return line
		return 0

	outputLine = findline(lib.outputOf(_fileName))	

	tsts = ['2', 'februari', 'February']
	test.test = lambda : assertlib.contains(outputLine, '24') and\
			     sum([assertlib.contains(outputLine, tst) for tst in tsts])\
		             and assertlib.contains(outputLine, '1947')

	output = lib.outputOf(_fileName).split("\n")
	source = " ".join(lib.removeComments(lib.source(_fileName)).split("\n"))

	if re.compile(".*" + outputLine + ".*").match(source):
		test.description = lambda : "let op: deze output is hardcoded. Dit geldt voor deze en de bovenstaande test"
	else:
		test.description = lambda : "print laatste dag van de langste periode dat het aaneengesloten heeft gevroren"

@t.test(40)
def correctFirstHeatWave(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '1911')
	test.description = lambda : "print het eerste jaartal waarin er sprake was van een hittegolf"

# @t.test(50)
# def showsGraph(test):
# 	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig") or assertlib.fileContainsFunctionCalls(_fileName, "show")
# 	test.description = lambda : "slaat een grafiek op, of laat een grafiek zien"


