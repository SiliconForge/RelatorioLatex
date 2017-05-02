#!/usr/bin/python

import os

filelist=[]
ignore=[]

for filename in os.listdir(os.getcwd()):
  filelist.append(filename)  

try:
    with open('ignore', 'r') as f2:  
        b = f2.readlines()
    for line in b:
        ignore.append(line.strip())
    f2.close()
except OSError:
    print "Error"
    pass

non_duplicates = set(filelist).difference(set(ignore))
non_duplicates = filter(None, non_duplicates)

listaimagens = open('imagens-snippets.tex', 'w')

for item in non_duplicates:
	print>>listaimagens, "%%Imagem "+item
	print>>listaimagens, "\\begin{figure}[h]"
	print>>listaimagens, "\\resizebox{0.5\\columnwidth}{!}{\\includegraphics{imagens/"+item+"}}"
	print>>listaimagens, "\\caption{Legenda}"
	print>>listaimagens, "\\label{fig:"+item+"}"
	print>>listaimagens, "\\end{figure}"
	print>>listaimagens, "  "

listaimagens.close()





