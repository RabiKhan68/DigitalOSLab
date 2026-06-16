from filesystem import FileSystem
from memory import MemoryManager
from disk import DiskScheduler
from security import users, get_role
from logger_module import log_event


# SYSTEM INITIALIZATION

fs = FileSystem()

memory_manager = MemoryManager(3)

# Root directory
root = fs.root

# Create default directory
fs.create_directory(root, "students")

students_dir = root.subdirectories["students"]

# Create default sample file
fs.create_file(
    students_dir,
    "notes.txt",
    "admin1"
)


# DISPLAY HEADER

def display_header():

    print("\n================================================")
    print("        DIGITAL LAB OS SIMULATOR")
    print("================================================")


# LOGIN SYSTEM

display_header()

username = input("\nEnter Username: ").strip()

if username not in users:

    print("\n[ERROR] Invalid User")

    log_event(f"FAILED LOGIN -> {username}")

    exit()

role = get_role(username)

print(f"\n[SUCCESS] Login Successful")

print(f"User Role : {role.upper()}")

log_event(f"USER LOGIN -> {username}")


# MAIN PROGRAM LOOP

while True:

    print("\n================================================")
    print("                    MAIN MENU")
    print("================================================")

    print("1. Memory Management")

    print("2. File System")

    print("3. Disk Scheduling")

    print("4. View Directory")

    print("5. Exit")

    choice = input("\nEnter Choice: ").strip()

    # MEMORY MANAGEMENT

    if choice == "1":

        print("\n================================================")
        print("              MEMORY MANAGEMENT")
        print("================================================")

        try:

            pages = input(
                "\nEnter page sequence (space separated): "
            ).split()

            pages = [int(page) for page in pages]

            for page in pages:

                memory_manager.access_page(page)

            memory_manager.show_statistics()

        except ValueError:

            print("\n[ERROR] Invalid page sequence")

    # FILE SYSTEM MENU

    elif choice == "2":

        while True:

            print("\n================================================")
            print("                 FILE SYSTEM")
            print("================================================")

            print("1. Create File")

            print("2. Write File")

            print("3. Read File")

            print("4. Delete File")

            print("5. Back")

            fs_choice = input("\nEnter Choice: ").strip()

            # CREATE FILE

            if fs_choice == "1":

                filename = input(
                    "\nEnter Filename: "
                ).strip()

                permission = input(
                    "Enter Permission (r/rw): "
                ).strip()

                fs.create_file(
                    students_dir,
                    filename,
                    username,
                    permission
                )

            # WRITE FILE

            elif fs_choice == "2":

                filename = input(
                    "\nEnter Filename: "
                ).strip()

                data = input(
                    "Enter Data: "
                )

                fs.write_file(
                    students_dir,
                    filename,
                    data,
                    username
                )

            # READ FILE

            elif fs_choice == "3":

                filename = input(
                    "\nEnter Filename: "
                ).strip()

                fs.read_file(
                    students_dir,
                    filename,
                    username
                )

            # DELETE FILE

            elif fs_choice == "4":

                filename = input(
                    "\nEnter Filename: "
                ).strip()

                fs.delete_file(
                    students_dir,
                    filename,
                    username
                )

            # BACK TO MAIN MENU

            elif fs_choice == "5":

                break

            else:

                print("\n[ERROR] Invalid Choice")

    # DISK SCHEDULING

    elif choice == "3":

        print("\n================================================")
        print("               DISK SCHEDULING")
        print("================================================")

        try:

            requests = input(
                "\nEnter Disk Requests (space separated): "
            ).split()

            requests = [int(request) for request in requests]

            initial_head = int(
                input("Enter Initial Head Position: ")
            )

            disk_scheduler = DiskScheduler(
                requests,
                initial_head
            )

            disk_scheduler.sstf()

        except ValueError:

            print("\n[ERROR] Invalid Disk Request Input")

    # VIEW DIRECTORY

    elif choice == "4":

        fs.list_directory(students_dir)

    # EXIT PROGRAM

    elif choice == "5":

        print("\n================================================")
        print("         EXITING DIGITAL LAB SIMULATOR")
        print("================================================")

        log_event("SYSTEM EXIT")

        break

    # INVALID CHOICE

    else:

        print("\n[ERROR] Invalid Menu Choice")
