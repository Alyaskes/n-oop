import sys

from container import Container


def main():
    if len(sys.argv) != 3:
        print("Incorrect command line!\n"
              "Waited: command in_file out_file")
        sys.exit(1)

    input_file = open(sys.argv[1], "r")

    print('Start')

    cont = Container()
    print(cont)

    cont.read_from(input_file)

    print('Filled container')

    cont.sort()
    output_file = open(sys.argv[2], "w")
    cont.write_to(output_file)

    cont.clear()

    print('Empty container')
    cont.write_to(output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()