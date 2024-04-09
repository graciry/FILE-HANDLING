def main():
    try:
        # File Creation
        with open("my_file.txt", "w") as file:
            file.write("Line 1: Hello, world!\n")
            file.write("Line 2: 12345\n")
            file.write("Line 3: Python file handling")

        # File Reading and Display
        print("Contents of my_file.txt:")
        with open("my_file.txt", "r") as file:
            for line in file:
                print(line.strip())

        # File Appending
        with open("my_file.txt", "a") as file:
            file.write("\nLine 4: Appended line 1\n")
            file.write("Line 5: Appended line 2\n")
            file.write("Line 6: Appended line 3\n")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File handling process completed.")


if __name__ == "__main__":
    main()
