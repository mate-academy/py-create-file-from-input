def main():
    # write your code here
    name = input("Enter name of the file: ")

    flag = True
    content_list = []
    while flag:

        content = input("Enter new line of content: ")
        content_list.append(content)
        if content == "stop":
            flag = False
            with open(f"{name}.txt", "a") as file:
                for index in range(len(content_list) - 1):
                    file.write(content_list[index] + "\n")


if __name__ == "__main__":
    main()
