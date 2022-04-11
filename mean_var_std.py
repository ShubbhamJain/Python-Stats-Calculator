import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    npList = np.array(list).reshape(3, 3)

    calculatedMean = mean(npList)
    calculatedVar = variance(npList)
    calculatedSTD = standardDeviation(npList)
    calculatedMax = maxValues(npList)
    calculatedMin = minValues(npList)
    calculatedSum = sumOfValues(npList)

    calculations = {
        "mean": calculatedMean,
        "variance": calculatedVar,
        "standard deviation": calculatedSTD,
        "max": calculatedMax,
        "min": calculatedMin,
        "sum": calculatedSum,
    }

    return calculations


def mean(values):
    meanAlongAxis0 = list(np.mean(values, axis=0))
    meanAlongAxis1 = list(np.mean(values, axis=1))
    meanOfTotal = np.mean(values)
    return [meanAlongAxis0, meanAlongAxis1, meanOfTotal]


def variance(values):
    varAlongAxis0 = list(np.var(values, axis=0))
    varAlongAxis1 = list(np.var(values, axis=1))
    varOfTotal = np.var(values)
    return [varAlongAxis0, varAlongAxis1, varOfTotal]


def standardDeviation(values):
    stdAlongAxis0 = list(np.std(values, axis=0))
    stdAlongAxis1 = list(np.std(values, axis=1))
    stdOfTotal = np.std(values)
    return [stdAlongAxis0, stdAlongAxis1, stdOfTotal]


def maxValues(values):
    maxAlongAxis0 = list(np.max(values, axis=0))
    maxAlongAxis1 = list(np.max(values, axis=1))
    maxOfTotal = np.max(values)
    return [maxAlongAxis0, maxAlongAxis1, maxOfTotal]


def minValues(values):
    minAlongAxis0 = list(np.min(values, axis=0))
    minAlongAxis1 = list(np.min(values, axis=1))
    minOfTotal = np.min(values)
    return [minAlongAxis0, minAlongAxis1, minOfTotal]


def sumOfValues(values):
    sumAlongAxis0 = list(np.sum(values, axis=0))
    sumAlongAxis1 = list(np.sum(values, axis=1))
    sumOfTotal = np.sum(values)
    return [sumAlongAxis0, sumAlongAxis1, sumOfTotal]
