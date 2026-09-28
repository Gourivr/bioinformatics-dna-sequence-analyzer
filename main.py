print("**BIOINFORMATICS DNA SEQUENCE ANALYZER**")
results = {
    "GC Content": "Not analysed",
    "Reverse Complement": "Not analysed",
    "RNA Sequence": "Not analysed",
    "Protein": "Not analysed",
    "Comparison": "Not analysed"
}

while True:
    dna = input("Enter the DNA sequence like ATGCCTAG.... ")
    dna = dna.upper()

    valid = True

    for base in dna:
        if base not in "ATGC":
            valid = False
            break

    if valid:
        print()
        break
    else:
        print("Please enter a valid DNA strand")

  #defining rna conversion function      
def rna_con(dna):
    rna = dna.replace("T", "U")
    return rna

def reverse_comp(dna):
            compliment=''
            pair={'A':'T','T':'A',
             'G':'C','C':'G'}
            for base in dna:
                compliment += pair[base]
            return compliment[::-1]

while True:
    print('********MENU********')
    print('what do you want to analyse?\n')
    print("1. Calculate GC count\n *helps in determining the stability of DNA\n")
    print("2. Find reverse complement\n *helps in comparision of genes in the direction of 5' to 3'\n")
    print("3. Transcribe DNA to RNA(transcription)\n *second step for protein synthesis\n")
    print("4. Translate DNA to amino acids(translation)\n *Shows how genetic information is converted into a protein sequence\n")
    print("5. Compare two DNA sequences\n  *Helps identify differences between DNA sequences\n")
    print("6. *Final analysis results*\n")
    print("7. Exit\n")
    print('**********_**********\n')

    choice_input = input("Enter your choice: ")
    
    if not choice_input.isdigit():
        print("Please enter a number from 1 to 7")
        continue
    choice = int(choice_input)
    if choice < 1 or choice > 7:
        print("Please enter a number from 1 to 7")
        continue
    if choice == 1:
        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        print("Adenine count =", a)
        print("Thymine count =", t)
        print("Guanine count =", g)
        print("Cytosine count =", c)
        gc_percentage = (g + c) / len(dna) * 100
        print("GC percentage =", gc_percentage, "%")
        results["GC Content"] = round(gc_percentage, 2)

    elif choice==2:
        print('original DNA=',dna)
        rev=reverse_comp(dna)
        print("Reverse complement =",rev)
        results["Reverse Complement"]=rev


    elif choice==3:
        print('the DNA sequence is=',dna)
        rna=rna_con(dna)
        print('the RNA sequence is=',rna)
        results["RNA Sequence"] =rna
        


            

    elif choice==4:
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
    "GGA": "Glycine", "GGG": "Glycine"}
        
        rna=rna_con(dna)
        protein=''
        print('The codons and the proteins synthesised are as follows:')
        print('the RNA is',rna)
        for i in range(0, len(rna) - 2, 3):
            codon = rna[i:i+3]
            amino_acid = code[codon]

            print(codon, "=", amino_acid)
            protein += amino_acid + " "
        results["Protein"] = protein
    elif choice == 5:
       
        while True:
            dna2 = input("Enter the second DNA sequence: ")
            dna2 = dna2.upper()

            valid = True

            for base in dna2:
                if base not in "ATGC":
                    valid = False
                    break
            if not valid:
                print("Please enter a valid DNA strand")
            elif len(dna) != len(dna2):
                print("The sequences must have the same length of",
                    len(dna), "bases")
            else:
                break
        print("given DNA strand =", dna)
        print("the second strand =", dna2)
        same = True

        for i in range(len(dna)):
            if dna[i] != dna2[i]:
                print("Position", i + 1, "does not match:",
                  dna[i], "vs", dna2[i])
                same = False

        if same:
            print("The bases are the same in both strands given.")


        if same:
            results["Comparison"] = "Sequences are identical"
        else:
            results["Comparison"] = "Sequences have differences"
        
    elif choice == 6:
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
        break

   
    elif choice == 7:
        break
