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


service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

response = service.matrix([origin, destination, York_Terrace_West, York_Square_Gardens, York_Rise_Estate_Gardens, York_Gardens, Yeading_Walk], profile='mapbox/walking', sources=[0, 1], annotations=['distance'])


response.headers['Content-Type']
'application/json; charset=utf-8'

data = response.json()
statusCode = response.status_code
header = response.headers

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
# pprint(statusCode)
# pprint(response.json()['distances'][0])
# pprint(distances_from_origin)




# def main():
