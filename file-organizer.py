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


def duplicate(src_file, dest_folder):
    user_input = input(
        "Another file has the same name\n1 to overwrite; 2 to rename; any other key to ignore : "
    )

    if user_input == "1":
        double_check = input(
            "This action will erase the already existing file, are you sure ? y/n : "
        )
        if double_check == "y":
            shutil.move(src_file, dest_folder / src_file.name)
        else:
            print("File ignored")

    elif user_input == "2":
        index = 1
        while True:
            new_name = f"{src_file.stem}[{index}]{src_file.suffix}"
            new_path = dest_folder / new_name
            if not new_path.exists():
                shutil.move(src_file, new_path)
                break
            else:
                index += 1

    else:
        print("File ignored")
        pass


def build_folders():

    directory = choose_folder()

    for p in directory.iterdir():

        # Ignore folders and files without an extension
        if p.suffix == "" or p.is_dir():
            continue

        # Create folder based on the extention
        new_directory = directory / p.suffix[1:]
        # No error message if the folder already exists
        new_directory.mkdir(exist_ok=True)

        # Move the file in the folder with the same extension
        if not (new_directory / p.name).exists():
            shutil.move(p, new_directory / p.name)
        else:
            duplicate(p, new_directory)


if __name__ == "__main__":

    build_folders()
