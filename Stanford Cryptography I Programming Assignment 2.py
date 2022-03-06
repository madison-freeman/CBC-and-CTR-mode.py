# Stanford University
# Cryptography I
#
# Week 2
# Questions 1-4
# AES in CBC and counter mode (CTR)
#
# In this project you will implement two encryption/decryption systems, one using AES in CBC mode and another using AES in counter mode (CTR).
# In both cases the 16-byte encryption IV is chosen at random and is prepended to the ciphertext.
# For CBC encryption we use the PKCS5 padding scheme discussed  in the lecture (14:04).
# While we ask that you implement both encryption and decryption, we will only test the decryption function.
# In the following questions you are given an AES key and a ciphertext (both are  hex encoded).
# Your goal is to recover the plaintext and enter it in the input boxes provided below.
# For an implementation of AES you may use an existing crypto library such as PyCrypto  (Python), Crypto++  (C++), or any other.
# While it is fine to use the built-in AES functions, we ask that as a learning experience you implement CBC and CTR modes yourself.
#
# Question 1
# CBC key: 140b41b22a29beb4061bda66b6747e14
# CBC Ciphertext 1: 4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81
# Result: Basic CBC mode encryption needs padding.
#
# Question 2
# CBC key: 140b41b22a29beb4061bda66b6747e14
# CBC Ciphertext 2: 5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253
# Result: Our implementation uses rand. IV
#
# Question 3
# CTR key: 36f18357be4dbd77f050515c73fcf9f2
# CTR Ciphertext 1: 69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329
# Result: CTR mode lets you build a stream cipher from a block cipher.
#
# Question 4
# CTR key: 36f18357be4dbd77f050515c73fcf9f2
# CTR Ciphertext 2: 770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451
# Result: Always avoid the two time pad!

from typing import Tuple, List
from Crypto.Cipher import AES


def convert_hex_str_to_int_list(a: str) -> List[int]:
    return [int(a[i: i + 2], 16) for i in range(0, len(a), 2)]


def extract_iv_cipher(cipher_list: List[int], iv_length: int) -> Tuple[List[int], List[int]]:
    # Extract initialization vector and ciphertext
    return (cipher_list[:iv_length], cipher_list[iv_length:])


def compute_block_num(key: List[int], cipher: List[int]) -> int:
    # Calculate the number of blocks
    return round(len(cipher) / len(key))


def cbc_decryption(key: str, cipher: str) -> str:
    # Decrypt CBC
    # :param key: hexadecimal encoded key
    # :param cipher: hexadecimal encoded ciphertext
    # :return: decrypted data

    key_list = convert_hex_str_to_int_list(key)
    block_size = len(key_list)
    cipher_list = convert_hex_str_to_int_list(cipher)
    iv_list, cipher_list = extract_iv_cipher(cipher_list, block_size)
    block_num = compute_block_num(key_list, cipher_list)
    aes_decoder = AES.new(bytes(key_list), AES.MODE_ECB)
    iv = bytes(iv_list)
    result_list = []
    for i in range(block_num):
        result_need_xor = aes_decoder.decrypt(bytes(cipher_list[i * block_size: (i + 1) * block_size]))
        result = [iv[j] ^ result_need_xor[j] for j in range(len(result_need_xor))]
        result_list.extend(result)
        iv = cipher_list[i * block_size: (i + 1) * block_size]
    return "".join([chr(x) for x in result_list[: len(result_list) - result_list[len(result_list) - 1]]])


def ctr_iv_add(key: List[int], step: int) -> List[int]:
    # Calculate the CTR key
    key_len = len(key)
    for i in range(key_len - 1, -1, -1):
        j = key[i] + step
        if j % 0xFF == j:
            key[i] = j
            break
        else:
            key[i] = j % 0xFF
            step = int(j / 0xFF)
    return key


def ctr_decryption(key: str, cipher: str) -> str:
    # CTR decryption
    # :param key: hexadecimal encoded key
    # :param cipher: hexadecimal encoded ciphertext
    # :return: decrypted data

    key_list = convert_hex_str_to_int_list(key)
    block_size = len(key_list)
    cipher_list = convert_hex_str_to_int_list(cipher)
    iv_list, cipher_list = extract_iv_cipher(cipher_list, block_size)
    block_num = compute_block_num(key_list, cipher_list)
    result_list = []
    aes_encoder = AES.new(bytes(key_list), AES.MODE_ECB)
    for i in range(block_num):
        round_iv = ctr_iv_add(iv_list[:], i)
        iv_cipher = aes_encoder.encrypt(bytes(round_iv))
        cipher_block = cipher_list[i * block_size: (i + 1) * block_size]
        result = [iv_cipher[j] ^ cipher_block[j] for j in range(len(cipher_block))]
        result_list.extend(result)
    return "".join([chr(x) for x in result_list])


print("Answers to Questions 1-4:")

if __name__ == "__main__":
    key = "140b41b22a29beb4061bda66b6747e14"
    cipher = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
    result = cbc_decryption(key, cipher)
    print("1) {}".format(result))

    key = "140b41b22a29beb4061bda66b6747e14"
    cipher = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
    result = cbc_decryption(key, cipher)
    print("2) {}".format(result))

    key = "36f18357be4dbd77f050515c73fcf9f2"
    cipher = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
    result = ctr_decryption(key, cipher)
    print("3) {}".format(result))

    key = "36f18357be4dbd77f050515c73fcf9f2"
    cipher = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
    result = ctr_decryption(key, cipher)
    print("4) {}".format(result))