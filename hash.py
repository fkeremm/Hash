import hashlib
import os

os.system("clear")
os.system("apt install cowsay")
os.system("clear")
os.system("cowsay -f ghostbusters CRYPT")
print("""  
\033[92m[1] \033[93mSHA512 CRYPT)

\033[92m[2] \033[93mMD5 CRYPT)
""")

seçim = input("Seçim yapınız: ")

if seçim == "1":
    m=hashlib.sha512()
    sha512 = input("Hashlenecek metini giriniz: ")
    m.update(sha512.encode('utf-8'))
    print(m.hexdigest())
if seçim == "2":
        sifreleyici = hashlib.md5()
        metin = input("Hashlenecek metini giriniz: ")
        sifreleyici.update(metin.encode("utf-8"))
        hash = sifreleyici.hexdigest()
        print("\033[91mSonuç= %s" % hash)
