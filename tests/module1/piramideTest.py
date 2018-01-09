import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import re

@t.test(0)
def exactMario0(test):
	test.test = lambda : not assertlib.contains(lib.outputOf(_fileName, stdinArgs=[1]), "##")
	test.description = lambda : "print een pyramide van 0 hoog"

@t.test(1)
def exactMario3(test):
  test.test = lambda : assertlib.match(lib.outputOf(_fileName, stdinArgs=[3]), 
    re.compile(".*"
      "(    # #)[ ]*(\n)"
      "(  # # #)[ ]*(\n)"
      "(# # # #)[ ]*"
      ".*", re.MULTILINE))
  test.description = lambda : "print een pyramide van 3 hoog"

@t.test(2)
def exactMario23(test):
	test.test = lambda : assertlib.match(lib.outputOf(_fileName, stdinArgs=[23]),
    re.compile(".*"
      "(                                            # #)[ ]*(\n)"
      "(                                          # # #)[ ]*(\n)"
      "(                                        # # # #)[ ]*(\n)"
      "(                                      # # # # #)[ ]*(\n)"
      "(                                    # # # # # #)[ ]*(\n)"
      "(                                  # # # # # # #)[ ]*(\n)"
      "(                                # # # # # # # #)[ ]*(\n)"
      "(                              # # # # # # # # #)[ ]*(\n)"
      "(                            # # # # # # # # # #)[ ]*(\n)"
      "(                          # # # # # # # # # # #)[ ]*(\n)"
      "(                        # # # # # # # # # # # #)[ ]*(\n)"
      "(                      # # # # # # # # # # # # #)[ ]*(\n)"
      "(                    # # # # # # # # # # # # # #)[ ]*(\n)"
      "(                  # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(                # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(              # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(            # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(          # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(        # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(      # # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(    # # # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(  # # # # # # # # # # # # # # # # # # # # # # #)[ ]*(\n)"
      "(# # # # # # # # # # # # # # # # # # # # # # # #)[ ]*"
      ".*", re.MULTILINE))
	test.description = lambda : "print een pyramide van 23 hoog"


@t.test(10)
def handlesWrongInput(test):
	test.test = lambda : not assertlib.contains(lib.outputOf(_fileName, stdinArgs=[-100, 100, 24, 1]), "##")
	test.description = lambda : "handelt een verkeerde input van -100, 100 en 24 af"
