from position_count import position_count
from conservered_region_finder import conservered_region_finder
from allele_finder import allele_finder
from trait_regression import trait_regression
from allele_count import allele_count
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

csv_file = "genotype_file.csv"
column1 = "GENOTYPE"
column2 = 'SYMPTOM RATING'

allele_finder(csv_file, column1, column2)

trait_regression(csv_file, column1, column2)

allele_count(csv_file, column1, column2)

