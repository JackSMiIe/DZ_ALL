class SimpleTreeNode:
    def __init__(self, val, parent=None):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень мб None

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is not None:
            ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
        else:
            self.Root = None

    def GetAllNodes(self):
        all_nodes = []

        def traverse(node):
            all_nodes.append(node)
            for child in node.Children:
                traverse(child)

        traverse(self.Root)
        return all_nodes




"""узлы"""
root_node = SimpleTreeNode("Root")
child1 = SimpleTreeNode("Child 1", root_node)
child2 = SimpleTreeNode("Child 2", root_node)
grandchild = SimpleTreeNode("Grandchild", child1)

"""дерево"""
tree = SimpleTree(root_node)
tree.AddChild(root_node, child1)
tree.AddChild(root_node, child2)
tree.AddChild(child1, grandchild)

"""Вывод"""
all_nodes = tree.GetAllNodes()
for node in all_nodes:
    print(node.NodeValue)

print(root_node.Children)
print(child1.Children)
print(child2.Children)
print(grandchild.Children)