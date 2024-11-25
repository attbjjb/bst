    def __init__(self, val=None):
        self.value = val
        if self.value:
            self.left = HeapTree()
            self.right = HeapTree()
        else:
            self.left = None
            self.right = None

    def isempty(self):
        return (self.value == None)

    def isleaf(self):
        return self.left is None and self.right is None

    def inorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder() + [self.value] + self.right.inorder())

    def insert(self, data):
        if self.isempty():
            self.value = data
            self.left = HeapTree()
            self.right = HeapTree()
            print("{} is inserted successfully".format(self.value))
        elif data < self.value:
            self.left.insert(data)
            return
        elif data > self.value:
            self.right.insert(data)
        elif data == self.value:
            return

    def find(self, v):
        if self.isempty():
            print("{} is not found".format(v))
            return False
        if self.value == v:
            print("{} is found".format(v))
            return True
        if v < self.value:
            return self.left.find(v)
        else:
            return self.right.find(v)

    def maxval(self):
        if self.right.isempty():
            return (self.value)
        else:
            return (self.right.maxval())

    def delete(self, v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return
            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return

    def to_anytree(self):
        if self.isempty():
            return None
        root = Node(str(self.value))
        children = []
        if self.left and not self.left.isempty():
            children.append(self.left.to_anytree())
        if self.right and not self.right.isempty():
            children.append(self.right.to_anytree())
        root.children = children
        return root

# Пример использования
# Корневой узел
heap_tree = HeapTree()
# Добавление узла
heap_tree.insert()
# Поиск узла
heap_tree.find()

# Визуализация дерева
tree_before = heap_tree.to_anytree()
print('дерево до удаления:')
for pre, fill, node in RenderTree(tree_before):
    print(f"{pre}{node.name}")

# Удаление узла
heap_tree.delete()

print('\nдерево после удаления:')
tree_after = heap_tree.to_anytree()
for pre, fill, node in RenderTree(tree_after):
    print(f"{pre}{node.name}")





