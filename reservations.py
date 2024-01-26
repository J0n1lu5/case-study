import os
from datetime import datetime

from users_reservations import User
from serializable_reservations import Serializable
from database_reservations import DatabaseConnector

class Reservation(Serializable):

    def __init__(self, name: str, start: datetime, end: datetime):
        super().__init__(name)
        self.name = name
        self.start = start
        self.end = end
    
    @classmethod
    def get_db_connector(cls):
        return DatabaseConnector().get_reservations_table()

    def store(self):
        print("Storing reservation...")
        super().store()
    
    @classmethod
    def load_by_id(cls, id):
        print("Loading reservation...")
        data = super().load_by_id(id)
        if data:
            return cls(data['name'], data['start'], data['end'])
        else:
            return None
    
    def delete(self):
        super().delete()
        print("Reservation deleted.")

    def __str__(self) -> str:
        return F"Reservation: {self.name} - From: {self.start} - To: {self.end}"

    def __repr__(self) -> str:
        return self.__str__()

if __name__ == "__main__":
    res1 = Reservation("Res1", datetime.strptime("2024-01-01", "%Y-%m-%d"), datetime.strptime("2024-02-01", "%Y-%m-%d"))
    res2 = Reservation("Res2", datetime.strptime("2024-02-01", "%Y-%m-%d"), datetime.strptime("2024-03-01", "%Y-%m-%d")) 
    res3 = Reservation("Res3", datetime.strptime("2024-03-01", "%Y-%m-%d"), datetime.strptime("2024-04-01", "%Y-%m-%d")) 
    res1.store()
    res2.store()
    res3.store()

    loaded_reservation = Reservation.load_by_id("Res2")
    if loaded_reservation:
        print(f"Loaded: {loaded_reservation}")
    else:
        print("Device not found.")

    all_reservations = Reservation.find_all()
    for res in all_reservations:
        print(res)