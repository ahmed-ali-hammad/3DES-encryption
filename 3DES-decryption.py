import ast

from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

encrypted_blocks_path = 'encrypted_blocks.txt'
blocks_path = 'blocks.txt'

global key
global nonce

with open('encryption_key.txt', 'r') as f:
    key = ast.literal_eval(f.read())

with open('nonce.txt', 'r') as f:
    nonce = ast.literal_eval(f.read())

cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)


with open(encrypted_blocks_path, "r") as encrypted_file, open(blocks_path, 'r') as block_text_file:
    encrypted_blocks = ast.literal_eval(encrypted_file.read())
    blocks = ast.literal_eval(block_text_file.read())

    decrypted_blocks = []

    for block, encrypted_block in zip(blocks, encrypted_blocks):
        conditon = True
        count = 0
        while conditon:
            """
            To test using brute force, uncomment the following lines
            """
            # count +=1
            # print(count)
            try:
                # key = DES3.adjust_key_parity(get_random_bytes(24))
                # cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
                # print(key)

                plaintext = cipher.decrypt(encrypted_block)
                decoded_plaintext = plaintext.decode('ascii')

                decrypted_blocks.append(decoded_plaintext)

                if decoded_plaintext != block:
                    raise ValueError('not correct.')

                conditon = False
            except:
                pass


print('\n\n')
print( ''.join(decrypted_blocks))
print('\n\n')
