from mapbox import Directions

# class mapbox.services.matrix.DirectionsMatrix(access_token=None, host=None, cache=None)
# Bases: mapbox.services.base.Service
#
# Access to the Matrix API V1
#
# Attributes:
# baseuri
# The service’s base URI
#
# username
# The username in the service’s access token
origin = [17.06009, 51.13386]


class DirectionsMatrix:
    def __init__(self, name):
        self.name = name


    def matrix(self, coordinates, profile='mapbox/driving', sources=None, destinations=None, annotations=None):
        c

# def main():
