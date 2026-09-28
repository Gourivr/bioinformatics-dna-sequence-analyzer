from dna_validation import validate_dna
from dna_operations import reverse_comp
from dna_analysis import calculate_gc_content
from translation import translate_rna
from sequence_comparison import compare_sequences
from report import display_report

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

    if validate_dna(dna):
        print()
        break
    else:
        print("Please enter a valid DNA strand")


def rna_con(dna):
    rna = dna.replace("T", "U")
    return rna


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
        a, t, g, c, gc_percentage = calculate_gc_content(dna)
        print("Adenine count =", a)
        print("Thymine count =", t)
        print("Guanine count =", g)
        print("Cytosine count =", c)
        print("GC percentage =", gc_percentage, "%")

        results["GC Content"] = gc_percentage

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
    elif choice == 4:
        rna = rna_con(dna)

        print("The codons and the proteins synthesised are as follows:")
        print("The RNA is", rna)

        protein = translate_rna(rna)

        results["Protein"] = protein
            

    
    elif choice == 5:
        while True:
            dna2 = input("Enter the second DNA sequence: ")
            dna2 = dna2.upper()

            if not validate_dna(dna2):
                print("Please enter a valid DNA strand")
            elif len(dna) != len(dna2):
                print("The sequences must have the same length of",
                      len(dna), "bases")
            else:
                break

        print("given DNA strand =", dna)
        print("the second strand =", dna2)

        differences = compare_sequences(dna, dna2)

        if not differences:
            print("The bases are the same in both strands given.")
            results["Comparison"] = "Sequences are identical"
        else:
            for difference in differences:
                print(difference)

            results["Comparison"] = "Sequences have differences"
        
    elif choice == 6:
        display_report(dna, results)
        break

   
    elif choice == 7:
        break
