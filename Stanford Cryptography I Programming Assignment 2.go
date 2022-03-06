package main
// Pretty straightforward solution using builtin go primitives
import (
"encoding/hex"
"crypto/aes"
"crypto/cipher"
"fmt"
)
func main() {
q1()
q2()
q3()
q4()
}
func q1() {
cbc("140b41b22a29beb4061bda66b6747e14", "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
}
func q2() {
cbc("140b41b22a29beb4061bda66b6747e14", "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")
}
func q3() {
ctr("36f18357be4dbd77f050515c73fcf9f2", "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329")
}
func q4() {
ctr("36f18357be4dbd77f050515c73fcf9f2", "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")
}
func cbc(k, c string) {
key, err := hex.DecodeString(k)
if err != nil {
panic(err)
}
cipher_text, err := hex.DecodeString(c)
if err != nil {
panic(err)
}
iv := cipher_text[0:16]
cipher_text = cipher_text[16:]
block, err := aes.NewCipher(key)
if err != nil {
panic(err)
}
dec := cipher.NewCBCDecrypter(block, iv)
dst := make([]byte, len(cipher_text))
dec.CryptBlocks(dst, cipher_text)
fmt.Println(string(dst))
}
func ctr(k, c string) {
key, err := hex.DecodeString(k)
if err != nil {
panic(err)
}
cipher_text, err := hex.DecodeString(c)
if err != nil {
panic(err)
}
iv := cipher_text[0:16]
cipher_text = cipher_text[16:]
block, err := aes.NewCipher(key)
if err != nil {
panic(err)
}
dec := cipher.NewCTR(block, iv)
dst := make([]byte, len(cipher_text))
dec.XORKeyStream(dst, cipher_text)
fmt.Println(string(dst))
}