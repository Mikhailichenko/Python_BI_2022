

import re
import seaborn as sns
import matplotlib.pyplot as plt


path_to_references = input("Enter path to file with references\n")
path_to_ftps = input("Enter the path to the file where ftp links will be written\n")
with open(path_to_ftps, "w") as ftps:
    with open(path_to_references, "r") as file1:
        for line in file1:
            op = re.split(r"[\t;\n]", line)
            for i in op:
                imgtag  = re.match(r"ftp.*?\/(.*?\/).*?\..*", i)
                if imgtag:
                    ftps.write(imgtag.group(0)+"\n")




path_to_text = input("Enter the path to the file with the text 2430AD\n")
ans = []
with open(path_to_text, "r") as file1:
    for line in file1:
        ans = ans + re.findall(r'-?\d+\.?\d*', line)
print(ans)


ans = []
with open(path_to_text, "r") as file1:
    for line in file1:
        ans = ans + re.findall(r"[\s\W]*(\w*[Aa]\w*)[\s\W]*", line)
print(ans)



ans = []
with open(path_to_text, "r") as file1:
    for line in file1:
        ans = ans + re.findall(r"[^\".!?]+[!]", line)
for i in range(len(ans)):
    ans[i] = re.sub("^\s+|\n|\r|\s+$", '', ans[i])
print(ans)


ans = set()
with open(path_to_text, "r") as file1:
    for line in file1:
        uws = re.findall(r"[A-Za-z]\w*", line.lower()) #re.findall(r"[A-Za-z]\w+", line.lower()) if we nead words with more then 1 letter 
        ans.update(uws)
ans = list(ans)
lenword = []
for i in ans:
    lenword.append(len(i))
g = sns.histplot(x = lenword, discrete=True, stat='density')
plt.xlabel('Len of word')
plt.ylabel('Density of lenght of unique words')

plt.show()



def brick_tongue(string):
    dictb = dict()
    for i in "еаоуяыи":
        dictb[i] = f"к{i}"
        dictb [i.upper()] = f"К{i.upper()}"
    for i in "AEIOUY":
        dictb[i] = f"K{i}"
        dictb [i.lower()] = f"k{i.lower()}"
        

    ans = []
    l = re.split('([еаоуяыиAEIOUY])', string, flags=re.IGNORECASE)

    ans = list(l[0])
    for i in range(1, len(l), 2):
        t = dictb[l[i]]
        ans.append(t.join(l[i:i+2]))

    ans=''.join(ans)
    return (ans)

print(brick_tongue(input("Enter the word you want to translate into brick language\n")))




def find_n_words_sentences(text, n):
    lines = re.split(r'\s*[!?.]\s*', text)
    ans = []
    for i in lines:
        words = re.findall(r"\w+", i)
        if len(words) == n:
            ans.append(words)
    return ans

text_n = input("Enter the text in which you want to find sentences of length n\n")
n = int(input("Enter n\n"))
print(find_n_words_sentences(text_n, n))