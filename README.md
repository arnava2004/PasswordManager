# PasswordManager

Involves HTML, CSS for front end
JavaScript, Python, SQL is used for the BackEnd

This is a chrome extension app that stores the encrypted passwords and can also generate strong passwords. 
										It takes a MASTER PASSWORD from the user that is not stored by the program. This master password is then used to generate a cryptographically strong key that is then used to encrypt/decrypt all your other passwords with a military grade algorithm called the AES-256.
										The master key is used to encrypt/decrypt all the passwords stored and is computed from the master password and a secret device code that is randomly generated by the program for each unique user.
