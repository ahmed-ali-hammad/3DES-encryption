from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

path = input('Enter the file path: \n\n')

# generating the encryption key
key = DES3.adjust_key_parity(get_random_bytes(24))
cipher = DES3.new(key, DES3.MODE_EAX)
nonce = cipher.nonce

with open('encryption_key.txt', 'w') as f:
    f.write(str(key))

with open('nonce.txt', 'w') as f:
    f.write(str(nonce))


with open(path, "r") as f:
    content = f.read()

    blocks = []
    encrypted_blocks = []

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


print('\n\n')
print("Data has been encrypted and key generated, check encrypted_blocks.txt and encryption_key.txt files.\n\n")