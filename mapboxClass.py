import pydash
from operator import add
from mapbox import DirectionsMatrix
# from .locationsObject import Locations

# allLocations = Locations.object.all()

York_Terrace_West  =  {'type': 'Feature', 'properties': {'name': 'York Terrace West'}, 'geometry': {'type': 'Point', 'coordinates': [-0.150578775, 51.52412738]}}
York_Square_Gardens  =  {'type': 'Feature', 'properties': {'name': 'York Square Gardens'}, 'geometry': {'type': 'Point', 'coordinates': [-0.040042164, 51.51333964]}}
York_Rise_Estate_Gardens  =  {'type': 'Feature', 'properties': {'name': 'York Rise Estate Gardens'}, 'geometry': {'type': 'Point', 'coordinates': [-0.143500164, 51.55638842]}}
York_Gardens  =  {'type': 'Feature', 'properties': {'name': 'York Gardens'}, 'geometry': {'type': 'Point', 'coordinates': [-0.177365387, 51.46699476]}}
Yeading_Walk  =  {'type': 'Feature', 'properties': {'name': 'Yeading Walk'}, 'geometry': {'type': 'Point', 'coordinates': [-0.367516667, 51.58489741]}}
Yardley_Recreation_Ground  =  {'type': 'Feature', 'properties': {'name': 'Yardley Recreation Ground'}, 'geometry': {'type': 'Point', 'coordinates': [-0.228778185, 51.36616707]}}
Yalta_Memorial_Garden  =  {'type': 'Feature', 'properties': {'name': 'Yalta Memorial Garden'}, 'geometry': {'type': 'Point', 'coordinates': [-0.17481463, 51.49483187]}}
Wyck_Gardens  =  {'type': 'Feature', 'properties': {'name': 'Wyck Gardens'}, 'geometry': {'type': 'Point', 'coordinates': [-0.105685898, 51.4595636]}}
WWT_London_Wetland_Centre  =  {'type': 'Feature', 'properties': {'name': 'WWT London Wetland Centre'}, 'geometry': {'type': 'Point', 'coordinates': [-0.236013033, 51.47688433]}}
Wrythe_Recreation_Ground  =  {'type': 'Feature', 'properties': {'name': 'Wrythe Recreation Ground'}, 'geometry': {'type': 'Point', 'coordinates': [-0.174007434, 51.37072169]}}
Wrythe_Green  =  {'type': 'Feature', 'properties': {'name': 'Wrythe Green'}, 'geometry': {'type': 'Point', 'coordinates': [-0.166756541, 51.37240698]}}
Wormwood_Scrubs_including_Old_Oak_Common  =  {'type': 'Feature', 'properties': {'name': 'Wormwood Scrubs including Old Oak Common'}, 'geometry': {'type': 'Point', 'coordinates': [-0.235717844, 51.52184199]}}
Wormholt_Park  =  {'type': 'Feature', 'properties': {'name': 'Wormholt Park'}, 'geometry': {'type': 'Point', 'coordinates': [-0.239049728, 51.51020195]}}
Wormholt_Estate  =  {'type': 'Feature', 'properties': {'name': 'Wormholt Estate'}, 'geometry': {'type': 'Point', 'coordinates': [-0.243301365, 51.51206419]}}
Woolwich_Common_and_Royal_Artillery_Barracks  =  {'type': 'Feature', 'properties': {'name': 'Woolwich Common and Royal Artillery Barracks'}, 'geometry': {'type': 'Point', 'coordinates': [0.053470899, 51.47756693]}}
Wool_House_Garden  =  {'type': 'Feature', 'properties': {'name': 'Wool House Garden'}, 'geometry': {'type': 'Point', 'coordinates': [-0.135466095, 51.50590308]}}
Woodside_Park  =  {'type': 'Feature', 'properties': {'name': 'Woodside Park'}, 'geometry': {'type': 'Point', 'coordinates': [-0.111252444, 51.60353366]}}


origin = [-0.071132, 51.518891]
destination = [-0.091250, 51.505262]

waypoint_coordinates = r'[-0.048721755995117,51.51258512161],
[-0.045418257473052,51.522421981895],
[-0.01279619151928,51.510183314858],
[-0.068770393713962,51.515614772134],
[-0.045302810969366,51.525117839052],
[-0.055348551291013,51.526184094351],
[-0.075555186872678,51.525618133595],
[-0.017776262243614,51.528252888321]'

service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

response = service.matrix([origin, destination, [-0.048721755995117,51.51258512161]], profile='mapbox/walking', sources=[0, 1], annotations=['distance'])

# York_Terrace_West, York_Square_Gardens, York_Rise_Estate_Gardens, York_Gardens, Yeading_Walk

data = response.json()
responseStatusCode = response.status_code
responseHeader = response.headers

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
    print(list_of_waypoints)

find_route_waypoints()



#
from pprint import pprint
# pprint(responseStatusCode)
pprint(responseHeader)
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
