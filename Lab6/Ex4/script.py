import os
import sys

if len(sys.argv) != 2:
    raise Exception("Invalid number of parameters")

directory = sys.argv[1]

result = dict()

try:
    if not os.path.exists(directory):
        raise Exception("Folder doesn't exist")

    if not os.path.isdir(directory):
        raise Exception("Invalid directory")

    files = os.listdir(directory)
    print(f"Files: {files}")

    for file in files:
        #find the extension
        point = file.index(".")
        ext = file[point:]
        if not ext in result:
            result[ext] = 1
        else:
            result[ext] += 1

except Exception as e:
    print(e, file=sys.stderr)
else:
    print(result)