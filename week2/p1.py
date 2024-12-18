# 링크드 리스트 구현 - 2

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

    # 링크드 리스트 모든 원소 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
        print()

    # 링크드 리스트 원소 찾기
    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    # 링크드 리스트 원소 추가
    def add_node(self, index, value):
        cur = Node(value)

        # 0인 경우 예외 처리
        if index == 0:
            cur.next = self.head
            self.head = cur
            return cur

        # 이전 노드의 다음 값은 새로운 노드
        pre_node = self.get_node(index - 1)
        next_node = pre_node.next

        pre_node.next = cur
        # 이전 노드의 기존 다음 노드는 새로운 노드의 다음 노드
        cur.next = next_node
        return cur

    # 링크드 리스트 원소 삭제
    def delete_node(self, index):
        cur = self.head

        # 0인 경우 예외 처리
        if index == 0:
            self.head = cur.next
            return

        pre_node = self.get_node(index - 1)
        next_node = pre_node.next
        pre_node.next = next_node.next
        return


linked_list = LinkedList(5)
linked_list.append(12)
node = linked_list.get_node(1)

linked_list.add_node(0, 3)
linked_list.print_all()

linked_list.delete_node(0)
linked_list.print_all()
