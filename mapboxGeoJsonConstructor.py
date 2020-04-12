# import mapbox
# import pydash

origin = [-0.071132, 51.518891]
collection_one = {
"Albert Gardens"	:(-0.048721755995117,51.51258512161),

"Alderney Road Cemetery"	:(-0.045418257473052,51.522421981895),

"All Saints Churchyard, Poplar"	:(-0.01279619151928,51.510183314858),

"Altab Ali Park"	:(-0.068770393713962,51.515614772134),

"Bancroft Road Cemetery"	:(-0.045302810969366,51.525117839052),

"Bethnal Green Gardens"	:(-0.055348551291013,51.526184094351),

"Boundary Gardens *"	:(-0.075555186872678,51.525618133595),

"Bow Churchyard"	:(-0.017776262243614,51.528252888321),

"Brady Street Cemetery"	:(-0.061301863303676,51.521786360354),

"Bromley Recreation Ground"	:(-0.013532569137843,51.526382561487),

"Ford Square Gardens"	:(-0.05720990921333,51.516323089494),

"Globe Road Open Space"	:(-0.051065100867099,51.525213734392),

"Grove Hall Park"	:(-0.019177902823842,51.529175831881),

"Holy Trinity Church Graveyard"	:(-0.035102821248716,51.527645181073),

"Ion Square Gardens"	:(-0.066721235716513,51.529969137313),

"King Edward Memorial Park"	:(-0.050315406539387,51.509014581232),

"Lady Jane Mico's Almshouses"	:(-0.041366715819842,51.516059558877),

"Meath Gardens"	:(-0.045225836659679,51.526915076361),

"Mercers Burial Ground"	:(-0.041443812107358,51.51426232236
),
"Mile End Road Verges"	:(-0.055616524858349,51.519893722332),

"Millwall Park"	:(-0.010855329562293,51.488567979003),

"Museum Gardens *"	:(-0.055271969554349,51.527981342069),

"Paradise Gardens *"	:(-0.056712637941541,51.528005220953),

"Poplar Park"	:(-0.017116408507303,51.510256445333),

"Queen's Building Forecourt, Queen Mary, University of London"	:(-0.041096815873977,51.522349881668),

"Rectory Gardens"	:(-0.032918650586594,51.511421844157),

"Sephardi Nuevo (New) Cemetery *"	:(-0.039579150441387,51.524123045013),

"Sephardi Velho (Old) Cemetery"	:(-0.045418257473052,51.522421981895),

"Shandy Park"	:(-0.041212499269476,51.519654029999),

"St Anne's Churchyard, Limehouse"	:(-0.03147852577133,51.511397678601),

"St Dunstan's Churchyard, Stepney"	:(-0.042806996167133,51.516083604578),

"St George's-in-the-East Churchyard"	:(-0.060395909406252,51.509181744854),

"St James's Gardens"	:(-0.041597980712523,51.510667847417),

"St John's Gardens"	:(-0.062064781654964,51.503813771304),

"St Leonardâ€™s Priory"	:(-0.013454340529617,51.528179764083),

"St Mary's Additional Burial Ground"	:(-0.064335241794335,51.518239429505),

"St Matthias Churchyard"	:(-0.017155426711002,51.509357839359),

"St Paul's Churchyard, Shadwell"	:(-0.053195540296469,51.509062430618),

"St Peter's Churchyard"	:(-0.065280496813107,51.529945380685),

"Stepney City Farm and Rural Arts Centre"	:(-0.044208783987261,51.517006252163),

"Stepney Green Gardens"	:(-0.048452902742563,51.518875475744),

"Stepney Green Park and Stepney Clocktower"	:(-0.047050971377665,51.517952877664)
}

class ConstructGeoJson:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        geo_json_item = {'type': 'Feature',
                            'properties': {'name': self.name},
                            'geometry': {'type': 'Point',
                                        'coordinates': self.coordinates}}
        print(str("_".join(self.name.split())), ' = ', geo_json_item, ',')

def populate_constructor():
    for item in collection_one.items():
        geo_json_builder = ConstructGeoJson(item[0], item[1])
        # return geo_json_builder

def create_list_names():
    list_names = []
    for item in collection_one.items():
        names = list_names.append(item[0])
    print(list_names)
    # x = collection_one.keys()
    # print(x)
    # print(y.replace("'",""))

def main():
    populate_constructor()
    # create_list_names()


if __name__ == "__main__":
    main()
