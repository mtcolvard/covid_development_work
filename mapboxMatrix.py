import mapbox
import pydash

origin = [-0.071132, 51.518891]
collection_one = {'York Terrace West':[-0.150578775,51.52412738]
,
'York Square Gardens':[-0.040042164,51.51333964],
'York Rise Estate Gardens':[-0.143500164,51.55638842],
'York House Gardens *':[-0.323488655,51.44759367],
'York Gardens':[-0.177365387,51.46699476],
'Yeading Walk':[-0.367516667,51.58489741],
'Yardley Recreation Ground':[-0.228778185,51.36616707],
'Yalta Memorial Garden':[-0.17481463,51.49483187],
'Wyck Gardens':[-0.105685898,51.4595636],
'WWT London Wetland Centre':[-0.236013033,51.47688433],
'Wrythe Recreation Ground':[-0.174007434,51.37072169],
'Wrythe Green':[-0.166756541,51.37240698],
'Wormwood Scrubs including Old Oak Common':[-0.235717844,51.52184199],
'Wormholt Park':[-0.239049728,51.51020195],
'Wormholt Estate':[-0.243301365,51.51206419],
'World\'s End Estate':[-0.17845059,51.48131873],
'Woolwich Common and Royal Artillery Barracks':[0.053470899,51.47756693],
'Woolwich Cemetery (Old and New)':[0.096639447,51.47680282],
'Wool House Garden':[-0.135466095,51.50590308],
'Woodside Park':[-0.111252444,51.60353366]
}

class ConstructGeoJson:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        geo_json_item = {'type': 'Feature',
                            'properties': {'name': self.name},
                            'geometry': {'type': 'Point',
                                        'coordinates': self.coordinates}}
        print(str("_".join(self.name.split())), ' = ', geo_json_item)

def populate_constructor():
    for item in collection_one.items():
        geo_json_builder = ConstructGeoJson(item[0], item[1])

def main():
    # populate_constructor()
    help(mapbox.DirectionsMatrix)
    
if __name__ == "__main__":
    main()
