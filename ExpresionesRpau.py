archivo_abierto=open('todo.txt')
texto=archivo_abierto.read()
#print(texto)

import re

expresion_larga=re.compile(r"\*.*?\*")
#expresion_corta=re.compile(r"\*\*.*?\*\*")
resultados_largos=expresion_larga.finditer(texto)
#resultados_cortos=expresion_corta.finditer(texto)
for resultado in resultados_largos:
	print(resultado.group(0))
	print()
	
#for resultado in resultados_cortos:
	#print(resultado.group(0))

archivo_abierto.close()
