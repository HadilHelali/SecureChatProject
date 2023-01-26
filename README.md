# SecureChat
SecureChat is  desktop application built with python where you can send secure messages encrypted with RSA

# Dependencies 

* [LDAP](https://pypi.org/project/python-ldap/) (Lightweight Directory Access Protocol) : LDAP authentication involves verifying provided usernames and passwords by connecting with a directory service that uses the LDAP protocol.
* [cryptography](https://pypi.org/project/cryptography/) : includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions. 
We used the cryptography package mainly for the X.509 Authentication Service
* [rsa](https://pypi.org/project/rsa/) : rsa implementation for python. It supports encryption and decryption, signing and verifying signatures, and key generation according to PKCS#1 version 1.5. We used this package to be send encrypted and secure messages between users.
* [customtkinter](https://pypi.org/project/customtkinter/0.3/) : is a modern and customizable python UI-library based on Tkinter that we use to create the iterfaces

# x509 Certification Process and LDAP authentification
<table align="center">
  <tr>
    <td><img src="https://techblognow.files.wordpress.com/2015/02/x509-2.gif" width=450 height=300></td>
     <td><img src="https://www.netsuite.com/portal/assets/img/business-articles/data-warehouse/infographic-bsa-how-ldap-defined-works.jpg" width=450 height=300></td>
  </tr>
   </table>

# ScreenShots

<table align="center">
  <tr>
    <td>Login</td>
     <td>Register</td>
     <td colspan="2"> ChatRoom </td>
  </tr>
  <tr>
    <td><img src="./Screenshots/Login.png" width=400 height=300></td>
    <td><img src="./Screenshots/Register.png" width=400 height=300></td>
    <td><img src="./Screenshots/ChatRoom.png" width=400 height=300></td>
  </tr>
   </table>

## Collaborators
This project was developped by :
| Raoua Trimech | Hadil Helali |
| --- | --- |
