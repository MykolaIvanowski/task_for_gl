import hashlib


def generate(file_path):
    md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for f in iter(lambda: file.read(4096), b""):
            md5.update(f)
    return md5.hexdigest()
