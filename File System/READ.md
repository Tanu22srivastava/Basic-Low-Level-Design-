# File Management System

This project is a simple object-oriented file system simulator written in Python. It allows for basic file and folder operations such as create, delete, move, read, write, append, and search.

## 📁 Structure

```
.
├── Entity.py        # Base class for File and Folder
├── File.py          # File class with content and size
├── Folder.py        # Folder class that holds files/folders
└── main.py          # Example usage and test cases
```

## 🚀 Features

- Create files and folders with hierarchy
- Add entities (files or folders) to folders
- Read, write, append content to files
- Move files/folders between folders
- Delete files/folders from a folder
- Recursively search for files/folders by name
- Print full path of an entity

## 🧩 Classes

### Entity

- `name`: Name of the file or folder
- `parent`: Reference to the parent folder
- `get_path()`: Returns the full path from root

### File(Entity)

- `content`: Stores string content
- `read()`: Returns content
- `write(data)`: Overwrites content
- `append(data)`: Appends data to content
- `get_size()`: Returns length of content

### Folder(Entity)

- `children`: List of files and folders inside it
- `add_entity(entity)`: Adds a file or folder
- `delete_entity(name)`: Deletes entity by name
- `list_entity()`: Lists all children
- `move(name, dest_folder)`: Moves child to another folder
- `search(name)`: Recursively searches children by name

## 🧪 Example Usage

```python
root = Folder("root")
docs = Folder("Documents")
pics = Folder("Pictures")

root.add_entity(docs)
root.add_entity(pics)

file1 = File("resume.pdf")
file2 = File("cover_letter.docx")
docs.add_entity(file1)
docs.add_entity(file2)

img = File("vacation.png")
pics.add_entity(img)

docs.move("resume.pdf", pics)
docs.delete_entity("cover_letter.docx")

results = root.search("vacation.png")
for path in results:
    print(path)
```

## 📌 Output Sample

```
 Initial structure:
Root contents:
Documents
Pictures
Documents contents:
resume.pdf
cover_letter.docx

 Moving resume.pdf from Documents to Pictures...

 After moving resume.pdf:
Documents contents:
cover_letter.docx
Pictures contents:
vacation.png
resume.pdf

 Deleting cover_letter.docx from Documents...
Documents contents:

 Searching for 'vacation.png' from root...
Found at: /root/Pictures/vacation.png

 Searching for 'nonexistent.txt'...
No results found.
```

## 🧠 Concepts Used

- Inheritance and Polymorphism
- Recursive algorithms
- Object Composition
- Encapsulation and OOP design principles

## ✅ How to Run

```bash
python Folder.py
```

> Make sure all `.py` files are in the same directory.

