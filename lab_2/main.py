from delimeter import Delimeter
from files_chain import FilesChain
from graphics import *

@InterpolationSpline
@InterpolationParabolic
@InterpolationLinear
@Lagranz
@Delimeter
def main():
    FILEIO = FilesChain()
    return FILEIO.client_code()


if __name__ == "__main__":
    main()