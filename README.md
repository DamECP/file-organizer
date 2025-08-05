
# File Organizer  

This Python script **automatically organizes files in a folder** by moving them into subfolders based on their file extensions.  
If duplicate filenames are found, the user can choose to **overwrite**, **rename**, or **ignore** the conflicting file.

---

## Features  

- Prompts the user to select a folder to organize.  
- Automatically creates subfolders for each file extension.  
  - Example: `image.jpg` will be moved to a `jpg/` folder.  
- Handles duplicate filenames interactively:  
  1. **Overwrite** the existing file.  
  2. **Rename** the new file by appending an index (`file[1].txt`).  
  3. **Ignore** the new file.  
- Ignores directories and files without extensions.  

---

## Usage  

1. **Run the script**:  
   ```bash
   python file_organizer.py
   ```

2. **Enter the folder path** when prompted.  
   Example:  
   ```
   Folder to tidy : C:\Users\John\Downloads
   ```

3. The script will create subfolders by extension and move the corresponding files.  

4. **Duplicate handling**:  
   If a file with the same name already exists in the destination folder, you’ll be prompted to:  
   - `1` → Overwrite the existing file.  
   - `2` → Rename the new file automatically.  
   - `3` → Ignore the file.  

---

## Example  

### Before:  
```
Downloads/
 ├── image.jpg
 ├── image.png
 ├── document.pdf
 ├── document (1).pdf
 └── notes.txt
```

### After:  
```
Downloads/
 ├── jpg/
 │    └── image.jpg
 ├── png/
 │    └── image.png
 ├── pdf/
 │    ├── document.pdf
 │    └── document[1].pdf
 └── txt/
      └── notes.txt
```

---

## Requirements  

- Python ≥ 3.6  
- Standard libraries:  
  - `pathlib`  
  - `shutil`  

---

## Limitations / Future Improvements

- Only processes files in the selected root directory (ignores subfolders).  
- Always requires user input to handle duplicate files (no automatic mode).  
- Does not handle special files like symbolic links or hidden files.  

---

## Author  

**DamECP** – Simple interactive file organization script.  
