def main() -> None:
    try:
        file = open("new_discovery.txt", "w")

        entry1 = "[ENTRY 001] New quantum algorithm discovered"
        entry2 = "[ENTRY 002] Efficiency increased by 347%"
        entry3 = "[ENTRY 003] Archived by Data Archivist trainee"

        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print("-" * 50)
        print("Initializing new storage unit: new_discovery.txt")
        print("Storage unit created successfully...")
        print("-" * 50)
        print("Inscribing preservation data...")
        print(entry1)
        print(entry2)
        print(entry3)
        print("-" * 50)
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

        file.write(entry1 + "\n")
        file.write(entry2 + "\n")
        file.write(entry3 + "\n")

        file.close()
    except Exception as e:
        print(f"CRITICAL ERROR: Storage unit initialization failed. ({e})")


if __name__ == "__main__":
    main()
