import time


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.created_time = time.ctime()
        self.last_accessed = None

    def open_file(self):
        self.last_accessed = time.ctime()
        print(f"\n[Opened] {self.name} | Size: {self.size} KB | Last Accessed: {self.last_accessed}")


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.sub_directories = []

    def create_file(self, file_name, file_size):
        self.files.append(File(file_name, file_size))
        print(f"Created file: {file_name} ({file_size} KB)")

    def create_directory(self, directory_name):
        self.sub_directories.append(Directory(directory_name))
        print(f"Created directory: {directory_name}")

    def list_files(self):
        print("\n--- Files ---")
        if not self.files:
            print("No files found.")
            return
        for file in self.files:
            print(f"- {file.name} ({file.size} KB)")

    def list_directories(self):
        print("\n--- Directories ---")
        if not self.sub_directories:
            print("No directories found.")
            return
        for directory in self.sub_directories:
            print(f"- {directory.name}")

    def open_file(self, file_name):
        for file in self.files:
            if file.name == file_name:
                file.open_file()
                return
        print("\nError: File not found.")


class FileSystem:
    def __init__(self):
        self.root = Directory("root")


file_system = FileSystem()
root = file_system.root

while True:
    print("\n PREDICTIVE FILE SYSTEM ")
    print("1. Create File       2. Create Directory")
    print("3. View Files        4. View Directories")
    print("5. Open File         6. Exit")

    choice = input("\nSelect option (1-6): ").strip()

    if choice == "1":
        file_name = input("File name: ").strip()
        try:
            file_size = int(input("File size (KB): "))
            root.create_file(file_name, file_size)
        except ValueError:
            print("Invalid size. Please enter a number.")

    elif choice == "2":
        directory_name = input("Directory name: ").strip()
        root.create_directory(directory_name)

    elif choice == "3":
        root.list_files()

    elif choice == "4":
        root.list_directories()

    elif choice == "5":
        file_name = input("File name to open: ").strip()
        root.open_file(file_name)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
