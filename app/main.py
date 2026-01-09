def main():
    name = input("Enter name of the file: ")
    file = open(name + ".txt", "a")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            file.write(line)
    file.close()   

if __name__ == "__main__":
    main()
