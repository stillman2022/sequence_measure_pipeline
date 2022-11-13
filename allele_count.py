from position_count import position_count
from conservered_region_finder import conservered_region_finder
from allele_finder import allele_finder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def allele_count(csv_file, column1, column2):
    df_allele_trait = allele_finder(csv_file, column1, column2)
    header_df = list(df_allele_trait.columns)
    header_allele = header_df[2:]
    allele_counts = {}

    for allele in header_allele:
        allele_count_list = df_allele_trait[allele].tolist()
        allele_sum_list = sum(allele_count_list)
        allele_counts[allele] =allele_sum_list

    df_allele_count = pd.DataFrame.from_dict(allele_counts, orient='index')

    names = list(allele_counts.keys())

    values = list(allele_counts.values())

    plt.bar(range(len(allele_counts)), values, tick_label=names)

    plt.title('COUNTS OF ALLELES IN SAMPLE SET')
    plt.xlabel('ALLELES')
    plt.ylabel('COUNTS')

    plt.show()

    plt.savefig("ALLELE_COUNTS.jpg")

    df_allele_count.columns = ['COUNT']

    df_allele_count.to_csv(r'C:\Users\Anthony D. Stillman\Desktop\machine_symptom\allele_count.csv')

#allele_count("genotype_file.csv", "GENOTYPE", 'SYMPTOM RATING')