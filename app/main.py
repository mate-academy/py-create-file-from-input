def main() -> None:
    name = input("Enter name of the file: ").strip()
    try:
        with open(f"{name}.txt", "w") as file:
            while True:
                command = input("Enter new line of content: ").strip()
                if command == "stop":
                    break
                file.write(f"{command}\n")
    except Exception as e:
        print(f"Cannot create file: {e}")


if __name__ == "__main__":
    main()
