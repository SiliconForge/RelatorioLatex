import os

filelist = open('filelist', 'w')
for filename in os.listdir(os.getcwd()):
  print>>filelist, filename
filelist.close()

with open('filelist', 'r') as f1, open('ignore', 'r') as f2:
    a = f1.readlines()
    b = f2.readlines()
f1.close()
f2.close()
os.remove('filelist')

non_duplicates = [line for line in a if line not in b]
non_duplicates += [line for line in b if line not in a]

non_duplicates = map(lambda s: s.strip(), non_duplicates)

os.remove('imagens-snippets.tex')

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
