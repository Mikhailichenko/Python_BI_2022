The **_main_** function filters reads by **GC content**, filters reads by **quality**, filters reads by **length**, **saves** the results in a file.

The **main** function takes **arguments**:
1. **input_fastq** - the path to the file that is fed to the input of the program.
2. **output_file_prefix** - path prefix to the file where the result will be written. "_passed.fastq" is added to the prefix for a file with filtered reads and "_failed.fastq" for files with filtered reads (only if the save_filtered argument is True).
3. **gc_bounds** - GC content interval (in percent) for filtering. If a single number is passed to the argument, then it is considered to be the upper bound. The default range is from 0 to 100.
4. **length_bounds** - length interval for filtering, everything is similar to gc_bounds. By default, the interval is from 0 to 2^32.
5. **quality_threshold** - average read quality threshold for filtering, by default equals 0 (phred33 scale). Reads with average quality for all nucleotides below the threshold are discarded.
6. **save_filtered** - whether to save filtered reads, default is False.
