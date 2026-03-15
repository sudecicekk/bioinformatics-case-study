# Mini-Bioinformatics Pipeline & Reporting

This project is a reproducible bioinformatics pipeline designed to perform Quality Control (QC) on long-read sequencing data. It was developed for **Professor Kılıç** to analyze raw FASTQ data before proceeding with alignment.

## Features
- **Fastq Analysis:** Custom Python script to calculate GC content, read length, and Phred quality scores.
- **Workflow Management:** Integrated with **Nextflow** for reproducibility.
- **Visualization:** Automated plotting of key metrics using Matplotlib and Seaborn.

## How to Run
1. Ensure you have Python 3.x installed with `pandas`, `matplotlib`, and `seaborn`.
2. Run the analyzer:
   ```bash
   python fastq_analyzer.py barcode77.fastq.gz read_statistics.csv 
   python visualize_results.py