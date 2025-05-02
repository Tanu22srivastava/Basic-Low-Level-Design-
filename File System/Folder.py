from Entity import Entity
from File import File
class Folder(Entity):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.chldren=[]

    def add_enitity(self,entity):
        entity.parent = self
        self.chldren.append(entity)
    
    def delete_entity(self,name):
        for i, entity in enumerate(self.chldren):
            if entity.name== name:
                del self.chldren[i]
                print(f"{name} is deleted successfully")
                return
            
        print(f"{name} file not found")

    def list_entity(self):
        for child in self.chldren:
            print(child)
    
    def move(self,name,dest_folder):
        for i, entity in enumerate( self.chldren):
            if entity.name== name:
                dest_folder.chldren.append(entity)
                del self.chldren[i]
                print(f"{name} file moved to {dest_folder}")
                return
        print(f"{name} not found!")

    def search(self,name):
        result=[]
        for entity in self.chldren:
            if entity.name==name:
                result.append(entity.get_path())
            elif isinstance(entity,Folder):
                result+=entity.search(name)
        return result

def main():
    root = Folder("root")
    docs = Folder("Documents")
    pics = Folder("Pictures")
    root.add_enitity(docs)
    root.add_enitity(pics)
    file1 = File("resume.pdf", "This is my resume")
    file2 = File("cover_letter.docx", "Dear Sir/Madam...")
    docs.add_enitity(file1)
    docs.add_enitity(file2)
    img1 = File("vacation.png", "binarydata...")
    pics.add_enitity(img1)
    print("\n Initial structure:")
    print("Root contents:")
    root.list_entity()
    print("Documents contents:")
    docs.list_entity()
    print("\n Moving resume.pdf from Documents to Pictures...")
    docs.move("resume.pdf", pics)
    print("\n After moving resume.pdf:")
    print("Documents contents:")
    docs.list_entity()
    print("Pictures contents:")
    pics.list_entity()
    print("\n Deleting cover_letter.docx from Documents...")
    docs.delete_entity("cover_letter.docx")
    print("Documents contents:")
    docs.list_entity()
    print("\n Searching for 'vacation.png' from root...")
    search_results = root.search("vacation.png")
    for path in search_results:
        print(f"Found at: {path}")
    print("\n Searching for 'nonexistent.txt'...")
    search_results = root.search("nonexistent.txt")
    if not search_results:
        print("No results found.")

if __name__ == "__main__":
    main()
