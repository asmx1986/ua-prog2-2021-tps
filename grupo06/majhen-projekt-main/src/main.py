from Import_index import General_state
from Interface.main_interface import Interface

if __name__ == "__main__":
    General_state.load_instances()  # dev
    General_state.load_previous_status_of_sensors()

    Interface()