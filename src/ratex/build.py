# // Class Imports
from .text import Text, Equation
from .list import List, LineList
from .adjust import Adjust
from .header import Header
from .errors import Errors
from .table import Table
from .space import Space
from .flex import Flex

# // Python Imports
import os, subprocess

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
    
    # // Returns a raw image string
    def image(
        self, path: str, scale: int
    ) -> str:
        if len(path) < 1:
            return Errors.warning("No image path was provided.")

        if not os.path.exists(f"{self.__file__}/{path}"):
            return Errors.critical("Image path does not exist!")
        return f"\includegraphics[scale={scale}]{{{self.__file__}/{path}}}"
    
    # // Update the data string
    def add(self, data: str):
        self.data += str(data)
        
    # // Create a new table element in the pdf
    def table(
        self, columns: int, headers: list[str], data: list[any]
    ) -> str:
        return str(Table(columns=columns, headers=headers, data=data))
    
    # // Create a new text element in the pdf
    def text(
        self, content: str, b: bool = False, it: bool = False
    ) -> str:
        return str(Text(content=content, b=b, it=it))
    
    # // Create a new adjust (adjustwidth) element in the pdf
    def adjust(
        self, width: int, items: list[any]
    ) -> str:
        return str(Adjust(width=width, items=items))
    
    # // Create a new header (/section) element in the pdf
    def header(
        self, content: str, enumerate: bool = False
    ) -> str:
        return str(Header(content=content, enumerate=enumerate))
    
    # // Create a new list element
    def list(
        self, type: str = "itemize", items: list[any] = []
    ) -> str:
        return str(List(type=type, items=items))
    
    # // Line list. List created by newlines in a string.
    def linelist(
        self, type: str = "itemize", content: str = ""
    ) -> str:
        return str(LineList(type=type, content=content))
    
    # // Create a new flex element
    def flex(
        self, width: int = 0.33, items = []
    ) -> str:
        return str(Flex(width=width, items=items))
    
    # // Create a new vertical space element
    def vspace(
        self, size: int = 1
    ) -> str:
        return str(Space(type="v", size=size))
        
    # // Create a new horizontal space element
    def hspace(
        self, size: int = 1
    ) -> str:
        return str(Space(type="h", size=size))
    
    # // Add a new line
    def newline(
        self, amount: int = 1
    ) -> str:
        return "".join("\\newline" for _ in range(amount))
    
    # // Add a new equation
    def eq(
        self, content: str, enumerate: bool = False
    ) -> str:
        return str(Equation(content=content, enumerate=enumerate))
        
    # // Create a new table element in the pdf
    def add_table(
        self, columns: int, headers: list[str], data: list[any]
    ) -> None:
        self.add(Table(columns=columns, headers=headers, data=data))
    
    # // Create a new text element in the pdf
    def add_text(
        self, content: str, b: bool = False, it: bool = False
    ) -> None:
        self.add(Text(content=content, b=b, it=it))
    
    # // Create a new adjust (adjustwidth) element in the pdf
    def add_adjust(
        self, width: int, items: list[any]
    ) -> None:
        self.add(Adjust(width=width, items=items))
    
    # // Create a new header (/section) element in the pdf
    def add_header(
        self, content: str, enumerate: bool = False
    ) -> None:
        self.add(Header(content=content, enumerate=enumerate))
    
    # // Create a new list element
    def add_list(
        self, type: str = "itemize", items: list[any] = []
    ) -> None:
        self.add(List(type=type, items=items))
    
    # // Line list. List created by newlines in a string.
    def add_linelist(
        self, type: str = "itemize", content: str = ""
    ) -> None:
        self.add(LineList(type=type, content=content))
    
    # // Create a new flex element
    def add_flex(
        self, width: int = 0.33, items = []
    ) -> None:
        self.add(Flex(width=width, items=items))
    
    # // Create a new vertical space element
    def add_vspace(
        self, size: int = 1
    ) -> None:
        self.add(Space(type="v", size=size))
        
    # // Create a new horizontal space element
    def add_hspace(
        self, size: int = 1
    ) -> None:
        self.add(Space(type="h", size=size))
    
    # // Add a new line
    def add_newline(
        self, amount: int = 1
    ) -> None:
        for _ in range(amount):
            self.add("\\newline")
    
    # // Add a new equation
    def add_eq(
        self, content: str, enumerate: bool = False
    ) -> None:
        self.add(Equation(content=content, enumerate=enumerate))

    # // Add a new image
    def add_image(
        self, path: str, scale: int
    ) -> None:
        if len(path) < 1:
            return Errors.warning("No image path was provided.")

        if not os.path.exists(f"{self.__file__}/{path}"):
            return Errors.critical("Image path does not exist!")
        self.add(f"\includegraphics[scale={scale}]{{{self.__file__}/{path}}}")

