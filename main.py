from filemanager import *


#1. Helper
def show_help():
    print("""
Commands:
  ls                        - List all files/folders
  touch <filename>          - Create a file
  mkdir <foldername>        - Create a folder
  rm <name>                 - Delete a file or folder
  rename <old> <new>        - Rename a file or folder
  cat <filename>            - Read a file
  write <filename> <text>   - Write text into a file (overwrites it)
  cd <foldername>           - Change current working directory  
  help                      - Show this help message
  exit                      - Exit the program
""")


#2. CLI 
def main():
    fm = FileManager()
    print("-- File Manager CLI --")
    print("Type 'help' to see available commands.")

    while True:
        try:
            command = input(">> ").strip().split()

            if not command:
                continue

            cmd = command[0]
            args = command[1:]

            if cmd == "ls":
                fm.list_items()
            elif cmd == "touch" and len(args) == 1:
                fm.create_file(args[0])
            elif cmd == "mkdir" and len(args) == 1:
                fm.create_folder(args[0])
            elif cmd == "rm" and len(args) == 1:
                fm.delete(args[0])
            elif cmd == "rename" and len(args) == 2:
                fm.rename(args[0], args[1])
            elif cmd == "cat" and len(args) == 1:
                fm.read_file(args[0])
            elif cmd == "write" and len(args) >= 2:
                fm.write_to_file(args[0], " ".join(args[1:]))
            elif cmd == "cd" and len(args) == 1:
                fm.change_directory(args[0])
            elif cmd == "help":
                show_help()
            elif cmd == "exit":
                print("-- Goodbye! --")
                break
            else:
                print("❌ Invalid command. Type 'help'.")

        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()