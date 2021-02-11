import sys

SCORES = ""

with open(sys.argv[1], "r") as f:
    SCORES = f.read()

for l in SCORES.split("\n")[1:]: # First row is column labels
    name, *points = l.split(",")
    contents = ["<td>%s</td>" % name]
    for pt in points:
        contents.append("<td>%s</td>" % pt)
    
    print("<tr>" + "".join(contents) + "<tr>")
