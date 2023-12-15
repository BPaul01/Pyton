import sys
import os
import json

try:
    if len(sys.argv) != 3:
        raise Exception("Error: Invalid number of parameters")

    target_directory = sys.argv[1]

    # check folder existence
    if not os.path.exists(target_directory):
        raise Exception("Error: Target folder doesn't exist")

    # check if it is a folder
    if not os.path.isdir(target_directory):
        raise Exception("Error: The given path doesn't correspond to a folder")

    # check if it is writeable
    if not os.access(target_directory, os.W_OK):
        raise Exception("Error: Target folder is not writeable")

    source_file = sys.argv[2]

    # check file existence
    if not os.path.exists(source_file):
        raise Exception("Error: Source file doesn't exist")

    # check if it is a folder
    if not os.path.isfile(source_file):
        raise Exception("Error: The given path doesn't correspond to a file")

    # check if it has the right extension
    if not source_file.endswith(".json"):
        raise Exception("Error: Expected a .json file")

    # check if it is readable
    if not os.access(target_directory, os.R_OK):
        raise Exception("Error: Source file is not readable")

    # read the source file
    try:
        s_file = open(source_file, mode="r")
        print(f"Contents of the source file: {s_file.read()}")
        s_file.close()
    except Exception as e:
        raise Exception("Error: Could not open te file")

except Exception as e:
    print(e, file=sys.stderr)
else:
    print("All gut")