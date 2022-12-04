## Task 1. Working with real data

The **read_gff** and **read_bed6** functions have been implemented to open GFF and BED6 type files.

The attached files contain an annotation of ribosomal RNA of some metagenomic dataset _rrna_annotation.gff_, as well as a file with alignment of the metagenomic assembly to the same _alignment.bed_ dataset.


The attribute column carried too much redundant information. For convenience of use, only data on the **type** of rRNA were left in one short line (16S, 23S, 5S).
For visualization, a table was created, where for each chromosome the number of rRNA of each type is shown. A barplot was built to display this data.


## Task 2. Chart customization

### Volcano plot

A Volcano plot was built to visualize differential gene expression data. On the X axis, logFC (Logarithmic Fold Change) is plotted on it - how many times the gene expression has changed in powers of two. The Y-axis plots the level of significance of these changes as the negative logarithm of the p-value (adjusted for multiple comparisons).

### Pie chart. 

The graph is built on dataset that was generated independently.
