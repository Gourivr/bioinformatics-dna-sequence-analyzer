def validate_dna(dna):
    for base in dna:
        if base not in "ATGC":
            return False
    return True