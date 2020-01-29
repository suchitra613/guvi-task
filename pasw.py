import hashlib
password=input('Enter the password')
p=hashlib.new('md4').hexdigest()
print(p)
