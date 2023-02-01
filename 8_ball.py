# Online Python - IDE, Editor, Compiler, Interpreter

import random

s_response_0 = "Sigue intentándolo"
s_response_1 = "Seguro que sí"
s_response_2 = "No cuentes con ello"
s_response_3 = "Estarás mejor si piensas en otra cosa"
s_response_4 = "Eso no va a compilar"
s_response_5 = "Lo veo claro, pero aun tienes que esperar"
s_response_6 = "Se que lo conseguirás"
s_response_error = "Se ha producido un error"

print("Pregunta algo")
question = input()

n_rndm = random.randint(0, 6)
print(n_rndm)

if n_rndm == 0:
    print(s_response_0)
elif n_rndm == 1:
    print(s_response_1)
elif n_rndm == 2:
    print(s_response_2)
elif n_rndm == 3:
    print(s_response_3)
elif n_rndm == 4:
    print(s_response_4)
elif n_rndm == 5:
    print(s_response_5)
elif n_rndm == 6:
    print(s_response_6)
else:
    print(s_response_err
    
    
