## @file test_driver.py
#  @author Jay Mody
#  @brief Tests driver for the DateT ADT and GPosT ADT.
#  @date ``

from date_adt import DateT
from pos_adt import GPosT

# unit test functions
def test_value_err(tests):
    passed = 0
    for test in tests:
        try:
            eval(test)
        except ValueError:
            print("PASS: {} returned ValueError".format(test))
            passed += 1
        except:
            print("FAIL: {} did not return ValueError".format(test))
    return passed

def test_eq(tests):
    passed = 0
    for l, r in tests:
        if eval("{} == {}".format(l, r)):
            print("PASS: {} == {}".format(l, r))
            passed += 1
        else:
            print("FAIL: {} == {}".format(l, r))
    return passed

def test_neq(tests):
    passed = 0
    for l, r in tests:
        if eval("{} != {}".format(l, r)):
            print("PASS: {} != {}".format(l, r))
            passed += 1
        else:
            print("FAIL: {} != {}".format(l, r))
    return passed

# module 1 test
def date_test():
    passed = 0
    total = 0

    print("\n----- invalid __init__() params tests -----")
    value_err_tests = [
        "DateT(-1, 1, 2000)",
        "DateT(0, 1, 2000)",
        "DateT(100, 1, 2000)",
        "DateT(10, -1, 2000)",
        "DateT(10, 0, 2000)",
        "DateT(-1, 13, 2000)",
        "DateT(1, 1, 10000)", # max year == 9999
        "DateT(1, 1, 0)", # min year == 1
    ]
    total += len(value_err_tests)
    passed += test_value_err(value_err_tests)

    print("\n----- day() tests -----")
    eq_tests = [
        ("DateT(23, 2, 2012).day()", "23"),
        ("DateT(1, 2, 2012).day()", "1")
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)


    neq_tests = [
        ("DateT(31, 1, 2012).day()", "30"),
        ("DateT(14, 2, 2012).day()", "-14")
    ]
    total += len(neq_tests)
    passed += test_neq(neq_tests)

    print("\n----- month() tests -----")
    eq_tests = [
        ("DateT(23, 2, 2012).month()", "2"),
        ("DateT(1, 12, 2012).month()", "12")
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)


    neq_tests = [
        ("DateT(31, 1, 2012).month()", "2"),
        ("DateT(14, 2, 2012).month()", "-2")
    ]
    total += len(neq_tests)
    passed += test_neq(neq_tests)

    print("\n----- year() tests -----")
    eq_tests = [
        ("DateT(23, 2, 200).year()", "200"),
        ("DateT(1, 12, 2031).year()", "2031"),
        ("DateT(1, 12, 10).year()", "10")
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)


    neq_tests = [
        ("DateT(31, 1, 2012).year()", "-2012"),
        ("DateT(14, 2, 2012).year()", "0"),
        ("DateT(14, 2, 2012).year()", "20120")
    ]
    total += len(neq_tests)
    passed += test_neq(neq_tests)

    print("\n----- next() (and equal()) tests -----")
    eq_tests = [
        ("DateT(1, 2, 2012).next().equal(DateT(2, 2, 2012))", "True"),
        ("DateT(28, 2, 2020).next().equal(DateT(29, 2, 2020))", "True"), # leap year
        ("DateT(28, 2, 2021).next().equal(DateT(1, 3, 2021))", "True"), # non leap year
        ("DateT(31, 12, 2021).next().equal(DateT(1, 1, 2022))", "True"), # month + year change
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print("\n----- prev() (and equal()) tests -----")
    eq_tests = [
        ("DateT(31, 12, 2021).prev().equal(DateT(30, 12, 2021))", "True"),
        ("DateT(1, 3, 1600).prev().equal(DateT(29, 2, 1600))", "True"), # 400 divisible leap year
        ("DateT(1, 3, 1700).prev().equal(DateT(28, 2, 1700))", "True"), # 100 divisible non leap year
        ("DateT(1, 2, 2012).prev().equal(DateT(31, 1, 2012))", "True"), #  month change
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print("\n----- before() tests -----")
    eq_tests = [
        ("DateT(30, 12, 2021).before(DateT(31, 12, 2021))", "True"), # days before
        ("DateT(1, 2, 1600).before(DateT(1, 3, 1600))", "True"), # months before
        ("DateT(1, 3, 1).before(DateT(1, 3, 1700))", "True"), # years before
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print("\n----- after() tests -----")
    eq_tests = [
        ("DateT(13, 12, 2021).after(DateT(12, 12, 2021))", "True"), # days after
        ("DateT(29, 3, 1600).after(DateT(29, 1, 1600))", "True"), # months after
        ("DateT(1, 3, 1701).after(DateT(28, 2, 1700))", "True"), # years after
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print("\n----- add_days() tests -----")
    eq_tests = [
        ("DateT(13, 12, 2021).add_days(12).equal(DateT(25, 12, 2021))", "True"),
        ("DateT(29, 1, 1600).add_days(-100).equal(DateT(21, 10, 1599))", "True"), # month + year change
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print("\n----- days_between() tests -----")
    eq_tests = [
        ("DateT(10, 12, 2000).days_between(DateT(20, 12, 2000))", "10"), # between years
        ("DateT(29, 3, 2014).days_between(DateT(29, 3, 2013))", "-365"), # 365 (year) negative days between
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print()
    print("### report ###")
    print("{} of {} tests passed".format(passed, total))

# module 2 test
def pos_test():
    passed = 0
    total = 0

    # unit tests here

    print()
    print("### report ###")
    print("{} of {} tests passed".format(passed, total))

# main function call
if __name__ == "__main__":
    print("########## DateT Tests ##########")
    date_test()

    print("\n"*5)

    print("########## GPosT Tests ##########")
    pos_test()
