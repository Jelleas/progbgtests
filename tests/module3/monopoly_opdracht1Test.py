import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

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


@t.test(0)
def hasworp_met_twee_dobbelstenen(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "worp_met_twee_dobbelstenen")
	test.description = lambda : "definieert de functie worp_met_twee_dobbelstenen"
	test.timeout = lambda : 60


# @t.passed(hasworp_met_twee_dobbelstenen)
@t.test(10)
def correctDice(test):
	test.test = lambda : assertlib.between(lib.getFunction("worp_met_twee_dobbelstenen", _fileName)(), 2, 12)
	test.description = lambda : "returnt een correcte waarde voor een worp van twee dobbelstenen"
	test.timeout = lambda : 60
	

# @t.passed(correctDice)
@t.test(20)
def hassimuleer_potjeAndsimuleer_groot_aantal_potjes_Monopoly(test):

	def testMethod():
		test_potje = assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_potje_Monopoly")
		test_groot_aantal_potjes = assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_groot_aantal_potjes_Monopoly")
		info = ""
		if not test_potje:
			info = "de functie simuleer_potje_Monopoly is nog niet gedefinieerd"
		elif not test_groot_aantal_potjes:
			info = "de functie simuleer_potje_Monopoly is gedefinieerd :) \n  - de functie simuleer_groot_aantal_potjes_Monopoly nog niet"
		return test_potje and test_groot_aantal_potjes, info

	test.test = testMethod
	test.description = lambda : "definieert de functie simuleer_potje_Monopoly en simuleer_groot_aantal_potjes_Monopoly"
	test.timeout = lambda : 60


# @t.passed(hassimuleer_potjeAndsimuleer_groot_aantal_potjes_Monopoly)
@t.test(30)
def correctAverageTrump(test):

	def try_run():
		try:	
			testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)()
			test.success = lambda info : "De code werkt zonder startgeld, je kunt nu startgeld invoeren!"
			if assertlib.sameType(lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(), None):
				test.fail = lambda info : "Zorg er voor dat de functie simuleer_groot_aantal_potjes_Monopoly het gemiddeld aan benodigde worpen returnt en ook alleen deze waarde returnt"
			return testInput
		except:
			testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1000000)
			if assertlib.sameType(lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1000000), None):
				test.fail = lambda info : "Zorg er voor dat de functie simuleer_groot_aantal_potjes_Monopoly het gemiddeld aan benodigde worpen returnt en ook alleen deze waarde returnt"
			return testInput


	test.fail = lambda info : "de correcte waarde is ongeveer 147"
	test.test = lambda : assertlib.between(try_run(), 145, 149)
	test.description = lambda : "Monopoly werkt in Trump-Mode"
	test.timeout = lambda : 60


# @t.passed(correctAverageTrump)
@t.test(40)
def correctAverageStartgeld(test):

	def try_run():
		try:
			return lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1500)
		except:
			return False

	test.fail = lambda info : "de correcte waarde is ongeveer 187"
	test.test = lambda : assertlib.between(try_run(), 184, 189)
	test.description = lambda : "Monopoly werkt met 1500 euro startgeld"
	test.timeout = lambda : 60

