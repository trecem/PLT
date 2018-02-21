#-*- coding: utf-8 -*-
import requests

   #Archivo a ser enviado
files = {'file': open('PLT*.+* (sin).txt', 'rb')}
      #Parámetros
params = {'outf': 'tagged', 'format': 'json'}
      #Enviar petición
url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"
r = requests.post(url, files=files, params=params)
      #Convertir de formato json
obj = r.json()

      #Ejemplo, obtener todos los lemas
for sentence in obj:
	for word in sentence:
		print( word["lemma"], word["tag"])
		with open('tag*PLT*.txt','a') as f:
			texto = 'tag es:' word['tag'] + '\n'
			f.write(texto)
