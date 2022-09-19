def check_sequense (s):
    n_nucleotides = s.count('a') + s.count('t') + s.count('c') + s.count('g') \
                      + s.count('A') + s.count('T') + s.count('C') + s.count('G')
    if n_nucleotides == len(s):
      return True
    else:
      return False

def transcribe (s):
    new_s = []
    for i in s:
        if i == 't':
            new_s.append('u')
        elif i == 'T':
            new_s.append('U')
        else:
            new_s.append(i)
    return ''.join(new_s)

def reverse (s):
    new_s = []
    for i in range(len(s)):
        new_s.append(s[-i-1])
    return ''.join(new_s)

def complement (s):
    new_s = []
    nucl_compl = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c', 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in range(len(s)):
        new_s.append(nucl_compl[s[i]])
    return ''.join(new_s)

def reverse_complement (s):
    new_s = []
    nucl_compl = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c', 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in range(len(s)):
        new_s.append(nucl_compl[s[-i-1]])
    return ''.join(new_s)


while 1 > 0:
    print ("Please enter command")
    command = input()
    if command == 'exit':
        break
    print ("Please enter DNA sequense")
    sequense = input()
    if check_sequense (sequense) == False:
        print ("Your sequence isn't a DNA sequence. Please try again")
    else:
        if command == 'transcribe':
            print (transcribe(sequense))
        elif command == 'reverse':
            print (reverse(sequense))
        elif command == 'complement':
            print (complement(sequense))
        elif command == 'reverse_complement':
          print (reverse_complement(sequense))
        else:
            print ("Sorry. I can't do that. 0^0")
    
print ('Thank you for using our tool')