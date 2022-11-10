

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import matplotlib.font_manager as font_manager
import matplotlib.ticker as ticker
from matplotlib.patches import ConnectionPatch


def read_bed6(path, headers = ["chromosome","start", "end", "name", "score", "strand"]):
    alignment = pd.read_table(path, header=None, names = headers)
    return alignment

alignment = read_bed6("/content/alignment.bed")
alignment


def read_gff(path, headers = ["chromosome", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]):
    annotation = pd.read_table(path, header=0, names = headers)
    return annotation

rrna_annotation = read_gff("/content/rrna_annotation.gff")
rrna_annotation


def what_attribut(a):
    if "5S_rRNA" in a:
        return "5S"
    elif "23S_rRNA" in a:
        return "23S"
    elif "16S_rRNA" in a:
        return "16S"
    else:
        return "NA"


rrna_annotation["attributes"] = rrna_annotation["attributes"].apply(what_attribut)
rrna_annotation



#without table
g = sns.catplot("chromosome", hue="attributes",
                data=rrna_annotation,
                kind="count")
plt.xticks(rotation=90)
plt.show()



#with table
rrna_annotation['count'] = rrna_annotation['attributes']
rrna_annotation_count = rrna_annotation.groupby(['chromosome', 'attributes'], as_index=False).agg({"count": "count"})
rrna_annotation.drop(columns = ['count'],axis = 1)
rrna_annotation_count
sns.barplot(data = rrna_annotation_count, x ='chromosome', y = 'count', hue = 'attributes')
plt.xticks(rotation=90)
plt.legend(title = 'RNA type', loc = 'upper right')

plt.show()




def check_intervals_intersect(a_start, a_end, b_start, b_end):
    are_intersect = b_start<a_start and b_end>a_end
    return are_intersect

def function1(rrna_annotation_row, alignment_row, df):
    alignment.apply(function, axis=1)

def function (rrna_annotation_row, alignment_row, df):
    if check_intervals_intersect(alignment["start"], alignment["end"], rrna_annotation["start"], rrna_annotation["end"]):
        temp = [rrna_annotation_row, alignment_row]
        df.loc[ len(df.index )] = temp
    return None

headers = ["chromosome", "source", "type", "start_x", "end_x", "score_x", "strand_x", "phase", "attributes", "start_y", "end_y", "name_y"]
df_intersect = pd.DataFrame(columns=headers)
df_intersect
rrna_annotation.apply(function1, axis=1)
for i in range(len(rrna_annotation.index)):
    for j in range(len(alignment.index)):
        function(rrna_annotation.iloc[i:(i+1), :], alignment[j:(j+1), :], df_intersect)






diffexp = pd.read_table("/content/diffexpr_data.tsv")
diffexp
fig, ax = plt.subplots()
limit_p_val = -math.log10(0.05)

ax.scatter(data=diffexp.loc[(diffexp['logFC'] < 0) & (diffexp['log_pval'] >= limit_p_val)], x="logFC", y="log_pval",
           c = 'b', s = 10)
ax.scatter(data=diffexp.loc[(diffexp['logFC'] >= 0) & (diffexp['log_pval'] >= limit_p_val)], x="logFC", y="log_pval",
           c = 'orange', s =10)
ax.scatter(data=diffexp.loc[(diffexp['logFC'] < 0) & (diffexp['log_pval'] < limit_p_val)], x="logFC", y="log_pval",
           c = 'g', s =10)
ax.scatter(data=diffexp.loc[(diffexp['logFC'] >= 0) & (diffexp['log_pval'] < limit_p_val)], x="logFC", y="log_pval",
           c = 'r', s =10)
  
plt.title('Volcano plot', style = 'italic', fontweight='bold', color='k', fontsize=25)
plt.xlabel('log$_{2}$(fold change)', style = 'italic', fontweight='bold', fontsize=20)
plt.ylabel('-log$_{10}$(p value corrected)', style = 'italic', fontweight='bold', fontsize=20)

font = font_manager.FontProperties(weight='bold',
                                   style='normal', size=15)

ax.legend(['Significantly downregulated','Significantly upregulated','Non-significantly downregulated','Non-significantly upregulated'], 
             shadow = True, prop=font , loc="upper right", markerscale = 4)

plt.axhline(y= limit_p_val, color='grey',linewidth=2.0, linestyle='dashed')
plt.axvline(x=0, color='grey',linewidth=2.0, linestyle='dashed')
plt.text(8, 1+limit_p_val, 'p-value = 0.05', fontsize = 15,  color='grey')
plt.rcParams.update({'font.size': 10, 'font.weight': 'bold'})

a = max(abs(float(diffexp.iloc[:,[1]].min(axis=0))), abs(float(diffexp.iloc[:,[1]].max(axis=0))))
plt.xlim([-a-1, a+1])

ax.tick_params(axis = 'both', which = 'major', length = 7, width = 4, pad = 2, labelsize = 15,
               bottom = True, left = True, labelbottom = True, labelleft = True)

ax.tick_params(axis = 'both', which = 'minor', direction = 'out', length = 4,
               width = 1, bottom = True, left = True) 
ax.minorticks_on()

ax.spines['bottom'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)


annot = (diffexp.loc[(diffexp['log_pval'] >= limit_p_val)])
annot = annot.sort_values("logFC", ascending=False)
annot = pd.concat([annot.head(2), annot.tail(2)])
for idx, row in annot.iterrows():
    ax.annotate(row['Sample'], (row['logFC'], row['log_pval']), (row['logFC']+0.2, row['log_pval']+10),'data',
                arrowprops=dict(facecolor='red', shrink=0.05), 
                size=10)

fig.set_figwidth(16) 
fig.set_figheight(8)

plt.show()



table_for_pie = pd.read_excel("/content/table_for_pie.xlsx")
table_for_pie
fig, ax = plt.subplots(figsize=(20, 6), subplot_kw=dict(aspect="equal"))

ax2 = fig.add_subplot(122)


labels = list(table_for_pie['Group'][0:16])
labels.append("Others")

ratios = list(table_for_pie['Count'][0:16])
ratios.append(sum(table_for_pie['Count'][16:]))

percent = list(table_for_pie["Percent"][0:16])
percent.append(round(100*sum(table_for_pie['Count'][16:])/sum(table_for_pie['Count']), 2))
 
wedges, texts = ax.pie(ratios, startangle=30*ratios[0], explode= [0.05]*17)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(f'{labels[i]}\n{percent[i]}%', xy=(x, y), xytext=(1.35*np.sign(x), 1.2*y),
                horizontalalignment=horizontalalignment, ha='center', 
                size=7, **kw)



xpos = 0
bottom = 0
ratios2 = list(table_for_pie['Count'][16:])
width = .2
colors = [i for i in range(16, table_for_pie.shape[0])]

for j in range(len(ratios2)):
    height = ratios2[j]
    ax2.bar(xpos, height, width, bottom=bottom)
    ypos = bottom + ax2.patches[j].get_height()/2
    bottom += height
    if ratios2[j] != 1:
        ax2.text(xpos+0.5*width,ypos, ratios2[j], ha='left', size = 6)


theta1, theta2 = ax.patches[16].theta1, ax.patches[16].theta2
center, r = ax.patches[16].center, ax.patches[16].r
bar_height = sum([item.get_height() for item in ax2.patches])
x = r*np.cos(math.pi/180*theta2)+center[0]
y = np.sin(math.pi/180*theta2)+center[1]
con = ConnectionPatch(xyA=(-width/2,bar_height), xyB=(x,y), coordsA="data", coordsB="data",
                      axesA=ax2, axesB=ax)
con.set_color([0,0,0])
con.set_linewidth(1)
ax2.add_artist(con)

x = r*np.cos(math.pi/180*theta1)+center[0]
y = np.sin(math.pi/180*theta1)+center[1]
con = ConnectionPatch(xyA=(-width/2,0), xyB=(x,y), coordsA="data", coordsB="data",
                      axesA=ax2, axesB=ax)
con.set_color([0,0,0])
ax2.add_artist(con)
con.set_linewidth(1)

plt.axis('off')
plt.xlim(-5*width, 5*width)


plt.show()