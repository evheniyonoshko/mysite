
def func1(n1, n2, n3):
    result = [x for x in range(n1, n2+1) if x % n3 == 0]
    count_result = len(result)
    return "{}, because {} are divisible by {}".format(count_result, result, n3)

print(func1(1, 10, 2))
print(func1(5, 20, 3))
print(func1(3, 56, 9))


def func2(sentense):
    result = sentense
    letters = [x for x in sentense if x.isalpha()]
    digits = [int(x) for x in sentense if x.isdigit()]
    return "{}\nLetters - {}\nDigits - {}".format(sentense, len(letters), len(digits))


print(func2(sentense="Hello world! 123!"))
print(func2(sentense="adqwdd11dcae23"))
print(func2(sentense="abracadabra11"))


def func3(data):
    sorted_by_first = sorted(data, key=lambda tup: (tup[0],))
    sorted_by_second = sorted(sorted_by_first, key=lambda tup: (tup[1], tup[2], tup[3]), reverse=True)
    return sorted_by_second

values = [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
]

print(func3(values))
