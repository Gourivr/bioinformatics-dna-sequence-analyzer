def reverse_comp(dna):
            compliment=''
            pair={'A':'T','T':'A',
             'G':'C','C':'G'}
            for base in dna:
                compliment += pair[base]
            return compliment[::-1]