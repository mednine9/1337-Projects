import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print("-" * 50)

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print("-" * 50)

    sys.stdout.write(f"[STANDARD] Archive status from"
                     f" {archivist_id}: {status_report}\n")

    sys.stderr.write("[ALERT] System diagnostic:"
                     " Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("-" * 50)
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
