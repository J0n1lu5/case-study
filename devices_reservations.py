import os
from datetime import datetime

from users_reservations import User
from reservations import Reservation
from serializable_reservations import Serializable
from database_reservations import DatabaseConnector
from tinydb import Query

class Device(Serializable):

    def __init__(self, device_name: str, managed_by_user_id: str, reservations: list = None, end_of_life: datetime = None, creation_date: datetime = None, last_update: datetime = None):
        super().__init__(device_name)
        self.device_name = device_name
        # The user id of the user that manages the device
        # We don't store the user object itself, but only the id (as a key)
        self.managed_by_user_id = managed_by_user_id
        self.is_active = True

        self.reservations = reservations if reservations else []
        self.end_of_life = end_of_life if end_of_life else datetime.today().date()
        self.__creation_date = creation_date if creation_date else datetime.today().date()
        self.__last_update = last_update if last_update else datetime.today().date()
    
    @classmethod
    def get_db_connector(cls):
        return DatabaseConnector().get_devices_table()

    def store(self):
        print("Storing device...")
        self.__last_update = datetime.today().date() # we need to update the last update date before storing the object
        super().store()
    
    @classmethod
    def load_by_id(cls, id):
        print("Loading device...")
        data = super().load_by_id(id)
        if data:
            return cls(data['device_name'], data['managed_by_user_id'], data['reservations'], data['end_of_life'], data['_Device__creation_date'], data['_Device__last_update'])
        else:
            return None
    
    def delete(self):
        super().delete()
        print("Device deleted.")

    def __str__(self) -> str:
        return F"Device: {self.device_name} ({self.managed_by_user_id}) - Active: {self.is_active} - Created: {self.__creation_date} - Last Update: {self.__last_update}"

    def __repr__(self) -> str:
        return self.__str__()

if __name__ == "__main__":
    # Create a device
    res1 = Reservation("Res1", datetime.strptime("2024-01-01", "%Y-%m-%d"), datetime.strptime("2024-02-01", "%Y-%m-%d"))
    res2 = Reservation("Res2", datetime.strptime("2024-02-01", "%Y-%m-%d"), datetime.strptime("2024-03-01", "%Y-%m-%d")) 
    res3 = Reservation("Res3", datetime.strptime("2024-03-01", "%Y-%m-%d"), datetime.strptime("2024-04-01", "%Y-%m-%d")) 
    res1.store()
    res2.store()
    res3.store()

    device1 = Device("Device1", "one@mci.edu", [res1.id])
    device2 = Device("Device2", "two@mci.edu", [res2.id]) 
    device3 = Device("Device3", "two@mci.edu", [res3.id]) 
    device1.store()
    device2.store()
    device3.store()
    device4 = Device("Device3", "four@mci.edu") 
    device4.store()

    loaded_device = Device.load_by_id("Device2")
    if loaded_device:
        print(f"Loaded: {loaded_device}")
    else:
        print("Device not found.")

    all_devices = Device.find_all()
    for device in all_devices:
        print(device)