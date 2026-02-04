Overview

This project is a Python-based file encryption and decryption tool that securely protects files using AES-256 encryption. It follows industry-standard cryptographic practices, including secure key derivation, random salt, and initialization vectors (IV).

The tool allows users to:

Encrypt files using a password

Decrypt encrypted files back to their original form

Maintain clean separation between input, encrypted, and decrypted files

This project is designed for cybersecurity learning, cryptography fundamentals, and secure software development.

🔒 Cryptography Used

AES-256 (Advanced Encryption Standard)

CBC (Cipher Block Chaining) mode

PBKDF2-HMAC-SHA256 for key derivation

Random Salt & IV for enhanced security

PKCS7 Padding

These techniques prevent:

Brute-force attacks

Rainbow table attacks

Pattern leakage

Weak password usage

📁 Project Structure
file_crypto_tool/
│
├── main.py                 # Main program (CLI interface)
├── crypto_utils.py         # Encryption & decryption logic
├── README.md               # Project documentation
│
├── input_files/            # Original files (plaintext)
├── encrypted_files/        # Encrypted output files (.enc)
└── decrypted_files/        # Decrypted/restored files

Folder Responsibilities
Folder	Purpose
input_files/	Stores original files to be encrypted
encrypted_files/	Stores encrypted .enc files
decrypted_files/	Stores decrypted output files

This separation prevents accidental overwrites and data loss.

⚙️ Requirements

Python 3.8+

cryptography library

Install Dependency
pip install cryptography

▶️ How to Run the Tool
1️⃣ Encrypt a File

Place the file inside input_files/

Run:

python main.py


Select option 1

Enter:

File name

Encryption password

Encrypted file will be created in encrypted_files/

2️⃣ Decrypt a File

Run:

python main.py


Select option 2

Enter:

Encrypted file name (.enc)

Correct password

Decrypted file will be restored in decrypted_files/

🧠 How It Works (High Level)

User enters a password

A secure encryption key is derived using PBKDF2

File data is encrypted using AES-256

Salt + IV + encrypted data are stored together

During decryption, the same password regenerates the key to restore the file

⚠️ Incorrect passwords will fail decryption safely.

🚫 Security Notes

Passwords are never stored

Keys are never saved to disk

Random salt and IV are generated for every encryption

Original files are never modified

🧪 Educational Value

This project demonstrates:

Practical cryptography implementation

Secure file handling

Proper project structure

Defensive security principles

Python security programming

Suitable for:

Cybersecurity students

Pentesting learners

Blue team practice

Portfolio projects

🚀 Future Enhancements

Password confirmation & strength checking

File integrity verification (HMAC)

Folder encryption support

AES-GCM (authenticated encryption)

Logging & report generation

GUI or web interface

Secure file deletion (shredding)

⚠️ Disclaimer

This tool is created for educational and learning purposes only.
Users are responsible for complying with applicable laws and regulations.

👤 Author

Vinay Kumar Vallala

OUTPUT :
<img width="648" height="583" alt="Image" src="https://github.com/user-attachments/assets/43e2ed03-1ed2-43fc-b565-9dba6787d652" />
