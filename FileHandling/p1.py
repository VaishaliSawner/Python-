from pathlib import Path 


path=Path("file-collection/abc.txt")

print(f"Name: {path.name}")
print(f"Absolute Path: {path.absolute()}")
print(f"is File: {path.is_file()}")
print(f" is Directory: {path.is_dir()}")
print(f"Size: {path.stat().st_size} bytes")