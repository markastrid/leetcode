def test_func():
    for i in range(10):
        yield i


for i in range(10):
    print(next(test_func()))
    print(next(test_func()))
