def main() -> None:
    fil = input("Enter name of the file: ")
    while fil == "":
        fil = input("Enter name of the file: ")
    with open(f"{fil}.txt", "w+") as fin:
        pass
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        with open(f"{fil}.txt", "a") as final:
            final.write(f"{content}\n")
    print(f'File name: "{fil}.txt"\n')
    with open(f"{fil}.txt", "r+") as fin:
        fin_list = fin.readlines()
    for cont in fin_list:
        print(cont, end="")


if __name__ == "__main__":
    main()
