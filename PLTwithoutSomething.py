import re


expresion_larga=re.compile(r"\-.+-")

	
with open('todo.txt','r') as f:
	for linea in f.read().split('\n'):
		if expresion_larga.match(linea):
			print ('*****************')
			print (expresion_larga)
			print('*****************')
			

#for linea in 'resultados_cortos':
#	if linea== ': <Archivo omitido>':
#		continue
#	print(resultados_cortos), texto
