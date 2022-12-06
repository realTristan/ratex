# // Class Imports
from .text import Text, Equation
from .list import List, LineList
from .adjust import Adjust
from .header import Header
from .table import Table
from .image import Image
from .space import Space
from .flex import Flex

# // Python Imports
import os, shutil, subprocess

# // Build class
class Build:
    # // Initialize the class and build folder
    def __init__(self, file_name: str, __file__: str):
        self.file_name = file_name
        self.__file__ = os.path.dirname(os.path.abspath(__file__))
        if not os.path.exists(f"{self.__file__}/build"):
            os.mkdir(f"{self.__file__}/build")

    # // Initialize the PDF Document
    def new(self, 
        doc_class = "article", packages = [""], title = "", author = "", custom = []
    ):
        # // Base Document
        self.data = (
            f"\\documentclass{{{doc_class}}}" + 
            "".join(f"\\usepackage{p}" for p in packages)
        )

        # // Top Title and Author if maketitle
        if len(title) > 0:
            self.add(f"\\title{{{title}}}\\author{{{author}}}")
        
        # // Custom args and begin document
        if len(custom) > 0:
            self.add(" ".join(l for l in custom))
        self.add("\\begin{document}")
    
        # // If title, maketitle
        if len(title) > 0:
            self.add("\\maketitle")
        open(f"{self.__file__}/build/{self.file_name}", "w").write("")
    
    # // Update the contents inside the provided .tex file
    def done(self):
        open(f"{self.__file__}/build/{self.file_name}", "w").write(self.data + "\\end{document}")
        if "compiled with zlib" in str(subprocess.check_output("pdflatex --version", shell=True)).lower():
            os.system(
                f"pdflatex -aux-directory={self.__file__}/build/ -output-directory={self.__file__}/build/ {self.__file__}/build/{self.file_name}"
            )
    
    # // Update the data string
    def add(self, data: str):
        self.data += str(data)
        
    # // Create a new table element in the pdf
    def table(self, columns: int, headers: list[str], data: list[any]):
        self.add(Table(columns=columns, headers=headers, data=data))
    
    # // Create a new text element in the pdf
    def text(self, content: str, b: bool = False, it: bool = False):
        self.add(Text(content=content, b=b, it=it))
    
    # // Create a new adjust (adjustwidth) element in the pdf
    def adjust(self, width: int, items: list[any]):
        self.add(Adjust(width=width, items=items))
    
    # // Create a new header (/section) element in the pdf
    def header(self, content: str, enumerate: bool = False):
        enum: str = {True: '', False: '*'}[enumerate]
        self.add(Header(content=content, enumerate=enum))
    
    # // Create a new list element
    def list(self, type: str = "itemize", items: list[any] = []):
        self.add(List(type=type, items=items))
    
    # // Line list. List created by newlines in a string.
    def line_list(self, type: str = "itemize", content: str = ""):
        self.add(LineList(type=type, content=content))
    
    # // Create a new flex element
    def flex(self, width: int = 0.33, items = []):
        self.add(Flex(width=width, items=items))
    
    # // Create a new vertical space element
    def vspace(self, size: int = 1):
        self.add(Space(type="v", size=size))
        
    # // Create a new horizontal space element
    def hspace(self, size: int = 1):
        self.add(Space(type="h", size=size))
    
    # // Add a new line
    def newline(self, amount: int = 1):
        for _ in range(amount):
            self.add("\\newline")
    
    # // Add a new equation
    def eq(self, content: str):
        self.add(Equation(content=content))

    # // Check image path for the image() and raw_image() functions
    def check_image_path(self, path: str):
        if not os.path.exists(f"{self.__file__}/build/images"):
            os.makedirs(f"{self.__file__}/build/images")
        shutil.copy(f"{self.__file__}/{path}", f"{self.__file__}/build/images")

    # // Add a new image
    def image(self, path: str, scale: int):
        self.check_image_path(path=path)
        self.add(f"\includegraphics[scale={scale}]{{{self.__file__}/{path}}}")

    # // Returns a raw image string
    def raw_image(self, path: str, scale: int):
        self.check_image_path(path=path)
        return f"\includegraphics[scale={scale}]{{{self.__file__}/{path}}}"

