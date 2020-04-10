from mapbox import DirectionsMatrix

origin = [17.06009, 51.13386]

service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

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

response = service.matrix([York_Terrace_West, York_Square_Gardens, York_Rise_Estate_Gardens, York_Gardens, Yeading_Walk], profile='mapbox/walking')

response.status_code

response.headers['Content-Type']
'application/json; charset=utf-8'

from pprint import pprint
pprint(response.json())


# def main():
