Help on class Geocoder in module mapbox.services.geocoding:

class Geocoder(mapbox.services.base.Service)
 |  Geocoder(name='mapbox.places', access_token=None, cache=None, host=None)
 |
 |  Access to the Geocoding API V5
 |
 |  Method resolution order:
 |      Geocoder
 |      mapbox.services.base.Service
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, name='mapbox.places', access_token=None, cache=None, host=None)
 |      Constructs a Geocoding Service object.
 |
 |      :param name: name of a geocoding dataset.
 |      :param access_token: Mapbox access token string.
 |      :param cache: CacheControl cache instance (Dict or FileCache).
 |
 |  forward(self, address, types=None, lon=None, lat=None, country=None, bbox=None, limit=None, languages=None)
 |      Returns a Requests response object that contains a GeoJSON
 |      collection of places matching the given address.
 |
 |      `response.geojson()` returns the geocoding result as GeoJSON.
 |      `response.status_code` returns the HTTP API status code.
 |
 |      Place results may be constrained to those of one or more types
 |      or be biased toward a given longitude and latitude.
 |
 |      See: https://www.mapbox.com/api-documentation/search/#geocoding.
 |
 |  reverse(self, lon, lat, types=None, limit=None)
 |      Returns a Requests response object that contains a GeoJSON
 |      collection of places near the given longitude and latitude.
 |
 |      `response.geojson()` returns the geocoding result as GeoJSON.
 |      `response.status_code` returns the HTTP API status code.
 |
 |      See: https://www.mapbox.com/api-documentation/search/#reverse-geocoding.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  country_codes
 |      A list of valid country codes
 |
 |  place_types
 |      A mapping of place type names to descriptions

 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  api_name = 'geocoding'
 |
 |  api_version = 'v5'
 |
 |  precision = {'proximity': 3, 'reverse': 5}
 |
 |  ----------------------------------------------------------------------
 |  ----------------------------------------------------------------------
 |  Methods inherited from mapbox.services.base.Service:
 |
 |  handle_http_error(self, response, custom_messages=None, raise_for_status=False)
 |      Converts service errors to Python exceptions
 |
 |      Parameters
 |      ----------
 |      response : requests.Response
 |          A service response.
 |      custom_messages : dict, optional
 |          A mapping of custom exception messages to HTTP status codes.
 |      raise_for_status : bool, optional
 |          If True, the requests library provides Python exceptions.
 |
 |      Returns
 |      -------
 |      None
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from mapbox.services.base.Service:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  baseuri
 |      The service's base URI
 |
 |      Returns
 |      -------
 |      str
 |
 |  username
 |      The username in the service's access token
 |
 |      Returns
 |      -------
 |      str
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from mapbox.services.base.Service:
 |
 |  default_host = 'api.mapbox.com'
