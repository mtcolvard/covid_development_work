import math
import mapbox; help(mapbox.DirectionsMatrix)
# # pride of spitalfields
# origin = [-0.071132, 51.518891]
# # hackney marshes
# destination = [-0.033834, 51.558065]
origin = [17.06009, 51.13386]
destination = [17.06009, 52.34473 ]
earth_radius = 6371.1
bb_width = 2.53
midpoint = []


class FindClosestPark:
    def __init__(self, lon_orig, lat_orig, lon_dest, lat_dest):
        self.lon_orig = math.radians(lon_orig)
        self.lat_orig = math.radians(lat_orig)
        self.lon_dest = math.radians(lon_dest)
        self.lat_dest = math.radians(lat_dest)

    def find_dist(self):
        global dist
        dist = math.acos(math.sin(self.lat_orig) * math.sin(self.lat_dest) + math.cos(self.lat_orig) * math.cos(self.lat_dest) * math.cos(self.lon_orig - self.lon_dest)) * earth_radius
        print(dist)
        return dist

        # d = acos( sin φ1 ⋅ sin φ2 + cos φ1 ⋅ cos φ2 ⋅ cos Δλ ) ⋅ R


    def find_midpoint(self):
        global midpoint, midpoint_deg
        Bx = math.cos(self.lat_dest) * math.cos(self.lon_dest - self.lon_orig)
        By = math.cos(self.lat_dest) * math.sin(self.lon_dest - self.lon_orig)
        lat_mid = math.atan2((math.sin(self.lat_orig)+math.sin(self.lat_dest)),
                math.sqrt(math.pow((math.cos(self.lat_orig)+Bx),2)+math.pow(By,2)))

        lon_mid = self.lon_orig + math.atan2(By, math.cos(self.lat_orig)+Bx)
        midpoint_deg = []
        midpoint = [lon_mid, lat_mid]
        midpoint_deg = [math.degrees(point) for point in midpoint]
        midpoint_deg.reverse()
        return midpoint

    def define_bbox(self):
        global bb_lon_min, bb_lat_min, bb_lon_max, bb_lat_max, bb_box, bb_box_deg
        # boundary box angular radius
        # bb_ang_rad = bb_width/earth_radius
        bb_ang_rad = dist/2/earth_radius
        bb_lat_min = midpoint[1] - bb_ang_rad
        bb_lat_max = midpoint[1] + bb_ang_rad
        bb_latT = math.asin(math.sin(midpoint[1])/math.cos(bb_ang_rad))
        bb_lon_delta = math.acos((math.cos(bb_ang_rad)-math.sin(bb_latT)*math.sin(midpoint[1]))/(math.cos(bb_latT)*math.cos(midpoint[1])))

        bb_lon_min = midpoint[0] - bb_lon_delta
        bb_lon_max = midpoint[0] + bb_lon_delta
        bb_box = [bb_lon_min, bb_lat_max, bb_lon_max, bb_lat_min]
        bb_box_deg = [math.degrees(point) for point in bb_box]
        bb_box_deg.reverse()
        origin.reverse()
        destination.reverse()
        print(origin + destination + midpoint_deg + bb_box_deg)

        return bb_lon_min, bb_lat_min, bb_lon_max, bb_lat_max

    # def create_dict(self):
    #     list_coords = origin + destination + midpoint_deg + bb_box_deg
    #     for
    #     print(list_coords)


def main():
    query1 = FindClosestPark(origin[0], origin[1], destination[0], destination[1])
    query1.find_dist()
    query1.find_midpoint()
    query1.define_bbox()
    # query1.create_dict()
    # print(origin + destination + midpoint_deg + bb_box_deg)


if __name__ == "__main__":
    main()

# _____________________________
# import re
# help(sort)

#

# # import re
# def printer_error(s):
#     type1 = re.compile('[m-z]')
#     type2 = type1.findall(s)
#     type3 = len(s)
#     type4 = len(type2)
#     type5 = str(type4)+'/'+str(type3)
#     return type5
#
# import re
# def printer_error(s):
#     type1 = re.compile('[n-z]')
#     type5 = str(len(type1.findall(s)))+'/'+str(len(s))
#     print(type5)
#     return type5
#
# printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz')
#
# # import re
# # def order(sentence):
#     # if sentence == '':
#     #     return ''
#     # type1 = re.split('\W+', sentence)
#     # type2 = 1
#     # type4 = []
#     # seperator = ' '
#     # for i in type1:
#     #     type3 = [i for i in type1 if str(type2) in i]
#     #     type4.append(type3.pop())
#     #     type2 = type2 + 1
#     # print(seperator.join(type4))
#     # return seperator.join(type4)
# #     print(sorted(sentence.split()))
# #
# #
# # order("is2 Thi1s T4est 3a")
#
# # import re
# # def order(sentence):
# #     if sentence == '':
# #         return ''
# #     type1 = re.split('\W+', sentence)
# #     type2 = 1
# #     type4 = []
# #     seperator = ' '
# #     for i in type1:
# #         type3 = [i for i in type1 if str(type2) in i]
# #         type4.append(type3.pop())
# #         type2 = type2 + 1
# #     print(seperator.join(type4))
# #     return seperator.join(type4)
# #
# #
# # order("is2 Thi1s T4est 3a")
#
#
# # def validate_pin():
# #     reg1 = re.compile(r'\d{6}')
# #     reg2 = re.findall(reg1, '123456')
# #     if reg2 = True:
# #         print(True)
# #     else:
# #         print(False)
# # validate_pin('1234')
#
# # import re
# # def validate_pin(pin):
# #     p = re.compile(r'\D')
# #     t = re.search(p, pin)
# #     if t is not None:
# #         print(False)
# #     elif len(pin) == 4|6:
# #         print(True)
# #     else:
# #         print(False)
# # validate_pin('1234')
#
# # import re
# # def validate_pin(pin):
# #     print(len(pin))
# #     p = re.compile(r'\D')
# #     t = re.search(p, pin)
# #     if t is not None:
# #         print(False)
# #     elif len(pin) is not 4:
# #         print(False)
# #     else:
# #         print(True)
# # validate_pin(r'12345')
#
#
# # def reverse_seq(n):
# #     # arry = range(n)
# #     x = []
# #     while n > 0:
# #         x.append(n)
# #         n -= 1
# #     print(x)
# #
# # reverse_seq(5)
#
#
#
# # def getCount(inputStr):
# #     count = 0
# #     for char in inputStr:
# #         if char in ['a', 'e', 'i', 'o', 'u']:
# #             count = count + 1
# #     print(count)
# #
# # getCount("abracadabree")
#
# # def getCount(inputStr):
# #     return sum(char in inputStr if char in 'aeiou')
# #
# # getCount("abracadabree")
#
# # def DNA_strand(dna):
# #     str1 = 'GTAC'
# #     str2 = 'CATG'
# #     mapped = str.maketrans(str1, str2)
# #     return dna.translate(mapped)
#
#
# # nums = [11, 200, 7, 44]
# #
# # # with map
# # nums2 = map(lambda x: x*2, nums)
# # print(nums2)
#
#
#
# # with list comprehension
# # nums2 = [x*2 for x in nums]
# # print(nums2)
#
#
# # def getCount(inputStr):
# #
# #     # num_vowels = 0
# #     # or 'e' or 'i' or 'o' or 'u'
# #     regex = 'a'
# #     match = re.findall(regex, inputStr)
# #     print(match)
