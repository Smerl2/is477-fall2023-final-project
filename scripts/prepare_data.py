import requests
import hashlib

#Bank Marketing Data

url = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"

response = requests.get(url)
   
with open('data/online+retail.zip', mode='wb') as f:
    f.write(response.content)

filename = 'data/online+retail.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

bank_marekting_hash_created = 'f5385cbb54bbebf7196389109c6b0621faab0c304e3702548165e71c84aede8b'
if  bank_marekting_hash_created != sha256hash:
    print("Computed hash does not match expected hash of original data")
else:
    print("Computed hash matches expected hash of origainal data")