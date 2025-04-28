

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)

def insert(root,value):
    new_node = TreeNode()
    new_node.data = value
    if root is None:
        return new_node

    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right
    return root





if __name__ == "__main__":
    numbers = [10,15,8,3,9]
    root = None

    for number in numbers[1:]:
        root = insert(root,number)

print("BST 구성 완료")
post_order(root)
# find_number = int(input())
#
# while True:
#     if find_number == current.data:
#         print(f"{find_number}를(을) 찾았습니다.")
#         break
#     elif find_number < current.data:
#         if current.left is None:
#             print(f"{find_number}이(가) 존재하지 않습니다.")
#             break
#         current = current.left
#     else:
#         if current.right is None:
#             print(f"{find_number}이(가) 존재하지 않습니다.")
#             break
#         current = current.right