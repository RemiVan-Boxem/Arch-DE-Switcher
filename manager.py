import os
import re
from installer import Installer


__all__ = ("DEManager",)


class DEScript:
    __slots__ = ("path", "name")

    def __init__(self, path, name):
        self.path = path
        self.name = name

    def __repr__(self):
        return f"DEScript(path='{self.path}', name='{self.name}')"


class DEManager:
    """
    A DEManager instance contains all the available installation scripts, and allow you to easily install them.
    """

    __slots__ = ("_available_DE_scripts", "path")
    _filename_pattern = re.compile(r"^install\-(?P<name>(\w)+)\.sh$")

    def __init__(self, path, *DE_scripts):
        self.path = path
        self._available_DE_scripts = {DE.name: DE for DE in DE_scripts}

    @classmethod
    def from_directory(cls, dir_path: str):
        """
        Read the available DE scripts from the directory 'dir_path' and returns a new instance of 'DEManager'.
        It matches all the bash file whose name follows the following pattern :
            'install-<DE_NAME>.sh'
        """
        if not os.path.exists(dir_path):
            raise ValueError("Directory does not exist.")
        if not os.path.isdir(dir_path):
            raise ValueError("'dir_path' must be a directory.")
        DE_scripts = []
        for filename in os.listdir(dir_path):
            filename_path = os.path.join(dir_path, filename)
            search_result = cls._filename_pattern.search(filename)
            if not os.path.isfile(filename_path) or search_result is None:
                continue
            DE_scripts.append(DEScript(
                filename_path,
                search_result.group("name")
            ))
        return cls(dir_path, *DE_scripts)

    def install(self, DE_name):
        pass

    def __iter__(self):
        return iter(self._available_DE_scripts.values())