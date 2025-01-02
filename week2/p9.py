# 배달의 민족 배달 가능 여부


shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    print("binary search")
    menus.sort()

    for order in orders:
        if not binary_search(menus, order):
            return False
    return True


def is_available_to_order(menus, orders):
    menus_sets = set(menus)

    for order in orders:
        # set에 대해서 in 연산은 O(1)의 시간복잡도
        if order not in menus_sets:
            return False
    return True


def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
