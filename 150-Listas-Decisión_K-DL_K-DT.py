#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class Node:
    def __init__(self, data=None, axis=None, left=None, right=None):
        self.data = data
        self.axis = axis
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, points):
        self.root = self.build_tree(points)

    def build_tree(self, points, depth=0):
        if len(points) == 0:
            return None
        k = len(points[0])
        axis = depth % k
        sorted_points = sorted(points, key=lambda x: x[axis])
        median_index = len(sorted_points) // 2
        return Node(
            data=sorted_points[median_index],
            axis=axis,
            left=self.build_tree(sorted_points[:median_index], depth + 1),
            right=self.build_tree(sorted_points[median_index + 1:], depth + 1)
        )

    def search(self, target, node=None, depth=0):
        if node is None:
            node = self.root
        if node is None:
            return None
        if np.array_equal(node.data, target):
            return node.data
        k = len(target)
        axis = depth % k
        if target[axis] < node.data[axis]:
            return self.search(target, node.left, depth + 1)
        else:
            return self.search(target, node.right, depth + 1)

# Ejemplo de uso
points = np.array([[2,3], [5,4], [9,6], [4,7], [8,1], [7,2]])
kdtree = KDTree(points)

target = [9, 6]
print("Punto más cercano a", target, ":", kdtree.search(target))
