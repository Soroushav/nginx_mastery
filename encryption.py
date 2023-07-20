import hashlib
import base64
import datetime
import time

def GenerateHashKey(secret, url, expires):
    value = f"{secret}{url}{expires}"
    hash_value = hashlib.md5(str(value).encode('utf-8')).digest()
    base64_value = base64.urlsafe_b64encode(hash_value)
    str_hash = base64_value.decode('utf-8').rstrip('=')
    return f'{url}?md5={str_hash}&expires={expires}'

s = '11235'
u = '/secure_link/test.mp3'
e = datetime.datetime(2024, 6, 22, 21, 25, 15)
e_ex = int(time.mktime(e.timetuple()))
print(GenerateHashKey(s,u,e_ex))
