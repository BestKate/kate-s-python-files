class Hashmap:
    size = None
    table = []


def create_ht(size: int) -> Hashmap:
    ht = Hashmap()
    ht.size = size
    ht.table = [None] * size
    return ht


def delete(ht: Hashmap):
    ht.size = None
    ht.table = [None]
    return ht


def jenkins_hash(key: str) -> int:
    """ jenkins hash-function! """
    h = 0
    for sym in key:
        h = (h + ord(sym)) & 0xFFFFFFFF
        h = (h + (h << 10)) & 0xFFFFFFFF
        h = (h ^ (h >> 6))
    h = (h + (h << 3)) & 0xFFFFFFFF
    h = (h ^ (h >> 11))
    h = (h + (h << 15)) & 0xFFFFFFFF
    return h


def insert(ht: Hashmap, key: str, value: str):
    idx = jenkins_hash(key) % ht.size
    length = ht.size
    try:
        for k in range(length):
            if ht.table[idx + k] is not None:
                continue
            else:
                ht.table[idx + k] = key, value
                break
    except:
        ht.size = ht.size * 2
        ht.table += [None] * ht.size
        insert(ht, key, value)


def resize(ht: Hashmap) -> Hashmap:
    new_ht = create_ht(ht.size * 2)
    length = ht.size
    for i in range(length):
        if ht.table[i] is not None:
            key, value = ht.table[i]
            insert(new_ht, key, value)
    ht = new_ht
    return ht


def find(ht: Hashmap, key: str):
    idx = jenkins_hash(key) % ht.size
    length = ht.size
    try:
        for i in range(length):
            if ht.table[idx + i] is not None:
                if key == ht.table[idx + i][0]:
                    return ht.table[idx + i]
    except:
        raise ValueError()


def find_idx(ht: Hashmap, key: str):
    idx = jenkins_hash(key) % ht.size
    length = ht.size
    try:
        for i in range(length):
            if ht.table[idx + i] is not None:
                if key == ht.table[idx + i][0]:
                    return idx + i
    except:
        raise ValueError()


def delete_idx(ht: Hashmap, key: str):
    idx = find_idx(ht, key)
    ht.table[idx] = None
    return ht


def foreach(ht: Hashmap, func):
    for i in range(ht.size):
        if ht.table[i] is not None:
            key, value = ht.table[i]
            ht.table[i] = func(key, value)


def function(key, value):
    value = int(value) / 2
    return key, str(value)


def tests():
    test_ht = create_ht(5)
    for i in range(5):
        insert(test_ht, str(i), str(i + 1))
    print(test_ht.table)
    assert find(test_ht, '3') == ('3', '4')
    assert find(test_ht, '4') == ('4', '5')

    delete(test_ht)
    print(test_ht.table)

    test_ht = create_ht(5)
    for i in range(7):
        insert(test_ht, str(i), str(i + 1))
    print(test_ht.table)
    delete_idx(test_ht, '4')
    assert find(test_ht, '4') is None
    print(test_ht.table)

    print(test_ht.size)
    foreach(test_ht, function)
    print(test_ht.table)
    assert (find(test_ht, '6')) == ('6', '3.5')


def main():
    tests()


if __name__ == "__main__":
    main()
