a =[]
with open("output2.txt", "rt") as fin:
    with open("output3.txt", "wt") as fout:
        for line in fin:
            a.append(line)
        b = set(a)
        b = sorted(b)
        for line in b:
            fout.write(line)