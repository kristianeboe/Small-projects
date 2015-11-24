complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
poolA = ['AAG', 'TAC', 'CGG', 'GAT', 'TTG', 'GTG', 'CAT', 'GGC', 'ATT', 'TCT']
poolB = ['TAA', 'CTA', 'AAC', 'TTC', 'AGA', 'CCC', 'CCG', 'GTA']

def matching_codons(complements, poolA, poolB):
    matches = []
    for a in poolA:
        for b in poolB:
            if match(complements, a, b):
                matches.append((a,b))
    return matches

def match(complements, seq1, seq2):
    temp_seq = ""
    for l in seq2:
        temp_seq += complements[l]
    return seq1 == temp_seq

print matching_codons(complements, poolA, poolB)
