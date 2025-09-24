<center>
<h1>Cryptography Documentation</h1>

<h1>Owen Lindsey</h1>
<h1>Professor Sluiter</h1>

<h1>Grand Canyon University</h1>
<h1>CST-407</h1>
</center> 
<div style="page-break-before: always;"></div>
# Part 1


_**PGP GUI Encryption**_ ![[Pasted image 20250909113523.png]]

---

<div style="page-break-before: always;"></div>

_**Command Line Interface**_

Encrypted file "awaiting encryption.md" using terminal GPG line:

_**gpg --symmetric --cipher-algo AES256 --armour "awaiting encryption.md"**_

_**Output:**_

![[Pasted image 20250909113853.png]]

_**Encrypted message in ASCII**_

![[Pasted image 20250909114719.png]]

---
<div style="page-break-before: always;"></div>
# Part 2

_**Asymmetric Encryption**_

Computer Code for RSA Cryptography

1. Create a new Java application.
    
2. Copy this code into the App class.
    
3. For best results download this document and open it in Microsoft Word. The copy/paste operation in Chrome will remove all line breaks.
    
    _**Input**_ ![[Pasted image 20250909123935.png]]
    
    _**Output**_ ![[Pasted image 20250909124005.png]]
    

---

<div style="page-break-before: always;"></div>
# Part 2
_**Asymmetric Encryption w GPG**_

_**Method 1**_

1. Create your own public key files:
    
    ```
     - gpg --gen-key
     
    ```
    
2. Follow steps in the terminal
    

_**output**_ ![[Pasted image 20250909124420.png]]

---

<div style="page-break-before: always;"></div>

_**Share keys with friends**_

![[Screenshot 2025-09-10 101541.png]]

![[Screenshot 2025-09-14 003224 1.png]]

---

_**Encrypt a Message**_

![[Screenshot 2025-09-09 114717.png]]

---

_**Decryption**_ ![[Pasted image 20250914004547.png]]


<div style="page-break-before: always;"></div>
# Part 5

_**Summarize**_

**Part 1** covers the fundamentals of symmetric encryption (DES, AES), hashing concepts, and tools like PGP/GPG, including their historical development and legal challenges.

**Part 2** dives deep into asymmetric encryption, explaining the RSA algorithm's seven-step process, from choosing prime numbers to creating public/private key pairs, along with the mathematical foundation that makes it secure.

**Part 3** examines how encryption is implemented across modern communication platforms, comparing the security approaches of WhatsApp, Signal, SMS, email, and other messaging services.

**Part 4** addresses the quantum computing threat to current encryption standards, explaining how quantum computers could break RSA encryption and the development of post-quantum cryptography solutions that companies are already implementing.

**Part 5** explores quantum computing's broader applications beyond cryptography, including scientific simulation, optimization problems, AI enhancement, and secure communication networks.