# Part 1

def nice_string(file):
    with open(file, "r") as f:
        nice = 0
        naughty = 0
        while True:
            if file == "data.txt":
                line = f.readline()
                if line != "":
                    vowels_count = line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u")
                    alphabet = list("abcdefghijklmnopqrstuvwxyz")
                    double_count = 0

                    for i in alphabet:
                        double_count += line.count(i + i)

                    forbidden_count = line.count("ab") + line.count("cd") + line.count("pq") + line.count("xy")

                    if vowels_count >= 3 and double_count >= 1 and forbidden_count == 0:
                        nice += 1
                    else:
                        naughty += 1
                else:
                    return nice, naughty
            else:
                line = f.readline()
                print(line)
                if line != "":
                    vowels_count = line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u")
                    print(f"Vowel count: {vowels_count}")
                    alphabet = list("abcdefghijklmnopqrstuvwxyz")
                    print(alphabet)
                    double_count = 0

                    for i in alphabet:
                        double_count += line.count(i + i)
                                        
                    print(f"Double count: {double_count}")

                    forbidden_count = line.count("ab") + line.count("cd") + line.count("pq") + line.count("xy")
                    print(f"Forbidden count: {forbidden_count}")

                    if vowels_count >= 3 and double_count >= 1 and forbidden_count == 0:
                        nice += 1
                        print("Veredict: Nice")
                    else:
                        naughty += 1
                        print("Veredict: Naughty")
                else:
                    return nice, naughty                

nice, naughty = nice_string("data.txt")

print(f"Number of nice strings: {nice}")
print(f"Number of naughty strings: {naughty}")

# Part 2
def new(file):
    with open(file, "r") as f:
        nice = 0
        naughty = 0
        while True:
            if file == "data.txt":
                line = f.readline().rstrip("\n")
                if line != "":
                    # print("--------------------------------------------------------------")
                    # print(line)                    
                    repeated_status = False                    
                    done = 0
                    double_count = 0
                    double_status = False
                    repeated_array = []                
                    while done < len(line):
                        if done + 3 <= len(line):                    
                            double = line.count(line[done:done + 2])
                            # print(f"Pair: {line[done:done + 2]}")
                            double_count += double
                            # print(f"Double: {double}")
                            if double >= 2:
                                double_status = True
                            repeated = line[done:done + 3]
                            repeated_array.append(repeated)
                            # print(f"Repeated: {repeated}")
                            repeated = list(repeated)
                            # print(f"Repeated (list):\n{repeated}\n")
                            

                            del repeated[1]

                            if repeated[0] == repeated[1]:
                                repeated_status = True
                                # print(f"Repeated count: {repeated_status}")

                            done += 1
                        else:
                            done += len(line)

                    # print(f"Times iterated: {done}")
                    # print(f"Line length: {len(line)}")
                    # print(f"Double count: {double_count}")
                    # if double_status == True:
                    #     print("Double status: \033[1;32;40mTrue\033[0m\n")  
                    # else:
                    #     print("Double status: \033[1;31;40mFalse\033[0m\n") 

                    # print(f"Repeated array: {repeated_array}")
                    # if repeated_status == True:
                    #     print("Repeated status: \033[1;32;40mTrue\033[0m\n")
                    # else:
                    #     print("Repeated status: \033[1;31;40mFalse\033[0m\n")

                    if double_status == True and repeated_status == True:
                        nice += 1
                        # print("Veredict: \033[1;32;40mNice\033[0m")
                    else:
                        naughty += 1
                        # print("Veredict: \033[1;31;40mNaughty\033[0m")

                    # print("--------------------------------------------------------------")
                else:
                    return nice, naughty
            else:
                line = f.readline().rstrip("\n")
                if line != "":
                    print("--------------------------------------------------------------")
                    print(line)                    
                    repeated_status = False                    
                    done = 0
                    double_count = 0
                    double_status = False
                    repeated_array = []                
                    while done < len(line):
                        if done + 3 <= len(line):                    
                            double = line.count(line[done:done + 2])
                            print(f"Pair: {line[done:done + 2]}")
                            double_count += double
                            print(f"Double: {double}")
                            if double >= 2:
                                double_status = True
                            repeated = line[done:done + 3]
                            repeated_array.append(repeated)
                            # print(f"Repeated: {repeated}")
                            repeated = list(repeated)
                            # print(f"Repeated (list):\n{repeated}\n")
                            

                            del repeated[1]

                            if repeated[0] == repeated[1]:
                                repeated_status = True
                                # print(f"Repeated count: {repeated_status}")

                            done += 1
                        else:
                            done += len(line)

                    print(f"Times iterated: {done}")
                    print(f"Line length: {len(line)}")
                    print(f"Double count: {double_count}")
                    if double_status == True:
                        print("Double status: \033[1;32;40mTrue\033[0m\n")  
                    else:
                        print("Double status: \033[1;31;40mFalse\033[0m\n") 

                    print(f"Repeated array: {repeated_array}")
                    if repeated_status == True:
                        print("Repeated status: \033[1;32;40mTrue\033[0m\n")
                    else:
                        print("Repeated status: \033[1;31;40mFalse\033[0m\n")

                    if double_status == True and repeated_status == True:
                        nice += 1
                        print("Veredict: \033[1;32;40mNice\033[0m")
                    else:
                        naughty += 1
                        print("Veredict: \033[1;31;40mNaughty\033[0m")

                    # print("--------------------------------------------------------------")
                else:
                    return nice, naughty

nice, naughty = new("data.txt")

print(f"\nNumber of new nice strings: {nice}")
print(f"Number of new naughty strings: {naughty}")