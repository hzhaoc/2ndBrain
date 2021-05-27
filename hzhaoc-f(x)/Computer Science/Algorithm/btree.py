from binarytree import Node 

def generate_btree4encode(node, depth):
    # generate a binary tree of 0, 1 for encoding
    if depth==0:
        return
    node.left = Node(0)
    node.right = Node(1)
    generate_btree4encode(node.left, depth-1)
    generate_btree4encode(node.right, depth-1)

def main():
    root = Node(0)
    depth = 3
    generate_btree4encode(root, depth)
    print(root)

if __name__ == "__main__":
    main()