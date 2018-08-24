with open("output3.txt", "rt") as fin:
    with open("output4.txt", "wt") as fout:
        for line in fin:
            line = line.replace("_","\n")
            fout.write(line)

a = []
with open("output4.txt", "rt") as fin:
    with open("output5.txt", "wt") as fout:
        for line in fin:
            a.append(line)
            b = set(a)
        for line in b:
            fout.write(line)
