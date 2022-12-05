# Программы имитирующие утилиты UNIX 


To make programs executable, run the following command line command from the utilities folder

> chmod +x *.py


Each program is in a separate script, which is named after the template *<utility_name>.py*.


### 1. wc 

Count newline, word, and byte for a file

Options:
- **-l** print number of newline
- **-w** print number of bytes words
- **-c** print number of bytes

Use comand ./wc.py to count newline, word, and byte for a file

> ./wc.py \<path to file>

Or select options you need  
  
> ./wc.py -l \<path to file>
> ./wc.py -l -с \<path to file>

The utility can work in pipelines
  
### 2. ls 

Print list of directory contents
  
Option:
- **-a** show hidden objects too
  
> ./ls.py \<path to dir>
> ./ls.py -a \<path to dir>

Default - current folder  
  
### 3. sort

Sort lines of text files in alphabetical order
  
> ./sort.py \<path to file>

The utility can work in pipelines  
  

### 4. rm with -r option

Remove a file or directory

  
Option:
- **-r** recursively remove directories and their contents
  
> ./rm.py \<path to file>
> ./rm.py \<path to dir>
> ./rm.py -r \<path to dir>

  
### 5. cat
Concatenate files and print on the standard output

> ./cat.py \<path to file>  
> ./cat.py \<path to file1> \<path to file2>  
> ./cat.py \<path to file1> <...> \<path to fileN> 

The utility can work in pipelines
  
### 6. tail with -n option
Output the last N (default N = 10) rows of files

Option:
- **-n** output the last N lines, instead of the last  10; or  use  -n +N to output starting with line N
> ./tail.py \<path to file> 
> ./tail.py -n 5 \<path to file> 
> ./tail.py -n +5 \<path to file> 
  
The utility can work in pipelines
  
### 7. ln
Make links

Option:
- **-s** make symbolic links instead of hard links

> ./ln.py \<path to file> \<path to link>
> ./ln.py -s \<path to file> \<path to link>

### 8. cp with -r option
Copy files and directories

Option:
- **-r** recursively copy directories and their contents

> ./cp.py \<path to file> \<path to dir for copy>
> ./cp.py \<path to dir> \<path to dir for copy>
> ./cp.py -r \<path to dir> \<path to dir for copy>

### 9. mv 
Move (rename) files

> ./mv.py \<path to file> \<path to dir where files should be moved>
