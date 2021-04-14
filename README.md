# BruteForce
To use brute force to find password for encrypted file.

PyPDF2 is used to decrypt an encrypted PDF File.

Algorithm

1. Open the encypted file in read binary mode.
2. Open dictionary.text file in read mode and store the dictionary words in a list.
3. Traverse through list of words and check condition if PdfReaderobject is decrypted with word in list.
4. If password is found then print 'Hacked Password' is password and exit.
5. If password is not found then keep traversing the list until it is found.
