import os
import random
import shutil
import string
from pathlib import Path


def create_file() -> Path:
    """
    You may need a random file which can be used to test file upload.
    The below makes a random name, copies existing file to that name,
    returns Path to that file, then deletes the temporary file when done.
    """

    random_name_suffix = "".join(random.choices(string.ascii_lowercase, k=5))
    new_name = f"./testdata/test-file-{random_name_suffix}.png"
    original_file = "./testdata/test-file.png"

    shutil.copy(original_file, new_name)
    print(f"Random file: {new_name}")

    return Path(new_name)

    os.remove(new_name)


create_file()
