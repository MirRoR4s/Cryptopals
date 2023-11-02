# 思路

我们有很多个长度相同的十六进制字符串密文，已知某个密文串是通过 AES-ECB 模式加密的，我们希望找出这个字符串。

ECB 模式存在的问题是什么？

- 无状态、确定性：相同的十六字节明文总是产生相同的十六字节密文。

看了一下，一个密文串长度是 320，这一共有 320 * 4 / 8 = 160 字节。也就是说，一个密文串刚好由10个 AES 密文组成。

现在不妨把密文串十等分，依据 ECB 模式的问题，如果发现较多相同的字串的话，或许该字符串就是通过 ECB 模式加密的。当然，这里要假设该字符串原文中有很多相同的部分。

```python
from Crypto.Cipher import AES
from base64 import b64decode


def compare(cipher: bytes) -> int:
    weight = 0
    for i in range(10, len(cipher) - 10, 10):
        pre = cipher[i-10: i]
        now = cipher[i: i+10]
        weight += 1 if pre == now else 0
    
    return weight
        

def main():
    # 读取密文
    cipher =  []
    with open("./Set1/Challenge-data/8.txt", "r") as f:
        cipher = f.readlines()
    # 去除末尾换行符，转成 bytes 格式
    cipher = [bytes.fromhex(i.strip()) for i in cipher]
    max_weight = 0
    for i in cipher:
        max_weight = max(max_weight, compare(i))
    
    print(max_weight)
    
main()
```