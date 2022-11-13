#Python 3.10
#Position Counter

import pandas as pd

def position_count(csv_file, column):
    genotype_df = pd.read_csv(csv_file)

    genotype_list = genotype_df[column].values.tolist()

    a = 0
    t = 0
    g = 0
    c = 0


    count_dict = {}

    for i in range(len(genotype_list[0])):
        for genotype in genotype_list:
            position = genotype[i]
            if position.lower() == 'a':
                a += 1
            elif position.lower() == 't':
                t += 1
            elif position.lower() == 'g':
                g += 1
            elif position.lower() == 'c':
                c += 1

        locus_key = i
        count_dict[locus_key] = {'a':a, 't':t, 'g':g, 'c':c}

        a = 0
        t = 0
        g = 0
        c = 0

    return count_dict

position_count("genotype_file.csv", "GENOTYPE")

