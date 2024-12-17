def main():
    name = input("Enter name of the file:")
    my_file = open(name, "a")
    while True:
        content = my_file.write(input('Enter new line of content:'))
        if content == "stop" or content == "Stop":
            break



if __name__ == "__main__":
    main()
