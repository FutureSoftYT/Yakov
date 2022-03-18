def get_unique(array):

    if len(array) < 1:
        return None

    new_array = []

    for index,num in enumerate(array):
        if num > 5 and not num in array[index:]:
            new_array.append(num)

    return new_array


def test_get_unique():
    result = get_unique([1, 5, 8, 8, 10])
    assert result == [10], f'Wrong answer {result}'
    result = get_unique([])
    assert result == None, f'Wrong answer {result}'

    print('Все тесты пройдены!!')


if __name__ == '__main__':
    test_get_unique()