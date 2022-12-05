from .adjust import Align, Adjust
from .text import Text, Equation
from .header import Header
from .table import Table
from .image import Image
from .space import Space
from .list import List
from .flex import Flex
import os, shutil

# // Build class
class Build:
    # // Initialize the class and build folder
    def __init__(self, build_file: str = "main.tex", file_dir: str = ""):
        self.build_file = build_file
        self.file_dir = ""
        
        if len(file_dir) > 0:
            self.file_dir = os.path.dirname(os.path.abspath(file_dir))
            
        if not os.path.exists(f"{self.file_dir}/build"):
            os.mkdir(f"{self.file_dir}/build")

    # // Initialize the PDF Document
    def new(self, 
            doc_class = "article", packages = [""], 
            title = "", author = "", 
            custom = []
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
        open(f"{self.file_dir}/build/{self.build_file}", "w").write("")
    
    # // Update the contents inside the provided .tex file
    def done(self):
        open(f"{self.file_dir}/build/{self.build_file}", "w").write(self.data + "\\end{document}")
    
    # // Update the data string
    def add(self, data: str):
        self.data += str(data)
        
    # // Create a new table element in the pdf
    def table(self, columns: int, headers: list[str], data: list[any]):
        self.add(Table(columns=columns, headers=headers, data=data))
    
    # // Create a new text element in the pdf
    def text(self, content: str = "", bold: bool = False, italic: bool = False):
        self.add(Text(content=content, bold=bold, italic=italic))
    
    # // Create a new adjust (adjustwidth) element in the pdf
    def adjust(self, width: int = 0, margin: int = 0, items: list[any] = []):
        self.add(Adjust(width=width, margin=margin, items=items))
    
    # // Create a new header (/section) element in the pdf
    def header(self, content: str, enumerate: bool = False):
        enum: str = {True: '', False: '*'}[enumerate]
        self.add(Header(content=content, enumerate=enum))
    
    # // Create a new list element
    def list(self, type: str = "itemize", items: list[any] = []):
        self.add(List(type=type, items=items))
    
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
    def newline(self):
        self.add("\\newline")
    
    # // Add a new equation
    def eq(self, content: str):
        self.add(Equation(content=content))
    
    # // Add a new image
    def image(self, path: str, scale: int):
        path_split: list[str] = path.split("/")
        file_name: str = "".join(f"\\{a}" for a in path_split[1:len(path_split) - 1])
        if not os.path.exists(f"{self.file_dir}/build/{file_name}"):
            os.mkdir(f"{self.file_dir}/build/{file_name}")
        shutil.copy(path, f"{self.file_dir}/build/{file_name}")
        self.add(Image(path=path, scale=scale))

