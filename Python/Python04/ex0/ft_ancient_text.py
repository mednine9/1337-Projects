if __name__ == "__main__":
    try:
        file = open("ancient_fragment.txt", "r")
        data = file.read()
        file.close()

        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print("-" * 50)
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print("-" * 50)
        print("RECOVERED DATA:")

        print(data.strip())

        print("-" * 50)
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
