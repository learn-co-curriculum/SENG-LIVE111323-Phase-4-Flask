# OBJECTIVES
## Authentication 
## Understand the purpose and functionality of cookies and sessions in web development.
## Explain the concept of hashing and its primary purpose in data integrity verification.
## Define encryption and its role in data confidentiality protection.
## Demonstrate how to create a signup method using hashing and encryption to securely store user passwords.

## Cookies vs sessions
### Cookies:
* Cookies are small text files used to store user information on the user’s computer.
* Cookies are located in the frontend, and they are not encrypted.
### Sessions:
* Sessions are used to store user information on the user’s server side.
* Sessions are located in the backend, and they are encrypted.
* For sensitive information like user ID and password, sessions are preferred.

## Why do we use session for authentication?:
* Session is encrypted.
* User logs in once and stays logged in.
* User refreshes the page, and they stay logged in.

## Hashing:
* Hashing is primarily used to transform data into a fixed-size string of characters, called a hash value or digest.
* The primary purpose of hashing is to verify data integrity and quickly look up data in hash tables.
* It is a one-way process, meaning it’s difficult to reverse the hash to obtain the original data.
* Hashing is commonly used for storing passwords and checking data integrity.
* Example: hashing -> blender (banana + strawberry + …)

## Encryption:
* Encryption is used to protect data confidentiality by converting it into an unreadable format, which can be later decrypted to its original form.
* Encryption is a two-way process, and the original data can be retrieved using a decryption key.
* Reversibility:
    -Hashing: irreversible
    -Encryption: Decrypt encrypted data with the decryption key.
* Security:
    -Hashing: fast for password verification, but this speed can make them vulnerable to certain attacks.
    -Encryption: complex and secure, harder to break without the decryption key.


### secret key
$python -c 'import os; print(os.urandom(16))'
