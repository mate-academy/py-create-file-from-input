<<<<<<< HEAD
def main() -> None:
    file_name = ""
    while not file_name:
        file_name = input("Enter name of the file: ").strip()

    if not file_name.lower().endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
=======
from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
>>>>>>> dd79131eca609e1ad65f2401148ca7e840e02c29

        with open(filename, "w") as f:
            f.write(content)

        print(f"{content} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
