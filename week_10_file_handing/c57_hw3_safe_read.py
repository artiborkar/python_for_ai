# safe_read jaise function banao jo ek allowed folder ke bahar ke path ko reject kare.


from pathlib import Path


def safe_read(file_path):
    allowed_folder = Path("allowed").resolve()
    file_path = Path(file_path).resolve()

    if allowed_folder not in file_path.parents:
        raise ValueError("Access denied: File is outside the allowed folder")

    with open(file_path, "r") as f:
        return f.read()


print(safe_read("allowed/data.txt"))