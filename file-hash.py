import hashlib


def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)
        return sha256.hexdigest()


file_path = input("Enter file path: ")
try:
    file_hash = hash_file(file_path)
    print("\nSHA-256: ", file_hash)

except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("Permision denied!")
