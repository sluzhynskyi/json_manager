import json

path = "YOUR_JSONFILE_PATH"
file = open(path, mode="r", encoding='utf8')
j_file = json.load(file)


def fld_lst(type):
    """
    any -> lst
    Function returns all posible folders where user can move
    """
    lst = []
    if isinstance(type, dict):
        return list(type.keys())
    elif isinstance(type, list):
        for i in range(1, len(type) + 1):
            lst.append("element " + str(i))
        return lst


def current_pos():
    """
    None -> None
    This function show your current position
    """
    st = "/ "
    for i in parents:
        st += i + " /"
    return st


def usage():
    """
    None -> None
    For user understanding
    """
    print("IF you wont move to another directory write folder_name")
    print("IF you wont move to the home directory just press Enter\n")


def main():
    """
    None -> None
    Main function for starting all module
    """
    global parents, current_lct
    parents = []
    current_lct = j_file

    # Printing usage
    usage()
    # Main program
    while True:
        st = ""
        try:
            # User position
            if parents:
                pos = current_pos()
                print(pos)
            # Folders that user can check out
            if isinstance(current_lct, dict) or isinstance(current_lct, list):
                for i in fld_lst(current_lct):
                    st += i + "|"
                print(st)
            else:
                print(current_lct)
            # User moving to the another folder
            prompt = input("$: ")
            if prompt == "":
                current_lct = j_file
                parents = []
            elif isinstance(current_lct, list):
                current_lct = current_lct[int(prompt[8:]) - 1]
                parents.append(prompt)
            elif isinstance(current_lct, dict):
                current_lct = current_lct[prompt]
                parents.append(prompt)
        except KeyError:
            print("This file not exist")
        except ValueError:
            print("This file not exist")


if __name__ == '__main__':
    main()
