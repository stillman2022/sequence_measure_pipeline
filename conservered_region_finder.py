from position_count import position_count

def conservered_region_finder(position_count):
    count_dict = position_count

    seq_length = len(count_dict)

    conserved_map = ['.']*seq_length

    for locus in count_dict.keys():
       loc_locus = count_dict[locus]

       total_bases = loc_locus['a']+loc_locus['t']+loc_locus['c']+loc_locus['g']
       exp = total_bases*0.25
       chi_a = ((loc_locus['a'] - exp) ** 2) / exp
       chi_t = ((loc_locus['t'] - exp) ** 2) / exp
       chi_g = ((loc_locus['g'] - exp) ** 2) / exp
       chi_c = ((loc_locus['c'] - exp) ** 2) / exp
       chi_loc = chi_c + chi_g + chi_t + chi_a

       if chi_loc > 20:
           conserved_map[locus] = 'K'
       elif chi_loc < 20:
           conserved_map[locus] = 'N'
       else:
           pass

    conserved_map = ''.join(conserved_map)

    loci = {}

    locus_count = 1

    index = 0

    while index < len(conserved_map):

        index_start = index

        while conserved_map[index] == 'K':
            index += 1

        if conserved_map[index_start] == "K":
            locus_key = "locus" + str(locus_count)

            loci[locus_key] = [index_start, index]

            locus_count += 1

        index += 1

    return loci

#print(conservered_region_finder(position_count("genotype_file.csv", "GENOTYPE")))