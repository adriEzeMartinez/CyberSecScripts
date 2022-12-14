# Uso: python3 xor_base64_sid.py
# En la pregunta "¿Quieres sacar un usuario o una sid?", sólo tienes que responder "usuario" o "sid"


# Pasos para sacar el usuario:
# 1. Codificar el parametro (SID) de la URL en Base64
# 2. Crear la funcion xor(data=parametro codificado, key) que nos dara como resultado el nombre del usuario en texto plano.

# Pasos para sacar el SID:
# 1. Crear la función XOR con el nombre de usuario y la clave
# 2. Codificar el resultado en Base64

# Funciones utilizadas:

# join(): SEPARADOR.join(un iterable que quieras unir)
# chr(): Pasas un número y te devuelve su valor ASCII    
# ord(): Pasas un valor ASCII y te devuelve su valor numérico
# zip(): en caso de tener dos iterables como parámetros, combina sus elementos en tuplas. Por ejemplo:
# zip([1,2,3], ['a','b', 'c']) daría: (1, 'a') (2, 'b', 3, 'c')
# cycle() devuelve un iterador que repite el contenido de los argumentos recibidos indefinidamente.
# ^ : operador XOR



from itertools import cycle
import base64



def principal():

    pregunta = input('¿Quieres sacar un usuario o una sid?\r\n')
    
    if pregunta == 'usuario':
        clave = input('Inserta la clave de cifrado XOR: \r\n')
        param = input('Inserta el parámetro correspondiente a la sid: \r\n')

        dec_param_enc = base64.b64decode(param).strip()
        dec_param = dec_param_enc.decode('utf-8')

        def xor_user(data, key):
     
            xor_user = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(dec_param, cycle(clave)))
            print('El nombre de usuario es: %s ' %(xor_user))

        xor_user(dec_param, clave)

    elif pregunta == 'sid':
        clave = input('Inserta la clave de cifrado XOR: \r\n')
        user = input('Inserta el nombre de usuario: \r\n')

        def xor_sid(data, key):

            sid = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(user, cycle(clave)))
            sid_bytes = sid.encode('ascii')
            base64_sid_bytes = base64.b64encode(sid_bytes)
            base64_sid = base64_sid_bytes.decode('utf-8')
            print("El parámetro de la sid es: %s" %(base64_sid))
        
        xor_sid(user, clave)
        
    else:
        print('Error de parámetro. ¿Quieres sacar un usuario o una sid?\r\n')
        return principal()

principal()
