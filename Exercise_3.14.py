# DNA string 
DNAstr = "GGGAAGCGGTATGGGGTCTGCCCAAGGCGT"
# Find ATG first occurance
atg = DNAstr.find('ATG')
print(f"First Occurence of ATG was found at inedx: {atg}")
# Find total GC count
GC_Cont = DNAstr.count("GC")
print(f"Total GC count in given DNA string is {GC_Cont}")