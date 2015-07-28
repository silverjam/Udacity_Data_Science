#!/usr/bin/env python2

from __future__ import print_function
from __future__ import division

import os
mydir = os.path.expanduser("~/dev/data_analytics")

work_hours_per_year = 52 * 40
print( work_hours_per_year )


red_hair = 71
black_hair = 108
total_population = 592

black_hair_proportion = black_hair / total_population
print( black_hair_proportion )

red_hair_percentage = red_hair / total_population
print( red_hair_percentage )

execfile(mydir + "/eruption_duration.py")
eruption_duration = eruption_duration.split()
eruption_duration = [float(I) for I in eruption_duration]

from pandas import DataFrame
data = DataFrame.from_dict({'eruption_duration': eruption_duration})

print( data.mode() )
print( data.var() )

def average(data):
    return sum(data)/len(data)

def variance(data):
    avg = average(data)
    return sum((avg - x)**2 for x in data) / len(data)

def svariance(data):
    avg = average(data)
    return sum((avg - x)**2 for x in data) / (len(data)-1)

eruption_duration2 = DataFrame.from_csv(mydir + "/eruption_duration2.csv",
                                        index_col=False)
eruption_duration2.keys()

data2 = eruption_duration2['Eruption Population'].values.tolist()
variance(data2)
svariance(data2)

eruption_duration2.var()

import numpy
numpy.var(data2)

import csv
fp = file("/tmp/data.csv", "w")
writer = csv.writer(fp)
writer.writerows([x] for x in data2)
fp.close()
fp.closed

len(data2)

import math

pop_var = 1.302728333
samp_var = 1.540217344

pop_std = math.sqrt(pop_var)
samp_var = math.sqrt(samp_var)

print( "%f\n%f" % (pop_std, samp_var) )
