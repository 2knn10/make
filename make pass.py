import random
import hashlib
import colorama
print('''
                  _                               
                 | |                              
  _ __ ___   __ _| | _____   _ __   __ _ ___ ___  
 | '_ ` _ \ / _` | |/ / _ \ | '_ \ / _` / __/ __| 
 | | | | | | (_| |   <  __/ | |_) | (_| \__ \__ \ 
 |_| |_| |_|\__,_|_|\_\___| | .__/ \__,_|___/___/ 
                            | |                   
''')

print('''
|=================================================|
|      [ + ] by kavani                            |
|=================================================|
|      [ + ] Instagram : 2knn01                   |                   
|=================================================|
|      [ + ] Telegram : https://t.me/kavani2knn10 |                   
|=================================================|
''')
A = "abcdefghijkImnopqrstuvwxyz"
a = "ABCDEFGHIJKLMNOPORSTUVWXYZ"
n = "0123456789"
y = "[10]#(*+{}=/@!%^<>,:;$"
all=A + a + n + y
length = 8
password ="".join(random.sample(all,length))
print("your password :",password)
        
        
md5  = hashlib.md5(password.encode())
print(md5.hexdigest())
