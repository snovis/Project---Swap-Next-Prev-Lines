# Python Script to find Next Card and Prev Card lines in a file and switch their order.
import sys

def main():
    args = sys.argv[1:]
    # args is a list of the command line args
    # Read-in the lines from input file
    if (len(args)): 
        input_file = args[0]
        output_file = args[1]
    else:
        input_file = 'input.txt'
        output_file = 'output.txt'

    print("Input File: ", input_file)
    print("Output File: ", output_file)

    with open(input_file, 'r') as f:
        s = f.readlines()

    print(s)
    to_swap = []
    first_line = "Next Card"

    for line in s:
        if first_line in line:
            move_down_line = s.index(line)
            print(move_down_line)
            print(line)
            to_swap.append(move_down_line)

    print(to_swap)

    l = 0
    output = []
    while l < len(s):
        if l in to_swap:
            output.append(s[l+1])
            output.append(s[l])
            l += 2
        else:
            output.append(s[l])
            l += 1

    print(output)
    with open(output_file, 'w') as f:
        f.writelines(output)


if __name__ == "__main__":
    main()

