


### Part 1 

***Symmetric Encryption****

- Symmetric encryption uses a single key for both encryption and decryption
  
  
  ![[Pasted image 20250909104255.png]]

- Symmetric encryption algorithms have been are not a new concept. 


***Important encryption algos: 
1. ***DES (Data Encryption Standard)***
	- Developed by IBM in 1971.
	- Became insecure due to advancements in computing power. 
	- Encrypts data using a 56-bit key. 
	- Vulnerable to brute-force attacks due to its relatively short key length. 
	- No longer used for serious encryption applications. 
2. AES (Advanced Encryption Standard)
	 - Replaced DES in the lates 1990's
	 - Uses key lengths of 128, 192, or 256 bits. Longer key lengths are more secure. 

---

***Asymmetric Encryption***

Hashing is a process that converts input data into a fixed-size string of characters, typically appearing as a random sequence.  Cannot be reversed. Used for data integrity and authentication.  

- Common hashing algos: SHA-256, SHA-1, MD 5

<u>How Hashing is similar to Encryption</u>

1. Data Transformation: Both hashing and encryption transform data from its original form to a different form. 
2. Security Purposes: Both are used to protect data. Encryption protects data in transit or at rest, while hashing ensures data integrity and is used for verifying the authenticity of data. 
3. Algorithms: Both use algos to transform data. 

***Are passwords Encrypted?*** 

No. Encryption is used for data that needs to be recovered in its original form, whereas passwords should not be reversable for security reasons.

- When users create passwords, the passwords are hashed and stored in a database.

- When users log in, their entered passwords are hashed, and the results is compared to the stored hashed, if matched login. 

---

### <u>Check for Understanding: </u>

1. What is the primary characteristic of symmetric encryption?

· A) It uses a public key for encryption and a private key for decryption.

· B) It uses different keys for encryption and decryption.

· C) It uses the same key for both encryption and decryption.

· D) It does not require a key for decryption.

Answer: C) It uses the same key for both encryption and decryption.

2. Which of the following encryption algorithms is no longer used for serious encryption due to its vulnerability to brute-force attacks?

· A) AES (Advanced Encryption Standard)

· B) DES (Data Encryption Standard)

· C) RSA (Rivest-Shamir-Adleman)

· D) SHA-256

Answer: B) DES (Data Encryption Standard)

3. What key length options does AES (Advanced Encryption Standard) offer?

· A) 56 bits

· B) 64 bits, 128 bits, and 192 bits

· C) 128 bits, 192 bits, and 256 bits

· D) 512 bits and 1024 bits

Answer: C) 128 bits, 192 bits, and 256 bits

4. How does asymmetric encryption differ from symmetric encryption?

· A) Asymmetric encryption uses the same key for both encryption and decryption.

· B) Asymmetric encryption is reversible, while symmetric encryption is irreversible.

· C) Asymmetric encryption uses a pair of keys: a public key for encryption and a private key for decryption.

· D) Asymmetric encryption does not require keys at all.

Answer: C) Asymmetric encryption uses a pair of keys: a public key for encryption and a private key for decryption.

5. Why are passwords typically hashed instead of encrypted?

· A) Hashing allows passwords to be decrypted when needed.

· B) Hashing is a reversible process, making it ideal for storing passwords.

· C) Hashing ensures that passwords are not stored in a recoverable form, enhancing security.

· D) Hashing is faster than encryption and requires less computational power.

Answer: C) Hashing ensures that passwords are not stored in a recoverable form, enhancing security.

---

***Data Encryption Tools***

***PGP (Pretty Good Privacy):*** provides cryptographic privacy and authentication. PGP is often used for securing emails, files, and data communication. It supports both symmetric and asymmetric encryption. 

***GNU Privacy Guard (GnuPG or GPG):*** is a free implementation of the OpenPGP standard. Created by the Free Software Foundation (FSF). It was created as an alternative to PGP, offering similar functions but open source. 

<u>GPG Historical Background</u>

1. <u>1991: Release of PGP(Pretty Good Privacy):</u> Phil Zimmerman releases PGP open source. 

2. <u>Legal Challenges:</u> 

- The US Government put Zimmermann under investigation for potentially violating the Arms Export Control Act, which carried severe penalties, including fines of up to $1 million and imprisonment for up to 10 years.

- In 1996, the U.S. government dropped the charges without any indictments. There was growing public support for Zimmermann and increasing recognition of the simplicity and value of encrypting data for personal and business use.

1. <u>Development of GnuPG (Gnu Privacy Guard):</u>  1999 Werner Koch creates GPG open source. 


![[Pasted image 20250909113523.png]]

---

***Command Line Interface***

Encrypted file "awaiting encryption.md" using terminal GPG line:  

***gpg --symmetric --cipher-algo AES256 --armour "awaiting encryption.md"***

| Cipher      | Key Length             | Description                                                                                            | Specialization / Speed                                                                                                                                 |
| ----------- | ---------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AES128      | 128 bits               | AES with a 128-bit key, a widely used encryption standard.                                             | Speed: Fast and efficient; Use Case: Ideal for general-purpose encryption where a balance of security and performance is needed.                       |
| AES192      | 192 bits               | AES with a 192-bit key, offering more security than AES128.                                            | Security: Offers higher security than AES128; Use Case: For applications needing stronger security with minimal performance loss.                      |
| AES256      | 256 bits               | AES with a 256-bit key, providing the highest security level among the AES options.                    | Security: Highest level of security among AES variants; Use Case: Preferred for highly sensitive data requiring maximum security.                      |
| 3DES        | 168 bits (56 bits x 3) | Applies the DES cipher algorithm three times to each data block, typically using three different keys. | Security: Legacy algorithm; Use Case: Still used in some financial and legacy systems, but generally slower and less efficient than AES.               |
| CAST5       | 40 to 128 bits         | A symmetric-key block cipher with a 64-bit block size and key sizes ranging from 40 to 128 bits.       | Specialization: Lightweight and flexible; Use Case: Suitable for applications requiring smaller key sizes or backward compatibility.                   |
| Blowfish    | 32 to 448 bits         | A symmetric-key block cipher with a variable key length from 32 bits up to 448 bits.                   | Speed: Fast and efficient for smaller key sizes; Use Case: Used in systems where flexibility in key length is advantageous.                            |
| Twofish     | Up to 256 bits         | A symmetric-key block cipher with a block size of 128 bits and key sizes up to 256 bits.               | Specialization: Strong and versatile; Use Case: Often considered a potential successor to AES, suitable for both software and hardware implementation. |
| Camellia12  | 128 bits               | Camellia cipher with a 128-bit key, similar to AES128 in security and performance.                     | Security: Comparable to AES128; Use Case: Alternative to AES, particularly in Japan and Europe, with similar security and efficienc                    |
| Camellia192 | 192 bits               | Camellia cipher with a 192-bit key.                                                                    | Security: Comparable to AES192; Use Case: Chosen when AES is not preferred, especially in specific regions or industries.                              |
| Camellia256 | 256 bits               | Camellia cipher with a 256-bit key, similar to AES256 in security and performance.                     | Security: Comparable to AES256; Use Case: Used for maximum security in areas where Camellia is preferred over AES.                                     |
***Output:*** 

![[Pasted image 20250909113853.png]]

***Encrypted message in ASCII***

![[Pasted image 20250909114719.png]]


---

### Part 2

***Asymmetric Encryption***

Uses a pair of keys

1. public key: Can be shared openly and is used to encrypt data. 
	
2. private key: Kept secret and is used to decrypt data. 

![[Pasted image 20250909115038.png]]

***Web Client and Server Key Exchange***

a web server and a browser client need to encrypt data before sending it over the internet. They both wish to share a common encryption key before sending and the same encryption key for decrypting data.

***Effective Key Sharing Solution***

1. Send a secure file that requires a code to open. That code is only known by the sender.
2. Send the file open to the recipient and allow the recipient to lock the file. 
3. The key cannot be opened by anybody but you and the file is secure. 

The open file would be the public key, and the locked file would be the private key. If someone were to steal the file, it wouldn't matter because they don't have the key to open it only the sender has this key. 


***Inventors***

In 1976, Whitfield Diffie and Martin Hellman from Sandford University, as seen in Figures 43 and 44, jointly invented Public and Private key cryptography, the most important advancement in cryptography in 2,000 years. They cited the work of Ralph Merkle, a graduate student at Berkely, as seen in Figure 45, who was solving a very similar problem. Merkel named his key exchange technique "Merkle Puzzles.


***RSA***

The RSA algorithm, named after its inventors Rivest, Shamir, and Adleman, as seen in Figures 46 through 49, was developed in 1977, just a year after Diffie and Hellman's work was published. RSA was the first practical implementation of the public key cryptography concept that Diffie and Hellman had theorized.

Before 1976, cryptography was based on symmetric key algorithms, where the same key is used for both encryption and decryption. The major challenge with this approach is that the secure exchange of the key is practically impossible.

Prime numbers are key to understanding public private keys.

The algorithm begins by choosing two very large prime numbers at random. These become the factors of a multiplication product that is computationally difficult

---

***The RSA Process in Five Steps***

**<u>Step 1: Choose Two Large Prime Numbers</u>

- Select two large prime numbers, typically labeled as p and q.

- These primes are chosen randomly and independently of each other. The larger the prime numbers, the more secure the keys will be, but also the more computationally intensive the process will be.

- For a 2048-bit RSA key, p and q are typically around 1024 bits each. This means that p and q are both 1024-bit prime numbers. Larger values for p and q are more secure.

**<u>Step 2: Compute the Modulus (n)</u>

- Multiply the two prime numbers to get the modulus n:

		𝑛=𝑝×𝑞

- The modulus n is used as part of both the public and private keys. The security of RSA relies on the difficulty of factoring this large number n back into its prime factors p and q.

<u>Step 3: Calculate the Euler's Totient Function (φ(n))</u>

- ***Totient Function Calculation:

	 - Compute the totient function φ(n), which is derived from p and q:

    - This function counts the number of integers up to n that are relatively prime to n (i.e., they have no common divisors with n other than 1).

<u>Step 4: Choose the Public Exponent (e)</u>

- ***Public Exponent Selection:

    - Choose an integer e that is relatively prime to φ(n) and lies between 1 and φ(n). This number e will be the public exponent. Common choices for e include small prime numbers like 3, 17 for human readability.

    - 65537 is a common choice for e.

    - 65537 is a Fermat prime (a prime of the form 65537=2216+1 )

    - For RSA to work, e must be relatively prime to ϕ(n).

    - Since 65537 is prime, it has a high probability of being relatively prime to ϕ(n) especially when p and q are large primes.

<u>Step 5: Compute the Private Exponent (d)</u>

- ***Private Exponent Calculation:

    - Calculate d as the modular multiplicative inverse of e modulo φ(n), meaning that d satisfies the equation:
      ![[Pasted image 20250909120728.png]]

    - The value d is the private exponent, and it is kept secret. This number allows the decryption of data that was encrypted using the public key.

<u>Step 6: Create Public and Private Keys:</u>

- ***Public Key:

    - The public key consists of the pair (n, e).

    - This key is shared openly and is used by others to encrypt messages intended for the key owner.

- ***Private Key:

    - The private key consists of the pair (n, d).

    -  This key is kept secret and is used by the key owner to decrypt messages that were encrypted with the corresponding public key.

<u>Step 7: Use the Two Keys</u>

· ***Encryption with the Public Key:

* Convert the message string into an array of bytes.

 - Convert the bytes into a large integer.

- A sender encrypts a message M (represented as an integer) using the recipient's public key (n, e):
     ![[Pasted image 20250909120917.png]]

 - The result C is the ciphertext, which can be sent over an insecure channel.

***Decryption with the Private Key:

- The recipient decrypts the ciphertext C using their private key (n, d):
    ![[Pasted image 20250909121024.png]]

- The result M is the original message.

- Convert the integer M into a string of bytes and then into ASCII characters to get the original message.
---

<u>Cracking the System:</u>

***1. Factoring Challenge:

- The security of RSA encryption relies on the difficulty of factoring the large number n into its prime factors p and q. As long as n is large enough (typically 2048 bits or more), it can take most computers an enormous amount of time to factor n using current technology.

***2. Prime Numbers:

- The use of prime numbers is important because the properties of prime numbers and modular arithmetic make it possible to create a one-way function for encryption that is easy to compute in one direction (encryption) but very difficult to reverse without the private key (decryption).

Computer Code for RSA Cryptography

1. Create a new Java application.

2. Copy this code into the App class.

3. For best results download this document and open it in Microsoft Word. The copy/paste operation in Chrome will remove all line breaks.
   
   ***Input**
![[Pasted image 20250909123935.png]]
   
   ***Output***
![[Pasted image 20250909124005.png]]

---

***Asymetric Encryption w GPG

***Method 1***

1. Create your own public key files:

		- gpg --gen-key
		
2. Follow steps in the terminal 
***output
![[Pasted image 20250909124420.png]]

--- 

***Share keys with friends


![[Screenshot 2025-09-10 101541.png]]



![[Screenshot 2025-09-14 003224 1.png]]
---

***Encrypt a Message


![[Screenshot 2025-09-09 114717.png]]
---

***Decryption
![[Pasted image 20250914004547.png]]

---

# Part 3

***Comparing Encryption Tools

| Application        | Encryption Method                            | Details                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WhatsApp           | Signal Protocol                              | End-to-end encryption (E2EE) ensures that only the communicating users can read the messages. Even WhatsApp cannot decrypt them.                                                                                                                                                                                                              |
| Instagram          | HTTPS/TLS for data in transit                | Messages and data are encrypted in transit using HTTPS/TLS, but direct messages are not end-to-end encrypted by default.                                                                                                                                                                                                                      |
| Facebook Messenger | Secret Conversations use the Signal Protocol | Standard messages are encrypted in transit using HTTPS/TLS. For end-to-end encryption, users must enable "Secret Conversations," which use the Signal Protocol                                                                                                                                                                                |
| SMS Texting        | None (in standard SMS                        | SMS messages are not encrypted, making them vulnerable to interception. Enhanced messaging services like RCS (Rich Communication Services) may offer better security but are not universally encrypted end-to-end. Many Two-Factor Authentication (2FA) systems use texting SMS, making them less secure than 2FA applications on your phone. |
| Emai               | Varies (TLS, PGP, S/MIME)                    | ***TLS: Encrypts email in transit between servers but not end-to-end.***<br><br>***PGP: Provides end-to-end encryption if both sender and receiver use PGP. ***<br><br>***S/MIME: Another protocol for end-to-end email encryption, typically used in enterprise settings.***                                                                 |
| Signal             | Signal Protocol                              | End-to-end encryption by default for all messages and calls.                                                                                                                                                                                                                                                                                  |
| Telegram           | MTProto                                      | Messages are encrypted in transit and on servers. "Secret Chats" provide end-to-end encryption.                                                                                                                                                                                                                                               |
| Google Message     | Signal Protocol (for RCS messages)           | SMS is not encrypted, but RCS messages can be end-to-end encrypted when both parties use compatible devices and carriers.                                                                                                                                                                                                                     |
| Apple iMessage     | End-to-end encryption                        | Uses a proprietary Apple protocol to provide end-to-end encryption for messages between Apple devices.                                                                                                                                                                                                                                        |


--- 

# Part 4

***A Big Step Forward in Encryption

Quantum computing is a huge leap in computing power. It uses ideas from quantum mechanics to perform calculations much faster than regular binary computers. Unlike traditional bits, which are either 0 or 1, quantum bits (qubits) can be both 0 and 1 at the same time because of a property called superposition. This lets quantum computers solve complex problems, like factoring large numbers, much more quickly than classical computers.

***The Threat to Current Encryption Standards

- Breaking RSA:

 - The RSA encryption algorithm is a key part of many secure communications today. Its security relies on how difficult it is to factor large prime numbers. Right now, factoring a large number used in RSA would take an impractical amount of time on regular computers.

 - Quantum computers, using methods like Shor's algorithm, could factor these large numbers much faster, effectively breaking RSA encryption. This would make RSA and similar encryption methods vulnerable to quantum attacks.

***Will Existing Messages Be Revealed?

 - If a powerful enough quantum computer is developed, it could potentially decrypt messages that were previously encrypted using RSA or similar algorithms. This means that encrypted data intercepted today could be stored and decrypted in the

- future when quantum computing becomes available. Sensitive communications, financial transactions, and state secrets could be at risk.

***The Future of RSA:

- While RSA is still secure today, its long-term future is in doubt due to the threat of quantum computing. Security experts are already looking into post-quantum cryptography, which involves creating new encryption methods that can resist quantum attacks.

- Huge Advantage:

- The country that leads in quantum computing will gain a significant advantage both militarily and economically. Quantum computers could break current encryption standards, giving the holder powerful abilities in cyber spying, secure communication, and data manipulation.

 - Militarily, being able to decrypt enemy communications could change the balance of power. Economically, access to decrypted data like financial transactions, corporate secrets, and personal information could provide a major advantage.

***What Will Replace RSA?

***Post-Quantum Cryptography:*** Researchers are developing new encryption methods believed to be secure against quantum attacks. These are known as post-quantum cryptography.

- Lattice-Based Cryptography: This method relies on tough math problems related to lattice points in high-dimensional spaces. These problems are hard for both classical and quantum computers to solve.

- Hash-Based Cryptography: This approach uses hash functions that are resistant to quantum attacks.

- Code-Based Cryptography: Techniques like the McEliece cryptosystem use the difficulty of decoding random linear codes, offering another quantum-resistant option.

- Multivariate Polynomial Cryptography: This involves solving systems of complex equations, which are believed to be hard even for quantum computers.

***Algorithm Updates:*** In September 2024, Google, Microsoft and other technology companies finished a years-long process of replacing RSA encryption with a new quantum-resistant algorithms in anticipation of upcoming quantum developments.

***Quantum Beyond Encryption***

Factoring large numbers isn't the only thing quantum computing can do. Quantum computers have the potential to revolutionize many fields by solving problems that are too hard for classical computers.

1. <u>Quantum Simulation</u>

	- Molecular and Chemical Simulations:

		- Quantum computers can simulate molecular structures and chemical reactions with high precision, which is extremely challenging for classical computers. This is important in drug discovery, material science, and chemistry, where understanding complex molecular interactions is important.

***Material Science:

- Quantum computers could help design new materials with specific properties by simulating atomic structures at the quantum level. This could lead to advances in superconductors, catalysts, and other unique materials.

2. <u>Optimization Problems</u>

 ***Logistics and Supply Chain Optimization:
 
- Many logistical problems, like optimizing delivery routes and scheduling, involve complex calculations that classical computers struggle with. Quantum computers can potentially solve these problems faster and more accurately.

- Companies like Volkswagen and DHL are already exploring quantum algorithms to improve traffic flow and delivery routes.

***Financial Modeling:

- In finance, quantum computers could optimize portfolio management, risk analysis, and pricing of complex financial products. They could model market trends and predict outcomes more effectively than traditional methods.

3. <u>Cryptography Beyond Factoring</u>

***Quantum Key Distribution (QKD):

- While quantum computers threaten current cryptographic methods, they also enable new forms of secure communication, like QKD. This uses quantum mechanics to create encryption keys that are theoretically unbreakable and can detect any attempt at eavesdropping.

- Protocols like BB84 allow two parties to securely share a cryptographic key. If someone tries to intercept the key, the authorized users will know.

4. <u>Machine Learning</u>

***Quantum Machine Learning:

- Quantum computers could speed up machine learning algorithms, allowing for faster training of models on large datasets. They might discover patterns that classical computers can't detect.

5. <u>Search Algorithms</u> 

***Grover’s Algorithm:

- Grover's algorithm is a quantum search method that speeds up unstructured search problems. While classical algorithms check each entry one by one, Grover's algorithm can find a specific item in an unsorted database much faster.

6. <u>Artificial Intelligence and Complex Decision-Making</u>

***Enhanced Decision-Making:

- Quantum computers could improve decision-making processes in AI by enabling more complex simulations and optimizations. This could lead to more advanced AI systems capable of solving harder problems with greater accuracy.

7. <u>Quantum Communication</u> 

***Secure Communication Networks:

 - Quantum communication protocols can build secure networks that are resistant to eavesdropping. Any attempt to intercept the communication would disturb the quantum state, revealing the presence of an eavesdropper. This is the foundation for developing a quantum internet, which could offer ultra-secure and efficient communication systems.

8. <u>Drug Discovery and Genomics</u>

***Personalized Medicine:

- Quantum computers could analyze huge amounts of genomic data to find patterns leading to personalized medicine. They could also simulate drug interactions at the molecular level, leading to more effective and targeted treatments.

9. <u>Climate Modeling</u>

***Environmental and Climate Modeling:

- Quantum computing could improve the accuracy of climate models by simulating complex atmospheric and oceanic processes. Better models could lead to improved predictions and strategies for addressing climate change.

--- 

# Part 5 

***Summarize



**Part 1** covers the fundamentals of symmetric encryption (DES, AES), hashing concepts, and tools like PGP/GPG, including their historical development and legal challenges.

**Part 2** dives deep into asymmetric encryption, explaining the RSA algorithm's seven-step process, from choosing prime numbers to creating public/private key pairs, along with the mathematical foundation that makes it secure.

**Part 3** examines how encryption is implemented across modern communication platforms, comparing the security approaches of WhatsApp, Signal, SMS, email, and other messaging services.

**Part 4** addresses the quantum computing threat to current encryption standards, explaining how quantum computers could break RSA encryption and the development of post-quantum cryptography solutions that companies are already implementing.

**Part 5** explores quantum computing's broader applications beyond cryptography, including scientific simulation, optimization problems, AI enhancement, and secure communication networks.