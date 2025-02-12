import bcrypt

def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

# Take password input
password = input("Enter your password: ")
hashed_password = hash_password(password)

print(f"Hashed Password: {hashed_password.decode()}")
