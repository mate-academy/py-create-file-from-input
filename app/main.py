def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as writer:
        temp = [None]
        while temp[-1] != "stop":
            temp.append(input("Enter new line of content: "))
            if temp[-1] == "stop":
                break
            writer.write(temp[-1] + "\n")


if __name__ == "__main__":
    main()
