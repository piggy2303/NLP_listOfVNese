with open("input.txt", "rt") as fin:
    with open("output.txt", "wt") as fout:
        for line in fin:
            if line != "\n":
                word = line.split("\t")
                a = word[1]
                a = a.upper()

                if a.find("_") != -1:
                    
                    fout.write(a+"\n")