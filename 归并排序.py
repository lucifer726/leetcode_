def process(array):
    length = len(array)
    if length <= 1: return array
    m = length >> 1
    left = array[:m]
    right = array[m:]
    left = process(left)
    right = process(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


if __name__ == '__main__':
    print(process([33, 11, 2, 3, 7, 223423423, 4, 23, 2, 3, 4, 7]))
