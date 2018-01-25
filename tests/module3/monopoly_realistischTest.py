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
def hassimuleer_groot_aantal_potjes_Monopoly(test):
	def try_run():
		if assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_groot_aantal_potjes_Monopoly"):
			try:	
				testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1000000, 1000000)
				return True
			except:
				return False
		return False

	test.test = try_run
	test.fail = lambda info : "Zorg dat de functie twee argumenten heeft, startgeld voor speler 1 en startgeld voor speler 2"
	test.description = lambda : "Definieert de functie simuleer_potje en simuleer_groot_aanal_potjes_Monopoly met twee argumenten"
	test.timeout = lambda : 90


# @t.passed(hassimuleer_groot_aantal_potjes_Monopoly)
@t.test(10)
def correctAverageDiv(test):
	def testMethod():
		outcome = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1500, 1500)
		
		type_output = type(outcome)
		fail_type = ""
		pos = {type(None): "niks, zorg dat deze het gemiddeld aan benodigde worpen returnt",\
		 		str: "een woord of zin, zorg dat de functie een getal returnt", \
				tuple: "meerdere waarden, zorg dat deze alleen het gemiddeld aan benodigde worpen returnt"}

		if type_output != int:
			fail_type = pos[type_output]
			info =  "De functie simuleer_groot_aantal_potjes_Monopoly returnt nu %s" %(fail_type)
		elif assertlib.between(outcome, -99999999, 0):
			info = "Als speler 1 meer straten heeft dan speler 2 is het verschil positief"
		else:
			info = "Het verschil is niet erg groot, gemiddeld zelfs minder dan 1 straat"
		return assertlib.between(outcome, .15, 0.45), info

	test.test = testMethod
	test.description = lambda : "Monopoly met twee spelers geeft de het correcte gemiddelde verschil in gekochten straten"
	test.timeout = lambda : 90



# @t.passed(correctAverageDiv)
@t.test(20)
def correctAverageDiv(test):

	def findline(outputOf):
		tsts = ['startgeld', 'evenveel', 'straten']
		for line in outputOf.split("\n"):
			if all([assertlib.contains(line, tst) for tst in tsts]):
				return line
		return ""

	line = findline(lib.outputOf(_fileName))


	test.test = lambda : assertlib.numberOnLine(115, line, deviation = 15)
	test.description = lambda : "Monopoly met twee spelers vindt het correcte extra startgeld voor speler 2"
	test.timeout = lambda : 90




