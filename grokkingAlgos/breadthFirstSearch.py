from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def breadthFirstSearch(name):
    print(graph)
    search_que = deque()
    search_que += graph[name]
    searched = []
    while search_que:
        person = search_que.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is mango seller')
                return True
            else:
                search_que += graph[person]
                searched.append(person)
    return False


def main():
    # search('you')
    breadthFirstSearch('you')



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
