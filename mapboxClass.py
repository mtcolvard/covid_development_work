from mapbox import DirectionsMatrix
from .locationsObject import Locations

origin = [-0.071132, 51.518891]
destination = [-0.091250, 51.505262]
service = DirectionsMatrix(access_token='pk.eyJ1IjoibXRjb2x2YXJkIiwiYSI6ImNrMDgzYndkZjBoanUzb21jaTkzajZjNWEifQ.ocEzAm8Y7a6im_FVc92HjQ')

allLocations = Locations.object.all()

response = service.matrix([origin, destination, York_Terrace_West, York_Square_Gardens, York_Rise_Estate_Gardens, York_Gardens, Yeading_Walk], profile='mapbox/walking', sources=[0], annotations=['distance'])

response.status_code

response.headers['Content-Type']
'application/json; charset=utf-8'

from pprint import pprint
pprint(response.json())


# def main():
