import re
PATH = "todo_fexhasnom"
regex_fechahora = re.compile(r"[0-9][0-9]?(/|-)[0-9][0-9]?(/|-)([0-9][0-9])?[0-9][0-9]?,? [0-9][0-9]?:[0-9][0-9]:?([0-9][0-9])?:? (((a. ?m.|p. ?m.)|(AM|PM))? ?(:|-))? ?") #memo
regexQuitarNombre = re.compile("^.*?:\s")

def preprocesamiento(s_texto):
	s_texto = regex_fechahora.sub("",s_texto)
	s_texto = regexQuitarNombre.sub("H:",s_texto)
	return s_texto

f=open('todo_pre.txt', 'w')


with open('todo.txt') as file:
        s_texto = file.read()
        #lo preproceso
        s_texto = preprocesamiento(s_texto)
        f.write(s_texto)
        print (s_texto)
f.close()
