import os

def createFile(finlename):
    try:
        with open(finlename, 'x') as f:
            print(f"File Name {finlename}: Createed sucsessfully!")
    except FileExistsError:
        print(f"File Name{finlename} already exit")
        
    except Exception as E:
        print("An Error Occured")
        
def viewFiles():
    files = os.listdir()
    if not files:
        print('No file found')
    else:
        print('Files in directories')
        for fil in files:
            print(fil)
            
def deleteFile(filename):
    try:
        os.remove(filename)
        print(f"{filename} Sucsessfully removed")
    except FileNotFoundError:
        print("File Not exist")
    except Exception as E:
        print("An errror Occured")
        
def readFile(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"content of '{filename}': \n{content}")
    except FileNotFoundError: 
        print(f"{filename} doesnot Exist")
        
    except Exception as E:
        print("An error Occured")

def editFile(filename):
    try:
        with open('output.txt', 'a') as f:
            content = input("enter the data: ")
            f.write(content +  "\n")
            print("Conetent add in the {filename} sucsessfully")  
    except FileNotFoundError: 
        print(f"{filename} doesnot Exist")
        
    except Exception as E:
        print("An error Occured")
        

def main():
    while True:
        print("File Management")
        print("1: Create file")
        print("2: view file")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")
        
        choice = input('Enter the choice(1-6) :')
        
        if choice == '1':
            filename = input('enter the file name: ')
            createFile(filename)
            
        elif choice == '2':
            viewFiles()
            
        elif choice == '3':
            filename = input('Enter the file name to delete:')
            deleteFile(filename)
            
        elif choice == '4':
            filename = input('Enter the file name to read:')
            readFile(filename)

        elif choice == '5':
            filename = input('Enter the file name to edit:')
            editFile(filename)
            
        elif choice == 6:
            print('Exit....')
            
        
        else:
            print("invelide input")
            break
if __name__ == "__main__":
    main()
            