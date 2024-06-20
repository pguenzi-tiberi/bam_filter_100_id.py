import pysam

input_bam = "bowles_all_file_its_pp_mapped_sorted.bam"
output_bam = "perfect_matches.bam"

with pysam.AlignmentFile(input_bam, "rb") as bamfile, pysam.AlignmentFile(output_bam, "wb", template=bamfile) as outf:
    for read in bamfile.fetch(until_eof=True):
        if read.has_tag("MD"):
            md_tag = read.get_tag("MD")
            if all(char.isdigit() for char in md_tag.replace('^', '')):
                # This means there are no mismatches, deletions or insertions in the aligned part
                outf.write(read)
