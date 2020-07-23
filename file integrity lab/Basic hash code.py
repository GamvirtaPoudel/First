from Crypto.Hash import SHA256

passwd = input("Enter your password: ")
hash_object = SHA256.new()
hash_object.update(f"{passwd}".encode('utf-8'))
hash_passwd = hash_object.hexdigest()
print(hash_passwd)
