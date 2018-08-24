with open("input.txt", "rt") as fin:
    with open("output2.txt", "wt") as fout:
        for line in fin:
            line1 = line.split("</i>")
            line2 = line1[0].split(">")
            fout.write(line2[1]+"\n")