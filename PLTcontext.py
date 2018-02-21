archivo_abierto=open("todo.txt")
lista_original=archivo_abierto.readlines()
lista_lineas=[]
#print(texto)

import re

#expresion_larga=re.compile(r"\*.*?\*")

#r".*\*\* .+?\*\*.*"
#r"\*+[^*]*\*+"

expresion_corta=re.compile(r"\* Respeto a las mujeres *")

#(r"\*\^*5\*")Repetida

#(r"\-se ")
# (r"\<.+>\*") CASUALIDAD
#(r"\*.*?\*")

#resultados_largos=expresion_larga.finditer(texto)
#resultados_cortos=expresion_corta.finditer(texto)
#for resultado in resultados_largos:
	#print(resultado.group(0))
	#print()

for linea in lista_original:
	texto=linea.strip()
	if texto :
		lista_lineas.append(texto)


	
for index,linea in enumerate(lista_lineas):
	#print(index,linea)
	resultados_cortos=expresion_corta.search(linea)
	if resultados_cortos:
		print('*****************')
		print(lista_lineas[index -15:index +15])
		print('*****************')
				

	
#~ for x in texto:
	 #~ resultados_cortos=expresion_corta.finditer(x)
	 #~ for resultado in resultados_cortos:
		#~ print(resultado.group(0))
	 
	 
	


archivo_abierto.close()
