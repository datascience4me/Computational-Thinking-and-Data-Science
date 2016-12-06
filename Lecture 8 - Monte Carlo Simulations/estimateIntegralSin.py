#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 01:28:02 2016

@author: jpdjere
"""

import random, numpy,math

def throwNeedles(numNeedles):
    inSin = 0
    for needles in range(1, numNeedles +1, 1):    
        y = random.random()
        x = random.uniform(0,numpy.pi)
        if y <= math.sin(x):
            inSin += 1
    return numpy.pi*(inSin/float(numNeedles))
    
def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Estimates = ' + str(curEst)+ ' Std Dev = ', str(round(sDev,6))
        + ', Needles = ' + str(numNeedles))
    return (curEst,sDev)
    
def estPi(precision, numTrials):
    """Calls getEst with an evergrowing numNeedles until getEst get an estimate 
    with a confidence of 95%. It does this by calling throwNeedles with a growing num of
    needles until the sDev of the results of numTrials is no larger than the
    desired precision divided 1.96. Under the assumption (by CLT) that errors are
    normally distribitued, this implies that 95% of values are within precision of mean"""
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

random.seed(0)
estPi(0.005,100)