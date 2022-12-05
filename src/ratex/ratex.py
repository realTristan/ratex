import os, shutil, re

# // Build class
class Build:
    # // Variables for autofill
    enumerate: str = "enumerate"
    itemize: str = "itemize"
    
    # // Initialize the class and build folder
    def __init__(self, build_file: str):
        self.build_file = build_file
        if not os.path.exists("./build"):
            os.mkdir("./build")

    # // Initialize the PDF Document
    def new(self, 
            doc_class = "article", packages = [""], 
            title = "", author = "", 
            custom = []
    ):
        self.data = (
            f"\\documentclass{{{doc_class}}}" + 
            "".join(f"\\usepackage{{{p}}}" for p in packages)
        )
        if len(title) > 0:
            self.add(f"\\title{{{title}}}\\author{{{author}}}")
            
        if len(custom) > 0:
            self.add(" ".join(l for l in custom))
        self.add("\\begin{document}")
    
        if len(title) > 0:
            self.add("\\maketitle")
        open(f"./build/{self.build_file}", "w").write("")
    
    # // Update the contents inside the provided .tex file
    def done(self):
        open(f"./build/{self.build_file}", "w").write(self.data + "\\end{document}")
    
    # // Update the data string
    def add(self, data: str):
        self.data += data
        
    # // Create a new table element in the pdf
    def table(self, columns: int, headers: list[str], data: list[any]):
        self.add(Table(columns=columns, headers=headers, data=data)._init())
    
    # // Create a new text element in the pdf
    def text(self, content: str = "", bold: bool = False, italic: bool = False):
        self.add(Text(content=content, bold=bold, italic=italic)._init())
    
    # // Create a new section (adjustwidth) element in the pdf
    def section(self, size: int = 0, margin: int = 0, items: list[any] = []):
        self.add(Section(size=size, margin=margin, items=items)._init())
    
    # // Create a new header (/section) element in the pdf
    def header(self, content: str, enumerate: bool = False):
        enum: str = {True: '', False: '*'}[enumerate]
        self.add(Header(content=content, enumerate=enum)._init())
    
    # // Create a new list element
    def list(self, type: str = "itemize", items: list[any] = []):
        self.add(List(type=type, items=items)._init())
    
    # // Create a new flex element
    def flex(self, width: int = 0.33, items = []):
        self.add(Flex(width=width, items=items)._init())
    
    # // Create a new vertical space element
    def vspace(self, size: int = 1):
        self.add(Space(type="v", size=size)._init())
        
    # // Create a new horizontal space element
    def hspace(self, size: int = 1):
        self.add(Space(type="h", size=size)._init())
    
    # // Add a new line
    def newline(self):
        self.add("\\newline")
    
    # // Add a new image
    def image(self, path: str, scale: int):
        path_split: list[str] = path.split("/")
        file_name: str = "".join(f"/{a}" for a in path_split[1:len(path_split) - 1])
        if not os.path.exists(f"./build/{file_name}"):
            os.mkdir(f"./build/{file_name}")
        shutil.copy(path, f"./build/{file_name}")
        self.add(Image(path=path, scale=scale)._init())


# // Image class
class Image:
    def __init__(self, path: str, scale: int = 1) -> None:
        self.path = path
        self.scale = scale
    
    def _init(self) -> str:
        return f"\includegraphics[scale={self.scale}]{{{self.path}}}"


# // Space class
class Space:
    def __init__(self, type: str = "v", size: int = 1) -> None:
        self.type = type
        self.size = size
        
    def _init(self) -> str:
        return f"\\{self.type}space{{{self.size}cm}}"
    
# // Flex class
class Flex:
    def __init__(self, width: int = 0.33, items: list[any] = []) -> None:
        self.width = width
        self.items = items
        
    def _init(self) -> str:
        return "".join((
            f"\\begin{{minipage}}{{{self.width}\\textwidth}}" +
            i._init() +
            f"\\end{{minipage}}\\leavevmode"
        ) for i in self.items)

# // Section class
class Section:
    def __init__(self, size: int = 0, margin: int = 0, items: list[any] = []) -> None:
        self.size = size
        self.margin = margin
        self.items = items
    
    def _init(self) -> str:
        if len(self.items) > 0:
            return (
                f"\\begin{{adjustwidth}}{{{self.size}cm}}{{{self.margin}pt}}" +
                "".join(i._init() for i in self.items) +
                f"\\end{{adjustwidth}}\\leavevmode\\\\"
            )
        return ""

# // Header class
class Header:
    def __init__(self, content: str = "", enumerate: bool = False) -> None:
        self.content = content
        self.enumerate = enumerate
        
    def _init(self) -> str:
        return f"\section{self.enumerate}{{{self.content}}}"

# // List class
class List:
    def __init__(self, type: str = "itemize", items: list[any] = []) -> None:
        self.type = type
        self.items = items
        
    def _init(self) -> str:
        return (
            f"\\begin{{{self.type}}}" +
            "".join(f"\\item {{{i._init()}}}" for i in self.items) +
            f"\\end{{{self.type}}}\\leavevmode"
        )
    
# // Text class
class Text:
    def __init__(self, content: str = "", bold: bool = False, italic: bool = False) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()
        self.bold = bold
        self.italic = italic
    
    def clean_content(self, content: str) -> str:
        active = False
        content = list(content)
        for i in range(len(content)):
            if content[i] == "$":
                active = not active

            if active:
                if content[i] == " ":
                    content[i] = "$ $"
        return r"".join(c for c in content) + " "
        
    def _init(self) -> str:
        self.content = self.clean_content(self.content)
        if self.bold:
            return f"\\textbf{{{self.content}}}"
        elif self.italic:
            return f"\\textit{{{self.content}}}"
        elif self.italic and self.bold:
            return f"\\textbf{{\\textit{{{self.content}}}}}"
        return self.content
    
# // Table class
class Table:
    def __init__(self, columns: int, headers: list[str], data: list[any]) -> None:
        self.headers = headers
        self.columns = columns
        self.data = data
        
    def _init(self) -> str:
        self.data = self._split_data(self.data)
        return (
            "\\begin{tabular}{" + "".join('|c' for _ in range(self.columns)) + "|}\hline " + 
            self._headers() + 
            self._body() + 
            "\\end{tabular}\\leavevmode\\\\"
        )
        
    def _split_data(self, data: list[any]) -> list[any]:
        return [data[x:x + self.columns] for x in range(0, len(data), self.columns)]
    
    def _headers(self) -> str:
        for i in range(len(self.headers)):
            if i != len(self.headers) - 1:
                self.headers[i] = f"{self.headers[i]} & "
            else:
                self.headers[i] = f"{self.headers[i]} \\\\ \\hline "
        return "".join(h for h in self.headers)
    
    def _body(self) -> str:
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j != len(self.data[i]) - 1:
                    self.data[i][j] = f"{self.data[i][j]} & "
                else:
                    self.data[i][j] = f"{self.data[i][j]} \\\\ \\hline "
        return "".join("".join(a for a in b) for b in self.data)
