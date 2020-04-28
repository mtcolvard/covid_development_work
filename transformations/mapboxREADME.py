class DirectionsMatrix(mapbox.services.base.Service)
 |  DirectionsMatrix(access_token=None, host=None, cache=None)
 |
 |  Access to the Matrix API V1
 |
 |  Method resolution order:
 |      DirectionsMatrix
 |      mapbox.services.base.Service
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  matrix(self, coordinates, profile='mapbox/driving', sources=None, destinations=None, annotations=None)
 |      Request a directions matrix for trips between coordinates
 |
 |      In the default case, the matrix returns a symmetric matrix,
 |      using all input coordinates as sources and destinations. You may
 |      also generate an asymmetric matrix, with only some coordinates
 |      as sources or destinations:
 |
 |      Parameters
 |      ----------
 |      coordinates : sequence
 |          A sequence of coordinates, which may be represented as
 |          GeoJSON features, GeoJSON geometries, or (longitude,
 |          latitude) pairs.
 |      profile : str
 |          The trip travel mode. Valid modes are listed in the class's
 |          valid_profiles attribute.
 |      annotations : list
 |          Used to specify the resulting matrices. Possible values are
 |          listed in the class's valid_annotations attribute.
 |      sources : list
 |          Indices of source coordinates to include in the matrix.
 |          Default is all coordinates.
 |      destinations : list
 |          Indices of destination coordinates to include in the
 |          matrix. Default is all coordinates.
 |
Returns
 |      -------
 |      requests.Response
 |
 |      Note: the directions matrix itself is obtained by calling the
 |      response's json() method. The resulting mapping has a code,
 |      the destinations and the sources, and depending of the
 |      annotations specified, it can also contain a durations matrix,
 |      a distances matrix or both of them (by default, only the
 |      durations matrix is provided).
 |
 |      code : str
 |          Status of the response
 |      sources : list
 |          Results of snapping selected coordinates to the nearest
 |          addresses.
 |      destinations : list
 |          Results of snapping selected coordinates to the nearest
 |          addresses.
 |      durations : list
 |          An array of arrays representing the matrix in row-major
 |          order.  durations[i][j] gives the travel time from the i-th
 |          source to the j-th destination. All values are in seconds.
 |          The duration between the same coordinate is always 0. If
 |          a duration can not be found, the result is null.
 |      distances : list
 |          An array of arrays representing the matrix in row-major
 |          order.  distances[i][j] gives the distance from the i-th
 |          source to the j-th destination. All values are in meters.
 |          The distance between the same coordinate is always 0. If
 |          a distance can not be found, the result is null.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  baseuri
 |      The service's base URI
 |
 |      Returns
 |      -------
 |      str
 |
----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  api_name = 'directions-matrix'
 |
 |  api_version = 'v1'
 |
 |  valid_annotations = ['duration', 'distance']
 |
 |  valid_profiles = ['mapbox/driving', 'mapbox/cycling', 'mapbox/walking'...
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from mapbox.services.base.Service:
 |
 |  __init__(self, access_token=None, host=None, cache=None)
 |      Constructs a Service object
 |
 |      This method should be overridden by subclasses.
 |
 |      Parameters
 |      ----------
 |      access_token : str
 |          Mapbox access token string.
 |      host : str, optional
 |          Mapbox API host (advanced usage only).
 |      cache : CacheControl cache instance (Dict or FileCache), optional
 |          Optional caching, not generally needed.
 |
 |      Returns
 |      -------
 |      Service
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
(END)
