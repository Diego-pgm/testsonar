#!/usr/bin/env python


def suma(*args):
   num1 = input('Insert a number: ')
   num2 = input('Insert other number: ')
   total = num1 + num2
   return total


def test_suma(*args):
   assert int(total) + 3 == 5

total = suma()
test_suma(total)
