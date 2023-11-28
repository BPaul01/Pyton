import sys
import os

try:
    if len(sys.argv) != 3:
        raise Exception("Invalid number of parameters")

    directory = sys.argv[1]
    file_ext = sys.argv[2]

    if not os.path.exists(directory):
        raise Exception("Directory doesn't exist")

    if not os.path.isdir(directory):
        raise Exception("Invalid directory")

    #print(os.listdir(directory))
    match = [file for file in os.listdir(directory) if file.endswith(file_ext)]
    if len(match) == 0:
        raise Exception(f"No files with the extension {file_ext} were found")

    #print(match)
    try:
        for file in match:
            print(f"Content of {os.path.join(directory, file)}:")
            f = open(os.path.join(directory, file), mode='r')
            for line in f:
                print(line.strip())
            f.close()
            print()
    except IOError as e:
        print(f"Access to file {file} denied", file=sys.stderr)

except Exception as e:
    print(e, file=sys.stderr)


