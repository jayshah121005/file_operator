from datetime import datetime
import os


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"


    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")

            if entry.strip() == "":
                print("Entry cannot be empty.")
                return

            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"[{date_time}]\n")
                file.write(entry + "\n")
                file.write("-" * 40 + "\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied while accessing the journal file.")


    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

                if data.strip() == "":
                    print("\nNo journal entries found.")
                else:
                    print("\nYour Journal Entries:")
                    print("-" * 40)
                    print(data)

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied while reading the journal file.")


    def search_entry(self):
        try:
            keyword = input("\nEnter keyword or date to search: ")

            if keyword.strip() == "":
                print("Search value cannot be empty.")
                return

            with open(self.filename, "r") as file:
                data = file.read()

            if keyword.lower() in data.lower():
                print("\nMatching entries:")
                print("-" * 40)

                entries = data.split("-" * 40)

                for entry in entries:
                    if keyword.lower() in entry.lower():
                        print(entry.strip())
                        print("-" * 40)

            else:
                print("\nNo matching entries found.")

        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("\nError: Permission denied while reading the journal file.")


    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return

            confirm = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            )

            if confirm.lower() == "yes":
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")

            elif confirm.lower() == "no":
                print("\nDeletion cancelled.")

            else:
                print("\nPlease enter yes or no.")

        except FileNotFoundError:
            print("\nNo journal entries to delete.")

        except PermissionError:
            print("\nError: Permission denied. Cannot delete the journal file.")



journal = JournalManager()

print("Welcome to Personal Journal Manager!")

while True:

    print("\nPlease select an option:")
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            journal.add_entry()

        elif choice == 2:
            journal.view_entries()

        elif choice == 3:
            journal.search_entry()

        elif choice == 4:
            journal.delete_entries()

        elif choice == 5:
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("\nInvalid option. Please select a valid option from the menu.")

    except ValueError:
        print("\nInvalid input. Please enter a number from 1 to 5.")