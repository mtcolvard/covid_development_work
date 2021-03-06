import math
from collections import deque

total_dict = {'origin': {'lon_lat': [-0.071136, 51.51887], 'crowflys_distance_and_bearing': {'from_origin': (0, 0)}}, 895: {'id': 895, 'name': 'Alwyne Square', 'lon_lat': [-0.096339847591415, 51.545740888868], 'crowflys_distance_and_bearing': {'from_origin': (3459.3318785356787, -0.5280120568528536), 'from_largest_park': (630.7407025699775, 1.919285734692207)}, 'distance_from_bestfit_line': {'origin_to_destination': 143.96661794302358, 'to_largest_park': 351.9274067893581, 'from_largest_park': 506.4874535464155}, 'size_in_hectares': 0.081}, 900: {'id': 900, 'name': "Annett's Crescent", 'lon_lat': [-0.093645125990251, 51.541200867613], 'crowflys_distance_and_bearing': {'from_origin': (2930.8930633454506, -0.5599329057019223), 'from_largest_park': (1061.0816819958143, 2.3168262177194916)}, 'distance_from_bestfit_line': {'origin_to_destination': 28.452835764200582, 'to_largest_park': 204.96057290425205, 'from_largest_park': 540.7809099960087}, 'size_in_hectares': 0.09}, 906: {'id': 906, 'name': 'Arlington Square', 'lon_lat': [-0.092467046844893, 51.534886945957], 'crowflys_distance_and_bearing': {'from_origin': (2312.9172293437077, -0.6917709241872393), 'from_largest_park': (1662.4795269595845, 2.597309691743875)}, 'distance_from_bestfit_line': {'origin_to_destination': 281.7747874050368, 'to_largest_park': 142.96226946017336, 'from_largest_park': 418.2188362726818}, 'size_in_hectares': 0.36}, 919: {'id': 919, 'name': 'Aske Gardens', 'lon_lat': [-0.08412343783119, 51.527556921105], 'crowflys_distance_and_bearing': {'from_origin': (1319.2477542651075, -0.7491740870349751), 'from_largest_park': (2659.5729583173647, 2.570258085230248)}, 'distance_from_bestfit_line': {'origin_to_destination': 235.5783608039522, 'to_largest_park': 156.9515711916467, 'from_largest_park': 738.4296785634264}, 'size_in_hectares': 0.0}, 924: {'id': 924, 'name': 'Aubert Court', 'lon_lat': [-0.10313503860268, 51.555742713728], 'crowflys_distance_and_bearing': {'from_origin': (4659.251370717976, -0.4947528189407305), 'from_largest_park': (905.1180772998833, 0.1362103007038773)}, 'distance_from_bestfit_line': {'origin_to_destination': 348.59664705534715, 'to_largest_park': 627.8671435792684, 'from_largest_park': 374.18667598060426}, 'size_in_hectares': 0.0}, 1040: {'id': 1040, 'name': 'Boundary Gardens *', 'lon_lat': [-0.075555186872678, 51.525618133595], 'crowflys_distance_and_bearing': {'from_origin': (810.2591106590513, -0.3868996676182817), 'from_largest_park': (3184.340895678464, 2.4499414239308197)}, 'distance_from_bestfit_line': {'origin_to_destination': 147.24507032191661, 'to_largest_park': 194.97783273359528, 'from_largest_park': 1244.9178284840798}, 'size_in_hectares': 0.2544}, 1133: {'id': 1133, 'name': 'Canonbury Square', 'lon_lat': [-0.10221709042268, 51.54313836629], 'crowflys_distance_and_bearing': {'from_origin': (3450.2805073040436, -0.6725298202814294), 'from_largest_park': (538.1249912761069, 2.7878346754367693)}, 'distance_from_bestfit_line': {'origin_to_destination': 354.3694072233426, 'to_largest_park': 146.96745934156138, 'from_largest_park': 34.29307270883705}, 'size_in_hectares': 0.24}, 1134: {'id': 1134, 'name': 'Canonbury Tower, Canonbury Estate', 'lon_lat': [-0.097856067313369, 51.543966982094], 'crowflys_distance_and_bearing': {'from_origin': (3347.2347504481836, -0.5848028531289031), 'from_largest_park': (639.0755160204033, 2.2727234802949425)}, 'distance_from_bestfit_line': {'origin_to_destination': 50.748455501080066, 'to_largest_park': 150.97022640444618, 'from_largest_park': 349.6304850566898}, 'size_in_hectares': 0.0}, 1178: {'id': 1178, 'name': 'Charles Square', 'lon_lat': [-0.085601812291904, 51.526681805717], 'crowflys_distance_and_bearing': {'from_origin': (1325.2108911842151, -0.8558955367745547), 'from_largest_park': (2689.73579520009, 2.621826012895372)}, 'distance_from_bestfit_line': {'origin_to_destination': 374.1881301345145, 'to_largest_park': 296.9215886009425, 'from_largest_park': 612.6200956810918}, 'size_in_hectares': 0.13}, 1221: {'id': 1221, 'name': 'Christ Church Highbury with St John and St Saviour', 'lon_lat': [-0.10040163556647, 51.552101486827], 'crowflys_distance_and_bearing': {'from_origin': (4213.276630831225, -0.5009500675762771), 'from_largest_park': (582.4162691494195, 0.5651454611969202)}, 'distance_from_bestfit_line': {'origin_to_destination': 289.18620830820447, 'to_largest_park': 541.8855912613891, 'from_largest_park': 439.5253052299479}, 'size_in_hectares': 0.0}, 1284: {'id': 1284, 'name': 'Compton Terrace Garden', 'lon_lat': [-0.10358355191767, 51.544958966906], 'crowflys_distance_and_bearing': {'from_origin': (3667.8577798030146, -0.6582731624626765), 'from_largest_park': (316.0270263840633, 2.846469121555866)}, 'distance_from_bestfit_line': {'origin_to_destination': 324.66482986134, 'to_largest_park': 103.9772968745068, 'from_largest_park': 1.6230230375375152}, 'size_in_hectares': 0.38}, 1568: {'id': 1568, 'name': 'Geffrye Museum Gardens', 'lon_lat': [-0.076768590395894, 51.531033573258], 'crowflys_distance_and_bearing': {'from_origin': (1407.5436794536267, -0.28047489582515095), 'from_largest_park': (2685.9268728065063, 2.3308121978458676)}, 'distance_from_bestfit_line': {'origin_to_destination': 401.3653258369772, 'to_largest_park': 481.91137196539677, 'from_largest_park': 1336.4308960730925}, 'size_in_hectares': 0.0}, 1647: {'id': 1647, 'name': 'Hackney Road Recreation Ground', 'lon_lat': [-0.07688220298944, 51.528337668669], 'crowflys_distance_and_bearing': {'from_origin': (1125.3185284238712, -0.3610321050426124), 'from_largest_park': (2895.4087742580177, 2.4077749953263035)}, 'distance_from_bestfit_line': {'origin_to_destination': 233.05247727602242, 'to_largest_park': 298.95273406104474, 'from_largest_park': 1243.2925915845694}, 'size_in_hectares': 0.2025}, 1744: {'id': 1744, 'name': 'Highbury Fields', 'lon_lat': [-0.10491278007282, 51.547678199045], 'crowflys_distance_and_bearing': {'from_origin': (3964.815941595679, -0.6299211285040349), 'from_largest_park': (0.0, 0.0)}, 'distance_from_bestfit_line': {'origin_to_destination': 238.8550386509668, 'to_largest_park': 0.0, 'from_largest_park': 0.0}, 'size_in_hectares': 11.75}, 1748: {'id': 1748, 'name': 'Highbury Roundabout and Highbury Corner Garden', 'lon_lat': [-0.10354618646758, 51.545857613343], 'crowflys_distance_and_bearing': {'from_origin': (3745.8280024928613, -0.6413982424599437), 'from_largest_park': (223.40993564033468, 2.704845839806117)}, 'distance_from_bestfit_line': {'origin_to_destination': 268.55980812620845, 'to_largest_park': 42.990351018136764, 'from_largest_park': 32.669851490206256}, 'size_in_hectares': 0.0}, 1810: {'id': 1810, 'name': 'Hoxton Square', 'lon_lat': [-0.082682760333115, 51.527533378947], 'crowflys_distance_and_bearing': {'from_origin': (1251.4704653980025, -0.6922625234486998), 'from_largest_park': (2716.8955459271106, 2.5399113115733734)}, 'distance_from_bestfit_line': {'origin_to_destination': 153.0729831560848, 'to_largest_park': 77.96788859261402, 'from_largest_park': 833.1931154476198}, 'size_in_hectares': 0.247}, 1811: {'id': 1811, 'name': 'Hoxton Trust Community Garden', 'lon_lat': [-0.081053155453814, 51.532003004746], 'crowflys_distance_and_bearing': {'from_origin': (1613.4621214610563, -0.4391444402477974), 'from_largest_park': (2400.2054031081375, 2.3833951386907213)}, 'distance_from_bestfit_line': {'origin_to_destination': 209.95411633900844, 'to_largest_park': 305.9471868739238, 'from_largest_park': 1083.1872542550018}, 'size_in_hectares': 0.0}, 1842: {'id': 1842, 'name': 'John Spencer Square', 'lon_lat': [-0.10070106726214, 51.544912331693], 'crowflys_distance_and_bearing': {'from_origin': (3545.1159372489797, -0.6146911536137517), 'from_largest_park': (423.5661546266649, 2.3833970599463457)}, 'distance_from_bestfit_line': {'origin_to_destination': 159.65412647039196, 'to_largest_park': 53.98993947067252, 'from_largest_park': 191.15018923210215}, 'size_in_hectares': 0.0}, 2051: {'id': 2051, 'name': 'Mark Street Garden', 'lon_lat': [-0.084274319440661, 51.523962363714], 'crowflys_distance_and_bearing': {'from_origin': (1070.9521182470698, -1.013602409768759), 'from_largest_park': (2998.648905402012, 2.6453038667635846)}, 'distance_from_bestfit_line': {'origin_to_destination': 459.9956082776117, 'to_largest_park': 400.89660050935834, 'from_largest_park': 614.2454393892679}, 'size_in_hectares': 0.0}, 2057: {'id': 2057, 'name': 'Marquess Estate', 'lon_lat': [-0.093457325647312, 51.545694075215], 'crowflys_distance_and_bearing': {'from_origin': (3358.635906237471, -0.4775159256806325), 'from_largest_park': (822.289473246916, 1.842351284092283)}, 'distance_from_bestfit_line': {'origin_to_destination': 308.97698157741263, 'to_largest_park': 509.89430909638986, 'from_largest_park': 696.0142710443022}, 'size_in_hectares': 0.0}, 2157: {'id': 2157, 'name': "New River Walk including Astey's Row Rock Gardens/Astey's Row Playground", 'lon_lat': [-0.093457325647312, 51.545694075215], 'crowflys_distance_and_bearing': {'from_origin': (3358.635906237471, -0.4775159256806325), 'from_largest_park': (822.289473246916, 1.842351284092283)}, 'distance_from_bestfit_line': {'origin_to_destination': 308.97698157741263, 'to_largest_park': 509.89430909638986, 'from_largest_park': 696.0142710443022}, 'size_in_hectares': 0.0}, 2325: {'id': 2325, 'name': 'Prebend Street Island', 'lon_lat': [-0.096714832552276, 51.536754454734], 'crowflys_distance_and_bearing': {'from_origin': (2661.9343386545097, -0.7269729198628601), 'from_largest_park': (1340.4595724067433, 2.704844347143383)}, 'distance_from_bestfit_line': {'origin_to_destination': 417.0816576072778, 'to_largest_park': 257.9401254704263, 'from_largest_park': 196.02108222711712}, 'size_in_hectares': 0.08}, 2451: {'id': 2451, 'name': 'Rosemary Gardens', 'lon_lat': [-0.089434695006163, 51.538434605974], 'crowflys_distance_and_bearing': {'from_origin': (2516.963482100055, -0.5268563631406364), 'from_largest_park': (1483.9765761905262, 2.335813831685815)}, 'distance_from_bestfit_line': {'origin_to_destination': 107.65442867021169, 'to_largest_park': 258.95123700175105, 'from_largest_park': 731.9315504052423}, 'size_in_hectares': 2.63}, 2522: {'id': 2522, 'name': 'Shoreditch Park', 'lon_lat': [-0.086741077265125, 51.533894432244], 'crowflys_distance_and_bearing': {'from_origin': (1989.095645242285, -0.5735915113666911), 'from_largest_park': (1982.0413255551598, 2.454679637614273)}, 'distance_from_bestfit_line': {'origin_to_destination': 7.857994783747947, 'to_largest_park': 111.98575193603776, 'from_largest_park': 766.22634074925}, 'size_in_hectares': 4.1}, 2667: {'id': 2667, 'name': 'St James Close and Clothworkers Almshouses', 'lon_lat': [-0.095236336036252, 51.537629707617], 'crowflys_distance_and_bearing': {'from_origin': (2670.3733674340588, -0.6741127667904466), 'from_largest_park': (1302.4034035164575, 2.6019127839108673)}, 'distance_from_bestfit_line': {'origin_to_destination': 278.47151598129557, 'to_largest_park': 117.96976798224924, 'from_largest_park': 321.83116166244935}, 'size_in_hectares': 0.0}, 2717: {'id': 2717, 'name': "St John's Garden", 'lon_lat': [-0.084010256091586, 51.530252837485], 'crowflys_distance_and_bearing': {'from_origin': (1547.6902939512752, -0.6131163456986846), 'from_largest_park': (2417.4840750708754, 2.5004517106097386)}, 'distance_from_bestfit_line': {'origin_to_destination': 67.26523079783026, 'to_largest_park': 26.007375115870655, 'from_largest_park': 831.5681313424468}, 'size_in_hectares': 0.405}, 2742: {'id': 2742, 'name': "St Leonard's Churchyard Garden", 'lon_lat': [-0.078398576235896, 51.526564010284], 'crowflys_distance_and_bearing': {'from_origin': (992.1765901319018, -0.5309903149903885), 'from_largest_park': (2979.1029859380824, 2.478309281617023)}, 'distance_from_bestfit_line': {'origin_to_destination': 38.33872261654564, 'to_largest_park': 97.99680038277992, 'from_largest_park': 1086.4371953359314}, 'size_in_hectares': 0.4}, 2783: {'id': 2783, 'name': 'St Mary Magdalene Gardens', 'lon_lat': [-0.10923678264256, 51.547747972772], 'crowflys_distance_and_bearing': {'from_origin': (4154.098033933704, -0.6869923914684215), 'from_largest_park': (299.09667664823644, -1.5448241450326252)}, 'distance_from_bestfit_line': {'origin_to_destination': 486.3712032130643, 'to_largest_park': 236.95094241192234, 'from_largest_park': 284.2909493093658}, 'size_in_hectares': 1.82}, 3107: {'id': 3107, 'name': 'Wilton Square', 'lon_lat': [-0.090950930538576, 51.536660786627], 'crowflys_distance_and_bearing': {'from_origin': (2406.7499436093053, -0.6058221869063969), 'from_largest_park': (1559.843317084427, 2.474021677597637)}, 'distance_from_bestfit_line': {'origin_to_destination': 87.0601568697888, 'to_largest_park': 57.99451247841599, 'from_largest_park': 575.0751873145114}, 'size_in_hectares': 0.13}, 3221: {'id': 3221, 'name': 'Wilton Square', 'lon_lat': [-0.08977332106377, 51.537235121809], 'crowflys_distance_and_bearing': {'from_origin': (2415.0517401998686, -0.5630269193740636), 'from_largest_park': (1563.5218906629216, 2.4077763369155707)}, 'distance_from_bestfit_line': {'origin_to_destination': 15.97314515075043, 'to_largest_park': 161.4325159659568, 'from_largest_park': 671.3765999923161}, 'size_in_hectares': 0.13}, 'destination': {'lon_lat': [-0.108486, 51.5551235], 'crowflys_distance_and_bearing': {'from_origin': (4787.899034325837, -0.5696409646736258)}}}



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

def filter_by_angle():
    waypoints_lon_lat = {k:v['lon_lat'] for k, v in total_dict.items()}
    waypoint_ids = list(total_dict.keys())
    waypoint_ids.pop()
    unprocessed_waypoints = deque(list(total_dict.keys()))
    unprocessed_waypoints.popleft()
    filtered_waypoints = {}
    for waypoint_id in waypoint_ids:
        filtered_waypoints[waypoint_id] = {}
        for next_id in unprocessed_waypoints:
            filtered_waypoints[waypoint_id][next_id] = crowflys_bearing(waypoints_lon_lat[waypoint_id], waypoints_lon_lat[next_id])[1]
        unprocessed_waypoints.popleft()

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
    backtrace_dijkstra_path()
    return waypoints_costs[graph_nodes[-1]]

def backtrace_dijkstra_path():
    dijkstra_path = []
    waypoint = waypoints_parents[graph_nodes[-1]]
    while waypoint is not graph_nodes[0]:
        dijkstra_path.append(waypoint)
        waypoint = waypoints_parents[dijkstra_path[-1]]
    dijkstra_path.reverse()
    print(dijkstra_path)
    return dijkstra_path

# run_dijkstra()
