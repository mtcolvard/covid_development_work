# UPDATE ITEMS IN A dictionary
temp_coords_list = {866: '-0.084613688708361,51.515874600322', 910: '-0.088671282889504,51.522235590909', 1095: '-0.090074197976318,51.523157700738', 1350: '-0.078814649948071,51.516679002793', 1369: '-0.080292766543172,51.515803950192', 1385: '-0.087494313257733,51.515921612032', 1518: '-0.087419024791445,51.517718896902', 1521: '-0.087306077458283,51.520414823021', 1850: '-0.080292766543172,51.515803950192', 2003: '-0.090337358976231,51.516867197055', 2629: '-0.083173379363984,51.515851067954', 2643: '-0.083211105598963,51.514952427538', 2767: '-0.081770826519204,51.514928878248'}

temp_coords_list.update((x, y.split(',')) for x, y in temp_coords_list.items())