from container import Container


def test_clear():
    container = Container()
    for i in range(10):
        container.add(i)

    container.clear()

    assert len(container) == 0


def test_len():
    container = Container()
    for i in range(10):
        container.add(i)

    assert len(container) == 10


def test_read_from():
    container = Container()

    with open('input.txt', 'r') as file:
        container.read_from(file)

    assert len(container) != 0


def test_write_to():
    container = Container()

    with open('input.txt', 'r') as file:
        container.read_from(file)

    with open('output.txt', 'w') as file:
        container.write_to(file)

    file_obs = open("output.txt", "r")
    file_exp = open("output_test_write.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_sort():
    container = Container()

    with open('input.txt', 'r') as file:
        container.read_from(file)

    container.sort()
    with open("output_test_sort.txt", "w") as file:
        container.write_to(file)

    file_obs = open("output_sort.txt", "r")
    file_exp = open("output_test_sort.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()


def test_write_two_dim_array_to():
    container = Container()

    with open('input.txt', 'r') as file:
        container.read_from(file)

    with open("output_test_write_two_dim_array_to.txt", "w") as file:
        container.write_to(file)

    file_obs = open("output_write_two_dim_array.txt", "r")
    file_exp = open("output_test_write_two_dim_array_to.txt", "r")

    assert file_obs.read() == file_exp.read()

    file_obs.close()
    file_exp.close()
