def compare_sequences(dna1, dna2):
    differences = []

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            differences.append(
                "Position " + str(i + 1) + " does not match: "
                + dna1[i] + " vs " + dna2[i]
            )

    return differences