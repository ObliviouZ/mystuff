from sys import exit

DNA_sample = ' '
bases = ['A', 'T', 'G', 'C']


def count_dna_bases():
    DNA_sample = input('Type in your DNA sample: ')
    if isinstance(DNA_sample, str) is True:
        pass
    for base in bases:
        if base in DNA_sample:
            pass
        else:
            print(' There is no ' + base)
            pass
    for x in DNA_sample:
        if x not in bases:
            print(' Not a DNA sequence')
            exit(1)
        else:
            pass

    print(((DNA_sample.count('A')), (DNA_sample.count('C')),
           (DNA_sample.count('G')), (DNA_sample.count('T'))))


count_dna_bases()
