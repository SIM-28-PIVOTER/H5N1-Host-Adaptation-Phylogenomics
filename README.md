# H5N1 Host-Adaptation & Phylogenomics Pipeline

An automated computational workflow for processing Influenza A (H5N1) PB2 gene sequences, conducting multiple sequence alignments, screening key host-adaptation amino acid mutations, and building phylogenetic trees.

## Overview
This repository contains a lightweight, reproducible bioinformatics pipeline developed in WSL2 (Ubuntu 22.04) to evaluate genetic markers associated with avian-to-mammalian adaptation.

## Pipeline Workflow
1. **Sequence Alignment**: Aligns raw fasta sequences using `MAFFT` (`--auto`).
2. **Mutation Screening**: Uses `scan_mutations.py` (Python/Biopython) to extract key phenotypic markers at PB2 positions 591, 627, and 701.
3. **Phylogenetic Inference**: Infers Maximum-Likelihood phylogenetic trees using `IQ-TREE 2` with automatic model selection (`-m MFP`).

## Project Structure
* `scan_mutations.py` - Python script for identifying host-adaptation mutations.
* `metadata.csv` - Sample metadata and isolation source details.
* `pb2_sequences.fasta` - Input sequence data.
* `pb2_aligned.fasta` - MAFFT aligned fasta output.
* `pb2_aligned.fasta.treefile` - Maximum-Likelihood tree in Newick format.
* `mutation_summary.csv` - Output matrix summarizing predicted viral phenotypes.

## Requirements
* WSL2 / Ubuntu 22.04
* MAFFT v7+
* IQ-TREE v2+
* Python 3.10+ (Biopython, pandas)
