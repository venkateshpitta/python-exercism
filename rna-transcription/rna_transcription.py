def to_rna(dna: str) -> str:
    table = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ''
    for n in dna:
        rna += table[n] if n in table.keys() else ''
    return rna if len(rna)==len(dna) else ''
