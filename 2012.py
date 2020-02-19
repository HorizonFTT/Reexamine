def get_points(path):
    nums = []

    with open(path, 'rb') as f:
        data = f.read()

        for i in range(len(data)//4):
            beg = 4 * i
            end = beg + 4
            b = data[beg:end]
            num = int.from_bytes(b, 'little', signed=True)
            nums.append(num)

    points = list(zip(nums[::2], nums[1::2]))
    return points


def valid(point, origin=(0, 0)):
    return point[0] > origin[0] and point[1] > origin[1]


def good_point(index, points):
    origin = points[index]
    for i, p in enumerate(points):
        if i != index and not valid(p, origin):
            return False
    return True


def get_groups(points):
    sorted_points = sorted(points, key=lambda p: p[0])
    groups = []
    while sorted_points:
        group = []
        group.append(sorted_points[0])
        sorted_points.pop(0)

        for i, p in enumerate(sorted_points.copy()):
            if p[1] > group[-1][1]:
                group.append(p)
                sorted_points.pop(i - len(group) + 1)

        groups.append(group)

    return groups


if __name__ == "__main__":
    path = 'org_2012.dat'
    points = get_points(path)
    valid_points = [p for p in points if valid(p)]

    print('num of points:', len(points))
    print('num of valid points:', len(valid_points))

    min_of_x = min(valid_points, key=lambda p: p[0])[0]
    min_of_y = min(valid_points, key=lambda p: p[1])[1]
    print('min of s:', min_of_x*min_of_y)

    good_points = [p for i, p in enumerate(valid_points) if good_point(i, valid_points)]
    print('good points:', good_points)

    print('groups:', get_groups(valid_points))
