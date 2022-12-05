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

> ./wc.py <path to file>

Or select options you need  
  
> ./wc.py -l <path to file>
> ./wc.py -l -с <path to file>

The utility can work in pipelines
  
### 2. ls 

Print list of directory contents
  
Option:
- **-a** show hidden objects too
  
> ./ls.py <path to dir>
> ./ls.py -a <path to dir>

Default - current folder  
  
### 3. sort

Sort lines of text files in alphabetical order
  
> ./sort.py <path to file>

The utility can work in pipelines  
  

### 4. rm with -r option

Remove a file or directory

  
Option:
- **-r** recursively remove directories and their contents
  
> ./rm.py <path to file>
> ./rm.py <path to dir>
> ./rm.py -r <path to dir>

  
### 5. cat
Concatenate files and print on the standard output

> ./cat.py <path to file>  
> ./cat.py <path to file1> <path to file2>  
> ./cat.py <path to file1> <...> <path to fileN> 

The utility can work in pipelines
  
### 6. tail with -n option
### 7. ln with -s option
### 8. cp with -r option
### 9. mv without options  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
