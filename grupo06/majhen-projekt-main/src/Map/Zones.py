from .MapGenerator import Map
import math
from Import_index import Sensor_table

class Zones:
    def __init__(self, zones, sensors_dict: dict) -> None:
        self.zones = zones
        self.sensors_by_zone = self.selection_sort_sensors(sensors_dict)
    
    def selection_sort_sensors(self, sensors_dict: dict) -> list:
        sensors_list = list([None, list(), list(), list(), list()])

        for _, sensor in sensors_dict.items():
            if sensor["event"]["zone"] == 1:
                sensors_list[1].append(sensor)
            elif sensor["event"]["zone"] == 2:
                sensors_list[2].append(sensor)
            elif sensor["event"]["zone"] == 3:
                sensors_list[3].append(sensor)
            elif sensor["event"]["zone"] == 4:
                sensors_list[4].append(sensor)

        return sensors_list

    def print_map_zone(self, zone_number):

        def get_par_number(number):
            rounded = number

            if number % 2 == 1:
                rounded = number + 1

            return math.ceil(rounded)

        length = get_par_number(len(self.sensors_by_zone[zone_number]) / 2)
        map_zone = Map(length, 2)

        sensors_dictionary = dict()
        sensors_zone_list = self.sensors_by_zone[zone_number]
        
        for sensor_info in sensors_zone_list:
            sensors_dictionary.update({ sensor_info["_id"]: sensor_info })

        sensor_table = Sensor_table(sensors_dictionary)
        
        order_sensors = sensor_table.order_sensors(True)
        
        x, y = 0, 0

        for i in range(0, len(sensors_zone_list)):
            sensor_concurrency = order_sensors[i]["concurrency"]

            map_zone.assign_event(x, y, sensor_concurrency)

            if y < 1:
                y += 1
            else:
                x += 1
                y = 0

        if length == 0:
            print("-- No hay sensores registrados en la zona --")
        map_zone.print_map()

    def get_statistics(self, zone_number, ranking = False):
        sensors_dictionary = dict()
        sensors_zone_list = self.sensors_by_zone[zone_number]
        
        for sensor_info in sensors_zone_list:
            sensors_dictionary.update({ sensor_info["_id"]: sensor_info })

        sensor_table = Sensor_table(sensors_dictionary)
        
        order_sensors = sensor_table.order_sensors(True)

        if ranking:
            if not len(order_sensors) < 3: 
                order_sensors = order_sensors[0:2]

        return order_sensors