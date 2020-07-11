import math

total_dict = {2742: {'id': 2742, 'name': "St Leonard's Churchyard Garden", 'lon_lat': [-0.078398576235896, 51.526564010284], 'crowflys_distance_and_bearing': {'from_origin': (992.1765901319018, -0.5309903149903885), 'from_largest_park': (2979.1029859380824, 2.478309281617023)}, 'distance_from_bestfit_line': {'origin_to_destination': 38.33872261654564, 'to_largest_park': 97.99680038277992, 'from_largest_park': 1086.4371953359314}, 'size_in_hectares': 0.4}, 1810: {'id': 1810, 'name': 'Hoxton Square', 'lon_lat': [-0.082682760333115, 51.527533378947], 'crowflys_distance_and_bearing': {'from_origin': (1251.4704653980025, -0.6922625234486998), 'from_largest_park': (2716.8955459271106, 2.5399113115733734)}, 'distance_from_bestfit_line': {'origin_to_destination': 153.0729831560848, 'to_largest_park': 77.96788859261402, 'from_largest_park': 833.1931154476198}, 'size_in_hectares': 0.247}, 919: {'id': 919, 'name': 'Aske Gardens', 'lon_lat': [-0.08412343783119, 51.527556921105], 'crowflys_distance_and_bearing': {'from_origin': (1319.2477542651075, -0.7491740870349751), 'from_largest_park': (2659.5729583173647, 2.570258085230248)}, 'distance_from_bestfit_line': {'origin_to_destination': 235.5783608039522, 'to_largest_park': 156.9515711916467, 'from_largest_park': 738.4296785634264}, 'size_in_hectares': 0.0}, 2717: {'id': 2717, 'name': "St John's Garden", 'lon_lat': [-0.084010256091586, 51.530252837485], 'crowflys_distance_and_bearing': {'from_origin': (1547.6902939512752, -0.6131163456986846), 'from_largest_park': (2417.4840750708754, 2.5004517106097386)}, 'distance_from_bestfit_line': {'origin_to_destination': 67.26523079783026, 'to_largest_park': 26.007375115870655, 'from_largest_park': 831.5681313424468}, 'size_in_hectares': 0.405}, 2522: {'id': 2522, 'name': 'Shoreditch Park', 'lon_lat': [-0.086741077265125, 51.533894432244], 'crowflys_distance_and_bearing': {'from_origin': (1989.095645242285, -0.5735915113666911), 'from_largest_park': (1982.0413255551598, 2.454679637614273)}, 'distance_from_bestfit_line': {'origin_to_destination': 7.857994783747947, 'to_largest_park': 111.98575193603776, 'from_largest_park': 766.22634074925}, 'size_in_hectares': 4.1}, 906: {'id': 906, 'name': 'Arlington Square', 'lon_lat': [-0.092467046844893, 51.534886945957], 'crowflys_distance_and_bearing': {'from_origin': (2312.9172293437077, -0.6917709241872393), 'from_largest_park': (1662.4795269595845, 2.597309691743875)}, 'distance_from_bestfit_line': {'origin_to_destination': 281.7747874050368, 'to_largest_park': 142.96226946017336, 'from_largest_park': 418.2188362726818}, 'size_in_hectares': 0.36}, 3107: {'id': 3107, 'name': 'Wilton Square', 'lon_lat': [-0.090950930538576, 51.536660786627], 'crowflys_distance_and_bearing': {'from_origin': (2406.7499436093053, -0.6058221869063969), 'from_largest_park': (1559.843317084427, 2.474021677597637)}, 'distance_from_bestfit_line': {'origin_to_destination': 87.0601568697888, 'to_largest_park': 57.99451247841599, 'from_largest_park': 575.0751873145114}, 'size_in_hectares': 0.13}, 3221: {'id': 3221, 'name': 'Wilton Square', 'lon_lat': [-0.08977332106377, 51.537235121809], 'crowflys_distance_and_bearing': {'from_origin': (2415.0517401998686, -0.5630269193740636), 'from_largest_park': (1563.5218906629216, 2.4077763369155707)}, 'distance_from_bestfit_line': {'origin_to_destination': 15.97314515075043, 'to_largest_park': 161.4325159659568, 'from_largest_park': 671.3765999923161}, 'size_in_hectares': 0.13}, 2667: {'id': 2667, 'name': 'St James Close and Clothworkers Almshouses', 'lon_lat': [-0.095236336036252, 51.537629707617], 'crowflys_distance_and_bearing': {'from_origin': (2670.3733674340588, -0.6741127667904466), 'from_largest_park': (1302.4034035164575, 2.6019127839108673)}, 'distance_from_bestfit_line': {'origin_to_destination': 278.47151598129557, 'to_largest_park': 117.96976798224924, 'from_largest_park': 321.83116166244935}, 'size_in_hectares': 0.0}, 1134: {'id': 1134, 'name': 'Canonbury Tower, Canonbury Estate', 'lon_lat': [-0.097856067313369, 51.543966982094], 'crowflys_distance_and_bearing': {'from_origin': (3347.2347504481836, -0.5848028531289031), 'from_largest_park': (639.0755160204033, 2.2727234802949425)}, 'distance_from_bestfit_line': {'origin_to_destination': 50.748455501080066, 'to_largest_park': 150.97022640444618, 'from_largest_park': 349.6304850566898}, 'size_in_hectares': 0.0}, 1133: {'id': 1133, 'name': 'Canonbury Square', 'lon_lat': [-0.10221709042268, 51.54313836629], 'crowflys_distance_and_bearing': {'from_origin': (3450.2805073040436, -0.6725298202814294), 'from_largest_park': (538.1249912761069, 2.7878346754367693)}, 'distance_from_bestfit_line': {'origin_to_destination': 354.3694072233426, 'to_largest_park': 146.96745934156138, 'from_largest_park': 34.29307270883705}, 'size_in_hectares': 0.24}, 1842: {'id': 1842, 'name': 'John Spencer Square', 'lon_lat': [-0.10070106726214, 51.544912331693], 'crowflys_distance_and_bearing': {'from_origin': (3545.1159372489797, -0.6146911536137517), 'from_largest_park': (423.5661546266649, 2.3833970599463457)}, 'distance_from_bestfit_line': {'origin_to_destination': 159.65412647039196, 'to_largest_park': 53.98993947067252, 'from_largest_park': 191.15018923210215}, 'size_in_hectares': 0.0}, 1284: {'id': 1284, 'name': 'Compton Terrace Garden', 'lon_lat': [-0.10358355191767, 51.544958966906], 'crowflys_distance_and_bearing': {'from_origin': (3667.8577798030146, -0.6582731624626765), 'from_largest_park': (316.0270263840633, 2.846469121555866)}, 'distance_from_bestfit_line': {'origin_to_destination': 324.66482986134, 'to_largest_park': 103.9772968745068, 'from_largest_park': 1.6230230375375152}, 'size_in_hectares': 0.38}, 1748: {'id': 1748, 'name': 'Highbury Roundabout and Highbury Corner Garden', 'lon_lat': [-0.10354618646758, 51.545857613343], 'crowflys_distance_and_bearing': {'from_origin': (3745.8280024928613, -0.6413982424599437), 'from_largest_park': (223.40993564033468, 2.704845839806117)}, 'distance_from_bestfit_line': {'origin_to_destination': 268.55980812620845, 'to_largest_park': 42.990351018136764, 'from_largest_park': 32.669851490206256}, 'size_in_hectares': 0.0}, 1744: {'id': 1744, 'name': 'Highbury Fields', 'lon_lat': [-0.10491278007282, 51.547678199045], 'crowflys_distance_and_bearing': {'from_origin': (3964.815941595679, -0.6299211285040349), 'from_largest_park': (0.0, 0.0)}, 'distance_from_bestfit_line': {'origin_to_destination': 238.8550386509668, 'to_largest_park': 0.0, 'from_largest_park': 0.0}, 'size_in_hectares': 11.75}}

{2742: {1810: [-0.082682760333115, 51.527533378947], 919: [-0.08412343783119, 51.527556921105], 2717: [-0.084010256091586, 51.530252837485]},
 1810: {919: [-0.08412343783119, 51.527556921105], 2717: [-0.084010256091586, 51.530252837485], 2522: [-0.086741077265125, 51.533894432244]},
  919: {2717: [-0.084010256091586, 51.530252837485], 2522: [-0.086741077265125, 51.533894432244], 906: [-0.092467046844893, 51.534886945957]},
   2717: {2522: [-0.086741077265125, 51.533894432244], 906: [-0.092467046844893, 51.534886945957], 3107: [-0.090950930538576, 51.536660786627]},
    2522: {906: [-0.092467046844893, 51.534886945957], 3107: [-0.090950930538576, 51.536660786627], 3221: [-0.08977332106377, 51.537235121809]},
     906: {3107: [-0.090950930538576, 51.536660786627], 3221: [-0.08977332106377, 51.537235121809], 2667: [-0.095236336036252, 51.537629707617]},
      3107: {3221: [-0.08977332106377, 51.537235121809], 2667: [-0.095236336036252, 51.537629707617], 1134: [-0.097856067313369, 51.543966982094]},
       3221: {2667: [-0.095236336036252, 51.537629707617], 1134: [-0.097856067313369, 51.543966982094], 1133: [-0.10221709042268, 51.54313836629]},
        2667: {1134: [-0.097856067313369, 51.543966982094], 1133: [-0.10221709042268, 51.54313836629], 1842: [-0.10070106726214, 51.544912331693]},
         1134: {1133: [-0.10221709042268, 51.54313836629], 1842: [-0.10070106726214, 51.544912331693], 1284: [-0.10358355191767, 51.544958966906]},
          1133: {1842: [-0.10070106726214, 51.544912331693], 1284: [-0.10358355191767, 51.544958966906], 1748: [-0.10354618646758, 51.545857613343]},
1842: {1284: [-0.10358355191767, 51.544958966906], 1748: [-0.10354618646758, 51.545857613343], 1744: [-0.10491278007282, 51.547678199045]},
1284: {1748: [-0.10354618646758, 51.545857613343], 1744: [-0.10491278007282, 51.547678199045]},
1748: {1748: [-0.10354618646758, 51.545857613343], 1744: [-0.10491278007282, 51.547678199045]},
              1744: {1748: [-0.10354618646758, 51.545857613343], 1744: [-0.10491278007282, 51.547678199045]}}


def crowflys_bearing(startpoint, endpoint):

    startpoint_lon = startpoint[0]
    startpoint_lat = startpoint[1]
    endpoint_lon = endpoint[0]
    endpoint_lat = endpoint[1]

    R = 6371000
    φ1 = startpoint_lat * math.pi/180
    φ2 = endpoint_lat * math.pi/180
    Δφ = (endpoint_lat - startpoint_lat) * math.pi/180
    Δλ = (endpoint_lon - startpoint_lon) * math.pi/180

    # CROWFLYS
    a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    crowflys = R * c

    # BEARING
    y = math.sin(Δλ) * math.cos(φ2)
    x = math.cos(φ1)*math.sin(φ2) - math.sin(φ1)*math.cos(φ2)*math.cos(Δλ)
    θ = math.atan2(y, x)
    bearing = (θ*180/math.pi + 360) % 360
    return crowflys, θ

graph_nodes = list(total_dict.keys())
infinity = float('inf')
waypoints_graph = {}
waypoints_costs = {}
waypoints_parents = {}
waypoints_processed = []

def create_waypoints_graph():
    count = 0
    for element in graph_nodes[1:]:
        waypoints_costs[element] = infinity
        waypoints_parents[element] = None
    for node in graph_nodes:
        waypoints_graph[node] = {}
        if len(graph_nodes) -3 > count:
            waypoints_graph[node][graph_nodes[count + 1]] = total_dict[graph_nodes[count + 1]]['lon_lat']
            waypoints_graph[node][graph_nodes[count + 2]] = total_dict[graph_nodes[count + 2]]['lon_lat']
            waypoints_graph[node][graph_nodes[count + 3]] = total_dict[graph_nodes[count + 3]]['lon_lat']
            count = count + 1
        elif len(graph_nodes) - 2 > count:
            waypoints_graph[node][graph_nodes[count + 1]] = total_dict[graph_nodes[count + 1]]['lon_lat']
            waypoints_graph[node][graph_nodes[count + 2]] = total_dict[graph_nodes[count + 2]]['lon_lat']
            count = count + 1
        elif len(graph_nodes) - 1 > count:
            waypoints_graph[node][graph_nodes[count + 1]] = total_dict[graph_nodes[count + 1]]['lon_lat']
            count = count + 1
    return waypoints_graph, waypoints_costs, waypoints_parents

def populate_waypoints_graph_distances():
    create_waypoints_graph()
    for k, v in waypoints_graph.items():
        for key, value in v.items():
            dist_from_current_waypoint_coord = crowflys_bearing(total_dict[k]['lon_lat'], value)[0]
            v.update({key: dist_from_current_waypoint_coord})

    waypoints_costs[graph_nodes[1]] = waypoints_graph[graph_nodes[0]][graph_nodes[1]]
    waypoints_costs[graph_nodes[2]] = waypoints_graph[graph_nodes[0]][graph_nodes[2]]
    waypoints_costs[graph_nodes[3]] = waypoints_graph[graph_nodes[0]][graph_nodes[3]]
    waypoints_parents[graph_nodes[1]] = graph_nodes[0]
    waypoints_parents[graph_nodes[2]] = graph_nodes[0]
    waypoints_parents[graph_nodes[3]] = graph_nodes[0]

    print(waypoints_graph, waypoints_costs, waypoints_parents)
    return waypoints_graph, waypoints_costs, waypoints_parents

def find_lowest_cost_node():
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in waypoints_costs:
        cost = waypoints_costs[node]
        if cost < lowest_cost and node not in waypoints_processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def run_dijkstra():
    populate_waypoints_graph_distances()
    node = find_lowest_cost_node()
    while node is not None:
        cost = waypoints_costs[node]
        neighbors = waypoints_graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if waypoints_costs[n] > new_cost:
                waypoints_costs[n] = new_cost
                waypoints_parents[n] = node
        waypoints_processed.append(node)
        node = find_lowest_cost_node()
    print(waypoints_parents)
    trace_dijkstra_path()
    return waypoints_costs[graph_nodes[-1]]

def trace_dijkstra_path():
    path = []
    waypoint = waypoints_parents[graph_nodes[-1]]
    while waypoint is not graph_nodes[0]:
        path.append(waypoint)
        waypoint = waypoints_parents[path[-1]]
    print(path)
    return path

run_dijkstra()
