def main():
    def get_name():
        global name
        """Input name and print odd characters"""
        name = input("Enter name:-")
        """Check that name is not blank"""
        while len(name) <= 0:
            print("Name is blank, enter again.")
            name = input("Enter name:-")
        return name

    def get_num():
        num = int(input("Enter number to skip:-"))
        return num

    def print_name(name, num):
        """Print odd characters in the name"""
        print(name[::num])
        """Another way of doing it"""
        for i in range(0, len(name), num):
            print(name[i], end="")

    name = get_name()
    num = get_num()
    print_name(name, num)

main()