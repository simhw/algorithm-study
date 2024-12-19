# 두 링크드 리스트의 합 계산
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 링크드 리스트 모든 원소 이어붙이기
    def join_all(self):
        sum = ""
        cur = self.head
        while cur is not None:
            sum += str(cur.data)
            cur = cur.next
        return int(sum)

    # 자릿수에 맞게 링크드 리스트 원소 더하기
    def get_single_linked_list_sum(self):
        sum = 0
        cur = self.head
        while cur is not None:
            sum = sum * 10 + cur.data
            cur = cur.next
        return sum


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum1 = linked_list_1.get_single_linked_list_sum()
    sum2 = linked_list_2.get_single_linked_list_sum()
    return sum1 + sum2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
