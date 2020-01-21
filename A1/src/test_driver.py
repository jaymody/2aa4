## @file test_driver.py
#  @author Jay Mody
#  @brief Tests driver for the DateT ADT and GPosT ADT.
#  @date 20/01/20 (dd/mm/yy)

from date_adt import DateT
from pos_adt import GPosT

import pytest

# DateT tests
def test_DateT_init():
    with pytest.raises(ValueError):
        DateT(-1, 1, 2000)
        DateT(0, 1, 2000)
        DateT(100, 1, 2000)
        DateT(10, -1, 2000)
        DateT(10, 0, 2000)
        DateT(-1, 13, 2000)
        DateT(1, 1, 10000)
        DateT(1, 1, 0)

def test_DateT_day():
    assert DateT(23, 2, 2012).day() == 23
    assert DateT(1, 2, 2012).day() == 1

    assert DateT(31, 1, 2012).day() != 30
    assert DateT(14, 2, 2012).day() != -14

def test_DateT_month():
    assert DateT(23, 2, 2012).month() == 2
    assert DateT(1, 12, 2012).month() == 12

    assert DateT(31, 1, 2012).month() != 2
    assert DateT(14, 2, 2012).month() != -2

def test_DateT_year():
    assert DateT(23, 2, 200).year() == 200
    assert DateT(1, 12, 2031).year() == 2031
    assert DateT(1, 12, 10).year() == 10

    assert DateT(31, 1, 2012).year() != -2012
    assert DateT(14, 2, 2012).year() != 0
    assert DateT(14, 2, 2012).year() != 20120

def test_DateT_equal():
    assert DateT(31, 12, 2021).equal(DateT(31, 12, 2021))
    assert DateT(1, 1, 1).equal(DateT(1, 1, 1))

    assert not DateT(1, 1, 1).equal(DateT(2, 1, 1))
    assert not DateT(31, 12, 2021).equal(DateT(30, 12, 2020))

def test_DateT_next():
    assert DateT(1, 2, 2012).next().equal(DateT(2, 2, 2012)) == True
    assert DateT(28, 2, 2020).next().equal(DateT(29, 2, 2020)) == True # leap year
    assert DateT(28, 2, 2021).next().equal(DateT(1, 3, 2021)) == True # non leap year
    assert DateT(31, 12, 2021).next().equal(DateT(1, 1, 2022)) == True # month + year change

def test_DateT_prev():
    assert DateT(31, 12, 2021).prev().equal(DateT(30, 12, 2021)) == True
    assert DateT(1, 3, 1600).prev().equal(DateT(29, 2, 1600)) == True # 400 divisible leap year
    assert DateT(1, 3, 1700).prev().equal(DateT(28, 2, 1700)) == True # 100 divisible non leap year
    assert DateT(1, 2, 2012).prev().equal(DateT(31, 1, 2012)) == True #  month change

def test_DateT_before():
    assert DateT(30, 12, 2021).before(DateT(31, 12, 2021)) == True # days before
    assert DateT(1, 2, 1600).before(DateT(1, 3, 1600)) == True # months before
    assert DateT(1, 3, 1).before(DateT(1, 3, 1700)) == True # years before

def test_DateT_after():
    assert DateT(13, 12, 2021).after(DateT(12, 12, 2021)) == True # days after
    assert DateT(29, 3, 1600).after(DateT(29, 1, 1600)) == True # months after
    assert DateT(1, 3, 1701).after(DateT(28, 2, 1700)) == True # years after

def test_DateT_add_days():
    assert DateT(13, 12, 2021).add_days(12).equal(DateT(25, 12, 2021)) == True
    assert DateT(29, 1, 1600).add_days(-100).equal(DateT(21, 10, 1599)) == True # month + year change

def test_DateT_days_between():
    assert DateT(10, 12, 2000).days_between(DateT(20, 12, 2000)) == 10 # between years
    assert DateT(29, 3, 2014).days_between(DateT(29, 3, 2013)) == -365 # 365 (year) negative days between


# GPosT tests
def test_GPosT_init():
    with pytest.raises(ValueError):
        GPosT(-90.0001, 0)
        GPosT(90.0001, 0)
        GPosT(0, -180.0001)
        GPosT(0, 180.0001)

    assert GPosT(-90., 0)
    assert GPosT(90., 0)
    assert GPosT(0, -180.)
    assert GPosT(0, 180.)

def test_GPosT_lat():
    assert GPosT(23., 0).lat() == 23
    assert GPosT(-12.1231, 1.).lat() == -12.1231

    assert GPosT(23.000001, 23).lat() != 23
    assert GPosT(23, -23).lat() != -23

def test_GPosT_long():
    assert GPosT(23., 0).long() == 0
    assert GPosT(2.1231, 1.).long() == 1.

    assert GPosT(1.01, 1.01).long() != 1.
    assert GPosT(23, -23).long() != 23

def test_GPosT_west_of():
    assert GPosT(1, 0).west_of(GPosT(2, 1)) == True
    assert GPosT(28, -2).west_of(GPosT(21, -20)) == False

def test_GPosT_north_of():
    assert GPosT(31, 12).north_of(GPosT(30, 14)) == True
    assert GPosT(-21, 3).north_of(GPosT(-20, 2)) == False

def test_GPosT_distance():
    assert (abs(1805.5 - GPosT(-1, 2).distance(GPosT(10, -10))) < 1) == True
    assert (abs(212 - GPosT(-11, 2).distance(GPosT(10, -10))) < 1) == False

def test_GPosT_equal():
    assert GPosT(-1, 2).equal(GPosT(-1, 2)) == True
    assert GPosT(-1.001, 2).equal(GPosT(-1, 2.001)) == True
    assert GPosT(-1.2, 2).equal(GPosT(0, 0)) == False
    assert GPosT(-20, 20).equal(GPosT(20, -20)) == False

## @cite used https://www.latlong.net/degrees-minutes-seconds-to-decimal-degrees to calculate expected output
def test_GPosT_move():
    pos = GPosT(10, 0)
    pos.move(30, 1000)

    # test if within 1m of target lat/long
    assert abs(17.74805556 - pos.lat()) < 0.001
    assert abs(4.70722222 - pos.long()) < 0.001

def test_GPosT_arrival_date():
    start_date = DateT(1, 1, 2000)
    start_pos = GPosT(0, 0)
    target_pos = GPosT(25, 25)

    assert start_pos.arrival_date(target_pos, start_date, 100).equal(DateT(8, 2, 2000))
