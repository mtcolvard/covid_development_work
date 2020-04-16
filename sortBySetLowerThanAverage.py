from operator import add
from mapbox import DirectionsMatrix
import pydash

service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

# features_list_dict_straight_line = {'bb': [51.550540, 0.101267][::-1],
# 'cc': [51.535669, 0.016456][::-1],
# 'dd': [51.521890, -0.046287][::-1],
# 'ee': [51.527436, -0.023635][::-1],
# 'ff': [51.531695, 0.018645][::-1],
# 'gg': [51.528275, 0.005575][::-1],
# 'hh': [51.531020, -0.011012][::-1],
# 'ii': [51.525327, -0.033322][::-1],
# 'jj': [51.525364, 0.059439][::-1]
# }



origin = [-0.047092, 51.519331 ]
destination = [-0.043618, 51.538311]

features_list_dict_tower_hamlets = {
'aa': origin,
'bb': destination,
'cc': [-0.045418257473052, 51.522421981895],
'dd': [-0.01279619151928, 51.510183314858],
'ee': [-0.068770393713962, 51.515614772134],
'ff': [-0.045302810969366, 51.525117839052],
'gg': [-0.044579, 51.522376],
'hh': [-0.033971,51.522356],
'ii': [-0.017776262243614, 51.528252888321],
'jj': [-0.061301863303676, 51.521786360354]
}
list_of_waypoints = []


def find_route_waypoints():
    loop_count = 0

    features_list = [features_list_dict_tower_hamlets['aa'], features_list_dict_tower_hamlets['bb'], features_list_dict_tower_hamlets['cc'], features_list_dict_tower_hamlets['dd'], features_list_dict_tower_hamlets['ee'], features_list_dict_tower_hamlets['ff'], features_list_dict_tower_hamlets['gg'], features_list_dict_tower_hamlets['hh']]

    response = service.matrix(features_list, profile='mapbox/walking', sources=[0,1],  annotations=['distance'])
    data = response.json()

    # calculate the distance to each possible waypoint from both the origin and the destination
    # for each potential waypoint in the features_list, sum its distance from both the origin and the destination and then find the waypoint with the smallest total distance.
    # convert the sum_distances list into a dictionary to keep track of indexes relative to the features_list
    # lets try converting distance from origin into a dictionary, sorting it, and then comparing it to the sum_distances_minus_average to find the lowest value from the set
    distances_from_origin = data['distances'][0]
    distances_from_destination = data['distances'][1]
    sum_distances = list(map(add, distances_from_origin, distances_from_destination))
    average_distance = sum(sum_distances[2::])/(len(sum_distances)-2)

    distances_from_origin_dict = dict(zip(features_list_dict_tower_hamlets.keys(), distances_from_origin))
    sum_distances_dict = dict(zip(features_list_dict_tower_hamlets.keys(), sum_distances))

    sum_distances_minus_average = {k:v-average_distance for (k,v) in sum_distances_dict.items()}
    waypoint_distances_closer_than_average = {k:v for (k, v) in sum_distances_minus_average.items() if v<0}
    waypoint_distance_from_origin = {k:v for (k,v) in distances_from_origin_dict.items() if k in distances_from_origin_dict.keys() & waypoint_distances_closer_than_average.keys()}
    del waypoint_distance_from_origin['aa']

    closest_waypoint = min(waypoint_distance_from_origin, key=waypoint_distance_from_origin.get)
    print(closest_waypoint)




#     min_distance = min(sum_distances_minus_average.values())
#     min_distance_index = [num for num, distance in sum_distances_minus_average.items() if distance == min_distance ]
# # add '2' to the min_distance_index to account for the origin and destination you deleted
#     min_distance_index = min_distance_index[0] + 2
#     waypoint_lon_lat = data['destinations'][min_distance_index]['location']
#     list_of_waypoints.append(waypoint_lon_lat)
#     features_list.remove(features_list[min_distance_index])
#     # loop_count = loop_count + 1
#     # print(list_of_waypoints)

find_route_waypoints()
