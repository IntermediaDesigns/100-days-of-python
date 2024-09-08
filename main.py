import os

def select_folder():
    while True:
        folder = input("Enter the path of the folder (or 'cancel' to abort): ")
        print()
        if folder.lower() == 'cancel':
            return None
        if os.path.isdir(folder):
            return folder
        else:
            print("Invalid folder path. Please try again.")
            print()


def list_files(folder):
    print(f"Files in {folder}:")
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,
                                       file)) and not file.startswith('.'):
            print(file)
    print()


def list_folders():
    print("Folders:")
    for item in os.listdir():
        if os.path.isdir(item) and not item.startswith('.'):
            print(item)
    print()


print()
while True:
    print(
        "1. Create Folder, 2. Create a File, 3. List Files, 4. Save copy, 5. Delete a File, 6. Exit"
    )
    print()
    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        list_folders()
        print()
        folder_name = input("Enter the name of the folder: ")
        print()
        if os.path.exists(folder_name):
            print("Folder already exists")
        else:
            os.mkdir(folder_name)
            print("Folder created successfully")
            print()
            list_folders()
        print()

    elif choice == "2":
        list_folders()
        print()
        folder = select_folder()
        if folder:
            list_files(folder)
            file_name = input("Enter the name of the file to create: ")
            print()
            file_path = os.path.join(folder, file_name)
            if os.path.exists(file_path):
                print("File already exists")
                print()
            else:
                with open(file_path, "w") as f:
                    f.write("This is a new file")
                print(f"File created successfully in {folder}")
                print()
                list_files(folder)
                print()
        else:
            print("Operation cancelled")
            print()

    elif choice == "3":
        list_folders()
        folder = select_folder()
        if folder:
            list_files(folder)
        else:
            print("Operation cancelled")
            print()

    elif choice == "4":
        print("Select source folder:")
        print()
        list_folders()
        source_folder = select_folder()
        if source_folder:
            print("Files in source folder:")
            print()
            list_files(source_folder)
            file_name = input("Enter the name of the file to save a copy: ")
            print()
            file_path = os.path.join(source_folder, file_name)
            if os.path.exists(file_path):
                print("Select destination folder:")
                print()
                list_folders()
                backup_folder = select_folder()
                if backup_folder:
                    backup_file = os.path.join(backup_folder,
                                               file_name + ".bak")
                    with open(file_path,
                              "r") as source, open(backup_file, "w") as target:
                        target.write(source.read())
                    print(f"File backed up successfully to {backup_folder}")
                    print()
                    print("Files in destination folder:")
                    list_files(backup_folder)
                else:
                    print("Operation cancelled")
            else:
                print("File not found")
                print()
        else:
            print("Operation cancelled")
            print()

    elif choice == "5":
        list_folders()
        folder = select_folder()
        if folder:
            list_files(folder)
            file_name = input("Enter the name of the file to delete: ")
            print()
            file_path = os.path.join(folder, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                print("File deleted successfully")
                print()
            else:
                print("File not found")
                print()
        else:
            print("Operation cancelled")
            print()

    elif choice == "6":
        break

    else:
        print("Invalid choice")
        print()
