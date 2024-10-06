# A program to calculate the frequency of bases in the DNA sequence 
file1 = "DNA.txt"
f = open(file1 , 'r')
DNA = f.read()
'''DNA = "GCATTCTGAGGCATTCTCTAACAGGTTCTC"'''
print("The orignal DNA: ", DNA)
G =(DNA.count('G')/len(DNA))
C =(DNA.count('C')/len(DNA))
A =(DNA.count('A')/len(DNA))
T =(DNA.count('T')/len(DNA))

print("The frequency of base G is: ", G)
print("The frequency of base C is: ", C)
print("The frequency of base A is: ", A)
print("The frequency of base T is: ", T)
