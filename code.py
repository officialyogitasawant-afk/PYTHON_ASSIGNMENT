codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",
    
    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

print("\n===== STANDARD CODON TABLE =====")

for codon, amino_acid in codon_table.items():
    print(codon, ":", amino_acid)

sequence_type = input(
    "\nEnter sequence type (DNA or RNA): "
).strip().upper()

if sequence_type == "DNA" or sequence_type == "RNA":

    sequence = input("Enter the nucleotide sequence: ")
    sequence = sequence.strip().upper()

if sequence_type == "RNA":
        sequence = sequence.replace("U", "T")

if sequence == "":
        print("Error: Sequence cannot be empty.")

elif not all(base in "ATGC" for base in sequence):
        print("Error: Enter only valid DNA/RNA nucleotides.")

else:
      pass

codons = []
for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]
        codons.append(codon)

amino_acids = []
start_codons = []
stop_codons = []

for codon in codons:

    if len(codon) < 3:
        amino_acids.append("Incomplete codon")

    else:
        amino_acid = codon_table[codon]
        amino_acids.append(amino_acid)

if codon == "ATG":
    start_codons.append(codon)

elif codon == "TAA" or codon == "TAG" or codon == "TGA":
    stop_codons.append(codon)

print("\n===== TRANSLATION RESULTS =====")
print("Sequence:", sequence)
print("Codons:", " - ".join(codons))
print("Amino acids:", " - ".join(amino_acids))

if len(start_codons) > 0:
    print("Start codon(s):", ", ".join(start_codons))
else:
    print("Start codon(s): None found")

if len(stop_codons) > 0:
    print("Stop codon(s):", ", ".join(stop_codons))
else:
    print("Stop codon(s): None found")

# Step 10: Check for incomplete codon
if len(sequence) % 3 != 0:
    print("Warning: Incomplete codon at the end.")

else:
    print("All codons contain three nucleotides.")




# comparison with NCBI standard genetic code

import ast

# Step 1: Load our dictionary from code_generator.py without running the program
with open("code.py") as file:
    tree = ast.parse(file.read())

our_table = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and node.targets[0].id == "codon_table":
        our_table = ast.literal_eval(node.value)

# Step 2: Build the NCBI reference table (base order T, C, A, G)
ncbi_string = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
names = {
    "F": "Phenylalanine", "L": "Leucine", "S": "Serine", "Y": "Tyrosine",
    "C": "Cysteine", "W": "Tryptophan", "P": "Proline", "H": "Histidine",
    "Q": "Glutamine", "R": "Arginine", "I": "Isoleucine", "M": "Methionine",
    "T": "Threonine", "N": "Asparagine", "K": "Lysine", "V": "Valine",
    "A": "Alanine", "D": "Aspartic acid", "E": "Glutamic acid",
    "G": "Glycine", "*": "Stop",
}

reference = {}
index = 0
for a in "TCAG":
    for b in "TCAG":
        for c in "TCAG":
            reference[a + b + c] = names[ncbi_string[index]]
            index += 1

# Step 3: Compare
print("Codons in our table:", len(our_table))
print("Codons in NCBI table:", len(reference))

differences = 0
for codon in sorted(reference):
    if our_table.get(codon) != reference[codon]:
        differences += 1
        print("Difference at", codon, "- ours:", our_table.get(codon), "| NCBI:", reference[codon])

if differences == 0:
    print("Result: all 64 codons match the NCBI standard genetic code.")

