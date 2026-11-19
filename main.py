from cryptography.fernet import Fernet

def main():
    key = Fernet.generate_key().decode("ascii")
    print("\n========== GENERATED FERNET KEY ==========")
    print(key)
    print("==========================================")
    print("Copy this key into your bot's ENCRYPTION_KEY variable.")
    print("Do not generate a new key after encrypting data.")

if __name__ == "__main__":
    main()
