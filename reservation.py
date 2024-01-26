import os
from users import User
from tinydb import TinyDB, Query
from serializer import serializer

"""
class reservation () :
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('reservations')

    def __init__(self, device_name : str, managed_by_user_id : str): 
    """

from datetime import datetime

class Reservation():
    # Class variable for the reservations table in the database
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('reservations')

    def __init__(self, device_name: str, reserved_by_user_id: str, start_time: datetime, end_time: datetime):
        self.device_name = device_name
        self.reserved_by_user_id = reserved_by_user_id
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f'Reservation for {self.device_name} by {self.reserved_by_user_id} from {self.start_time} to {self.end_time}'

    def __repr__(self):
        return self.__str__()

    def store_data(self):
        print("Storing reservation data...")
        self.db_connector.insert(self.__dict__)  
        print("Reservation data inserted.")

    def delete_data(self):
        print("Deleting reservation data...")
        ReservationQuery = Query()
        result = self.db_connector.remove((ReservationQuery.device_name == self.device_name) & (ReservationQuery.reserved_by_user_id == self.reserved_by_user_id))
        print(f"Deleted {result} reservation(s).")

    @classmethod
    def load_data_by_device_name(cls, device_name):
        print("Loading reservation data...")
        ReservationQuery = Query()
        result = cls.db_connector.search(ReservationQuery.device_name == device_name)

        if result:
            reservations = []
            for data in result:
                reservations.append(cls(data['device_name'], data['reserved_by_user_id'], data['start_time'], data['end_time']))
            return reservations
        else:
            return None

