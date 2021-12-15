import random
from warnings import catch_warnings

# Message to encrypt
msg = "Hello world how are you doing today!!!"
print(msg)

# Encryption level, every character is 8-bit so divide by 8. Create character pool to make a list of characters to pull from.
encryption_level = 128 // 8 
char_pool = ''

# Loop to fill out the charater pool, for every possible 8-bit value it throws it in the character pool.
for i in range(0x00, 0xff):
    char_pool += chr(i)


# Generate the key, for i in range whatever the encyption level is (16-bits), it will grab a random charater from the pool and append that to the key str
key = ''
for i in range(encryption_level):
    key += random.choice(char_pool)

# The encryption process
key_index = 0
max_key_index = encryption_level - 1
encrypted_msg = ''
# Grabs every character in the message, and XOR that character whatever its binary value is with the current key index (current character in the key) and appends to encrypted message.
for char in msg:
    encrypted_char = ord(char) ^ ord(key[key_index])
    encrypted_msg += chr(encrypted_char)
    # Makes sure when we get to the end of the key, it loops back around and start the process again.
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(encrypted_msg)

# The Decryption process (same as the encryption process)
key_index = 0
decrypted_msg = ''
for char in encrypted_msg:
    decrypted_char = ord(char) ^ ord(key[key_index])
    decrypted_msg += chr(decrypted_char)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(decrypted_msg)
