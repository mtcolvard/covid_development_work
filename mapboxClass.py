import pydash
from operator import add
from mapbox import DirectionsMatrix
import mapboxGeoJsonConstructor

thingy = list(mapboxGeoJsonConstructor.collection_one.values())

q=[-0.048721755995117, 51.51258512161]
w=[-0.045418257473052, 51.522421981895]
e=[-0.01279619151928, 51.510183314858]
r =[-0.068770393713962, 51.515614772134]
t= [-0.045302810969366, 51.525117839052]
y=[-0.055348551291013, 51.526184094351]
u=[-0.075555186872678, 51.525618133595]
i=[-0.017776262243614, 51.528252888321]
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
qq=[-0.03957915044187, 51.524123045013]
ww=[-0.04541825747305, 51.522421981895]
ee=[-0.041212499269476, 51.519654029999]
rr=[-0.03147852577133, 51.511397678601]
tt=[-0.042806996167133, 51.516083604578]
yy=[-0.060395909406252, 51.509181744854]
uu=[-0.041597980712523, 51.510667847417]
ii=[-0.062064781654964, 51.503813771304]
oo=[-0.013454340529617, 51.528179764083]
pp=[-0.064335241794335, 51.518239429505]
aa=[-0.017155426711002, 51.509357839359]
ss=[-0.053195540296469, 51.509062430618]
dd=[-0.065280496813107, 51.529945380685]
ff=[-0.044208783987261, 51.517006252163]
gg=[-0.048452902742563, 51.518875475744]
hh=[-0.047050971377665, 51.517952877664]


pride_of_spitalfields = (-0.071132, 51.518891)
origin = (-0.071880,51.516319)
destination = (-0.020552, 51.523678)
list_of_waypoints = []


service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

response = service.matrix([origin, destination, q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,m,qq,rr], profile='mapbox/walking',  annotations=['distance'])


data = response.json()
responseStatusCode = response.status_code
responseHeader = response.headers

def find_route_waypoints():
    # calculate the distance to each possible waypoint from both the origin and the destination
    number_of_loops = 0
    distances_from_origin = data['distances'][0]
    while number_of_loops < 7:
        distances_from_destination = data['distances'][1]

        # for each possible waypoint, sum its distance from both the origin and the destination and then find the waypoint with the smallest total distance.  that will the waypoint of the shortest route. use the index of that waypoint to get the lon_lat
        sum_distances = list(map(add, distances_from_origin, distances_from_destination))
        shortest_distance_index = sum_distances.index(sorted(sum_distances)[2])
        distances_from_origin = data['distances'][shortest_distance_index]
        number_of_loops = number_of_loops + 1
        waypoint_lon_lat = data['destinations'][shortest_distance_index]['location']

        list_of_waypoints.append(waypoint_lon_lat)
        # print(sum_distances)
        # print(shortest_distance_index)
        print(distances_from_origin)
        # print(waypoint_lon_lat)
        print(list_of_waypoints)

find_route_waypoints()



#
from pprint import pprint
# pprint(responseStatusCode)
# pprint(responseHeader)
# pprint(response.json())
# pprint(response.json()['distances'][0])
# pprint(response.json()['distances'][1])
# pprint(distances_from_origin)

# def main():
