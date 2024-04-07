# Structure Generator


## Project: B6

#### Task:

Create a script that takes as input from the command line a path to a directory and a file JSON FILE. In the JSON file is a dictionary containing a structure of directories and files so that: each key that has a dictionary value is a directory and the dictionary is the container,
and each key that has a string value is a file and that string is
the content of the file. The script will create in the folder given as argument the directories and files according to the JSON dictionary.

---------------------------------------------------------------------

Creati un script care primeste de la linia de comanda un path catre un director si un fisier
JSON. In fisierul JSON se afla un dictionar in care se afla o structura de directoare si fisiere
astfel: fiecare cheie care are ca valoare un dictionar este un director iar dictionarul contintul,
iar fiecare cheie care are ca valoare un string reprezinta un fisier iar string-ul respectiv este
continutul fisierului. Scriptul va crea in folderul dat ca argument directoarele si fisierele 
conform dictionarului din JSON.


### INPUT:
**create_structure.py root_folder_path structure_json_file_path**  

Exemplu de dictionar:  
{“dir1” : {“dir2”: {“file1”: “*continut1*”, “file2”: “*continut2*”}, “file3”: “*continut3*”}, “file4”: “*continut4*”}


### OUTPUT:
root_folder  
----dir1  
--------dir2  
------------file1: *continut1*  
------------file2: *continut2*  
--------file3: *continut3*  
----file4: *continut4*