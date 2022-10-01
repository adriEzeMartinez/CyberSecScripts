#---------------------------------
#v1
import codecs

text = 'Hello'
rot13 = codecs.encode(text, 'rot_13')
print(rot13)

text = codecs.decode(rot13, 'rot_13')
print(text)

#---------------------------------
#v2
abc = "textToDecode"
rot_13 = lambda x: "".join([abc[(abc.find(c)+13)%26] for c in x])


# encryption
clear_text = 'cleartext'
encrypted_text = rot_13(clear_text)
print('Your encrypted text: ' + encrypted_text)

# decryption
decrypted_text = rot_13(encrypted_text)
print('Your decrypted text: ' + decrypted_text)
