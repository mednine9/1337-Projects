def handle_archive_access(filename: str, access_type: str = "CRISIS ALERT") -> None:
    print(f"{access_type}: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            data = file.read().strip()

        print(f"SUCCESS: Archive recovered - '{data}'")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {e}")
        print("STATUS: Crisis containment failed")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("-" * 50)

    handle_archive_access("lost_archive.txt")
    print("-" * 50)

    handle_archive_access("classified_vault.txt")
    print("-" * 50)

    handle_archive_access("standard_archive.txt", access_type="ROUTINE ACCESS")
    print("-" * 50)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
