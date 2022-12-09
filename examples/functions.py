from ratex import Build, Text

# // New Ratex build
r: Build = Build("main.tex")
r.new(
    doc_class = "article", 
    title = "RaTeX", 
    author = "Tristan Simpson",
    packages = [
        "multirow",
        "cancel",
        "changepage",
        "graphicx"
    ]
)

# // Create a new table element
r.add_header("Observations", enumerate = False)
r.add_text(r"With such a readable command new LaTeX learners can understand what's happening!\newline\newline")
r.add_table(columns = 3, headers = ["Mass ($kg$)", "Height ($m$)", "Force (N)"], data = [
    "10kg", "11.4m", "108.73N",
    "20kg", "16.7m", "276.52N",
])

# // Create a new section
r.add_header("Who am I?", enumerate = True)
r.add_section(size = 1, margin = 0, items = [
    Text(r"My name is Tristan Simpson and I'm a Systems Software Engineer! RaTeX builds fast, clean, concise LaTeX files.")
])

# // Create a new list
r.add_list(type = r.itemize, items = [
    Text(r"The first step.."),
    Text(r"is all it takes.")
])

# // Create a new flex box
r.add_flex(width = 0.5, items = [
    Text(r"This object is on the left!"),
    Text(r"This object is on the right!")
])
r.add_newline()

# // Create a new image
r.add_image(path = "./images/ratex1.png", scale = 0.33)

# // Finalize the build
r.done()



"""
To Do:

    // Align(type = "fl" or "fr" or "")

"""