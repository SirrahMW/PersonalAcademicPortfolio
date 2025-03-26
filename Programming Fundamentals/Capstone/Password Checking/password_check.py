__studentName__ = 'Harris McCall'
__professor__ = 'Matthew Boehnke'
__date__ = 'Nov 1, 2024'
__assignment__ = 'password_check'

# Import
import argparse
import pickle
from hashlib import pbkdf2_hmac

# Data file
FILE = 'password_check.dat'

# Salt for the hash
SALT = b'SomeKindOfSalt'

# The number of iterations, set high enough to increase
# the computational cost of dictionary attacks but low 
# enough to maintain acceptable performance.
# Per NIST SP 800-132 A.2.2
XITERATIONS = 500_000


# Function to easily create SHA1 hash
def CreateHash(password):
  genHash = pbkdf2_hmac('sha1', password.encode(), SALT * 2, XITERATIONS)
  # Return only the generated SHA1 hash
  return genHash.hex()


# Loads the file into a variable
def Load(file):
  with open(file, 'rb') as f:
    userPass = pickle.load(f)
  return userPass


# Save the python dict to a file
def Save(passwords, file):
  with open(file, 'wb') as f:
    pickle.dump(passwords, f)


# Easily check a string to meet password req
def PasswordValid(password):
  # Check the length of the password
  if not (8 <= len(password) <= 12):
    return False

  # Counters for lowercase, uppercase, and digits
  lowercaseCount = 0
  uppercaseCount = 0
  digitCount = 0

  # Iterate through each char in password
  for char in password:
    if char.islower():
      lowercaseCount += 1
    elif char.isupper():
      uppercaseCount += 1
    elif char.isdigit():
      digitCount += 1
    else:
      # If the character is not alphanumeric
      return False
  
  # Check if the counts meet requirements
  if (lowercaseCount >= 3 and uppercaseCount >= 2 and digitCount >= 1):
    return True

  return False


# Authenticate a user by confirming password
def Authenticate(user, password):
  userPass = Load(FILE)
  # Check if the user exists
  if user in userPass:
    # If the user does exist, is the password correct?
    if userPass[user] == CreateHash(password):
      return 'Success'
    else:
      return 'Error: Wrong password'
  else:
    return 'Error: No such user'


# Change a given user's password
def ChangePassword(user, oldPass, newPass):
  # Load the passwd file
  userPass = Load(FILE)

  # Check if the user exists
  if user in userPass:
    # Check that the old password is correct
    if CreateHash(oldPass) == userPass[user]:
      # Check that the new password is valid
      if PasswordValid(newPass):
        # Change to the new password
        userPass[user] = CreateHash(newPass)
        Save(userPass, FILE) # Save the new password to the file
        return 'Success'
      else:
        # If password not valid
        return 'Error: Password policy failure'
    else:
      # If old password is wrong
      return 'Error: Wrong password'
  else:
    # If the user does not exist
    return 'Error: No such user'
  

def main():
  # Setting up the main parser
  parser = argparse.ArgumentParser(description='Checks the validity of a given password for a given user.')

  # Create subparser
  subparsers = parser.add_subparsers(dest='command', required=True)

  # Create a parser for the Authenticate command
  authParser = subparsers.add_parser('Authenticate', help='Authenticates a user.')
  authParser.add_argument('username', type=str, help='The username')
  authParser.add_argument('password', type=str, help='The password')

  changeParser = subparsers.add_parser('ChangePassword', help='Changes an existing user\'s password.')
  changeParser.add_argument('username', type=str, help='The username')
  changeParser.add_argument('old_password', type=str, help='The old password')
  changeParser.add_argument('new_password', type=str, help='The new password')

  # Parse the command-line arguments
  args = parser.parse_args()

  # Call appropriate function based on the command
  if args.command == 'Authenticate':
    result = Authenticate(args.username, args.password)
    print(result)
  elif args.command == 'ChangePassword':
    result = ChangePassword(args.username, args.old_password, args.new_password)
    print(result)


main()