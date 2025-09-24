# <center>PASSWORD HASHING AND SECURITY ANALYSIS</center>

## <center>Owen Lindsey</center>
## <center>Professor Sluiter, Shad </center>
## <center>CST-407</center>
## <center>Grand Canyon University</center>
<div style="page-break-after: always;"></div>
### **Introduction:**

In today's digital landscape, protecting sensitive information such as passwords and ensuring the integrity of data is more crucial than ever. Password hashing is a fundamental security practice that prevents attackers from easily reversing exposed or stolen passwords into their original form. Similarly, hashing is used in numerous other areas to guarantee data integrity, from file signatures and network transmissions to version control systems like GitHub and advanced technologies like blockchain.

In this activity, you will learn the basics of password hashing, its real-world applications, and the methods hackers use to crack password hashes. You will write Java programs to explore different hashing algorithms, including MD5, SHA-256, and BCrypt, and experiment with various password cracking techniques. Additionally, you will examine how hashing is used beyond password security—such as verifying file integrity, ensuring data transmission accuracy, and safeguarding commit history in version control systems like Git.

You will also be able to explain how hashing works in blockchain technology, where it provides immutability and security to the chain of data blocks. By the end of this activity, you will not only understand how password hashing works but also appreciate how modern security measures like salting and secure hashing algorithms prevent attacks.

# Part 1 - How Hashing Works

In this part of the activity, you will read about hashing and write a response to some questions.

### About Hashing

Hashing is an algorithmic function that takes a large amount of information as an input and outputs a smaller, fixed-size value, called a hash. Think of it as a way to create a unique _fingerprint_ for the data. The hashing process is commonly used for keeping passwords secure and checking data integrity.

### One Way Street

A hash is a one-way function, meaning that it is not reversable. Unlike encryption, there is no inherent information about the original value stored in the hash. The hashing function creates a fixed length result regardless of the size of the input. A single password hash will produce the same length of output as the hash value of an entire book. Theoretically, it is possible, although extremely unlikely, for two pieces of data to produce an identical output, called a collision, from a hash function. Collisions are more likely if the length of the output string is not sufficiently long.

### Hashing Demonstrated

Follow these steps to see a hashing function in action.

1.      Navigate to md5hashgenerator.com

2.      Enter a string and click “Generate”.  You will see an example of a hashed password, shown in Figure 1.

![[Pasted image 20250918194133.png]]

3. You will soon discover that common passwords have been hashed and stored in lists. These are sometimes called Dictionaries or “Rainbow Tables”. They are useful for quickly hacking stolen passwords.

![[Pasted image 20250918194158.png]]

### Hashing Use Case #1 Passwords

Hashing passwords is a method used to securely store passwords in a database. Instead of saving the actual password, a hashed version of the password is stored in the database. Here's a step-by-step explanation of how it works:

![[Pasted image 20250918194216.png]]
1. User Creates a Password: When a user creates a password, the system takes the password and processes it through a hashing algorithm.

2. Hashing the Password: A hashing algorithm takes the password and transforms it into a fixed-length string of characters, which is the hashed password. This process is one-way, meaning it is extremely difficult to convert the hashed password back to the original password. Common hashing algorithms include SHA-256, BCrypt, and Argon2.

A database table with user accounts with clear text passwords
![[Pasted image 20250918194316.png]]

User accounts with hashed passwords
![[Pasted image 20250918194346.png]]

3. Salting: To further secure the hashed passwords, a random value called a "salt" is added to the password before hashing. This ensures that even if two users have the same password, their hashed passwords will be different. The salt is usually stored in the database alongside the hashed password.

4. Storing the Hashed Password: The hashed password is stored in the database instead of the plain text password.

User Accounts with Hashed Passwords and Salt
![[Pasted image 20250918194417.png]]

5. Verifying the Password:

-  When the user logs in, they enter their password.

-  The system retrieves the salt (if used) and the hashed password from the database.

-  The entered password is combined with the salt (if used) and hashed using the same algorithm.

-  The newly hashed password is compared with the stored hashed password. If they match, the password is correct, and the user is authenticated.

<div style="page-break-after: always;"></div>
### Why use Password Hashing?

1. Security: Even if the user table database is stolen, the attacker only gets hashed passwords, which are very difficult to reverse-engineer.

2. Unique Hashes with Salts: Adding a salt ensures that even common passwords produce unique hashes.

3. Prevents Rainbow Table Attacks: Salting and using secure hashing algorithms make precomputed hash attacks (rainbow tables) ineffective.

### About Rainbow Tables

A rainbow table, sometimes called a password dictionary, is a pre-computed list of hash values for commonly used passwords. Rainbow tables can help hackers crack passwords in seconds if an insecure password is used.

![[Pasted image 20250918194926.png]]

Commonly used passwords are weak because password dictionaries remove the need for intense computing power to find the reverse hash values. There are plenty of commonly used passwords and hashed result lists available online.

![[Pasted image 20250918194947.png]]


<div style="page-break-after: always;"></div>
### Hashing User Case #2 Data Verification

Hashing ensures data integrity and security, particularly when verifying whether data has been corrupted or tampered with during transmission, storage, or retrieval. A hash function transforms input data (such as files or messages) into a fixed-size string of characters, often

called a hash value or digest. These hashes can be used to ensure that data has not been altered, as even the slightest change to the input will result in a vastly different hash value.

1. **File Downloads**

When users download files from the internet, especially large files like software packages or operating system images, hashing is often employed to verify the integrity of the downloaded data. The website or file provider will typically publish the hash value (often using algorithms like SHA-256 or MD5) alongside the file. After downloading the file, the user can calculate the hash value of the downloaded file using a hashing utility and compare it to the hash provided by the website. If the values match, the file was downloaded correctly and has not been tampered with.

![[Pasted image 20250918195324.png]]


**Example:**

· Website provides a file app.zip along with its hash:

app.zip hash (SHA-256): 5d41402abc4b2a76b9719d911017c592

· User downloads the file and runs a hash check:

Hash of downloaded file (SHA-256): 5d41402abc4b2a76b9719d911017c592

· Since the hash values match, the file is verified as unaltered.

2. **Data Transmission**

In network communication, data can be corrupted or altered as it moves between the sender and receiver. To ensure that the data received is the same as the data sent, hashing is commonly used along with checksums or message digests. The sender creates a hash of the data before transmitting it and sends both the data and the hash to the receiver. Upon receiving the data, the receiver hashes the data again and compares the result with the hash sent by the sender. If the hashes match, the data is considered intact.

**![[Pasted image 20250918195448.png]]

Example:

· Sender sends the message:

"Hello World" with hash value (MD5): b10a8db164e0754105b7a99be72e3fe5

· Receiver calculates the hash of the received message and gets:

b10a8db164e0754105b7a99be72e3fe5

· The hashes match, so the message was transmitted correctly.

This method is often used in **TCP/IP** protocols, where checksums verify packet integrity in network layers.

3. **Data Storage and Backup Verification**

When data is backed up or stored for long periods of time, it’s important to ensure that it hasn’t been corrupted or altered. Hashing helps detect corruption by periodically hashing stored data and comparing it to the original hash created when the data was first stored. If the hashes differ, the stored data has likely become corrupted and needs to be restored from a backup.

![[Pasted image 20250918195545.png]]

5. **Version Control in Code Repositories**

In version control systems like Git, every commit is assigned a unique hash value (often called a commit hash) based on the contents of the files in the commit. This hash ensures that every change is uniquely identified and tracked. If a single byte in a file changes, the entire commit hash changes, providing a robust mechanism for tracking changes in the codebase.

![[Pasted image 20250918195609.png]]

![[Pasted image 20250918195617.png]]

Example of a Commit Hash

When you create a commit in Git, the commit hash is automatically generated. For example, after committing a change, you might see a message like this:

[main d3e5c4f] Add a new feature

1 file changed, 10 insertions(+)

Here, d3e5c4f is the abbreviated version of the commit hash, but the full commit hash looks like this:

d3e5c4f2b0932a5fdfc01977f1a4bde9058e0c7d

You can view the full commit hash with:

git log

This shows a list of commits with their corresponding hashes. The hash value ensures that every change is accurately recorded and identifiable.

6. **Digital Signatures and Certificates**

Digital signatures use a combination of hashing and encryption to verify the authenticity of digital messages or documents. A digital signature is created by hashing the message and

encrypting the hash with the sender’s private key. The receiver decrypts the signature using the sender's public key and compares the hash to a newly calculated hash of the message. If they match, the document’s integrity and authenticity are verified.

Example:

· Sender creates a digital signature by hashing the document and encrypting the hash.

· Receiver decrypts the signature and compares it with the hash they generate from the document.

· If both hashes match, the document is considered authentic and unaltered.

7. **Blockchain and Cryptocurrencies**

Hashing is used in blockchain technology. Every block in a blockchain contains a hash of the previous block, ensuring that any modification to a block would invalidate the entire chain. This hashing chain provides security and integrity for cryptocurrencies like Bitcoin, as altering past transactions would require recalculating the hashes for all subsequent blocks, which is computationally infeasible.

![[Pasted image 20250918195746.png]]

The next block’s hash is based on the previous block’s hash. If any data in the previous block is altered, the hash changes, invalidating the entire chain.

<div style="page-break-after: always;"></div>
### **Observations about Hashing**

1. You should notice that each hashing result from the same algorithm is always the same length. More modern hashing algorithms produce hash outputs much longer, and more secure, than MD5.

2. You should notice that the hash result has no pattern related to the input. A single letter difference in two passwords will produce completely different output values.


Hashing Algorithms Compared

Hashing Algorithm Year Introduced Hash Length (bits) Security Level Speed Automatic Salt Support Notes

MD2 1989 128 Low Slow No Obsolete, vulnerable to various attacks

MD4 1990 128 Low Fast No Obsolete, vulnerable to collision attacks

MD5 1991 128 Low Fast No Vulnerable to collision attacks

SHA-0 1993 160 Low Fast No Withdrawn due to significant flaws

SHA-1 1995 160 Low Fast No Deprecated due to collision vulnerabilities

SHA-256 2001 256 High Moderate No Part of the SHA-2 family

SHA-512 2001 512 Very High Slow No Part of the SHA-2 family

BCrypt 1999 Variable High Slow Yes Adaptive function resistant to brute force

SCrypt 2009 Variable Very High Very Slow Yes Memory-intensive, resistant to hardware attacks

PBKDF2 2000 Variable High Slow Yes Part of RSA's PKCS #5, configurable iterations

Argon2 2015 Variable Very High Slow Yes Winner of the Password Hashing


### **What are hash “collisions”?**

A collision occurs when two different input string produce the exact hash result. Collisions are theoretically possible since the domain (input) of a hashing function is essentially infinite and the range (output) of a hashing function is finite. However, the range of a hashing function is very large, and collisions are rare.

### **Birthday Function Collision Analogy**

Let’s imagine a very limited hashing algorithm using birthdays. Imagine we have a room of people, and each person has a birthday that falls on one of the 365 days of the year. If we think of each person's birthday as a piece of input data (the domain) and the days of the year as possible hash values (the range), we can understand how hashing works and why collisions (two people having the same birthday) might occur.

Int day = BirthdayHash(“January 3”); // day is 3

Int day = BirthdayHash(“December 31”); // day is 365

Int day = BirthdayHash(“February 1”); // day is 32

### **Probability of Birthday Collisions**

The range of the Birthday Function is very limited since there are only 365 days in the year. The probability of at least two people sharing the same birthday increases as the number of people in the group increases. This is known as the birthday problem. Let's see the collision probabilities in a table:

![[Pasted image 20250918200054.png]]
Table 1 The probability of a collision grows as the size of a group grows, seen in Figure 5.

![[Pasted image 20250918200131.png]]

### **Why Hash Collisions Matter**

In hashing, collisions occur when two different pieces of data produce the same hash value. Just like with birthdays, the more items in a collection we have, the higher the chance of a hash collision.

### **What is the probability of a MD5 collision?**

MD5 produces a 128-bit hash value. This means there are 2 128 possible different hash values. Using MD5 we need about 1.54×10 19 random items to have a 50% chance of at least one collision.

1.54×10 19 = 15,400,000,000,000,000,000. (15 quintillion)

### **Real-World Results**

Although the number for a collision probability is extremely low, there have been ways to cause MD5 to produce collisions.

In 1996, researchers found a weakness in the MD5 algorithm that could potentially allow collision attacks, meaning two different inputs could produce the same output. By 2004, they showed that attackers could create these collisions. In 2005, it was demonstrated that attackers could generate colliding x.509 certificates, which are used for SSL secure communications.

In 2008, further research showed that Public Key Infrastructures (PKI), which rely on these certificates, were vulnerable to these attacks. Researchers even created a fake SSL certificate that could make an attacker appear as a trusted root Certificate Authority (CA). Most operating systems come with a collection of trusted CA certificates, some of which use the MD5 algorithm, making them easy targets for attackers to spoof. As a result, MD5 is no longer considered secure.

### Deliverables

There are no deliverables for part 1. However, the review questions will help you prepare for upcoming assessments.

<div style="page-break-after: always;"></div>
## Part 2 - Coding a Password Hashing Program in Java

In this section we will create a simple program that uses various hashing algorithms on a sample password. We will use the program to demonstrate hashing, and then use it to perform some password cracking.
### Deliverables
![[Pasted image 20250918201515.png]]

![[Pasted image 20250918201308.png]]

### Password Cracking Time Estimate Table

The following table demonstrates the time required to crack passwords of varying complexity using different attack methods and computational power. These estimates assume brute-force attacks against different hashing algorithms.

| Password Type | Character Set | Length | MD5 (Standard PC) | MD5 (GPU Cluster) | SHA-256 (Standard PC) | SHA-256 (GPU Cluster) | BCrypt (Cost 12) |
|---------------|---------------|--------|-------------------|-------------------|----------------------|----------------------|------------------|
| **Weak Passwords** | | | | | | | |
| Numeric PIN | 0-9 | 4 chars | < 1 second | < 1 second | < 1 second | < 1 second | 1 minute |
| Simple Word | a-z | 6 chars | 5 minutes | 2 seconds | 15 minutes | 5 seconds | 2 years |
| Common Password | a-z, 0-9 | 8 chars | 3 hours | 30 seconds | 12 hours | 2 minutes | 500 years |
| **Moderate Passwords** | | | | | | | |
| Mixed Case | a-z, A-Z | 8 chars | 2 days | 5 minutes | 8 days | 15 minutes | 25,000 years |
| Alphanumeric | a-z, A-Z, 0-9 | 8 chars | 3 weeks | 2 hours | 12 weeks | 6 hours | 800,000 years |
| Basic Symbols | a-z, A-Z, 0-9, !@# | 10 chars | 200 years | 2 months | 800 years | 8 months | 10^15 years |
| **Strong Passwords** | | | | | | | |
| Full ASCII | All printable chars | 12 chars | 10^8 years | 10^5 years | 10^9 years | 10^6 years | 10^25 years |
| Passphrase | Dictionary words + spaces | 25 chars | 10^15 years | 10^12 years | 10^16 years | 10^13 years | 10^50 years |
| **Enterprise Passwords** | | | | | | | |
| Complex Policy | a-z, A-Z, 0-9, symbols | 14 chars | 10^12 years | 10^9 years | 10^13 years | 10^10 years | 10^35 years |
| High Security | Full char set + length | 16 chars | 10^18 years | 10^15 years | 10^19 years | 10^16 years | 10^45 years |

#### **Attack Scenario Assumptions:**

- **Standard PC**: Single CPU, ~10^6 MD5 hashes/second, ~10^5 SHA-256 hashes/second, ~10 BCrypt hashes/second
- **GPU Cluster**: High-end graphics cards, ~10^10 MD5 hashes/second, ~10^9 SHA-256 hashes/second, ~10^3 BCrypt hashes/second
- **BCrypt Cost 12**: Industry-standard work factor providing good security/performance balance

#### **Key Observations:**

1. **Algorithm Speed Impact**: MD5's speed makes it vulnerable; BCrypt's intentional slowness provides security
2. **Password Length**: Each additional character exponentially increases cracking time
3. **Character Set Complexity**: Including uppercase, numbers, and symbols dramatically improves security
4. **Hardware Advantage**: Specialized hardware reduces cracking time but BCrypt remains resistant
5. **Practical Security**: Passwords taking >100 years to crack are considered secure against current technology

#### **Compliance Recommendations:**

- **Minimum Standard**: 12+ characters with mixed case, numbers, and symbols
- **Preferred Algorithm**: BCrypt with cost factor 12 or higher
- **Enterprise Systems**: 14+ character passwords with full complexity requirements
- **Critical Systems**: Consider multi-factor authentication beyond password strength

*Note: These estimates reflect current computational capabilities (2025) and may decrease as technology advances. Regular password policy updates are essential for maintaining compliant security standards.*


### **Key Differences Between BCrypt and Other Algorithms**

**Speed:**

**MD5, SHA-1, SHA-256, etc.:** These algorithms are designed to be very fast. For example, MD5 can hash the password "asdf" 10000 times in around 204 milliseconds. Their speed is a critical characteristic in applications where fast hashing is necessary, such as checksums and data integrity checks.

**BCrypt:** In contrast, BCrypt is intentionally slow. Hashing a password 10 times takes around 966 milliseconds. BCrypt is specifically designed for hashing passwords. It incorporates a salt to protect against rainbow table attacks and is designed to be slow to thwart brute-force attacks. Its computational expense can be adjusted with a cost factor.

### **Security:**

**MD5, SHA-1:** These algorithms are no longer considered secure for cryptographic purposes due to vulnerabilities such as collision attacks.

**SHA-256, SHA-512:** These are more secure than MD5 and SHA-1, but still not ideal for password hashing due to their speed.

**BCrypt:** BCrypt is designed to be secure for password hashing. Its slowness and salt incorporation make it resistant to brute-force attacks and precomputed attacks like rainbow tables.

### **Hashing Algorithms Compared**

Algorithm Hash Length Speed (ms for 1000 hashes) Security Level Notes

MD5 128 bits 204 Low Fast, vulnerable to collisions

SHA-1 160 bits 206 Low Deprecated, vulnerable to collisions

SHA-256 256 bits 169 High Secure, widely used

SHA-512 512 bits 227 Very High Very secure

SHA-384 384 bits 173 High Balanced security

SHA-224 224 bits 104 Moderate Shorter hash length

SHA3-224 224 bits 111 Moderate Part of SHA-3 family

SHA3-256 256 bits 126 High Secure, different structure

SHA3-384 384 bits 164 High Secure, longer hash length

SHA3-512 512 bits 212 Very High Most secure among SHA-3

MD2 128 bits 108 Low Obsolete, slow

MD4 128 bits 56 Low Obsolete, insecure

BCrypt Variable 966 (10 times) Very High Slow, designed for password hashing

<div style="page-break-after: always;"></div>
## **Part 3 - Password Cracking Application**

In this section we are going to use a Java program to attempt to guess passwords based on their hash value. At the heart of the program, the same hashing process and hashing algorithms are used as the previous example. The difference is that this program will attempt to guess the original password from which a hash is generated, seen in Figure 24. The program will try a dictionary attack (rainbow table) first, followed by a brute-force attack.

![[Pasted image 20250918202205.png]]


### Compare Dictionary Attacks to Brute Force Attacks

#### Dictionary Attack Brute Force Attack

Method A dictionary attack uses a list of potential passwords, known as a dictionary. This list typically contains common passwords, words from the dictionary, and phrases. A brute force attack tries every possible combination of characters until the correct one is found. This can include letters (uppercase and lowercase), numbers, and special characters.

Efficiency It's more efficient than a brute force attack because it targets passwords that are likely to be used by people. Some dictionaries are collections of a few thousand common words while other dictionaries can contain millions. Even the largest dictionaries are many times faster than brute force methods. It is much less efficient than a dictionary attack because it must go through all possible combinations, which can be extremely time-consuming, especially for long and complex passwords. An 8-letter password using lower case letters only contains 268 combinations! 208,827,064,576 (208 billion)

Limitations It is limited to the passwords within the dictionary. If the actual password is not in the list, the attack will fail. While theoretically guaranteed to find the password, the time required can be impractically long for complex passwords, making it infeasible in many cases.

Usage Dictionary attacks are often used when the attacker has some knowledge or guess about the possible passwords, such as common passwords or passwords based on user information. Brute force attacks are used when the dictionary attack fails to find a password. There is no knowledge about the password or the password is expected to be very complex and not easily guessed.

1. Download and open the CST-407-RS-T3.Hashing.zip file. It is provided as topic resources.

2. Unzip / extract the file to a separate folder.

3. Open the application and inspect the contents.

4. You should see a list of txt files used by the program, shown in Figure 25. These are the dictionary lists that the program will use in a variety of combinations.

<div style="page-break-after: always;"></div>
## Part 5 – Demonstrate Hashing in a Block Chain

Block Chain Demo

This program demonstrates the basic principles of how a blockchain works by simulating the creation and linking of blocks in a simplified blockchain structure. Each block contains data, a unique identifier (ID), a hash of its own data, and a reference to the hash of the previous block

(known as the previous hash). Additionally, each block records the exact time it was created, giving a timestamp to the block.

### Deliverables: 
![[Pasted image 20250918203936.png]]

![[Pasted image 20250918203833.png]]

---

<div style="page-break-after: always;"></div>

## Summary of Key Concepts

This lesson demonstrated fundamental cryptographic principles essential for compliant security systems through hands-on programming and theoretical analysis.



### Why Hashing is Superior to Encryption for Password Security

Hashing provides superior password security through its one-way mathematical architecture. Unlike encryption, which is reversible with proper keys, hashing creates irreversible data transformation. When attackers compromise hash databases, they cannot directly decrypt passwords back to plaintext because no decryption mechanism exists. This "zero knowledge storage" means systems never store actual passwords, eliminating plaintext exposure risks. Authentication simply compares hash values without requiring decryption operations. Encryption-based storage creates vulnerabilities through key management requirements and adds unnecessary computational complexity. If encryption keys are compromised, all passwords become immediately accessible, making hashing the preferred approach for compliant password storage systems.



### Hashing Applications Beyond Password Security

Cryptographic hashing serves as cornerstone technology for data integrity verification across multiple domains. File verification ensures downloaded software remains uncorrupted during transmission by comparing hash values. Network protocols use checksums to detect data corruption during communication, while TCP/IP incorporates hashing for packet integrity. Version control systems like Git assign unique hash values to every commit, enabling precise change tracking and code repository security. Blockchain technology uses hashing to create immutable chains where each block contains the previous block's hash, preventing historical data alteration. Digital forensics relies on hash verification to maintain legal admissibility of evidence through tamper-evident proof. These applications demonstrate hashing's critical role in modern data protection strategies.



### Critical Insights About Password Strength and Security Implementation

Password security analysis revealed that length often provides better protection than complexity alone. A 12-character simple password frequently offers superior security compared to 8-character complex passwords due to exponential security scaling. Character set diversity including uppercase, lowercase, numbers, and symbols dramatically improves security, while long passphrases with spaces provide exceptional protection while remaining memorable. Algorithm selection proves equally important as password strength. Fast algorithms like MD5 enable rapid brute-force attacks, while adaptive algorithms like BCrypt scale security with advancing computing power. Rainbow table vulnerabilities make common passwords useless regardless of complexity. Based on timing analysis, compliant policies should enforce 12+ character minimums with BCrypt implementation and multi-factor authentication for critical systems.

