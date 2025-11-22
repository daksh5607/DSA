from collections import deque
import heapq

class BuildingData:
    def __init__(self, building_id, name, location, connections=None):
        self.building_id = building_id
        self.building_name = name
        self.location_details = location
        self.connections = connections if connections is not None else {} 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return f"ID:{self.building_id}, Name:{self.building_name}, Loc:{self.location_details}"

    def __lt__(self, other):
        return self.building_id < other.building_id

class BST:
    def __init__(self):
        self.root = None

    def _get_node_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_node_height(node.left), self._get_node_height(node.right))

    def insert_building(self, data: BuildingData):
        if self.root is None:
            self.root = data
        else:
            self._insert_recursive(self.root, data)
        print(f"BST: Inserted Building ID {data.building_id}")

    def _insert_recursive(self, node, data):
        if data.building_id < node.building_id:
            if node.left is None:
                node.left = data
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = data
            else:
                self._insert_recursive(node.right, data)

    def search_building(self, building_id):
        return self._search_recursive(self.root, building_id)

    def _search_recursive(self, node, building_id):
        if node is None or node.building_id == building_id:
            return node
        if building_id < node.building_id:
            return self._search_recursive(node.left, building_id)
        return self._search_recursive(node.right, building_id)

    def traverse_buildings(self, order='inorder'):
        results = []
        if order == 'inorder':
            self._inorder(self.root, results)
        elif order == 'preorder':
            self._preorder(self.root, results)
        elif order == 'postorder':
            self._postorder(self.root, results)
        
        print(f"\n--- BST {order.upper()} Traversal ---")
        for res in results:
            print(res)

    def _inorder(self, node, results):
        if node:
            self._inorder(node.left, results)
            results.append(str(node))
            self._inorder(node.right, results)

    def _preorder(self, node, results):
        if node:
            results.append(str(node))
            self._preorder(node.left, results)
            self._preorder(node.right, results)

    def _postorder(self, node, results):
        if node:
            self._postorder(node.left, results)
            self._postorder(node.right, results)
            results.append(str(node))

    def get_height(self):
        return self._get_node_height(self.root)

class AVLTree(BST):
    
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y): 
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        
        print(f"*** AVL Rotation: RR/Right Rotation demonstrated at ID {y.building_id} ***")
        return x

    def _left_rotate(self, x): 
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        print(f"*** AVL Rotation: LL/Left Rotation demonstrated at ID {x.building_id} ***")
        return y
    
    def insert_building(self, data: BuildingData):
        self.root = self._insert_recursive(self.root, data)
        print(f"AVL: Inserted Building ID {data.building_id}")
        
    def _insert_recursive(self, root, data):
        if not root:
            return data
        
        if data.building_id < root.building_id:
            root.left = self._insert_recursive(root.left, data)
        elif data.building_id > root.building_id:
            root.right = self._insert_recursive(root.right, data)
        else:
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and data.building_id < root.left.building_id:
            return self._right_rotate(root)

        if balance < -1 and data.building_id > root.right.building_id:
            return self._left_rotate(root)

        if balance > 1 and data.building_id > root.left.building_id:
            root.left = self._left_rotate(root.left)
            print(f"*** AVL Rotation: LR Case detected/demonstrated at ID {root.building_id} ***")
            return self._right_rotate(root)
        
        if balance < -1 and data.building_id < root.right.building_id:
            root.right = self._right_rotate(root.right)
            print(f"*** AVL Rotation: RL Case detected/demonstrated at ID {root.building_id} ***")
            return self._left_rotate(root)

        return root

class CampusGraph:
    def __init__(self, building_ids):
        self.nodes = building_ids
        self.num_nodes = len(building_ids)
        self.id_to_index = {id: i for i, id in enumerate(building_ids)}
        
        self.adj_matrix = [[0] * self.num_nodes for _ in range(self.num_nodes)]
        self.adj_list = {id: {} for id in building_ids}

    def add_edge(self, id1, id2, weight, directed=False):
        i, j = self.id_to_index[id1], self.id_to_index[id2]
        
        self.adj_matrix[i][j] = weight
        if not directed:
            self.adj_matrix[j][i] = weight

        self.adj_list[id1][id2] = weight
        if not directed:
            self.adj_list[id2][id1] = weight

    def display_representations(self):
        print("\n--- Graph Representation (Part 2.1) ---")
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
        print("\nAdjacency List:")
        for node, neighbors in self.adj_list.items():
            print(f"Building {node}: {neighbors}")

    def bfs(self, start_id):
        visited = set()
        queue = deque([start_id])
        traversal_order = []
        
        print(f"\n--- Graph Traversal: BFS starting at {start_id} ---")
        while queue:
            node_id = queue.popleft()
            if node_id not in visited:
                traversal_order.append(node_id)
                visited.add(node_id)
                print(f"Visited (BFS): {node_id}")
                
                for neighbor_id in self.adj_list.get(node_id, {}):
                    if neighbor_id not in visited:
                        queue.append(neighbor_id)
        return traversal_order

    def dfs(self, start_id):
        visited = set()
        traversal_order = []
        
        print(f"\n--- Graph Traversal: DFS starting at {start_id} ---")
        self._dfs_recursive(start_id, visited, traversal_order)
        return traversal_order

    def _dfs_recursive(self, node_id, visited, order):
        visited.add(node_id)
        order.append(node_id)
        print(f"Visited (DFS): {node_id}")
        
        for neighbor_id in self.adj_list.get(node_id, {}):
            if neighbor_id not in visited:
                self._dfs_recursive(neighbor_id, visited, order)

    def find_optimal_path(self, start_id, end_id):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_id] = 0
        priority_queue = [(0, start_id)]
        path = {node: None for node in self.nodes}

        print(f"\n--- Optimal Path (Dijkstra's) from {start_id} to {end_id} ---")
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue
            
            if current_node == end_id:
                break

            for neighbor, weight in self.adj_list[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        if distances[end_id] == float('inf'):
            return "Path not found."

        final_path = []
        node = end_id
        while node is not None:
            final_path.append(node)
            node = path[node]
        final_path.reverse()

        print(f"Shortest Distance: {distances[end_id]}")
        print(f"Optimal Path: {' -> '.join(map(str, final_path))}")
        return final_path, distances[end_id]

    def plan_utility_layout(self):
        edges = []
        for u in self.adj_list:
            for v, weight in self.adj_list[u].items():
                if u < v: 
                    edges.append((weight, u, v))
        
        edges.sort()
        parent = {node: node for node in self.nodes}
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i
                return True
            return False

        mst_edges = []
        total_cost = 0
        
        for weight, u, v in edges:
            if union(u, v):
                mst_edges.append((u, v, weight))
                total_cost += weight
                
        print("\n--- Utility Layout (Kruskal's MST) ---")
        print(f"Cost-effective Cable Layout (Edges): {mst_edges}")
        print(f"Total Minimum Cost: {total_cost}")
        return mst_edges, total_cost

class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def evaluate_expression(self, root):
        if root is None:
            return 0
        if root.value not in ['+', '-', '*', '/']:
            return float(root.value) 

        left_val = self.evaluate_expression(root.left)
        right_val = self.evaluate_expression(root.right)

        if root.value == '+':
            return left_val + right_val
        elif root.value == '-':
            return left_val - right_val
        elif root.value == '*':
            return left_val * right_val
        elif root.value == '/':
            if right_val == 0:
                raise ZeroDivisionError("Cannot divide by zero in energy calculation.")
            return left_val / right_val
        
    def construct_from_postfix(self, postfix_list):
        stack = []
        operators = ['+', '-', '*', '/']
        for token in postfix_list:
            node = ExpressionNode(token)
            if token not in operators:
                stack.append(node)
            else:
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        return stack.pop()


class CampusNavigationPlanner:
    def __init__(self, building_ids):
        self.building_tree_bst = BST()
        self.building_tree_avl = AVLTree()
        self.campus_graph = CampusGraph(building_ids)
        self.expression_tree_planner = ExpressionTree()

    def add_building_record(self, data: BuildingData):
        self.building_tree_bst.insert_building(data)
        self.building_tree_avl.insert_building(data)

    def list_campus_locations(self):
        print("\n" + "="*50)
        print("LISTING CAMPUS LOCATIONS VIA TREE TRAVERSALS (Part 1.1)")
        print("="*50)
        self.building_tree_bst.traverse_buildings('inorder')
        self.building_tree_bst.traverse_buildings('preorder')
        self.building_tree_bst.traverse_buildings('postorder')

    def compare_tree_heights(self):
        bst_height = self.building_tree_bst.get_height()
        avl_height = self.building_tree_avl.get_height()
        print(f"\n--- Height Comparison (Part 1.2) ---")
        print(f"BST Height: {bst_height}")
        print(f"AVL Tree Height: {avl_height}")
        print(f"Analysis: AVL is expected to be shorter/more balanced (log n height).")

    def build_and_traverse_graph(self):
        self.campus_graph.display_representations()
        
        if self.campus_graph.nodes:
            start_node = self.campus_graph.nodes[0]
            self.campus_graph.bfs(start_node)
            self.campus_graph.dfs(start_node)

    def find_optimal_path(self, start, end):
        return self.campus_graph.find_optimal_path(start, end)
        
    def plan_utility_layout(self):
        return self.campus_graph.plan_utility_layout()

    def calculate_energy_bill(self, postfix_expression):
        print("\n--- Energy Bill Calculation (Expression Tree) ---")
        try:
            root = self.expression_tree_planner.construct_from_postfix(postfix_expression)
            result = self.expression_tree_planner.evaluate_expression(root)
            print(f"Expression: {' '.join(postfix_expression)} evaluates to: {result}")
            return result
        except Exception as e:
            print(f"Error during calculation: {e}")
            return None


if __name__ == "__main__":
    buildings_data = [
        BuildingData(50, "CSE Dept", "North Wing"),
        BuildingData(25, "Lab 1", "CSE Wing"),
        BuildingData(10, "Server Room", "Basement"),
        BuildingData(75, "Faculty Offices", "CSE Wing"),
        BuildingData(101, "Admin Block", "Main Entry"),
        BuildingData(150, "Library", "Central Zone"),
        BuildingData(125, "Auditorium", "East Wing"),
        BuildingData(175, "Cafeteria", "South Wing")
    ]
    building_ids = [b.building_id for b in buildings_data]
    
    planner = CampusNavigationPlanner(building_ids)

    print("="*60)
    print("DEMO: PART 1 - TREES (BST & AVL)")
    print("="*60)

    for b in buildings_data:
        planner.add_building_record(b) 

    planner.list_campus_locations()
    
    planner.compare_tree_heights()

    print("\n" + "="*60)
    print("DEMO: PART 2 - GRAPHS")
    print("="*60)

    planner.campus_graph.add_edge(101, 50, 10)
    planner.campus_graph.add_edge(101, 150, 5)
    planner.campus_graph.add_edge(50, 25, 3)
    planner.campus_graph.add_edge(50, 75, 4)
    planner.campus_graph.add_edge(150, 125, 7)
    planner.campus_graph.add_edge(150, 175, 2)
    planner.campus_graph.add_edge(125, 175, 1)
    planner.campus_graph.add_edge(10, 25, 2)
    
    planner.build_and_traverse_graph()

    planner.find_optimal_path(101, 175)

    planner.plan_utility_layout()

    energy_expression = ['100.5', '50', '+', '5', '2', '-', '*']
    planner.calculate_energy_bill(energy_expression)
