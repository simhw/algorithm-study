# 요세푸스 문제
# https://www.acmicpc.net/problem/1158

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        # 첫 번째 노드는 자기 자신을 참조
        node.next = self.head

    def append(self, value):
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        node = Node(value)
        cur.next = node
        node.next = self.head


def josephus_problem(n, k):
    answer = []
    linked_list = LinkedList(1)

    for i in range(2, n + 1):
        linked_list.append(i)

    i = 1
    cur = linked_list.head

    # k가 1인 경우 예외 처리
    if k == 1:
        while cur.next != linked_list.head:
            answer.append(str(cur.data))
            cur = cur.next
        answer.append(str(cur.data))
        return "<" + ", ".join(answer) + ">"

    # k 번째 노드 마다 삭제
    while cur != cur.next:
        i += 1
        if i == k:
            i = 1
            answer.append(str(cur.next.data))
            cur.next = cur.next.next
        cur = cur.next
    # 마지막 노드 값 저장
    answer.append(str(cur.next.data))
    return "<" + ", ".join(answer) + ">"


# <3, 6, 2, 7, 5, 1, 4>
n, k = map(int, input().split())
print(josephus_problem(n, k))
