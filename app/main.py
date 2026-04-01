def main():
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            f.write(f"{line}\n")





if __name__ == "__main__":
    main()
