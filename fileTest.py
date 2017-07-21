def testa():
    my_list = [i**2 for i in range(1,11)]
    # Generates a list of squares of the numbers 1 - 10

    f = open("output.txt", "w")

    for item in my_list:
        f.write(str(item) + "\n")

    f.close()
testa()


def testb():
    my_file = open("output.txt", "r")
    print my_file.read()
    my_file.close()
testb()


def testc():
    my_file = open("output.txt","r")
    print my_file.readline()
    print my_file.readline()
    print my_file.readline()
    my_file.close()
testc()


def testd():
    with open("text.txt", "w") as textfile:
        textfile.write("Success!")
testd()