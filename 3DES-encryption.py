from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

path = input('Enter the file path: \n\n')

def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

key = DES3.adjust_key_parity(get_random_bytes(24))

print(key, '\n\n\n\n')


with open(path, "r") as f:
    content = f.read()

    blocks = []
    encrypted_blocks = []
    decrypted_blocks = []

    cipher = DES3.new(key, DES3.MODE_EAX)

    nonce = cipher.nonce

    print(nonce)

    while True:
        blocks.append(content[0:8])
        encrypted_blocks.append(cipher.encrypt(content[0:8].encode('ascii')))
        content = content[8:]
        if len(content) == 0:
            break


with open('encrypted_blocks.txt', 'w') as f:
    f.write(str(encrypted_blocks))

with open('blocks.txt', 'w') as f:
    f.write(str(blocks))