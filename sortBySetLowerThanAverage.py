from operator import add
from mapbox import DirectionsMatrix
import math

service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

features_list_dict = {'bb': [51.550540, 0.101267][::-1],
'cc': [51.535669, 0.016456][::-1],
'dd': [51.521890, -0.046287][::-1],
'ee': [51.527436, -0.023635][::-1],
'ff': [51.531695, 0.018645][::-1],
'gg': [51.528275, 0.005575][::-1],
'hh': [51.531020, -0.011012][::-1],
'ii': [51.525327, -0.033322][::-1],
'jj': [51.525364, 0.059439][::-1]
}
list_of_waypoints = []


def find_route_waypoints():
    loop_count = 0
    aa = [-0.084254, 51.518961]
    features_list = [aa, features_list_dict['bb'],features_list_dict['cc'],features_list_dict['dd'],features_list_dict['ee'],features_list_dict['ff'],features_list_dict['gg'],features_list_dict['hh']]
    while loop_count < 6:
        response = service.matrix(features_list, profile='mapbox/walking', sources=[0,1],  annotations=['distance'])
        data = response.json()
# calculate the distance to each possible waypoint from both the origin and the destination
        distances_from_origin = data['distances'][0]
        distances_from_destination = data['distances'][1]
# for each potential waypoint in the features_list, sum its distance from both the origin and the destination and then find the waypoint with the smallest total distance.
        sum_distances = list(map(add, distances_from_origin, distances_from_destination))
        dictex = dict(zip(features_list_dict.keys(), sum_distances))
        print(dictex)
# delete the first two values as they represent the origin and the destination in the features_list
        del sum_distances[0:2]
        average_distance = sum(sum_distances)/len(sum_distances)
# convert the sum_distances list into a dictionary to keep track of indexes relative to the features_list

# lets try converting distance from origin into a dictionary, sorting it, and then comparing it to the sum_distances_minus_average to find the lowest value from the set

        sum_distances_dict = {}
        for i in range(len(sum_distances)):
            sum_distances_dict[i] = sum_distances[i]
        sum_distances_minus_average = {k:v-average_distance for (k,v) in sum_distances_dict.items()}

        min_distance = min(sum_distances_minus_average.values())
        min_distance_index = [num for num, distance in sum_distances_minus_average.items() if distance == min_distance ]
# add '2' to the min_distance_index to account for the origin and destination you deleted
        min_distance_index = min_distance_index[0] + 2
        waypoint_lon_lat = data['destinations'][min_distance_index]['location']
        list_of_waypoints.append(waypoint_lon_lat)
        features_list.remove(features_list[min_distance_index])
        loop_count = loop_count + 1
        # print(list_of_waypoints)

find_route_waypoints()
