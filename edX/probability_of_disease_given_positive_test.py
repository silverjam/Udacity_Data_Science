#!/usr/bin/env python2

from __future__ import print_function
from __future__ import division

# Probability of having a positive test

p_positive_test = 99/100.0
p_false_positive = 1 - p_positive_test

# Probability that you actually have the disease
p_have_disease = 1/10000.0

# Number of people in 10000 that will have a false positive
num_false_positives = int(10000 * p_false_positive)
num_false_positives

print('Number of false positives:', num_false_positives)

# For each of the 100 people that have false positives, they have a probability
#  of (9999-N)/(10000-N) of not having the disease, for N in 0..99 inclusive.

def not_sick():
    p_falsepos_and_no_disease = 1
    num_dont_have_disease = 9999
    total_population = 10000

    for x in range(num_false_positives):
        p_falsepos_and_no_disease *= num_dont_have_disease/total_population
        num_dont_have_disease -= 1
        total_population -=1

    return( p_falsepos_and_no_disease )

p_falsepos_and_no_disease = not_sick()
print( p_falsepos_and_no_disease )

p_have_disease_after_positive_test = 1 - p_falsepos_and_no_disease
print( p_have_disease_after_positive_test )

p_have_disease_after_positive_test1 = ((1/10000.) * (99/100.)) / (99/100.)
print( p_have_disease_after_positive_test1 )

p_have_disease_after_positive_test2 = 99/(99+9999.0)
print( p_have_disease_after_positive_test2 )
