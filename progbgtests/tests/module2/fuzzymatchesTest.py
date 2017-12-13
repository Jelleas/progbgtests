import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

#### split_needle

@t.test(0)
def has_split_needle(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "split_needle")
    test.description = lambda : "definieert de functie split_needle"

@t.passed(has_split_needle)
@t.test(1)
def is_list_split_needle(test):
    test.test = lambda : assertlib.sameType(lib.getFunction("split_needle", _fileName)("a"), [])
    test.description = lambda : "split_needle geeft een lijst terug"

@t.passed(is_list_split_needle)
@t.test(2)
def split_needle_a(test):
    test.test = lambda : set(lib.getFunction("split_needle",
        _fileName)("ab")) == set([('', 'b'), ('a', '')])

    test.description = lambda : "split_needle werkt voor de invoer 'ab'"

@t.passed(is_list_split_needle)
@t.test(3)
def split_needle_b(test):
    test.test = lambda : set(lib.getFunction("split_needle",
        _fileName)("abcde")) == set([('', 'bcde'), ('a', 'cde'), ('ab', 'de'), ('abc', 'e'), ('abcd', '')])
    test.description = lambda : "split_needle werkt voor de invoer 'abcde'"


@t.passed(is_list_split_needle)
@t.test(4)
def split_needle_c(test):
    test.test = lambda : set(lib.getFunction("split_needle",
        _fileName)("")) == set([])
    test.description = lambda : "split_needle werkt voor de invoer ''"

#### fuzzy_matches

@t.test(5)
def has_fuzzy_matches(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "fuzzy_matches")
    test.description = lambda : "definieert de functie fuzzy_matches"


@t.passed(has_fuzzy_matches)
@t.test(6)
def is_list_fuzzy_matches(test):
    test.test = lambda : assertlib.sameType(lib.getFunction("fuzzy_matches", _fileName)("a", "a"), [])
    test.description = lambda : "fuzzy_matches geeft een lijst terug"

@t.passed(is_list_fuzzy_matches)
@t.test(7)
def fuzzy_matches_a(test):
    test.test = lambda : set(lib.getFunction("fuzzy_matches",
        _fileName)("atgacatgca", "atgc")) == set([0, 5])
    test.description = lambda : "fuzzy_matches werkt voor de invoer 'atgacatgca', 'atgc'"

@t.passed(is_list_fuzzy_matches)
@t.test(8)
def fuzzy_matches_b(test):
    test.test = lambda : set(lib.getFunction("fuzzy_matches",
        _fileName)("atgacatgca", "atga")) == set([0, 5])
    test.description = lambda : "fuzzy_matches werkt voor de invoer 'atgacatgca', 'atga'"

@t.passed(is_list_fuzzy_matches)
@t.test(9)
def fuzzy_matches_c(test):
    test.test = lambda : set(lib.getFunction("fuzzy_matches",
        _fileName)("atgacatgca", "aggc")) == set([5])
    test.description = lambda : "fuzzy_matches werkt voor de invoer 'atgacatgca', 'aggc'"

@t.passed(is_list_fuzzy_matches)
@t.test(10)
def fuzzy_matches_d(test):
    test.test = lambda : set(lib.getFunction("fuzzy_matches",
        _fileName)("atgacatgca", "ax")) == set([0, 3, 5])
    test.description = lambda : "fuzzy_matches werkt voor de invoer 'atgacatgca', 'ax'"

@t.passed(is_list_fuzzy_matches)
@t.test(11)
def fuzzy_matches_e(test):
    test.test = lambda : set(lib.getFunction("fuzzy_matches",
        _fileName)("atgacatgca", "")) == set([])
    test.description = lambda : "fuzzy_matches werkt voor de invoer 'atgacatgca', ''"

@t.passed(is_list_fuzzy_matches)
@t.test(12)
def fuzzy_matches_f(test):
    test.test = lambda : set(lib.getFunction("fuzzy_matches",
        _fileName)("", "abcd")) == set([])
    test.description = lambda : "fuzzy_matches werkt voor de invoer '', 'abcd'"


