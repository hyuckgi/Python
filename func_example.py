
input_value = raw_input("gugudan?")


def my_gugudan(num):
    for index in range(1, 10):
        print num, "x", index, " = ", num*index

my_gugudan(int(input_value))
