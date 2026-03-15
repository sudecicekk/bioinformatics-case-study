import gzip
import csv 
import sys

input_fastq = sys.argv[1] 
output_csv = sys.argv[2]

def calculate_gc_content(sequence):
    """Calculates G/C percentage."""
    if len(sequence) == 0: return 0
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    return (gc_count / len(sequence)) * 100

def calculate_mean_quality(quality_string):
    """Converts ASCII to Phred scores and calculates mean."""
    if not quality_string: return 0
    scores = [ord(char) - 33 for char in quality_string]
    return sum(scores) / len(scores)

def analyze_fastq(file_path, output_path):

    with gzip.open(file_path, "rt") as handle, open(output_path, "w", newline='') as csvfile:
        
        fieldnames = ['read_id', 'length', 'gc_content', 'mean_quality']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() 

        count = 0
        while True:
            header = handle.readline().strip()
            if not header: break 
            
            sequence = handle.readline().strip()
            plus = handle.readline().strip()
            quality = handle.readline().strip()

            
            read_id = header.split()[0] 
            length = len(sequence)
            gc_val = calculate_gc_content(sequence)
            mean_qual = calculate_mean_quality(quality)

            
            writer.writerow({
                'read_id': read_id,
                'length': length,
                'gc_content': round(gc_val, 2),
                'mean_quality': round(mean_qual, 2)
            })
            
            count += 1
            
            if count % 1000 == 0:
                print(f"Processed {count} reads...")

    print(f"Analysis complete! Total reads processed: {count}")
    print(f"Results saved to: {output_path}")

if __name__ == "__main__":
    analyze_fastq(input_fastq, output_csv)