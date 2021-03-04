import string
import random

# abecedario
alphabet = string.ascii_lowercase

def get_random_key():
    pass

def encrypt(msg, key, alphabet):
    pass

def decrypt(cipher, key, alphabet):
    pass

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