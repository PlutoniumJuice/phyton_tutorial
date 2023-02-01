#bankpin



def guardar_pin():
    b_ok = False
    pin_1 = str(input('Inserta el PIN de 4 digitos: '))
    while b_ok == False:
        if len(pin_1) != 4:
            print("El pin solo puede tener 4 digitos")
            pin_1 = str(input('Inserta el PIN de 4 digitos: '))
        else:
            if not(pin_1.isdigit()):
                print("El pin NO  puede tener caracteres")
                pin_1 = str(input('Inserta el PIN de 4 digitos: '))
            else:
                b_ok = True
                print("PIN guardado")
                #return true
guardar_pin()
