# Import libraries
import numpy as np
import pandas as pd
from sklearn import grid_search
from sklearn.cross_validation import train_test_split

from lib.data.wrangler import readData
from lib.helpers import runTests, writeToCsv

X_test, \
    X_train, \
    y_test, \
    y_train = readData('./tmp/testTrainData.npz')

classifiers, \
    train_times, \
    pred_times, \
    f1_trains, \
    f1_tests = runTests(X_test, X_train, y_test, y_train)

writeToCsv(classifiers, train_times, pred_times, f1_trains, f1_tests)
