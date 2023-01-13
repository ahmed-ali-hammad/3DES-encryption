from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes
import ast

encrypted_blocks_path = 'encrypted_blocks.txt'
blocks_path = 'blocks.txt'

global key
global nonce

with open('encryption_key.txt', 'r') as f:
    key = str(f.read())

with open('nonce.txt', 'r') as f:
    nonce = str(f.read())

cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)


with open(encrypted_blocks_path, "r") as f_1, open(blocks_path, 'r') as f_2:
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
