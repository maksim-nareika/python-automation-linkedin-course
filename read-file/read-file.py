file = open("inputFile.txt", "r")
passFile = open("passFile.txt", "w")
failFile = open("failFile.txt", "w")

for line in file:
    split_line = line.split()
    if split_line[2] == "P":
        passFile.write(f"{line}")
    elif split_line[2] == "F":
        failFile.write(f"{line}")

file.close()
passFile.close()
failFile.close()