def hello():
    return "Hello from function!"


def hello_any(greeting, name="You"):
    return f"{greeting}, {name}!"


print(hello_any("Hello"))


def is_number(user_input):
    if user_input.isdigit():
        return True
    return False


def integerator(strint):
    return int(strint)


def is_sum_bigger_than_100(x, y):
    result = integerator(x) + integerator(y)
    if result >= 100:
        return result
    return f"{result} < 100!!!"
#
#
# number_1 = input("enter first number: ")
# number_2 = input("enter second number: ")
#
# if is_number(number_1) and is_number(number_2):
#     print(is_sum_bigger_than_100(number_1, number_2))


def function_test(name, last_name, greeting="Hello", bye="Bye Bye!"):
    return f"""
            {greeting}, {name} {last_name}!
            {bye}, {name}"""


print(function_test(bye="Alloha", last_name="Marley", name="Bob", greeting="Salut"))


def all_elements_sum(*args):
    print(args)
    return sum(args)


print(all_elements_sum(2, 3, 10, 9, 3, 10, 3, 10, 100, 123))


def student_info(*args, **kwargs):  # arguments, keyword arguments
    courses = args
    print(args)
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    for course in courses:
        print(course)

student_info("math", "art", "it", name="Clint", age=21, sex="m")

# cources = ["math", "art", "it"]
# info = {"name": "Clint","age": 21,"sex": "m"}

student_info("math", "art", "it", name="Clint", age=21, sex="m")
student_info(*["math", "art", "it"], **{"name": "Clint", "age": 21, "sex": "m"})
