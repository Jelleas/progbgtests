import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

#### split_needle

@t.test(0)
def has_levenshtein(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName,
        "levenshtein_distance")
    test.description = lambda : "definieert de functie levenshtein_distance"

@t.passed(has_levenshtein)
@t.test(1)
def is_int_levenshtein(test):
    test.test = lambda : assertlib.sameType(lib.getFunction("levenshtein_distance", _fileName)("a", "b"), 0)
    test.description = lambda : "levenshtein_distance geeft een int terug"

@t.passed(has_levenshtein)
@t.test(2)
def levenshtein_a(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("majeur", "mineur"), 4)
    test.description = lambda : "levenshtein_distance werkt voor de invoer 'majeur', 'mineur'"

@t.passed(has_levenshtein)
@t.test(3)
def levenshtein_b(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("mineur", "majeur"), 4)
    test.description = lambda : "levenshtein_distance werkt voor de invoer 'mineur', 'majeur'"

@t.passed(has_levenshtein)
@t.test(4)
def levenshtein_c(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("kitten", "sitting"), 5)
    test.description = lambda : "levenshtein_distance werkt voor de invoer 'kitten', 'sitting'"

@t.passed(has_levenshtein)
@t.test(5)
def levenshtein_d(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("sitten", "sittin"), 2)
    test.description = lambda : "levenshtein_distance werkt voor de invoer 'sitten', 'sittin'"

@t.passed(has_levenshtein)
@t.test(6)
def levenshtein_e(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("sitting", "sittin"), 1)
    test.description = lambda : "levenshtein_distance werkt voor de invoer 'sitting', 'sittin'"

@t.passed(has_levenshtein)
@t.test(7)
def levenshtein_f(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("hello", "hello"), 0)
    test.description = lambda : "levenshtein_distance werkt voor de invoer 'hello', 'hello'"

@t.passed(has_levenshtein)
@t.test(8)
def levenshtein_f(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("hello", ""), 5)
    test.description = lambda : "levenshtein_distance werkt voor de invoer 'hello', ''"

@t.passed(has_levenshtein)
@t.test(9)
def levenshtein_g(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levenshtein_distance",
        _fileName)("", "hello"), 5)
    test.description = lambda : "levenshtein_distance werkt voor de invoer '', 'hello'"
