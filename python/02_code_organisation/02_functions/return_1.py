def triangle_area(length_of_base, height):
    area = length_of_base * height * 0.5
    return area


def triangle_area_2(length_of_base, height):
    return length_of_base * height * 0.5


result = triangle_area(10, 10)

print(result)

print(triangle_area_2(10, 10))
print(triangle_area(10, 10))
