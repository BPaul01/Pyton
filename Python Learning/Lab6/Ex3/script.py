import os
import sys

try:
    if len(sys.argv) != 2:
        raise Exception("Invalid number of parameters")

    directory = sys.argv[1]

    size = 0

    if not os.path.exists(directory):
        raise Exception("Folder doesn't exist")

    if not os.path.isdir(directory):
        raise Exception("Invalid directory")

    for root, dirs, files in os.walk(directory):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))

except Exception as e:
    print(e, file=sys.stderr)
else:
    print(f"Total size is: {size}")