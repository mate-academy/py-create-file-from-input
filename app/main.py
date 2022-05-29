file_name = input("Enter file name you want to create:") + ".txt"
with open(file_name, "a") as file_add_info:
    while True:
        line = input("Enter file content or 'stop' to exit input:")
        if line == "stop":
            break
        file_add_info.write(f"{line}\n")
