def display_report(dna, results):
    print("========================================================")
    print("              FINAL DNA ANALYSIS REPORT")
    print("========================================================")

    print("DNA SEQUENCE")
    print(dna)

    print("--------------------------------------------------------")
    print("1. DNA COMPOSITION")
    print("--------------------------------------------------------")

    if results["GC Content"] == "Not analysed":
        print("GC Content        : Not analysed")
    else:
        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        print("Adenine (A)       :", a)
        print("Thymine (T)       :", t)
        print("Guanine (G)       :", g)
        print("Cytosine (C)      :", c)
        print("GC Content        :", results["GC Content"], "%")

    print("--------------------------------------------------------")
    print("2. REVERSE COMPLEMENT")
    print("--------------------------------------------------------")
    print("Reverse complement:", results["Reverse Complement"])

    print("--------------------------------------------------------")
    print("3. TRANSCRIPTION")
    print("--------------------------------------------------------")
    print("RNA sequence      :", results["RNA Sequence"])

    print("--------------------------------------------------------")
    print("4. TRANSLATION")
    print("--------------------------------------------------------")
    print("Protein sequence   :", results["Protein"])

    print("--------------------------------------------------------")
    print("5. SEQUENCE COMPARISON")
    print("--------------------------------------------------------")
    print("Comparison         :", results["Comparison"])

    print("========================================================")
    print("             END OF ANALYSIS")
    print("========================================================")