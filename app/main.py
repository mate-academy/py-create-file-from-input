def main():
    # write your code here
    file_name = input("Enter name of the file:") + ".txt"
    with open(file_name, "a") as file:
        inline = input("Enter new line of content: ") + "\n"
        while inline != "stop\n":
            file.write(inline)
            inline = input("Enter new line of content: ") + "\n"




if __name__ == "__main__":
    main()
