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

## Output
- AMRFinder_genes_matrix.csv
- AMRFinder_gene_class_matrix.csv

## Input
AMRFinderPlus combined output CSV file
