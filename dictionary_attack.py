import hashlib


def crackHash(inputPass):
    passFile = open('wordlist.txt', 'r')
    for passwd in passFile:
        encPass = passwd.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            print(f"Password found: {passwd}")
            return

    print("Password not found...")


if __name__ == "__main__":
    crackHash("1a1dc91c907325c69271ddf0c944bc72") # MD5 hash