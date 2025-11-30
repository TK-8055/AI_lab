def a_star(graph, h, start, goal):
    open_list = [(start, [start], 0)] 
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: x[2] + h[x[0]])
        current, path, cost = open_list.pop(0)

        if current == goal:
            return path, cost

        visited.add(current)

        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                total_cost = cost + edge_cost
                open_list.append((neighbor, path + [neighbor], total_cost))

    return None, None


def greedy_bfs(graph, h, start, goal):
    open_list = [(start, [start])]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: h[x[0]])
        current, path = open_list.pop(0)

        if current == goal:
            return path

        visited.add(current)

        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor]))

    return None


def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        for neighbor, weight in graph[path[i]]:
            if neighbor == path[i + 1]:
                cost += weight
                break
    return cost


graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ").strip()
    neighbors = input(f"Enter neighbors of {node} as (name cost), separated by commas: ").strip()
    neighbor_list = []
    if neighbors:
        for pair in neighbors.split(','):
            name, cost = pair.strip().split()
            neighbor_list.append((name, int(cost)))
    graph[node] = neighbor_list

h = {}
print("\nEnter heuristic values:")
for node in graph:
    h[node] = int(input(f"Heuristic for {node}: "))

start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

a_star_path, a_star_cost = a_star(graph, h, start, goal)

greedy_path = greedy_bfs(graph, h, start, goal)
greedy_cost = calculate_cost(graph, greedy_path) if greedy_path else None

print("\n====== FINAL COMPARISON ======")
print("A* Search Path:", " -> ".join(a_star_path) if a_star_path else "No Path")
print("A* Total Cost:", a_star_cost if a_star_path else "-")

print("\nGreedy Best-First Search Path:", " -> ".join(greedy_path) if greedy_path else "No Path")
print("Greedy BFS Total Cost:", greedy_cost if greedy_path else "-")

if a_star_cost and greedy_cost:
    print("\n→ A* gives the optimal (minimum-cost) path.")
    print("→ Greedy BFS may fail to give optimal path because it considers only heuristic.")



#check how to give input in 2.txt sample output
