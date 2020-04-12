import pydash
from operator import add
from mapbox import DirectionsMatrix
import mapboxGeoJsonConstructor

input = mapboxGeoJsonConstructor.collection_one.values()
print(input)

origin = [-0.071132, 51.518891]
destination = [-0.091250, 51.505262]


service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

# response = service.matrix([origin, destination, mapboxGeoJsonConstructor.collection_one], profile='mapbox/walking', sources=[0, 1], annotations=['distance'])

# York_Terrace_West, York_Square_Gardens, York_Rise_Estate_Gardens, York_Gardens, Yeading_Walk

# data = response.json()
# responseStatusCode = response.status_code
# responseHeader = response.headers

def find_route_waypoints():
    # calculate the distance to each possible waypoint from both the origin and the destination
    distances_from_origin = data['distances'][0]
    distances_from_destination = data['distances'][1]

    # for each possible waypoint, sum its distance from both the origin and the destination and then find the waypoint with the smallest total distance.  that will the waypoint of the shortest route. use the index of that waypoint to get the lon_lat
    sum_distances = list(map(add, distances_from_origin, distances_from_destination))
    shortest_distance_index = sum_distances.index(sorted(sum_distances)[2])
    waypoint_lon_lat = data['destinations'][shortest_distance_index]['location']
    list_of_waypoints = []
    list_of_waypoints.append(waypoint_lon_lat)
    # print(list_of_waypoints)

find_route_waypoints()



#
from pprint import pprint
# pprint(responseStatusCode)
# pprint(responseHeader)
# pprint(response.json()['distances'][0])
# pprint(distances_from_origin)

# def main():

# [-0.061301863303676,51.521786360354],
# [-0.013532569137843,51.526382561487],
# [-0.05720990921333,51.516323089494],
# [-0.051065100867099,51.525213734392],
# [-0.019177902823842,51.529175831881],
# [-0.035102821248716,51.527645181073],
# [-0.066721235716513,51.529969137313],
# [-0.050315406539387,51.509014581232],
# [-0.041366715819842,51.516059558877],
# [-0.045225836659679,51.526915076361],
# [-0.041443812107358,51.51426232236],
# [-0.055616524858349,51.519893722332],
# [-0.010855329562293,51.488567979003],
# [-0.055271969554349,51.527981342069],
# [-0.056712637941541,51.528005220953],
# [-0.017116408507303,51.510256445333],
# [-0.041096815873977,51.522349881668],
# [-0.032918650586594,51.511421844157],
# [-0.039579150441387,51.524123045013],
# [-0.045418257473052,51.522421981895],
# [-0.041212499269476,51.519654029999],
# [-0.03147852577133,51.511397678601],
# [-0.042806996167133,51.516083604578],
# [-0.060395909406252,51.509181744854],
# [-0.041597980712523,51.510667847417],
# [-0.062064781654964,51.503813771304],
# [-0.013454340529617,51.528179764083],
# [-0.064335241794335,51.518239429505],
# [-0.017155426711002,51.509357839359],
# [-0.053195540296469,51.509062430618],
# [-0.065280496813107,51.529945380685],
# [-0.044208783987261,51.517006252163],
# [-0.048452902742563,51.518875475744],
# [-0.047050971377665,51.51795287766],
