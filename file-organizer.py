from pathlib import Path
import shutil


def choose_folder():
    while True:
        main_directory = Path(input("Folder to tidy : "))
        if main_directory.is_dir():
            break
        else:
            print("Folder not found")
    return main_directory


def add_file(src_file, dest_path, overwrite=False):
    try:
        if dest_path.exists() and not overwrite:
            return False

        shutil.move(src_file, dest_path)
        return True

    except PermissionError:
        print(f"{src_file.name} : Permission denied")
        return False


def duplicate(src_file, dest_folder):
    user_input = input(
        "Another file has the same name\n1 to overwrite; 2 to rename; any other key to ignore : "
    )

    if user_input == "1":
        double_check = input(
            "This action will erase the already existing file, are you sure ? y/n : "
        )
        if double_check == "y":
            add_file(src_file, dest_folder / src_file.name, overwrite=True)
        else:
            print("File ignored")

    elif user_input == "2":
        index = 1
        while True:
            new_name = f"{src_file.stem}[{index}]{src_file.suffix}"
            new_path = dest_folder / new_name
            if not new_path.exists():
                add_file(src_file, new_path)
                break
            else:
                index += 1

    else:
        print("File ignored")


def organize_files():

    directory = choose_folder()

    for p in directory.iterdir():

        # Ignore folders, files without an extension, hidden files (linux)
        if p.suffix == "" or p.is_dir() or p.name.startswith("."):
            continue

        # Create folder based on the extention
        new_directory = directory / p.suffix[1:].lower()
        # No error message if the folder already exists
        new_directory.mkdir(exist_ok=True)

        # Move the file in the folder with the same extension
        if not add_file(p, new_directory / p.name):
            duplicate(p, new_directory)


if __name__ == "__main__":

    organize_files()
