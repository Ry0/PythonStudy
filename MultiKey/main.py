from contextlib import contextmanager
import time
import random
import datetime


@contextmanager
def timer(name):
    t0 = int(time.time() * 1000)
    print(f'[{name}] start')
    yield
    t1 = int(time.time() * 1000)
    t = (t1 - t0)
    print(f'[{name}] done in {t} ms')


class sststorage():
    def __init__(self):
        self.storage_dict = {}

    def addDict(self, key1: tuple, key2: tuple, value: float):
        if key1 not in self.storage_dict:
            temp = {}
            temp[key2] = value
            self.storage_dict[key1] = temp
        else:
            if key2 not in self.storage_dict[key1]:
                self.storage_dict[key1][key2] = value

    def getValue(self, key1: tuple, key2: tuple):
        if key1 in self.storage_dict:
            if key2 in self.storage_dict[key1]:
                return self.storage_dict[key1][key2]
            else:
                return None
        else:
            return None


def main():
    dt_now = datetime.datetime.now()
    print(dt_now.strftime('%Y-%m-%d_%H.%M.%S'))

    storage = sststorage()
    # sample_dict[(89, 3, 40)] = 6
    for i in range(100000):
        a = random.randint(0, 5)
        b = random.randint(0, 5)
        c = random.randint(0, 5)
        tuple_tmp1 = (a, b, c)

        d = random.randint(0, 5)
        e = random.randint(0, 5)
        f = random.randint(0, 5)
        tuple_tmp2 = (d, e, f)
        storage.addDict(tuple_tmp1, tuple_tmp2, i)

    with timer("serch dict"):
        key_test1 = (0, 2, 4)
        key_test2 = (2, 2, 4)
        d = storage.getValue(key_test1, key_test2)
    print(d)


if __name__ == "__main__":
    main()
