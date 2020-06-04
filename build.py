import os

template_file = ""
with open("./template.html") as t:
    template_file = t.read()
with open("./style.css") as s:
    template_file = template_file.replace("<link rel=\"stylesheet\" href=\"style.css\"/>", "<style>" + s.read() + "</style>");

print("Length of template:", len(template_file))

for dirpath, dirnames, filenames in os.walk("./build/"):
    for fn in filenames:
        with open(os.path.join(dirpath, fn)) as f:
            title, *remainder = f.read().split("\n")
            content = "\n".join(remainder)
            newdir = dirpath.replace("/build", "")
            os.makedirs(newdir, exist_ok=True)
            with open(os.path.join(newdir, fn), "w") as o:
                o.write(template_file.replace("Template Page", title).replace("<p> This text should have been replaced in the template. Yes this is a bad way to webdev, but at least it is easy and it works </p>", content))
            print("Successfully built", os.path.join(newdir, fn))

