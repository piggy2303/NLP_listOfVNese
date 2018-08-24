a = []
with open("output.txt", "rt") as fin:
    with open("output2.txt", "wt") as fout:
        for line in fin:
            a.append(line)
        a = sorted(a)
        for line in a:
            fout.write(line)
