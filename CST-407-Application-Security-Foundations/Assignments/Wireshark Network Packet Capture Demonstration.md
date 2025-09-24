<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; text-align: center;">

# Wireshark Network Packet Capture Demonstration

## Owen Lindsey
## Professor Sluiter, Shad
## CST-407
## Grand Canyon University

</div>



### **Overview**

Application security is both an internal and external challenge. The way in which an application sends data across a network will determine how secure the data remains. This lesson will demonstrate that unencrypted network requests are vulnerable to packet sniffers, as seen in Figure 1.

Wireshark is a popular hacking tool as well as network engineer's diagnostic tool for viewing communication over a computer network. For engineers, seeing error messages, response times and traffic routes can be valuable to improving the performance of network devices. For hackers, network traffic may reveal sensitive information.

1. Tools Needed: (a) Java IDE (b) Wireshark application.

2. Using this tutorial, create a very simple application that has a login form and form processor. The Java application will run a web server that operates a login screen and results screen.

3. We will capture the network traffic using Wireshark and steal credentials from an unencrypted login session.

4. Finally, we will convert the unencrypted http traffic to an encrypted https protocol and compare the traffic captured by Wireshark.

### **Output of Spring Boot Project**

![[Pasted image 20250923104043.png]]

![[Pasted image 20250923104026.png]]


<div style="page-break-before: always;"></div>

### **Wireshark Instructions**  
  
 Download and install Wireshark.  
  
The application might ask you to install ChmodBPF and relaunch the app.  
  
 Windows will need a module called npcap. Npcap is a packet capture library for Windows  
  
that includes a "loopback adapter" that allows you to capture loopback traffic with  
  
![[Pasted image 20250923105250.png]]

You should see a long list of text. Each line in the report represents a packet of communications between your computer and the localhost web server.

![[Pasted image 20250923105558.png]]
 
Apply a filter to show only "http" packets.  
Select one of the http packets with a 200 result and text/html content.   
Expand the "Line-based text data" to see the contents of this request

![[Pasted image 20250923105842.png]]

You can retrieve a more readable version of the packet by right-clicking the line in the log >Follow > HTTP Stream

![[Pasted image 20250923105953.png]]

Select the POST request and expand the contents. You should be able to see the form items for username and password by opening the items in the bottom window

![[Pasted image 20250923110121.png]]

You can also display the entire packet in a more readable format by right-clicking > Follow > HTTP stream

![[Pasted image 20250923110214.png]]

<div style="page-break-before: always;"></div>

**About Internet Protocol Exchanges**  
  
Every time a service needs to communicate with a client over digital networks, a protocol must  be designed to make the transaction work smoothly. In human life, we have developed protocols of communication that help make the process standardized.  
  
“Hello?”  
“Hi, this is _______ from the _______. How are you today?”  
“I’m fine, thank you. What can I do for you?”  
  
(Payload of the conversation)  
  
“OK. Thank you calling. That helps a lot.”  
  “Glad to help. Good bye”  
  
In digital communications the clients and servers work in a similar manner. Each transaction usually begins with a "hello" packet. There are many "Acknowledge" packets, which are essentially "OK" messages. Finally, a "Goodbye" packet ends the transaction. Wireshark enables you to see many conversations that are taking place simultaneously on a network in a variety of protocols. 


### **Other Common Protocols**  

Here is a list of common protocols. Complete the table by researching the name and a one sentence description of each protocol.


| Initials | Name                               | What it is used for                        |
| -------- | ---------------------------------- | ------------------------------------------ |
| **HTTP** | Hypertext Transfer Protocol        | Send hypertext                             |
| **TCP**  | Transmission Control Protocol      | Reliable data transmission over networks   |
| **SNMP** | Simple Network Management Protocol | Monitor and manage network devices         |
| **FTP**  | File Transfer Protocol             | Transfer files between computers           |
| **SMTP** | Simple Mail Transfer Protocol      | Send email messages                        |
| **IMAP** | Internet Message Access Protocol   | Access email messages stored on server    |
| **POP3** | Post Office Protocol 3             | Download email messages to local device   |
| **DNS**  | Domain Name System                 | Translate domain names to IP addresses    |
| **SSH**  | Secure Shell                       | Secure remote access to computers         |
| **UDP**  | User Datagram Protocol             | Fast but unreliable data transmission     |
| **RDP**  | Remote Desktop Protocol            | Remote desktop access to Windows systems  |
| **VoIP** | Voice over Internet Protocol       | Make voice calls over internet networks   |
| **DHCP** | Dynamic Host Configuration Protocol| Automatically assign IP addresses         |
| **LDAP** | Lightweight Directory Access Protocol | Access and manage directory services   |
| **TLS**  | Transport Layer Security           | Encrypt communications for security       |

<div style="page-break-before: always;"></div>

### **How to Fix the Application's Vulnerability**

To protect data in transit, we need to add encryption to the login application. The **http** protocol is unencrypted and therefore vulnerable to network sniffers like Wireshark. The **https** protocol was developed to provide secure transport. At first, https was used only for sensitive information such as logins or financial transactions. Unencrypted data is less computationally expensive. Later, https became the default mode to transfer all data.  
  

Here are the tasks we must do to transmit data in encrypted format:

1.      Create an SSL / TLS certificate.

2.      Configure the application to use the https protocol.

3.      Direct old http requests to https.

### **About Certificates**

### **What Are SSL Certificates?**

SSL (secure sockets layer) certificates are digital certificates that provide a way to encrypt communication between a user's browser and a web server. SSL was replaced by TLS in 2015, but the protocol remains to be called SSL. SSL certificates are like the public and private keys used in the GPG exercise done earlier in this course.

### **How SSL Certificates Help Encrypt Data**

When a client connects to a server via HTTPS, an SSL handshake occurs. During this handshake, the client and server use the public and private keys to create a shared encryption key that is used for the duration of the session, as seen in Figure 43.

- The server presents its SSL certificate to the client. The server's public key is part of the certificate.

- The client and server agree on an encryption method.

- A unique session key is created for this specific connection.

- This session key is used to encrypt and decrypt the data exchanged during the session.
  
![[Pasted image 20250923111758.png]]

<div style="page-break-before: always;"></div>

### **How Do We Know if an SSL Certificate is Valid?

**Any computer can generate an SSL. In fact, in the next steps we will create our own certificate. However, on a real website you need to choose from a list of "white listed" certificate providers.**  A **certificate Aathority (CA)** is an organization or entity responsible for issuing digital certificates. Some well-known CA organizations include **Symantec, Comodo**, and **GoDaddy**, as seen in Figures 44 and 45. These companies are recognized and trusted by Apple, Google, Microsoft, and other leading tech companies. As of August 2024, 133 CA organizations are trusted by Microsoft Windows. The US Federal Government manages the **Federal PKI** for use with all government applications.

- **Validity Period**: SSL certificates have a validity period, often one or two years. They must be renewed before they expire to continue ensuring secure connections.

### **Error Messages from Self-Signed Certificates**

Self-signed certificates are SSL/TLS certificates that are generated and signed by the organization itself, rather than a trusted CA. These certificates can be used for testing and internal purposes but are not trusted by browsers by default because they do not come from a recognized CA.

**Common Errors with Self-Signed Certificates**:

- **"Your connection is not private"**: Seen in Figure 46, this error occurs because the browser cannot verify the certificate's authenticity.
- **"Invalid certificate" or "Untrusted certificate"**: This indicates that the certificate is not from a trusted CA.
- **"Self-signed certificate in the certificate chain"**: This error specifically indicates that the certificate is self-signed and not trusted.


### **About the SSL Create Statement**

keytool -genkeypair -alias springboot -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore keystore.p12 -validity 3650

Here's a breakdown of each part of the SSL generator.

- **-genkeypair**: Generates a public-private key pair.
- **-alias springboot**: Specifies the alias for the key pair in the keystore.
- **-keyalg RSA**: Specifies the algorithm to be used for generating the key pair, in this case, RSA.
- **-keysize 2048**: Specifies the size of the key, which is 2048 bits.
- **-storetype PKCS12**: Specifies the type of keystore to be created, PKCS12 is a standard for storing cryptographic information.
- **-keystore keystore.p12**: Specifies the name of the keystore file to be created.
- **-validity 3650**: Specifies the validity period of the certificate in days, which in this case is 10 years.

![[Pasted image 20250923113151.png]]

### **Repeat the Wireshark Process with the SSL-Enabled Application**

Complete the following steps to demonstrate that even though the login credentials can still be captured by Wireshark, the packets are now unreadable due to SSL encryption.

- Start Wireshark or restart the capture
  
![[Pasted image 20250923114856.png]]

The traffic protocol used by the application is no longer listed as **http** (clear text). Nor is there a protocol listed as **https**. Instead, you will see several TLSv1.2 events in the log. Wireshark labels the packets as "TLS" (or "SSL" for older versions) instead of "HTTPS" because it is indicating that the traffic is encrypted with the TLS protocol. Wireshark does not show "HTTPS" as the protocol because HTTPS is not a protocol layer on its own. Https it is just HTTP wrapped inside a secure TLS/SSL "tunnel,"

![[Pasted image 20250923113650.png]] 

<div style="page-break-before: always;"></div>

**Explanation of the Wireshark data**

- The captured packets show a sequence of secure communications.

- It is impossible to determine if these occurred during a login event or some other transaction.

- The encryption provided by TLS ensures that sensitive information like usernames and passwords cannot be easily intercepted or viewed by unauthorized parties.

- Any attempt to view the packets is futile. For example, the description of packet #1 shown below is "application data," a generic term.

- Viewing the contents results in a message that describes the data as "encrypted data."

- Each TLS packets is followed by a TCP Acknowledge packet, as seen in Figures 67 and 68. The Acknowledge packet is simply a confirmation that the previous transaction occurred without communication errors.
![[Pasted image 20250923113817.png]]


<div style="page-break-before: always;"></div>

### **Summary of Key Concepts**

This lesson demonstrated the critical importance of data encryption in web applications through hands-on network traffic analysis. Using Wireshark, we observed how unencrypted HTTP communications expose sensitive information such as usernames and passwords in plain text, making them vulnerable to network sniffing attacks. The exercise showed that any data transmitted over HTTP can be easily intercepted and read by unauthorized parties monitoring network traffic. To address this vulnerability, we implemented HTTPS by generating an SSL/TLS certificate and configuring our Spring Boot application for secure communications. The comparison between HTTP and HTTPS traffic in Wireshark clearly illustrated how TLS encryption transforms readable login credentials into unintelligible encrypted data packets labeled as "Application Data." This demonstration reinforced that HTTPS is essentially HTTP wrapped within a secure TLS tunnel, and that proper certificate implementation is essential for protecting data in transit. The lesson emphasized that while network monitoring tools like Wireshark serve legitimate purposes for network diagnostics and security analysis, they also highlight why encryption protocols are fundamental to modern web security and user privacy protection.
