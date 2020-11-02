import os
from manager import DEManager

# root : 'pkexec' command to prompt for password

DE_INSTALL_PATH = "DE/Install"


if __name__ == "__main__":
    PATH = os.path.dirname(__file__)
    manager = DEManager.from_directory(os.path.join(PATH, DE_INSTALL_PATH))
    print(*manager, sep="\n")