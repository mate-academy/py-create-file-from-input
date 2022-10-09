def main():

    stroka = input("Enter name of the file: ") + ".txt"
    i = 1
    f = open(stroka, "w+")
    while i == 1:
        index = input("Enter new line of content: ")
        if index == "stop":
            i = 0
        else:
            f.write(index + '\n')
    f.close()


if __name__ == "__main__":
    main()
