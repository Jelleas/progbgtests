import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exact1(test):
	test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, stdinArgs=[1]), 0))
	test.description = lambda : "vind het 1ste priemgetal: 2"

@t.test(10)
def exact1000(test):
	test.test = lambda : assertlib.numberOnLine(7919, lib.getLine(lib.outputOf(_fileName, stdinArgs=[1000]), 0))
	test.description = lambda : "vind het 1000ste priemgetal: 7919"

@t.test(20)
def exact377(test):
	test.test = lambda : assertlib.numberOnLine(2591, lib.getLine(lib.outputOf(_fileName, stdinArgs=[377]), 0))
	test.description = lambda : "vind het 377ste priemgetal: 2591"

@t.passed(exact1)
@t.test(30)
def handlesWrongInput(test):
	test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, stdinArgs=[-90, -1, 0, 1]), 0))
	test.description = lambda : "handelt foute input af: -90, -1, 0"