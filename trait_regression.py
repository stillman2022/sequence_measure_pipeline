from position_count import position_count
from conservered_region_finder import conservered_region_finder
from allele_finder import allele_finder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def trait_regression(csv_file, column1, column2):
    df_allele_trait = allele_finder(csv_file, column1, column2)

    header_df = list(df_allele_trait.columns)

    header_allele = header_df[2:]

    X = df_allele_trait[header_allele]

    y = df_allele_trait['sym_rate']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

    lm = LinearRegression()

    lm.fit(X_train, y_train)

    prediction = lm.predict(X_test)

    plt.scatter(y_test, prediction)

    plt.title('Prediction vs Actual')

    plt.ylabel('y_test')

    plt.xlabel('Prediction')

    plt.savefig("Prediction_vs_Actual.jpg")

    plt.show()