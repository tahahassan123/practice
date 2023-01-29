import math
#part 1
def largest(num1, num2, num3):
    return max(num1, num2, num3)
def test_largest():
    if largest(1, 2, 3) == 3:
        print("First test passed")
    else:
        print("First test failed")
    if largest(-5, 0, 5) == 5:
        print("Second test passed")
    else:
        print("Second test failed")
    if largest(3.14, 2.7, 1.6) == 3.14:
        print("Third test passed")
    else:
        print("Third test failed")
    if largest(0, 0, 0) == 0:
        print("Fourth test passed")
    else:
        print("Fourth test failed")
    if largest(-5, -10, -15) == -5:
        print("Fifth test passed")
    else:
        print("Fifth test failed")
#part 2
def least(a, b):
    if a <= 0 and b <= 0:
        raise ValueError("Must be positive")
    return abs(a*b) // math.gcd(a, b)
def test_least():
    if least(2, 3) == 6:
        print("First test passed")
    else:
        print("First test failed")
    if least(4, 2) == 12:
        print("Second test passed")
    else:
        print("Second test failed")
    if least(5, 1) == 35:
        print("Third test passed")
    else:
        print("Third test failed")
    try:
        least(0, 3)
    except ValueError:
        print("Fourth test passed")
    else:
        print("Fourth test failed")
    try:
        least(-3, 3)
    except ValueError:
        print("Fifth test passed")
    else:
        print("Fifth test failed")
#part 3
def root(num):
    return math.sqrt(num)
def test_root():
    if abs(root(4) - 2) < 0.0001:
        print("First test passed")
    else:
        print("First test failed")
    if abs(root(9) - 3) < 0.0001:
        print("Second test passed")
    else:
        print("Second test failed")
    if abs(root(16) - 4) < 0.0001:
        print("Third test passed")
    else:
        print("Third test failed")
    if abs(root(2) - 1.41421) < 0.0001:
        print("Fourth test passed")
    else:
        print("Fourth test failed")
    if abs(root(0.25) - 0.5) < 0.0001:
        print("Fifth test passed")
    else:
        print("Fifth test failed")
#part 4
def sort(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers
def test_sort():
    if sort(3, 1, 2) == [1, 2, 3]:
        print("First test passed")
    else:
        print("First test failed")
    if sort(0, -5, 2) == [-5, 0, 2]:
        print("Second test passed")
    else:
        print("Second test failed")
    if sort(100, -100, 0) == [-100, 0, 100]:
        print("Third test passed")
    else:
        print("Third test failed")
#part 5
def arraysort(A, n):
    A.sort()
    return A
def test_arraysort():
    if arraysort([3, 1, 2], 3) == [1, 2, 3]:
        print("First test passed")
    else:
        print("First test failed")
    if arraysort([0, -5, 2], 3) == [-5, 0, 2]:
        print("Second test passed")
    else:
        print("Second test failed")
    if arraysort([100, -100, 0], 3) == [-100, 0, 100]:
        print("Third test passed")
    else:
        print("Third test failed")

print("Part 1:")
test_largest()
print("\nPart 2:")
test_least()
print("\nPart 3:")
test_root()
print("\nPart 4:")
test_sort()
print("\nPart 5:")
test_arraysort()

