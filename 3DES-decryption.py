from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes
import itertools as IT

import ast

path = 'encrypted_blocks.txt'
path_2 = 'blocks.txt'

key = b'I\xa8#\xbc\x13\x8a\xc7h4\xc7;\xb3\x0b\xfeh/8\x89\x19\xe6CT\xea#'

nonce = b'\x90\x19\xb0[GX\xf5\xe3+\x0bDK\x8c\x05\x19@'

cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)


with open(path, "r") as f_1, open(path_2, 'r') as f_2:
    encrypted_blocks = ast.literal_eval(f_1.read())
    blocks = ast.literal_eval(f_2.read())

    decrypted_blocks = []

    for block, encrypted_block in zip(blocks, encrypted_blocks):
        conditon = True
        count = 0
        while conditon:
            count +=1
            print(count)
            try:
                key = DES3.adjust_key_parity(get_random_bytes(24))
                cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
                print(key)
                plaintext = cipher.decrypt(encrypted_block)
                decoded_plaintext = plaintext.decode('ascii')

                decrypted_blocks.append(decoded_plaintext)
                print(decoded_plaintext, '\n')
                print(block)

                if decoded_plaintext != block:
                    raise ValueError('not correct.')

                conditon = False
            except:
                pass


print( ''.join(decrypted_blocks))
