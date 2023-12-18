import shutil
import sys
import os
import ijson


def reset_folder(folder):
    try:
        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            shutil.rmtree(item_path)
    except Exception as e:
        print("Something has gone terribly wrong", file=sys.stderr)
        raise SystemExit

def create_structure(source_file, target_directory):
    not_the_first = False
    current_dir = target_directory
    file_name = ""

    # read the source file and load its contents into a dictionary
    try:
        json_data = open(source_file, mode="rb")

        for prefix, event, value in ijson.parse(json_data):
            # handle directory creation
            if event == "start_map" and not_the_first:
                # get the name of the directory
                dirs = prefix.split(".")
                dir_name = dirs[len(dirs) - 1]

                # check if there are other folders with the same name
                if dir_name in os.listdir(current_dir):
                    # revert the target folder
                    reset_folder(target_directory)

                    raise Exception("Error: Found two folders with the same name at the same level\n"
                                    "Target folder has been reseted")
                else:
                    # create the folder
                    print(f"Creating the folder {dir_name}")
                    try:
                        os.mkdir(os.path.join(current_dir, dir_name))
                    except Exception as e:
                        raise Exception("Error: Could not create the folder")

                    # update the current directory
                    current_dir = os.path.join(current_dir, dir_name)

            else:
                not_the_first = True

            if event == "map_key":
                file_name = value

            #handle file creation
            if event == "string":

                # check if there are other files with the same name
                if file_name in os.listdir(current_dir):
                    # revert the target folder
                    reset_folder(target_directory)

                    raise Exception("Error: Found two files with the same name at the same level\n"
                                    "Target folder has been reseted")
                else:
                    # create the file
                    try:
                        file = open(os.path.join(current_dir, file_name), mode="w")

                        # write the content of the file in chunks
                        for i in range(0, len(value), 1024):
                            chunk_to_write = value[i:i + 1024]
                            file.write(chunk_to_write)

                        file.close()
                    except Exception as e:
                        raise Exception(f"Error: Could not create the file {file_name}")

            if event == "end_map":
                # update the current directory
                current_dir = os.path.dirname(current_dir)


        json_data.close()

    except Exception as e:
        raise e


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
    if not os.access(source_file, os.R_OK):
        raise Exception("Error: Source file is not readable")

    create_structure(source_file, target_directory)

except Exception as e:
    print(e, file=sys.stderr)
else:
    print("Operation completed successfully")
