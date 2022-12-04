# RaTeX ![Stars](https://img.shields.io/github/stars/Simpson-Computer-Technologies-Research/RaTeX?color=brightgreen) ![Watchers](https://img.shields.io/github/watchers/Simpson-Computer-Technologies-Research/RaTeX?label=Watchers)
![LaTeX_logo svg](https://user-images.githubusercontent.com/75189508/205514342-de019b59-ae1e-44a0-952e-02e289abf584.png)

# Preview

<h3>Code</h3>

```py
# // Create a new build
r: Ratex = Ratex("main.tex")
r.new(
    doc_class = "article", 
    title = "RaTeX", 
    author = "Tristan Simpson",
    packages = [
        "multirow",
        "cancel",
        "changepage"
    ]
)

# // Create a new table element!
r.header("Observations", enumerate = False)
r.text(r"With such a readable command new LaTeX learners can understand what's happening!\newline\newline")
r.table(columns = 3, headers = ["Mass ($kg$)", "Height ($m$)", "Force (N)"], data = [
    "10kg", "11.4m", "108.73N",
    "20kg", "16.7m", "276.52N",
])

# // Create a new section!
r.header("Who am I?", enumerate = True)
r.section(size = 1, margin = 0, items = [
    Text(r"My name is Tristan Simpson and I'm a Systems Software Engineer! RaTeX builds fast, clean, concise LaTeX files.")
])
```

<h3>Output</h3>

![ratex2](https://user-images.githubusercontent.com/75189508/205514223-3d07cb5a-4226-43f6-b6ed-57ea95ddde2b.png)

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
