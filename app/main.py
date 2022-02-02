file_name = input("Please enter the name of the file: ")
file_content = ""

while True:
    new_line = input("Waiting for input: ")
    if new_line == "stop":
        break
    else:
        file_content += new_line + "\n"

with open(file_name, "w") as f:
    f.writelines(file_content)
