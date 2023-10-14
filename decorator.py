# flake8: noqa
import time


def duration_time(func):
    def wraper(*args):
        initial = time.time()
        func(*args)
        final = time.time()
        print(f'O tempo de duração da execução da função {func.__name__} foi de {final - initial}')

    return wraper


def counter(x):
    @duration_time
    def inner():
        for i in range(x):
            time.sleep(1)
            print(i)
    return inner


if __name__ == '__main__':
    count_3_sec = counter(3)
    count_2_sec = counter(2)
    count_7_sec = counter(7)

    count_3_sec()
    print()
    count_2_sec()
    print()
    count_7_sec()
