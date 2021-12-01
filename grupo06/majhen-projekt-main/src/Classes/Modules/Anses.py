from .Dataset import dataset

class Anses:
    @staticmethod
    def validate_citizen(citizen_cuil) -> bool:
        return bool(Anses.get_citizen_data(citizen_cuil))

    @staticmethod
    def get_citizen_data(citizen_cuil) -> dict:
        return dataset.get(citizen_cuil)