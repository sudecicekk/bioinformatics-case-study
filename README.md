# Mini-Bioinformatics Pipeline & Reporting

This project is a reproducible bioinformatics pipeline designed to perform Quality Control (QC) on long-read sequencing data. It was developed for Professor Kılıç to analyze raw FASTQ data before proceeding with alignment.

## Features
- Fastq Analysis: Custom Python script to calculate GC content, read length, and Phred quality scores.
- Workflow Management: Integrated with Nextflow for reproducibility.
- Visualization: Automated plotting of key metrics using Matplotlib and Seaborn.

## How to Run
1. Ensure you have Python 3.x installed with `pandas`, `matplotlib`, and `seaborn`.
2. Run the analyzer:
   ```bash
   python fastq_analyzer.py barcode77.fastq.gz read_statistics.csv 
   python visualize_results.py

## Email Draft
To: Professor Kılıç  
Subject: Quality Control Report for Long-Read Sequencing Data (Barcode 77)

Dear Professor Kılıç,

I have completed the initial quality control analysis of the raw sequencing data (barcode77.fastq.gz). Below is a summary of the findings and my recommendations for the next steps.

### Data Interpretation:
* Read Lengths: The distribution shows a mean length of 1,038 bp and a median of 547 bp. This is consistent with expectations for long-read sequencing, showing a good range of fragment sizes.
* GC Content: The average GC content is 53%, which is within the typical biological range and suggests no significant contamination.
* Quality Scores: The mean Phred quality score is 17.9 . While slightly lower than the ideal Q20 threshold, it is sufficient for Oxford Nanopore data and will allow for successful alignment.

### Recommendation:
The data quality is sufficient to proceed. I recommend moving forward with the alignment step using a long-read compatible aligner.

Best regards,  
Sude Çiçek