import timeit

def main():
    for i in range(20000):
        i ** 2

if __name__ == "__main__":
    print(timeit.timeit(main, number=1))