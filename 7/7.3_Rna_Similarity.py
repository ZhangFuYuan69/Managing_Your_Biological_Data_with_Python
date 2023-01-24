table = []
for line in open('RNA_similarity.txt'):
	table.append(line.strip().split('\t'))
for row in table:
	print(row, '\n')
seq1 = 'AGCAUCUA'
seq2 = 'ACCGUUCU'
RNA_similarity = 0.0
b1 = 0
b2 = 0
local = {"A": 1 , "G": 2 , "C": 3 , "U": 4 } 
for base1, base2 in zip(seq1, seq2):
	b1 = local[base1]
	b2 = local[base2]
	RNA_similarity += float(table[b1][b2])
	print(RNA_similarity)
print(RNA_similarity)
