from operator import itemgetter
inf = open('Homo.fasta', 'r')
flag = 0
seq = ''
col = {}
for line in inf:
    if line.startswith('>') and flag ==1:
        col[ac_number] = seq
        seq = ''
        ac_number = line.strip().split('|')[1]
        #print(col)
    elif line.startswith('>'):
        ac_number = line.strip().split('|')[1]
    else:
        seq += line.strip()
        flag = 1
else:
    col[ac_number] = seq

#print(table)
col_sorted = sorted(col.keys())
for a in col_sorted:
    print(a + ':' + col.get(a))
