import string
import random

# abecedario
alphabet = string.ascii_lowercase

def get_random_key():
    key_list = list(alphabet)
    random.shuffle(key_list)

    return ''.join(key_list)

def encrypt(msg, key, alphabet):
    text_cipher = ""
    for translate in msg:
        if translate.lower() in alphabet:
            index = alphabet.find(translate.lower())
            '''
            print(index)
            print(key[index])
            '''
            if translate.islower():
                text_cipher += key[index].lower()
            else:
                text_cipher += key[index].upper()

    return text_cipher

def decrypt(cipher, key, alphabet):
    text = []
    for i in cipher:
        text.append(key.index(i))
    return ''.join(alphabet[i] for i in text)

if __name__ == '__main__':
    mensaje = input('Ingrese el mensaje: ')
    key_random = get_random_key()
    print('='*50)
    print('Se genero una llave aleatoria: %s' % key_random)
    cipher = encrypt(mensaje, key_random, alphabet)
    print('='*50)
    print('Mensaje encriptado: %s' % cipher)
    print('='*50)
    normal_text = decrypt(cipher, key_random, alphabet)
    print('Mensaje desencriptado: %s' % normal_text)