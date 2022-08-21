from typing import Literal
from .encoder import EnvEncoder
from .env_args import EnvArg
from .decoder import EnvDecoder
import os


class EnvManager:
    def __init__(self, path: str = ..., mode: Literal["w", "r"] = "r"):
        found = False
        if path == ...:
            if ".pyenv" in os.listdir():
                found = True
                self.__filename = ".pyenv"
                self.__mode: Literal["w",
                                     "r"] = mode
                self.__file = None
        else:
            if ".pyenv" in os.listdir(path):
                found = True
                self.__filename = path + ".pyenv"
                self.__mode: Literal["w",
                                         "r"] = mode
                self.__file = None

        if found: pass
        else:
            raise FileNotFoundError("File '.pyenv' was not found")

    def write(self, data: dict[str, EnvArg]):
        if self.__file:
            if self.__mode == "w":
                self.__file.write(EnvEncoder(data).encode())
            else:
                raise NotImplementedError(
                    "Undefined method 'write' with mode 'r'")
        else:
            raise Exception("File was not opened")

    def load(self):
        if self.__file:
            if self.__mode == "r":
                return EnvDecoder(self.__file.read()).decode()
            else:
                raise NotImplementedError(
                    "Undefined method 'load' with mode 'w'")
        else:
            raise Exception("File was not opened")

    def __enter__(self):
        if self.__file:
            pass
        else:
            self.__file = open(self.__filename, self.__mode)
        return self

    def __exit__(self, *args):
        if self.__file:
            if not self.__file.closed:
                self.__file.close()


def load_pyenv(path: str = ...):
    "Load the `.pyenv` file"
    with EnvManager(path) as env:
        env_data = env.load()
    return env_data
