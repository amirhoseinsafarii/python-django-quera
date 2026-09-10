import os
import sys
import time

inputs = sys.argv
source = inputs[1]
dest = inputs[2]

if not os.path.exists(dest):
    os.mkdir(dest)

for root, dirs, files in os.walk(source):
    for file in files:
        name, ext = os.path.splitext(file)
        if ext.lstrip(".").lower() in ("jpg", "jpeg", "png"):
            year = time.ctime(os.path.getmtime(os.path.join(root, file))).split()[-1]
            if not os.path.exists(os.path.join(dest, year)):
                os.mkdir(os.path.join(dest, year))
            if not os.path.exists(os.path.join(dest, year, "photos")):
                os.mkdir(os.path.join(dest, year, "photos"))
            f1 = open(os.path.join(root, file), "rb")
            binary_data = f1.read()
            f2 = open(os.path.join(dest, year, "photos", file), "wb")
            f2.write(binary_data)
            f1.close()
            f2.close()

        elif ext.lstrip(".").lower() in (
            "mp4",
            "avi",
            "3gp",
            "mpeg",
            "mkv",
            "wmv",
            "mov",
        ):
            year = time.ctime(os.path.getmtime(os.path.join(root, file))).split()[-1]
            if not os.path.exists(os.path.join(dest, year)):
                os.mkdir(os.path.join(dest, year))
            if not os.path.exists(os.path.join(dest, year, "videos")):
                os.mkdir(os.path.join(dest, year, "videos"))

            f1 = open(os.path.join(root, file), "rb")
            binary_data = f1.read()
            f2 = open(os.path.join(dest, year, "videos", file), "wb")
            f2.write(binary_data)
            f1.close()
            f2.close()
