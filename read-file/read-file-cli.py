file = open("./read-file/inputFile.txt", "r")
passFile = open("./read-file/passFile.txt", "w")
failFile = open("./read-file/failFile.txt", "w")

for line in file:
    split_line = line.split()
    if split_line[2] == "P":
        passFile.write(f"{line}")
    elif split_line[2] == "F":
        failFile.write(f"{line}")

file.close()
passFile.close()
failFile.close()