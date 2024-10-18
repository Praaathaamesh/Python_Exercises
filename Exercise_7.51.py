# insertion, substitution and deletion mutation
import random
base = ['T','A','G','C']

#insertion
DNA = "ATGCGCTAGCTAGGCT"
print("original sequence: ",DNA)
DNA_ind = random.randint(0, len(DNA)-1)
base_ind = random.randint(0, len(base)-1)
DNA_list = list(DNA)
DNA_list.insert(DNA_ind, base[base_ind])
DNA = ''.join(DNA_list)
print("After insertion mutation: ",DNA)
print()

#Deletion
DNA = "ATGCGCTAGCTAGGCT"
print("original sequence: ",DNA)
DNA_ind = random.randint(0, len(DNA)-1)
base_ind = random.randint(0, len(base)-1)
DNA_list = list(DNA)
DNA_list.pop(DNA_ind)
DNA = ''.join(DNA_list)
print("After deletion mutation: ",DNA)
print()

#Substitution
DNA = "ATGCGCTAGCTAGGCT"
print("original sequence: ",DNA)
DNA_ind = random.randint(0, len(DNA)-1)
base_ind = random.randint(0, len(base)-1)
DNA_list = list(DNA)
DNA_list.pop(DNA_ind)
DNA_list.insert(DNA_ind, base[base_ind])
DNA = ''.join(DNA_list)
print("After substitution mutation: ", DNA)
print()
