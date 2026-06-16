from logger_module import log_event
from security import (
    get_role,
    can_read,
    can_write,
    can_delete,
    log_security_violation
)

# FILE CLASS

class File:
    """
    Represents a file inside the simulated operating system.
    """

    def __init__(self, name, owner, permission="rw"):

        self.name = name
        self.owner = owner
        self.permission = permission
        self.content = ""

    def read(self):
        """
        Return file content.
        """
        return self.content

    def write(self, data):
        """
        Write data into the file.
        """

        if self.permission == "r":
            return "WRITE PERMISSION DENIED"

        self.content += data

        return "WRITE SUCCESSFUL"


# DIRECTORY CLASS

class Directory:
    """
    Represents a directory/folder in the file system.
    """

    def __init__(self, name):

        self.name = name
        self.files = {}
        self.subdirectories = {}


# FILE SYSTEM CLASS

class FileSystem:
    """
    Main file system controller.
    Handles all file and directory operations.
    """

    def __init__(self):

        self.root = Directory("root")

    # CREATE FILE

    def create_file(self, directory, filename, owner, permission="rw"):

        if filename in directory.files:

            print("\n[ERROR] File already exists")

            return

        new_file = File(
            filename,
            owner,
            permission
        )

        directory.files[filename] = new_file

        print(f"\n[SUCCESS] File '{filename}' created")

        log_event(
            f"FILE CREATED | "
            f"File: {filename} | "
            f"Owner: {owner}"
        )

    # WRITE FILE

    def write_file(self, directory, filename, data, username):

        if filename not in directory.files:

            print("\n[ERROR] File not found")

            return

        role = get_role(username)

        if not can_write(role):

            log_security_violation(
                username,
                f"WRITE -> {filename}"
            )

            return

        result = directory.files[filename].write(data)

        print(f"\n[{result}]")

        log_event(
            f"FILE WRITE | "
            f"User: {username} | "
            f"File: {filename}"
        )

    # READ FILE

    def read_file(self, directory, filename, username):

        if filename not in directory.files:

            print("\n[ERROR] File not found")

            return

        role = get_role(username)

        if not can_read(role):

            log_security_violation(
                username,
                f"READ -> {filename}"
            )

            return

        content = directory.files[filename].read()

        print("\n========== FILE CONTENT ==========")

        print(content)

        print("==================================")

        log_event(
            f"FILE READ | "
            f"User: {username} | "
            f"File: {filename}"
        )

    # DELETE FILE

    def delete_file(self, directory, filename, username):

        if filename not in directory.files:

            print("\n[ERROR] File not found")

            return

        role = get_role(username)

        if not can_delete(role):

            log_security_violation(
                username,
                f"DELETE -> {filename}"
            )

            return

        del directory.files[filename]

        print(f"\n[SUCCESS] '{filename}' deleted")

        log_event(
            f"FILE DELETED | "
            f"User: {username} | "
            f"File: {filename}"
        )

    # CREATE DIRECTORY

    def create_directory(self, parent_directory, dirname):

        if dirname in parent_directory.subdirectories:

            print("\n[ERROR] Directory already exists")

            return

        new_directory = Directory(dirname)

        parent_directory.subdirectories[dirname] = new_directory

        print(f"\n[SUCCESS] Directory '{dirname}' created")

        log_event(
            f"DIRECTORY CREATED | "
            f"Directory: {dirname}"
        )

    # LIST DIRECTORY CONTENTS

    def list_directory(self, directory):

        print("\n========== DIRECTORY LIST ==========")

        print("\nDirectories:")

        if directory.subdirectories:

            for dirname in directory.subdirectories:

                print(f"  [DIR]  {dirname}")

        else:

            print("  No Directories")

        print("\nFiles:")

        if directory.files:

            for filename, file_obj in directory.files.items():

                print(
                    f"  [FILE] {filename} "
                    f"(Permission: {file_obj.permission})"
                )

        else:

            print("  No Files")

        print("\n====================================")