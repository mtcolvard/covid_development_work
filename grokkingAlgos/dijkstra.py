from collections import deque
graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
#
# graph['a'] = {}
# graph['a']['fin'] = 1
#
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
#
# graph['fin'] = {}
#
# infinity = float("inf")
# costs = {}
# costs["a"] = 6
# costs["b"] = 2
# costs["fin"] = infinity
#
# parents = {}
# parents["a"] = "start"
# parents["b"] = "start"
# parents["fin"] = None

graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2

graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7

graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3

graph['d'] = {}
graph['d']['fin'] = 1

graph['fin'] = {}

print(graph)

infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = None
parents['b'] = None
parents['c'] = None
parents['d'] = None
parents['fin'] = None

processed = []

def dijkstra():
    node = find_lowest_cost_node()
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node()
    print(costs['fin'])
    return costs['fin']


def find_lowest_cost_node():
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def main():
    dijkstra()

if __name__ == "__main__":
    main()
