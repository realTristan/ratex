# RaTeX ![Stars](https://img.shields.io/github/stars/realTristan/ratex?color=brightgreen) ![Watchers](https://img.shields.io/github/watchers/realTristan/ratex?label=Watchers)
![LaTeX_logo svg](https://user-images.githubusercontent.com/75189508/205514342-de019b59-ae1e-44a0-952e-02e289abf584.png)

# Install
If you don't have LaTeX installed, go to https://www.overleaf.com/ and copy + paste the "/build/main.tex" file code into the editor!
```py
pip install ratex
```

# Math Snippets
If using vscode, create a folder named .vscode in your project directory then copy the **math.code-snippets** file into it.

Math snippets by https://github.com/thomanq/math-snippets


# Preview
### Code

```py
from ratex import Build, Text, Packages

# // New Ratex build
r: Build = Build("main.tex", __file__)
r.new(
    doc_class = "article", 
    title = "RaTeX Physics Lab", 
    author = "Tristan Simpson",
    packages = [
        "{multirow}",
        "{cancel}", # custom packages or
        Packages.changepage, # use the ones provided
    ]
)

# // Observations
r.add_header("Observations", enumerate = False)
r.add_text(b=False, it=False, content=r"""
    Using the two provided objects we could calculate net force of the 
    bounceback from a mass and a string. By 30kg the string broke after the mass was dropped. 
    The table below describes our group observations.\newline\newline
""")
r.add_table(columns = 3, headers = ["Mass ($kg$)", "Height ($m$)", "Force (N)"], data = [
    "10kg", "11.4m", "108.73N",
    "20kg", "16.7m", "276.52N",
])

# // Procedure
r.add_header("Procedure", enumerate = False)
r.add_list(type = "enumerate", items = [
    r.text(r"The string was attached to the table."),
    r.text(r"The mass was attached to the opposite end of the string."),
    r.text(r"The mass was dropped and the bounceback height was measured."),
    r.text(r"The net force was calculated.")
])

# // Finalize the build
r.done()
```

### Output

![ratex2](https://user-images.githubusercontent.com/75189508/205525983-dcfbc5a0-1aa8-4180-8706-cdb778c22e63.png)

# License
MIT License

Copyright (c) 2022 Simpson Computer Technologies Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
