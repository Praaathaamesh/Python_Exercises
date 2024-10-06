# Calculate the properties of user-defined peptide sequence (length, molecular weight, count of hydrophobic and hydrophilic residues). (Use file Handling)

file1 = "PROT.txt"
f = open(file1, 'r')
seq = f.read()

# Length of peptide sequence
length = len(seq)
print(f"length of the peptide sequence: {length} AA")
# Molecular weight of each aa
weights = {
    "A": 71.037114,"R": 156.101111,"N": 114.042927,"D": 115.026943,"C": 103.009185,
    "E": 129.042593,"Q": 128.058578,"G": 57.021464,"H": 137.058912,"I": 113.084064,
    "L": 113.084064,"K": 128.094963,"M": 131.040485,"F": 147.068414,"P": 97.052764,
    "S": 87.032028,"T": 101.047679,"U": 150.95363,"W": 186.079313,"Y": 163.06332,
    "V": 99.068414,"X": 0, "B": 113.084064, "Z": 0 }
Mol = 0
for i in seq:
    Mol += weights[i]
Final_Mol = Mol - (18* (len(seq)-1))
print("Final molecular weight of the sequence: ", Final_Mol, "Da")

# count hydrophobic and hydrophillic amino acids
Hypho =  ['A', 'C', 'I', 'L', 'M', 'F', 'W', 'V']
Neut = ['G', 'H', 'P', 'S', 'T', 'Y']
Hyphi=  ['R', 'N', 'D', 'Q', 'E', 'K']

for i in Hypho:
    print(f"The count of hydrophobic amino acid {i} is {seq.count(i)}")
for j in Hyphi:
    print(f"The count of hydrophillic amino acid {j} is {seq.count(j)}")
