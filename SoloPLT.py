archivo_abierto=open('todo.txt')
texto=archivo_abierto.read()
#print(texto)

import re

expresion_larga=re.compile(r"\*\^* Respeto a las mujeres *\*")
#expresion_corta=re.compile(r"\*\*.*?\*\*") larga(r"\*.*?\*")
resultados_largos=expresion_larga.finditer(texto)
#resultados_cortos=expresion_corta.finditer(texto)
#\[.+]
#\<\<-+>
f=open('PLTvigulilla.txt','w')


with open('todo.txt') as file:
	for resultado in resultados_largos:
		resultados_largos = file.read()
		f.write(resultados_largos)
		print('***********')
		print(resultados_largos)
		print('***********')
	#print()
	
#for resultado in resultados_cortos:
#	print(resultado.group(0))

archivo_abierto.close()
f.close()
