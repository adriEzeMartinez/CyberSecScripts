import string

encMessage = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186".split()

modsList = [i for i in range(1,38)]

charList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_") 

d = {modsList[i]: charList[i] for i in range(len(modsList))}
print("v2 - picoCTF{", end = '')

for i in range(len(encMessage)):
    print(d[pow(int(encMessage[i]), -1, 41)], end= '') # mod inverse is 1/encMessage[i] % 41
    #print(d[int(encMessage[i]) % 37], end= '') mod operator
    
print("}")
