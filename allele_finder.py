from position_count import position_count
from conservered_region_finder import conservered_region_finder
import pandas as pd

def allele_finder(csv_file, column1, column2):
    loci = conservered_region_finder(position_count(csv_file, column1))

    data_dict = {}
    loci_allele = {}

    genotype_df = pd.read_csv(csv_file)

    data_dict['genotypes'] = genotype_df[column1].tolist()

    data_dict['sym_rate'] = genotype_df[column2].tolist()

    allele_count = 0

    for locus in loci.keys():
        locus_range = loci[locus]
        locusx = {}

        for genotype in data_dict['genotypes']:
            allele = genotype[locus_range[0]:locus_range[1]]

            if allele not in locusx.values():
                locusx[('allele' + str(allele_count))] = allele
                allele_count += 1

            else:
                pass

            loci_allele[str(locus)] = locusx

    df_allele = pd.DataFrame(loci_allele)

    df_allele.to_csv(r'C:\Users\Anthony D. Stillman\Desktop\machine_symptom\locus_allele_seq_key.csv')


    loci_allele_bollean = {}

    for locus in loci_allele.keys():
        locusx = {}
        locus_range = loci[locus]

        for allele in loci_allele[locus]:
            allele_boolean = []
            for genotype in data_dict['genotypes']:
                geneotype_locus = genotype[(locus_range[0]):(locus_range[1])]
                if geneotype_locus == loci_allele[locus][allele]:
                    allele_boolean.append(1)
                elif geneotype_locus != loci_allele[locus][allele]:
                    allele_boolean.append(0)
                else:
                    allele_boolean.append('ERROR')



            locusx[allele] = allele_boolean


        loci_allele_bollean[locus] = locusx

    """print(len(data_dict['genotypes']))
    for locus in loci_allele_bollean.keys():
        for allele in loci_allele_bollean[locus]:
            print(str(allele) + ': ' + str(loci_allele_bollean[locus][allele]))
            print(len(loci_allele_bollean[locus][allele]))"""



    final_data_dict = {'DATA':{}}

    final_data_dict['DATA']['genotypes'] = data_dict['genotypes']
    final_data_dict['DATA']['sym_rate'] = data_dict['sym_rate']

    final_data_dict.update(loci_allele_bollean)

    df = pd.DataFrame()

    header_upper = []


    for keys1 in final_data_dict.keys():
        for i in range((len(final_data_dict[keys1]))):
            header_upper.append(str(keys1))

        for keys2 in final_data_dict[keys1]:
            df[str(keys2)] = final_data_dict[keys1][keys2]

    #header_lower = list(df.columns)

    #header = [header_upper, header_lower]

    #df.columns = header

    df.to_csv(r'C:\Users\Anthony D. Stillman\Desktop\machine_symptom\data_dict.csv')


    return df

#allele_finder("genotype_file.csv", "GENOTYPE", 'SYMPTOM RATING')
