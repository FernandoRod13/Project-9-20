import uuid
import hashlib
 
def hash_password(password):
    # uuid is used to generate a random number
    salt =uuid.uuid3(uuid.NAMESPACE_DNS, 'proyect920.org').hex
    return hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha1(salt.encode() + user_password.encode()).hexdigest()

def get_password(hashed_password):
    password, salt = hashed_password.split(':')
    print(salt)
 
new_pass = raw_input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = raw_input('Now please enter the password again to check: ')
#get_password()
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')