a = []
with open("output5.txt", "rt") as fin:
    with open("output6.txt", "wt") as fout:
        for line in fin:
            a.append(line)
            b = sorted(a)
        for line in b:
            fout.write(line)