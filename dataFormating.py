from operator import add
from mapbox import DirectionsMatrix
import math

service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')



# origin = [1,1]
# destination = [2,3]
# w=[-0.045418257473052, 51.522421981895]
# e=[-0.01279619151928, 51.510183314858]
# r =[-0.068770393713962, 51.515614772134]
# t= [-0.045302810969366, 51.525117839052]
# y=[-0.055348551291013, 51.526184094351]
# u=[-0.075555186872678, 51.525618133595]
# i=[-0.017776262243614, 51.528252888321]
# q=[-0.048721755995117, 51.51258512161]
# w=[-0.045418257473052, 51.522421981895]
# e=[-0.01279619151928, 51.510183314858]
# r =[-0.068770393713962, 51.515614772134]
# t= [-0.045302810969366, 51.525117839052]
# y=[-0.055348551291013, 51.526184094351]
# u=[-0.075555186872678, 51.525618133595]
# i=[-0.017776262243614, 51.528252888321]
# o=[-0.061301863303676, 51.521786360354]
# p=[-0.013532569137843, 51.526382561487]
# a=[-0.05720990921333, 51.516323089494]
# s=[-0.051065100867099, 51.525213734392]
# d=[-0.019177902823842, 51.529175831881]
# f=[-0.035102821248716, 51.527645181073]
# g=[-0.066721235716513, 51.529969137313]
# h=[-0.050315406539387, 51.509014581232]
# j=[-0.041366715819842, 51.516059558877]
# k=[-0.045225836659679, 51.526915076361]
# l=[-0.041443812107358, 51.51426232236]
# z=[-0.055616524858349, 51.519893722332]
# x=[-0.010855329562293, 51.488567979003]
# c=[-0.055271969554349, 51.527981342069]
# v=[-0.056712637941541, 51.528005220953]
# b=[-0.017116408507303, 51.510256445333]
# n=[-0.041096815873977, 51.522349881668]
# m=[-0.032918650586594, 51.511421844157]
# qq=[-0.03957915044187, 51.524123045013]
# ww=[-0.04541825747305, 51.522421981895]
# ee=[-0.041212499269476, 51.519654029999]
# rr=[-0.03147852577133, 51.511397678601]
# tt=[-0.042806996167133, 51.516083604578]
# yy=[-0.060395909406252, 51.509181744854]
# uu=[-0.041597980712523, 51.510667847417]
# ii=[-0.062064781654964, 51.503813771304]
# oo=[-0.013454340529617, 51.528179764083]
# pp=[-0.064335241794335, 51.518239429505]
# aa=[-0.017155426711002, 51.509357839359]
# ss=[-0.053195540296469, 51.509062430618]
# dd=[-0.065280496813107, 51.529945380685]
# ff=[-0.044208783987261, 51.517006252163]
# gg=[-0.048452902742563, 51.518875475744]
# hh=[-0.047050971377665, 51.517952877664]

# a=11
# b=12
# c=13
# d=14
# e=15
# f=16
# g=17
# h=18
# i=19
#
#
# features_list = [a,b,c,d,e,f,g,h,i]
# print(features_list[5])
# features_list.remove(features_list[5])
# print(features_list)
#
# gmaplist_of_waypoints = [[0.036388, 51.535784], [0.018659, 51.531669], [0.005693, 51.528083], [-0.033214, 51.525162], [-0.011057, 51.531048], [-0.046244, 51.521906]]
# gmaplist_of_waypoints2 = [x[::-1] for x in gmaplist_of_waypoints]
# print(gmaplist_of_waypoints2)
# [51.535784, 0.036388], [51.531669, 0.018659], [51.528083, 0.005693], [51.525162, -0.033214], [51.531048, -0.011057], [51.521906, -0.046244]


# xs = ['a', 'b', 'c', 'd', 'e' ]
#
# my_dict = {}
# for i in range(len(xs)):
#     my_dict[i] = xs[i]
#
# print(my_dict)
bb = [51.550540, 0.101267][::-1]
cc  =[51.535669, 0.016456][::-1]
dd  =[51.521890, -0.046287][::-1]
ee =[51.527436, -0.023635][::-1]
ff =[51.531695, 0.018645][::-1]
gg =[51.528275, 0.005575][::-1]
hh =[51.531020, -0.011012][::-1]
ii  =[51.525327, -0.033322][::-1]
jj =[51.525364, 0.059439][::-1]
list_of_waypoints = []


def find_route_waypoints():
    loop_count = 0
    aa = [-0.084254, 51.518961]
    features_list = [aa,bb,cc,dd,ee,ff,gg,hh]
    while loop_count < 6:
        response = service.matrix(features_list, profile='mapbox/walking', sources=[0,1],  annotations=['distance'])
        data = response.json()
# calculate the distance to each possible waypoint from both the origin and the destination
        distances_from_origin = data['distances'][0]
        distances_from_destination = data['distances'][1]
# for each potential waypoint in the features_list, sum its distance from both the origin and the destination and then find the waypoint with the smallest total distance.
        sum_distances = list(map(add, distances_from_origin, distances_from_destination))
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
        print(list_of_waypoints)

find_route_waypoints()
