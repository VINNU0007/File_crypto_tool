from crypto_utils import encrypt_file, decrypt_file
import os

def main():
    print("""
    ==============================
      FILE ENCRYPTION TOOL (AES-256)
    ==============================
    1. Encrypt a file
    2. Decrypt a file
    """)

    choice = input("Select option: ").strip()

    if choice == "1":
        filename = input("Enter filename from input_files/: ").strip()
        password = input("Enter encryption password: ").strip()

        input_path = f"input_files/{filename}"
        output_path = f"encrypted_files/{filename}.enc"

        encrypt_file(input_path, output_path, password)
        print("✅ File encrypted successfully")

    elif choice == "2":
        filename = input("Enter encrypted filename (.enc): ").strip()
        password = input("Enter decryption password: ").strip()

        input_path = f"encrypted_files/{filename}"
        output_path = f"decrypted_files/{filename.replace('.enc','')}"

        decrypt_file(input_path, output_path, password)
        print("✅ File decrypted successfully")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
