#!/usr/bin/env python3
import subprocess # used to run command prompt commands
                  # https://www.python-engineer.com/posts/python-execute-system-command/
                  # https://docs.python.org/3/library/subprocess.html
import os
import shutil # https://docs.python.org/3/library/shutil.html
import sys

"""
Defines three functions:

1. list_envs_and_paths()
2. export_package_list()
3. remove_environment()

"""

def list_envs_and_paths():
    """Accepts 0 args. Lists environments and paths."""
    print("List environments and paths:\n")
    command = "conda info --envs"
    result = subprocess.check_output(command, shell=True, text=True)
    print(result)

list_envs_and_paths()

def export_package_list():
    """Accepts 0 args. Exports package list to file."""
    try:
        # use pip to list installed packages and versions
        result = subprocess.check_output("pip list --format=freeze", shell=True, text=True)

        # edit output to exclude version numbers
        package_list = []
        for line in result.splitlines():
            package_info = line.split("==")
            if len(package_info) >= 2:
                package_list.append(f"{package_info[0]}=={package_info[1]}")

        # write output to file
        with open("testenv_package_list.txt", "w") as f:
            f.write("\n".join(package_list))
            f.write("\n")

        print("Successfully exported package list to \"testenv_package_list.txt\"")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

export_package_list()

# USE WITH CAUTION!!
def remove_environment(force_deletion=True):
    """Delete testenv folder"""
    print("\nDeleting...\n")
    # remove the testenv environment directory
    testenv_path = r"C:\Users\photo\anaconda3\envs\testenv"

    if force_deletion:
        shutil.rmtree(testenv_path, ignore_errors=False)  # force deletion
        print("Successfully removed testenv environment completely, including directory.")
    else:
        try:
            os.rmdir(testenv_path)
            print("\nSuccessfully removed testenv environment completely, including directory.")
        except PermissionError:
            print(f"Error: Permission denied while removing '{testenv_path}'.")
        except OSError as e:
            raise

remove_environment()