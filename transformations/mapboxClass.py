import pydash
from operator import add
from mapbox import DirectionsMatrix
import mapboxGeoJsonConstructor

thingy = list(mapboxGeoJsonConstructor.collection_one.values())
pride_of_spitalfields = (-0.071132, 51.518891)

q=[-0.048721755995117, 51.51258512161]
w=[-0.045418257473052, 51.522421981895]
e=[-0.01279619151928, 51.510183314858]
r =[-0.068770393713962, 51.515614772134]
t= [-0.045302810969366, 51.525117839052]
y=[-0.055348551291013, 51.526184094351]
u=[-0.075555186872678, 51.525618133595]
i=[-0.017776262243614, 51.528252888321]
o=[-0.061301863303676, 51.521786360354]
p=[-0.013532569137843, 51.526382561487]
a=[-0.05720990921333, 51.516323089494]
s=[-0.051065100867099, 51.525213734392]
d=[-0.019177902823842, 51.529175831881]
f=[-0.035102821248716, 51.527645181073]
g=[-0.066721235716513, 51.529969137313]
h=[-0.050315406539387, 51.509014581232]
j=[-0.041366715819842, 51.516059558877]
k=[-0.045225836659679, 51.526915076361]
l=[-0.041443812107358, 51.51426232236]
z=[-0.055616524858349, 51.519893722332]
x=[-0.010855329562293, 51.488567979003]
c=[-0.055271969554349, 51.527981342069]
v=[-0.056712637941541, 51.528005220953]
b=[-0.017116408507303, 51.510256445333]
n=[-0.041096815873977, 51.522349881668]
m=[-0.032918650586594, 51.511421844157]
q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,m



list_of_waypoints = []
bb = [51.550540, 0.101267][::-1]
cc  =[51.535669, 0.036456][::-1]
dd  =[51.521890, -0.046287][::-1]
ee =[51.527436, -0.023635][::-1]
ff =[51.531695, 0.018645][::-1]
gg =[51.528275, 0.005575][::-1]
hh =[51.531020, -0.011012][::-1]
ii  =[51.525327, -0.033322][::-1]
jj =[51.525364, 0.059439][::-1]



service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')




def find_route_waypoints():
    loop_count = 0
    aa = [-0.084254, 51.518961]
    features_list = [aa,bb,cc,dd,ee,ff,gg,hh]
    while loop_count < 1:
        response = service.matrix(features_list, profile='mapbox/walking', sources=[0,1],  annotations=['distance'])
        data = response.json()
# calculate the distance to each possible waypoint from both the origin and the destination
        distances_from_origin = data['distances'][0]
        distances_from_destination = data['distances'][1]
# for each possible waypoint, sum its distance from both the origin and the destination and then find the waypoint with the smallest total distance.  that will the waypoint of the shortest route. use the index of that waypoint to get the lon_lat
        sum_distances = list(map(add, distances_from_origin, distances_from_destination))
        print(sum_distances)
        del sum_distances[0:2]
        average_distance = sum(sum_distances)/len(sum_distances)
        sum_distances_dict = {}
        for i in range(len(sum_distances)):
            sum_distances_dict[i] = sum_distances[i]
        print(sum_distances_dict)
        sum_distances_minus_average = {k:v-average_distance for (k,v) in sum_distances_dict.items()}
        sum_distances_dict_min = {k:v for k,v in sorted(sum_distances_minus_average.items(), key=lambda item: item[1])}
        print(sum_distances_dict_min)
        # shortest_distance_index = sum_distances_dic_min.index(sorted(sum_distances_dic_min)[0])
        waypoint_lon_lat = data['destinations'][sum_distances_dict_min]['location']
        list_of_waypoints.append(waypoint_lon_lat)
        features_list.remove(features_list[sum_distances_dict_min])
        aa = waypoint_lon_lat
        loop_count = loop_count + 1
        # print('shortest_distance_index', shortest_distance_index)
        # print('distances_from_destination',distances_from_destination)
        # print('sum_distances', sum_distances)
        # print('sorted_sum_distances',sorted(sum_distances))
        # print('list_of_waypoints',list_of_waypoints)
find_route_waypoints()

# responseStatusCode = response.status_code
# responseHeader = response.headers



#
from pprint import pprint
# pprint(responseStatusCode)
# pprint(responseHeader)
# pprint(response.json()['distances'][0])
# pprint(response.json()['distances'][1])
# pprint(response.json())
# pprint(distances_from_origin)

# def main():
