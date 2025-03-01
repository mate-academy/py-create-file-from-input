def main():
    file_name = input("Enter name of the file: ")
    cmd_list = list()
    while True:
        cmd = input("Enter new line of content: ")
        if cmd.lower().strip() == "stop":
            break
        cmd_list.append(cmd)
        
    with open(f"{file_name}.txt", "a") as fn:
        for i in cmd_list:
            fn.write(f"{i}\n")

if __name__ == "__main__":
    main()
