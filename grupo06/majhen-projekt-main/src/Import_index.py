import sys

from Classes.Modules.Dataset import dataset # dev (delete)

from Classes.Modules.Anses import Anses
from Classes.Modules.Generators import generate_id, generate_password
from Classes.Citizen import Citizen
from Classes.Admin import Admin, Admin_dev
from Classes.General_state import General_state, Citizens_state
from Classes.Table import Sensor_table, General_table
from Classes.Requests_module.Friend_requests import Friend_request, Request
from Classes.Event import Birthday_event, Concert_event, Party_event, Events
from Classes.Sensor import Sensor
from Classes.Requests_module.Event_report import Event_invite_friend
from Classes.Table import Table, Sensor_table, General_table
from Classes.Modules.Erase_screen import erase_screen

sys.path.append("..") # Relative imports works with this