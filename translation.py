code = {
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",

    "UCU": "Serine", "UCC": "Serine",
    "UCA": "Serine", "UCG": "Serine",

    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UAA": "Stop", "UAG": "Stop",

    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGA": "Stop", "UGG": "Tryptophan",

    "CUU": "Leucine", "CUC": "Leucine",
    "CUA": "Leucine", "CUG": "Leucine",

    "CCU": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",

    "CAU": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",

    "CGU": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "AUU": "Isoleucine", "AUC": "Isoleucine",
    "AUA": "Isoleucine", "AUG": "Methionine",

    "ACU": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",

    "AAU": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",

    "AGU": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GUU": "Valine", "GUC": "Valine",
    "GUA": "Valine", "GUG": "Valine",

    "GCU": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",

    "GAU": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",

    "GGU": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}


def translate_rna(rna):
    protein = ""

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = code[codon]

        print(codon, "=", amino_acid)
        protein += amino_acid + " "

    return protein