nextflow.enable.dsl=2

params.input_file = "barcode77.fastq.gz"
params.outdir = "results"

process ANALYZE_FASTQ {
    
    publishDir params.outdir, mode: 'copy'

    input:
    path fastq_file

    output:
    path "read_statistics.csv"

    script:
    """
    python ${baseDir}/fastq_analyzer.py
    """
}

workflow {
    fastq_ch = Channel.fromPath(params.input_file)

    ANALYZE_FASTQ(fastq_ch)
}