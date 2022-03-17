# Stanford University - Cryptography I

## Week 2 - AES in CBC and CTR Mode

## Table of Contents

1. [Overview](#overview)
    1. [Problem Statement](#problem)
    2. [Project Motivation](#project-motivation)
3. [Solution](#solution)
4. [Result](#result)
5. [Author](#author)

## Overview <a name="overview"></a>

We will use Python to create a program that will implement encryption/decryption systems, one using AES in CBC mode and another using AES in counter mode (CTR).

### Problem Statement <a name="problem"></a>

 In both encryption/decryption systems, the 16-byte encryption IV is chosen at random and is prepended to the ciphertext. For CBC encryption we use the PKCS5 padding scheme discussed  in the lecture (14:04).
 We have been asked to implement both encryption and decryption, but we will only be tested the decryption function.
 
 In the following questions (1-4) we are given an AES key and a ciphertext (both are  hex encoded).
 Our goal is to recover the plaintext and enter it in the input boxes provided below.
 For an implementation of AES we may use an existing crypto library such as PyCrypto  (Python), Crypto++  (C++), or any other. While it is fine to use the built-in AES functions, as learning experience, we must implement CBC and CTR modes ourselves.

 Question 1:
 
 * CBC key: 140b41b22a29beb4061bda66b6747e14
 
 * CBC Ciphertext 1:
4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81
 
 Question 2:
 
 * CBC key: 140b41b22a29beb4061bda66b6747e14
 * CBC Ciphertext 2:
5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253
 
 Question 3:
 
 * CTR key: 36f18357be4dbd77f050515c73fcf9f2
 * CTR Ciphertext 1: 69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329
 
 Question 4:
 
 * CTR key: 36f18357be4dbd77f050515c73fcf9f2
 * CTR Ciphertext 2: 770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451
 
 ### Project Motivation <a name="project-motivation"></a>
 
 ## Solution <a name="solution"></a>

 ## Result <a name="result"></a>
 
* Result 1: Basic CBC mode encryption needs padding.

* Result 2: Our implementation uses rand. IV

* Result 3: CTR mode lets you build a stream cipher from a block cipher.

* Result 4: Always avoid the two time pad!

## Author<a name="author"></a>
* [Madison F.](https://github.com/madison-freeman)
