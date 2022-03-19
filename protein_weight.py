# MW OF EVERY AA in daltons
# alanine	    A	89
# arginine	R	174
# asparagine	N	132
# aspartic	D	133
# cysteine	C	121
# glutamic acid	 E   146
# glutamine	Q	147
# glycine	    G	75
# histidin	H	155
# isoleucine	I	131
# leucine	    L	131
# lysine	    K	146
# methionine	     M	149
# phenylalanine	 F	165
# proline	    P	115
# serine	    S	105
# threonine	T	119
# tryptophan	W	204
# tyrosine	Y	181
# valine	    V	117
###

from sys import exit

protein_sequence = ''
amino_acids = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H',
               'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
count_aa = []
mw_aa = []
my_aa_dict = {}


def count_protein_aa(protein_sequence):
    if isinstance(protein_sequence, str) is True:
        pass
    for aa in amino_acids:
        if aa in protein_sequence:
            pass
        else:
            print('The protein contains no ' + aa)
            pass
        for a_acid in protein_sequence:
            if a_acid not in amino_acids:
                print(
                    'Not a valid protein sequence :(\nOnly sequences that have the amino acids well defined.')
                exit(1)
            else:
                pass
    count_aa.append(protein_sequence.count('A'))
    mw_aa.append(protein_sequence.count('A') * 89)
    count_aa.append(protein_sequence.count('R'))
    mw_aa.append(protein_sequence.count('R') * 174)
    count_aa.append(protein_sequence.count('N'))
    mw_aa.append(protein_sequence.count('N') * 132)
    count_aa.append(protein_sequence.count('D'))
    mw_aa.append(protein_sequence.count('D') * 133)
    count_aa.append(protein_sequence.count('C'))
    mw_aa.append(protein_sequence.count('C') * 121)
    count_aa.append(protein_sequence.count('E'))
    mw_aa.append(protein_sequence.count('E') * 146)
    count_aa.append(protein_sequence.count('Q'))
    mw_aa.append(protein_sequence.count('Q') * 147)
    count_aa.append(protein_sequence.count('G'))
    mw_aa.append(protein_sequence.count('G') * 75)
    count_aa.append(protein_sequence.count('H'))
    mw_aa.append(protein_sequence.count('H') * 155)
    count_aa.append(protein_sequence.count('I'))
    mw_aa.append(protein_sequence.count('I') * 131)
    count_aa.append(protein_sequence.count('L'))
    mw_aa.append(protein_sequence.count('L') * 131)
    count_aa.append(protein_sequence.count('K'))
    mw_aa.append(protein_sequence.count('K') * 146)
    count_aa.append(protein_sequence.count('M'))
    mw_aa.append(protein_sequence.count('M') * 149)
    count_aa.append(protein_sequence.count('F'))
    mw_aa.append(protein_sequence.count('F') * 165)
    count_aa.append(protein_sequence.count('P'))
    mw_aa.append(protein_sequence.count('P') * 115)
    count_aa.append(protein_sequence.count('S'))
    mw_aa.append(protein_sequence.count('S') * 105)
    count_aa.append(protein_sequence.count('T'))
    mw_aa.append(protein_sequence.count('T') * 119)
    count_aa.append(protein_sequence.count('W'))
    mw_aa.append(protein_sequence.count('W') * 204)
    count_aa.append(protein_sequence.count('Y'))
    mw_aa.append(protein_sequence.count('Y') * 181)
    count_aa.append(protein_sequence.count('V'))
    mw_aa.append(protein_sequence.count('V') * 117)


count_protein_aa('MKTRQNKDSMSMRSGRKKEAPGPREELRSRGRASPGGVSTSSSDGKAEKSRQTAKKARVE'
                 'EASTPKVNKQGRSEEISESESEETNAPKKTKTEQELPRPQSPSDLDSLDGRSLNDDGSSD'
                 'PRDIDQDNRSTSPSIYSPGSVENDSDSSSGLSQGPARPYHPPPLFPPSPQPPDSTPRQPE'
                 'ASFEPHPSVTPTGYHAPMEPPTSRMFQAPPGAPPPHPQLYPGGTGGVLSGPPMGPKGGGA'
                 'ASSVGGPNGGKQHPPPTTPISVSSSGASGAPPTKPPTTPVGGGNLPSAPPPANFPHVTPN'
                 'LPPPPALRPLNNASASPPGLGAQPLPGHLPSPHAMGQGMGGLPPGPEKGPTLAPSPHSLP'
                 'PASSSAPAPPMRFPYSSSSSSSAAASSSSSSSSSSASPFPASQALPSYPHSFPPPTSLSV'
                 'SNQPPKYTQPSLPSQAVWSQGPPPPPPYGRLLANSNAHPGPFPPSTGAQSTAHPPVSTHH'
                 'HHHQQQQQQQQQQQQQQQQQQQQHHGNSGPPPPGAFPHPLEGGSSHHAHPYAMSPSLGSL'
                 'RPYPPGPAHLPPPHSQVSYSQAGPNGPPVSSSSNSSSSTSQGSYPCSHPSPSQGPQGAPY'
                 'PFPPVPTVTTSSATLSTVIATVASSPAGYKTASPPGPPPYGKRAPSPGAYKTATPPGYKP'
                 'GSPPSFRTGTPPGYRGTSPPAGPGTFKPGSPTVGPGPLPPAGPSGLPSLPPPPAAPASGP'
                 'PLSATQIKQEPAEEYETPESPVPPARSPSPPPKVVDVPSHASQSARFNKHLDRGFNSCAR'
                 'SDLYFVPLEGSKLAKKRADLVEKVRREAEQRAREEKEREREREREKEREREKERELERSV'
                 'KLAQEGRAPVECPSLGPVPHRPPFEPGSAVATVPPYLGPDTPALRTLSEYARPHVMSPGN'
                 'RNHPFYVPLGAVDPGLLGYNVPALYSSDPAAREREREARERDLRDRLKPGFEVKPSELEP'
                 'LHGVPGPGLDPFPRHGGLALQPGPPGLHPFPFHPSLGPLERERLALAAGPALRPDMSYAE'
                 'RLAAERQHAERVAALGNDPLARLQMLNVTPHHHQHSHIHSHLHLHQQDAIHAASASVHPL'
                 'IDPLASGSHLTRIPYPAGTLPNPLLPHPLHENEVLRHQLFAAPYRDLPASLSAPMSAAHQ'
                 'LQAMHAQSAELQRLALEQQQWLHAHHPLHSVPLPAQEDYYSHLKKESDKPL')


my_aa_count_dict = dict(zip(amino_acids, count_aa))
print(my_aa_count_dict)


total_mw = sum(mw_aa)

print('Molecular weight of your protein in Da is: ' + str(total_mw) + ' Da.')
