# Importing modules from packages
from MolOp import GC_Op
from MolOp import AA_Op
from MolOp import MW_Op
# Specifying the sequence
DNA = "AGTACCGAG"
print(f'The total GC content for sequence {DNA} is {GC_Op.GC(DNA)}')
AA_Seq = AA_Op.translate(DNA)
print(f'For given sequence {DNA}, the translated amino acid sequence is {AA_Seq}')
print(f'The total molecular weight for peptide sequence {AA_Seq} is {MW_Op.mw(AA_Seq)}')
