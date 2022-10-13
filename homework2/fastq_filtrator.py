#checking GC content according to conditions
def check_gc (seq, gc_bound_min, gc_bound_max):
    gc_content = 100 * (sum(char == "G" or char == "C" for char in seq)) / len(seq)
    if gc_content >= gc_bound_min and gc_content <= gc_bound_max:
        return True
    return False

#checking lenght according to conditions
def check_lenght (seq, length_bound_min, length_bound_max):
    l = len(seq)
    if l >= length_bound_min and l <= length_bound_max:
        return True
    return False

#checking basecall qualities according to conditions
def check_bq (seq_bq, quality_threshold):
    mean_seq_bq = 0
    l = len(seq_bq)
    for i in seq_bq:
        mean_seq_bq += (ord(i) - 33) / l
    if mean_seq_bq >= quality_threshold:
        return True
    return False


def main (input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0, save_filtered = False):

#define bounds for GC content
    if type(gc_bounds) == type(1):
        gc_bound_min = 0
        gc_bound_max = gc_bounds
    else:
        gc_bound_min = gc_bounds[0]
        gc_bound_max = gc_bounds[1]

#define bounds for length
    if type(length_bounds) == type(1):
        length_bound_min = 0
        length_bound_max = length_bounds
    else:
        length_bound_min = length_bounds[0]
        length_bound_max = length_bounds[1]

#open output files
    output_file_passed = f"{output_file_prefix}_passed.fastq"
    f_passed = open(output_file_passed, "w")
    if save_filtered == True:
        output_file_failed = f"{output_file_prefix}_failed.fastq"
        f_failed = open(output_file_failed, "w")

#analise fastq file by lines
    with open(input_fastq) as file:
        count_line = 1
        for line in file:
            if count_line == 1:
                name_seq = line.strip()
                count_line += 1
            elif count_line == 2:
                seq = line.strip()
                count_line += 1
            elif count_line == 3:
                separator = line.strip()
                count_line += 1
            elif count_line == 4:
                seq_bq = line.strip()
                if check_gc (seq.upper(), gc_bound_min, gc_bound_max) and check_lenght (seq, length_bound_min, length_bound_max) and check_bq (seq_bq, quality_threshold):
                    f_passed.write(f"{name_seq}\n{seq}\n{separator}\n{seq_bq}\n")
                elif save_filtered == True:
                    f_failed.write(f"{name_seq}\n{seq}\n{separator}\n{seq_bq}\n")
                count_line = 1

#close output files
    f_passed.close()
    if save_filtered == True:
        f_failed.close()
