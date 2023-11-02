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