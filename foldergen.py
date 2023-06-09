#!/usr/bin/env python

import sys
import os
import yaml

def yaml_flat(x):
    for key, value in x.items():
        if isinstance(value, dict):
            for k, v in yaml_flat(value):
                k = f'{key}/{k}'
                yield (k, v)
        else:
            yield (key, value)

def _folder_gen_recursive(filename):
    with open(filename, "r") as file:
        try:
            data = yaml.load(file, Loader = yaml.FullLoader)
        except:
            print ("ERROR: file \"%s\" is not a yaml file.\n"%filename)
            sys.exit(2)
    
    if type(data) is dict:
        folder_name_list = yaml_flat(data)
        print("Current Folder "+os.getcwd())
        for folder_name,value in folder_name_list:
            if os.path.exists(folder_name):
                print("    Folder \""+folder_name+"\" already existes!")
            else:
                os.makedirs(folder_name, exist_ok=True)
                if os.path.exists(folder_name):
                    print("    Folder \""+folder_name+"\" Create Successfully!")
                else:
                    print("    Folder \""+folder_name+"\" Create Failed!")
    else:
        print ("ERROR: file \"%s\" is not a yaml file.\n"%filename)
        sys.exit(2)

def usage(sw_name):
    usage = "This is used to recursively create folders based on yaml file with folder structure!" \
            "\n\nUsage: "+sw_name+" <Yaml File> [-h|--help] " \
            "\n\nOptions: " \
            "\n  -h    --help      Show the help " \
            "\n\nExample: " \
            "\n----------------------------------- " \
            "\n\n  user@host> "+sw_name+" folder.yaml " \
            "\n\n-----------------------------------\n "
    print(usage)
    sys.exit(2)

if __name__ == "__main__":
    sw_name=(str(sys.argv[0][sys.argv[0].rfind(os.sep) + 1:]).split("/")[-1])
    if len(sys.argv) < 2:
        print ("ERROR: missing yaml file for fodler structure!\n")
        usage(sw_name)
    else:
        folder_yaml_file=sys.argv[1]
        if "-h" == folder_yaml_file or "--help" == folder_yaml_file:
            usage(sw_name)
        elif os.path.isfile(folder_yaml_file) and os.stat(folder_yaml_file).st_size != 0:
            _folder_gen_recursive(sys.argv[1])
        else:
            print ("ERROR: No such yaml file \"%s\" or it is empty!\n"%folder_yaml_file)
            sys.exit(2)
