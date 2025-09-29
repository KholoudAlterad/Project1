from pathlib import Path
from functools import wraps
import shutil


#1. Decorator
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        command = f"[LOG] {func.__name__} called with args: {args[1:]}"  # Skip 'self'

        # Log file in the same folder as the script
        log_file = Path("logs.txt")
        with log_file.open("a", encoding="utf-8") as f:
            f.write(command + "\n")

        return func(*args, **kwargs)
    return wrapper


#2. File Manager Class
class FileManager:
    def __init__(self):
        self.base_dir = Path.cwd()

    def _full_path(self, name: str) -> Path:
        return self.base_dir / name

    # Generator to lazily list directory items
    def _item_generator(self):
        for item in self.base_dir.iterdir():
            yield item

    @log_action
    def list_items(self):
        print(f"\nContents of {self.base_dir}:\n")
        for item in self._item_generator():
            kind = "[DIR]" if item.is_dir() else "[FILE]"
            print(f"{kind} {item.name}")

    @log_action
    def create_file(self, name: str):
        path = self._full_path(name)
        path.touch(exist_ok=True)
        print(f"File created: {path.name}")

    @log_action
    def create_folder(self, name: str):
        path = self._full_path(name)
        path.mkdir(exist_ok=True)
        print(f"Folder created: {path.name}")

    @log_action
    def delete(self, name: str):
        path = self._full_path(name)
        if path.is_file():
            path.unlink()
            print(f"File deleted: {path.name}")
        elif path.is_dir():
            shutil.rmtree(path)
            print(f"Folder deleted: {path.name}")
        else:
            print("Item not found.")

    @log_action
    def rename(self, old: str, new: str):
        old_path = self._full_path(old)
        new_path = self._full_path(new)
        if old_path.exists():
            old_path.rename(new_path)
            print(f"Renamed to: {new}")
        else:
            print("Item not found.")

    @log_action
    def read_file(self, name: str):
        path = self._full_path(name)
        if path.is_file():
            with path.open("r") as file:
                print(file.read())
        else:
            print("File not found.")
    
    @log_action
    def write_to_file(self, filename: str, content: str):
        path = self._full_path(filename)
        if path.is_file():
            with path.open("w") as f:
                f.write(content)
            print(f"Content written to {filename}.")
        else:
            print("File not found.")

    @log_action
    def change_directory(self, path_input: str):
        # Resolve new path relative to current base_dir
        new_path = (self.base_dir / path_input).resolve()

        if new_path.exists() and new_path.is_dir():
            self.base_dir = new_path
            print(f"Changed directory to: {self.base_dir}")
        else:
            print("❌ Folder not found or not a directory.")

    