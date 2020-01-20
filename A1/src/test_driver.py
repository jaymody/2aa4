## @file test_driver.py
#  @author Jay Mody
#  @brief Tests driver for the DateT ADT and GPosT ADT.
#  @date 20/01/20 (dd/mm/yy)

from date_adt import DateT
from pos_adt import GPosT

# unit test functions
def test_value_err(tests):
    passed = 0
    for test in tests:
        try:
            eval(test)
            print("FAIL: {} did not return ValueError".format(test))
        except ValueError:
            print("PASS: {} threw ValueError".format(test))
            passed += 1
        except:
            print("FAIL: {} did not throw ValueError".format(test))
    return passed

def test_no_err(tests):
    passed = 0
    for test in tests:
        try:
            eval(test)
            print("PASS: {} ran with no exceptions".format(test))
            passed += 1
        except:
            print("FAIL: {} returned an exception".format(test))
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

# DateT tests
def test_DateT():
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

# GPosT tests
def test_GPosT():
    passed = 0
    total = 0

    print("\n----- invalid __init__() params tests -----")
    value_err_tests = [
        "GPosT(-90.0001, 0)",
        "GPosT(90.0001, 0)",
        "GPosT(0, -180.0001)",
        "GPosT(0, 180.0001)",
    ]
    total += len(value_err_tests)
    passed += test_value_err(value_err_tests)

    no_err_tests = [
        "GPosT(-90., 0)",
        "GPosT(90., 0)",
        "GPosT(0, -180.)",
        "GPosT(0, 180.)",
    ]
    total += len(no_err_tests)
    passed += test_no_err(no_err_tests)

    print("\n----- lat() tests -----")
    eq_tests = [
        ("GPosT(23., 0).lat()", "23"),
        ("GPosT(-12.1231, 1.).lat()", "-12.1231")
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    neq_tests = [
        ("GPosT(23.000001, 23).lat()", "23"),
        ("GPosT(23, -23).lat()", "-23")
    ]
    total += len(neq_tests)
    passed += test_neq(neq_tests)

    print("\n----- long() tests -----")
    eq_tests = [
        ("GPosT(23., 0).long()", "0"),
        ("GPosT(2.1231, 1.).long()", "1.")
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    neq_tests = [
        ("GPosT(1.01, 1.01).long()", "1."),
        ("GPosT(23, -23).long()", "23")
    ]
    total += len(neq_tests)
    passed += test_neq(neq_tests)

    print("\n----- west_of() tests -----")
    eq_tests = [
        ("GPosT(1, 0).west_of(GPosT(2, 1))", "True"),
        ("GPosT(28, -2).west_of(GPosT(21, -20))", "False"),
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print("\n----- north_of() tests -----")
    eq_tests = [
        ("GPosT(31, 12).north_of(GPosT(30, 14))", "True"),
        ("GPosT(-21, 3).north_of(GPosT(-20, 2))", "False"),
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    print("\n----- distance() tests (accurate to 1km) -----")
    eq_tests = [
        ("abs(1805.5 - GPosT(-1, 2).distance(GPosT(10, -10))) < 1", True),
        ("abs(1 - GPosT(-11, 2).distance(GPosT(10, -10))) < 1", "False"),
    ]
    total += len(eq_tests)
    passed += test_eq(eq_tests)

    # print("\n----- equal() (and distance()) tests -----")
    # eq_tests = []
    # total += len(eq_tests)
    # passed += test_eq(eq_tests)

    # print("\n----- move() tests -----")
    # need special test cases

    # print("\n----- arrival_date() tests -----")
    # eq_tests = []
    # total += len(eq_tests)
    # passed += test_eq(eq_tests)

    print()
    print("### report ###")
    print("{} of {} tests passed".format(passed, total))

# main function call
if __name__ == "__main__":
    print("########## DateT Tests ##########")
    test_DateT()

    print("\n"*5)

    print("########## GPosT Tests ##########")
    test_GPosT()
