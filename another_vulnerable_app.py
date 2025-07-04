import os

def main():
    user_input = input("Enter a filename to list (e.g., /etc): ")
    # WARNING: This is intentionally vulnerable to command injection
    os.system("ls " + user_input)

if __name__ == "__main__":
    main()
