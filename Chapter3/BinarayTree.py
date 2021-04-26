class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        left = self.left.depth() if self.left else 0
        right = self.right.depth() if self.right else 0

        if left > right :
            return left + 1
        #elif right > left:
        #    return right + 1
        else: return right + 1
            #return 0



class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
              return self.root.depth()
        else:
            return None


    def depth(self):
        if self.root:
            return self.root.depth()
        elif self.root ==1:
            return 1
        else:
            return 0


def solution(x):
    return 0