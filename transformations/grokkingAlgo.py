from collections import deque
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node():
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

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
# graph = {}
# graph["you"] = ["alice", "bob", "claire"]
# graph["bob"] = ["anuj", "peggy"]
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []
#
# def person_is_seller(name):
#     return name[-1] == 'm'
#
# def search(name):
#     print(graph)
#     search_que = deque()
#     search_que += graph[name]
#     searched = []
#     while search_que:
#         person = search_que.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(person + ' is mango seller')
#                 return True
#             else:
#                 search_que += graph[person]
#                 searched.append(person)
#     return False


def main():
    # search('you')
    dijkstra()



if __name__ == "__main__":
    main()
#
# def sum_list(list):
#     if list == []:
#         return 0
#     print(list[0] + sum_list(list[1:]))
#     return list[0] + sum(list_list[1:])


# def max_num(list):
#     if list == []:
#         return 0
#     return list[0]


# def max_list(list):
#     if len(list) == 2:
#         print(list[0] if list[0] > list[1] else list[1])
#         return list[0] if list[0] > list[1] else list[1]
#     sub_max = max_list(list[1:])
#     print(list[0] if list[0] > sub_max else sub_max)
#     return list[0] if list[0] > sub_max else sub_max
