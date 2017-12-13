import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def containsRequiredFunctionDefinitions(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "initials")
	test.description = lambda : "definieert de functie initials()"

@t.passed(containsRequiredFunctionDefinitions)
@t.test(10)
def correctInitials1(test):
	test.test = lambda : assertlib.exact(lib.getFunction("initials", _fileName)("Johann Friedrich Miescher").upper(), "JFM")
	test.description = lambda : "initials() geeft de correcte initialen van \"Johann Friedrich Miescher\""

@t.passed(containsRequiredFunctionDefinitions)
@t.test(11)
def correctInitials2(test):
	test.test = lambda : assertlib.exact(lib.getFunction("initials", _fileName)("Phoebus Levene").upper(), "PL")
	test.description = lambda : "initials() geeft de correcte initialen van \"Phoebus Levene\""

@t.passed(containsRequiredFunctionDefinitions)
@t.test(12)
def correctInitials3(test):
	test.test = lambda : assertlib.exact(lib.getFunction("initials", _fileName)("Martha Chase").upper(), "MC")
	test.description = lambda : "initials() geeft de correcte initialen van \"Martha Chase\""

@t.passed(containsRequiredFunctionDefinitions)
@t.test(20)
def almostWrongInput(test):
	test.test = lambda : assertlib.exact(lib.getFunction("initials", _fileName)("John  Double  Spaces").upper(), "JDS")
	test.description = lambda : "initials() geeft de correcte initialen van \"John  Double  Spaces\""