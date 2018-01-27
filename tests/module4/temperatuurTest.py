import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

def sandbox():
	lib.require("DeBiltTempMax.txt", "http://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMax.txt")
	lib.require("DeBiltTempMin.txt", "http://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMin.txt")

# Thanks to Vera Schild!

@t.test(0)
def correctHighestTemp(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '36.8')
	test.description = lambda : "print hoogste temperatuur"

@t.test(1)
def correctDateHighestTemp(test):
	tsts = ['6', 'juni', 'June']
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '27') and\
			     sum([assertlib.contains(lib.outputOf(_fileName), tst) for tst in tsts])\
		             and assertlib.contains(lib.outputOf(_fileName), '1947')
	test.description = lambda : "print datum hoogste temperatuur"

@t.test(2)
def correctLowestTemp(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '-24.8')
	test.description = lambda : "print laagste temperatuur"

@t.test(3)
def correctDateLowestTemp(test):
	tsts = ['1', 'januari', 'January']
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '27') and\
			     sum([assertlib.contains(lib.outputOf(_fileName), tst) for tst in tsts])\
		             and assertlib.contains(lib.outputOf(_fileName), '1942')
	test.description = lambda : "print datum laagste temperatuur"

@t.test(4)
def correctLongestFreezing(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '21')
	test.description = lambda : "print de langste periode dat het aaneengesloten heeft gevroren"

@t.test(5)
def correctDateLongestFreezingp(test):
	tsts = ['2', 'februari', 'February']
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '24') and\
			     sum([assertlib.contains(lib.outputOf(_fileName), tst) for tst in tsts])\
		             and assertlib.contains(lib.outputOf(_fileName), '1947')
	test.description = lambda : "print laatste dag van de langste periode dat het aaneengesloten heeft gevroren"

@t.test(6)
def correctFirstHeatWave(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName), '1911')
	test.description = lambda : "print het eerste jaartal waarin er sprake was van een hittegolf"

# @t.test(7)
# def showsGraph(test):
# 	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig") or assertlib.fileContainsFunctionCalls(_fileName, "show")
# 	test.description = lambda : "slaat een grafiek op, of laat een grafiek zien"


