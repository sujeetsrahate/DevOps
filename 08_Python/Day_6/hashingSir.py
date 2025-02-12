import hashlib



def hash_password(password, salt=None):

  """Hashes a password using SHA256 and an optional salt.

  Args:

    password: The password string to hash.

    salt (optional): A salt string to add to the password before hashing.

  Returns:

    The hexadecimal representation of the hashed password, or None if an error occurs.

  """

  try:

    password_bytes = password.encode('utf-8') # Encode password to bytes

    if salt: # If salt is provided

      salt_bytes = salt.encode('utf-8')

      password_bytes = salt_bytes + password_bytes # Prepend Salt

    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    return hashed_password

  except Exception as e:

    print(f"An error occurred during hashing: {e}")

    return None

def verify_password(password, hashed_password, salt=None):

  """Verifies a password against a stored hash.

  Args:

    password: The password string to verify.

    hashed_password: The stored hashed password (hexadecimal representation).

    salt (optional): The salt used when hashing the password.

  Returns:

    True if the password matches the hash, False otherwise.

  """

  try:

    new_hash = hash_password(password, salt)

    return new_hash == hashed_password

  except Exception as e:

    print(f"An error occurred during verification: {e}")

    return False

# Example usage:

password = "mysecretpassword"

salt = "my_secret_salt" # Store the salt securely!

hashed = hash_password(password, salt)

if hashed:

  print(f"Hashed password: {hashed}")

  # Verification:

  correct = verify_password(password, hashed, salt)

  incorrect = verify_password("wrongpassword", hashed, salt)

  print(f"Correct password verification: {correct}")

  print(f"Incorrect password verification: {incorrect}")

  # Example without salt (less secure):

  hashed_no_salt = hash_password(password)

  print(f"\nHashed password (no salt): {hashed_no_salt}")

  correct_no_salt = verify_password(password, hashed_no_salt)

  print(f"Correct password verification (no salt): {correct_no_salt}")

else:

  print("Hashing failed.")