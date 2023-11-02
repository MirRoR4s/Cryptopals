# 思路

密钥已经给出，利用 python 常见的密码学库即可完成解密。

```python
from Crypto.Cipher import AES
from base64 import b64decode


def main():
    # 读取密文
    cipher =  ""
    with open("./Set1/Challenge-data/7.txt", "r") as f:
        cipher = f.read()
    # base64 解码
    cipher = b64decode(cipher)
    # 密钥结合库函数完成解密
    plain = AES.new("YELLOW SUBMARINE".encode(), mode=1).decrypt(cipher)
    print(plain)
    
main()

```