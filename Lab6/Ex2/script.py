import os
import sys

if len(sys.argv) != 2:
    raise Exception("Invalid number of parameters")

directory = sys.argv[1]

try:
    if not os.path.exists(directory):
        raise Exception("Folder doesn't exist")

    if not os.path.isdir(directory):
        raise Exception("Invalid directory")

    files = os.listdir(directory)
    print(files)

    try:
        #prefix the index to the filename
        for index, file in enumerate(files):
            new_path = os.path.join(directory, f"{index}_{file}")
            os.renames(os.path.join(directory, file), new_path)
    except Exception as e:
        print("File can't be renamed", file=sys.stderr)

except Exception as e:
    print(e, file=sys.stderr)