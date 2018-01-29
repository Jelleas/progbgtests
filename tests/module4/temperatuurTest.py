import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

def sandbox():
	lib.require("DeBiltTempMax.txt", "http://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMax.txt")
	lib.require("DeBiltTempMin.txt", "http://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMin.txt")

# Thanks to Vera Schild!

@t.test(0)
def correctHighestTemp(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		return assertlib.contains(output, '36.8')
	test.test = testMethod
	test.description = lambda : "print hoogste temperatuur"

@t.test(1)
def correctDateHighestTemp(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		correctDay = assertlib.contains(output, '27')
		correctMonth = any([assertlib.contains(output.lower(), month) for month in ["6", "juni", "june", "jun"]])
		correctYear = assertlib.contains(output, '1947')
		return correctDay and correctMonth and correctYear

	test.test = testMethod
	test.description = lambda : "print datum hoogste temperatuur"

@t.test(2)
def correctLowestTemp(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		return assertlib.contains(output, '-24.8')
	test.test = testMethod
	test.description = lambda : "print laagste temperatuur"

@t.test(3)
def correctDateLowestTemp(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		correctDay = assertlib.contains(output, '27')
		correctMonth = any([assertlib.contains(output.lower(), month) for month in ["1", "januari", "january", "jan"]])
		correctYear = assertlib.contains(output, '1942')
		return correctDay and correctMonth and correctYear

	test.test = testMethod
	test.description = lambda : "print datum laagste temperatuur"

@t.test(4)
def correctLongestFreezing(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		return assertlib.contains(output, '21')
	test.test = testMethod
	test.description = lambda : "print de langste periode dat het aaneengesloten heeft gevroren"

@t.test(5)
def correctDateLongestFreezingp(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		correctDay = assertlib.contains(output, '24')
		correctMonth = any([assertlib.contains(output.lower(), month) for month in ["2", "februari", "february", "feb"]])
		correctYear = assertlib.contains(output, '1947')
		return correctDay and correctMonth and correctYear

	test.test = testMethod
	test.description = lambda : "print laatste dag van de langste periode dat het aaneengesloten heeft gevroren"

@t.test(6)
def correctFirstHeatWave(test):
	def testMethod():
		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)
		return assertlib.contains(output, '1911')
	test.test = testMethod
	test.description = lambda : "print het eerste jaartal waarin er sprake was van een hittegolf"

# @t.test(7)
# def showsGraph(test):
# 	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig") or assertlib.fileContainsFunctionCalls(_fileName, "show")
# 	test.description = lambda : "slaat een grafiek op, of laat een grafiek zien"
