import os
for filename in os.listdir(os.getcwd()):
	if(filename != "Criarimagens.py"):
		if(filename != "imagens.tex"):
			if(filename != "criar.sh"):
				print("%%Imagem "+filename)
				print("\\begin{center}")
				print("\\resizebox{1\\columnwidth}{!}{\\includegraphics{{imagens/"+filename+"}}}")
				print("\\begingroup")
				print("\\fontsize{7pt}{10pt}\\selectfont")
				print("\\\\\\textit{Nome da figura}: descricao da figura\\\\ ")
				print("\\endgroup")
				print("\\end{center}")
				print("  ")
