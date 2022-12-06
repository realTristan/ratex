from src.ratex import Build, Text, Header

# // New Ratex build
r: Build = Build("main.tex", __file__)
r.new(
    doc_class = "article", 
    title = "RaTeX Physics Lab", 
    author = "Tristan Simpson",
    packages = [
        "{multirow}",
        "{cancel}",
        "{changepage}",
    ]
)

# // Observations
r.header("Observations", enumerate = False)
r.text(b=False, it=False, content=r"""
    Using the two provided object we could calculate net force of the 
    bounceback from a mass and a string. By 30kg the string broke after the mass was dropped. 
    The table below describes our group observations.\newline\newline
""")
r.table(columns = 3, headers = ["Mass ($kg$)", "Height ($m$)", "Force (N)"], data = [
    "10kg", "11.4m", "108.73N",
    "20kg", "16.7m", "276.52N",
])

# // Procedure
r.header("Procedure", enumerate = False)
r.list(type = "enumerate", items = [
    Text(r"The string was attached to the table."),
    Text(r"The mass was attached to the opposite end of the string."),
    Text(r"The mass was dropped and the bounceback height was measured."),
    Text(r"The net force was calculated.")
])

# // Finalize the build
r.done()
