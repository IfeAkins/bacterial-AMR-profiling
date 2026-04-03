# Bacterial AMR Profiling Scripts

Python scripts for parsing and analyzing 
[AMRFinderPlus ](https://github.com/ncbi/amr) output files.

## What it does
- Loads AMRFinderPlus combined output
- Filters AMR elements only (removes stress, virulence)
- Filters by coverage > 80%
- Builds gene presence/absence matrix
  (genes grouped under drug class)
- Builds drug class presence/absence matrix
- Reports summary statistics
- Saves matrices as CSV files ready for 
  downstream analysis

## Requirements
- Python 3
- pandas (pip install pandas)

## Usage
python amrfinder_matrix.py

## Input
AMRFinderPlus combined output CSV file

## Output Files

### AMRFinder_genes_matrix.csv
Presence/absence matrix (1=present, 0=absent) 
of individual AMR genes per isolate, 
with genes grouped under their drug class.

### AMRFinder_gene_class_matrix.csv
Count matrix showing the number of AMR genes 
per drug class per isolate. For example, 
a value of 3 means the isolate carries 
3 genes belonging to that drug class.

## Example Data
Example input and output files are provided 
in the `example_data/` folder, using data 
from the following published study:

[Akintayo et al. (2026) PLOS Water](https://journals.plos.org/water/article?id=10.1371/journal.pwat.0000419)

- `example_amrfinder_result.csv` → example AMRFinderPlus input (10 isolates)
- `AMRFinder_genes_matrix.csv` → gene presence/absence matrix
- `AMRFinder_gene_class_matrix.csv` → drug class count matrix
