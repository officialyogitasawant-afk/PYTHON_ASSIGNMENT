# Codon Table Generator

A Python program that builds the standard genetic code (all 64 codons), accepts a DNA or RNA sequence, validates it, divides it into codons, translates each codon into its amino acid, and identifies start and stop codons.


## Features

- Dictionary of all 64 codons and their amino acids (standard genetic code)
- Input validation: DNA accepts only `A, T, G, C`; RNA accepts only `A, U, G, C`
- Re-prompts until the sequence type and the sequence are valid
- Divides the sequence into codons of three nucleotides
- Translates each codon using the codon table
- Identifies the start codon (`ATG` / `AUG`) and stop codons (`TAA, TAG, TGA` / `UAA, UAG, UGA`)
- Handles an incomplete codon at the end (reported, not translated)
- Displays the full codon table and the result in table format
- **Additional challenge:** RNA input (T is replaced by U; codons are shown with U)

## Files

| File | Purpose |
|------|---------|
| `code.py` | Main program |
| `compare_codon_tables.py` | Compares our table with the NCBI standard genetic code |
| `README.md` | Documentation |

## How to run

```bash
python code.py
```

1. Enter the sequence type: `DNA` or `RNA`
2. The codon table is displayed
3. Enter the sequence
4. The translation table and summary are displayed

## How it works

1. **Dictionary** - `codon_table` maps each of the 64 DNA codons to an amino acid or `Stop`.
2. **Sequence type** - a `while` loop repeats until the user enters DNA or RNA.
3. **Codon table display** - nested loops print the table in the layout of the assignment figure.
4. **Validation** - `all(base in valid_bases ...)` rejects any other character; empty input is rejected too.
5. **RNA conversion** - `U` is replaced by `T` so the same dictionary works for both.
6. **Splitting** - `range(0, len(sequence), 3)` slices the sequence into groups of three.
7. **Translation** - each complete codon is looked up in the dictionary; `ATG` is marked Start, and `TAA`, `TAG`, `TGA` are marked Stop.
8. **Incomplete codons** - a final group shorter than three is marked "Not translated" and a warning is printed.
9. **Display** - results are shown as a table followed by a summary.

## Sample runs

### DNA: `ATGGCTTTTTAA`

```
No.  Codon   Amino acid        Note
----------------------------------------
1    ATG     Methionine        Start
2    GCT     Alanine
3    TTT     Phenylalanine
4    TAA     Stop              Stop
----------------------------------------
Codons: ATG - GCT - TTT - TAA
Amino acids: Methionine - Alanine - Phenylalanine - Stop
Start codon(s): ATG
Stop codon(s): TAA
All codons contain three nucleotides.
```

### RNA with an incomplete codon: `AUGGCUUUUUAAGC`

```
No.  Codon   Amino acid        Note
----------------------------------------
1    AUG     Methionine        Start
2    GCU     Alanine
3    UUU     Phenylalanine
4    UAA     Stop              Stop
5    GC      Incomplete codon  Not translated
----------------------------------------
Warning: Incomplete codon 'GC' at the end was not translated.
```

### Invalid input

`ATGX` in DNA mode, or `AUGT` in RNA mode, gives an error message and the program asks again.

## Comparison with online codon tables (Requirement 9)

Run:

```bash
python compare_codon_tables.py
```

The script reads our dictionary and compares all 64 entries with the NCBI standard genetic code. **Result: all 64 codons match.**

### Differences in structure compared with GitHub repositories

| Feature | This project | Typical GitHub repositories |
|---------|--------------|-----------------------------|
| Amino acid names | Full names (`Methionine`) | One-letter (`M`) or three-letter (`Met`) |
| Stop codons | `"Stop"` | `"*"` or `"STOP"` |
| Codon letters | DNA (`ATG`), RNA converted | Often RNA only (`AUG`) |
| Layout | Flat dictionary | Sometimes nested by first/second/third letter |

### Repositories reviewed

<!-- Replace with the repositories you looked at, for example:
1. https://github.com/<user>/<repo> - what you noticed
2. https://github.com/<user>/<repo> - what you noticed -->

## Learning outcomes

Python dictionaries, loops, conditional statements, string manipulation, input validation, and basic biological sequence analysis.

## Author

Yogita Krishnakumar Sawant
