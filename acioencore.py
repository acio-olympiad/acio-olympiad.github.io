SCORES = '''iiliffe 100 100 100 100 100 100
theepiccowoflife 100 100 100 100 100 56
arthur 100 100 100 100 0 17
angus 100 100 0 60 100 0
jakingy 100 100 100 0 0 0
jerry 100 100 0 100 0 0
ryno 100 100 20 0 0 56
jbroeksteeg 100 100 0 0 0 0
netanya 100 13.37 0 0 0 0
blaizong 0 100 0 0 0 0
dylanp 0 69.69 0 0 0 0'''

for l in SCORES.split("\n"):
    name, *points = l.split()
    contents = ["<th>%s</th>" % name]
    tot = 0
    for pt in points:
        pti = float(pt)
        tot += pti
        contents.append("<td>%s</td>" % pt)
    if int(tot) == tot:
        contents.append("<td>%d</td>" % tot)
    else:
        contents.append("<td>%f</td>" % tot)
    
    print("<tr>" + "".join(contents) + "<tr>")
