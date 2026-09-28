def calculate_gc_content(dna):
    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    gc_percentage = (g + c) / len(dna) * 100

    return a, t, g, c, round(gc_percentage, 2)