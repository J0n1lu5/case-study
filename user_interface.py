### Erste Streamlit App

import streamlit as st
from queries import find_devices
from devices import Device
import datetime
from reservation import Reservation

# Eine Überschrift der ersten Ebene
st.write("# Gerätemanagement")

# tabs
tab1, tab2, tab3 = st.tabs(["Gerät anlegen", "Geräte Verwalten","Gerät reservieren"])


with tab1:
    with st.form("New Device"):
            

            #checkbox_val = st.checkbox("Is active?", value=loaded_device.is_active)
            #loaded_device.is_active = checkbox_val

            new_devicename = st.text_input("Gerätename")
            device_user = st.text_input("Verantwortlicher")
            

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                new_device= Device(new_devicename,device_user)
                new_device.store_data()
                st.write("Data stored.")
                st.rerun()

    


with tab2:

    genre = st.radio("Bitte auswählen",
    ["Verantwortlichen ändern", "Gerät löschen"],
    captions = ["", ""])

    if genre == "Verantwortlichen ändern":

        # Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
        devices_in_db = find_devices()

        if devices_in_db:
            current_device_name = st.selectbox(
                'Gerät auswählen',
                options = devices_in_db, key="sbDevice")

            if current_device_name in devices_in_db:
                loaded_device = Device.load_data_by_device_name(current_device_name)
                st.write(f"Loaded {loaded_device}")


            with st.form("Device"):
                st.write(loaded_device.device_name)

                #checkbox_val = st.checkbox("Is active?", value=loaded_device.is_active)
                #loaded_device.is_active = checkbox_val

                text_input_val = st.text_input("Geräte-Verantwortlicher", value=loaded_device.managed_by_user_id)
                loaded_device.managed_by_user_id = text_input_val

                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")
                if submitted:
                    loaded_device.store_data()
                    st.write("Data stored.")
                    st.rerun()
    
    elif genre == "Gerät löschen":
        
        devices_in_db = find_devices()
        if devices_in_db:
            current_device_name = st.selectbox(
                'Gerät auswählen',
                options = devices_in_db, key="sbDevice")

            if current_device_name in devices_in_db:
                loaded_device = Device.load_data_by_device_name(current_device_name)
                st.write(f"Loaded {loaded_device}")


            with st.form("Device"):
                st.write(loaded_device.device_name,"wirklich löschen?")

                
                submitted = st.form_submit_button("Delete Device")
                if submitted:
                    loaded_device.delete_data()
                    st.write("Device deleted.")
                    st.rerun()
    
with tab3:
    
    genre = st.radio("Bitte auswählen",
    ["reservierung einsehen", "resevieren"],
    captions = ["", ""])
    
    if genre == "reservierung einsehen":
        devices_in_db = find_devices()

        if devices_in_db:
            current_device_name = st.selectbox(
                'Gerät auswählen',
                options = devices_in_db, key="sbDevice_reservation")
            
        if current_device_name in devices_in_db:
                loaded_device = Device.load_data_by_device_name(current_device_name)
                #loaded_reservation = Reservation.load_data_by_device_name(loaded_device.device_name)
                st.write(f"Loaded {loaded_device}")

        #st.write("Das Gerät",loaded_device.device_name, "vom" ,loaded_reservation.start_time,"bis",loaded_reservation.end_time)

        loaded_reservations = Reservation.load_data_by_device_name(loaded_device.device_name)
        if loaded_reservations:
            for reservation in loaded_reservations:
                st.write(f"{reservation}")
        else:
            st.write("No reservations found for the device.")    
    
    elif genre == "resevieren":
        # Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
        devices_in_db = find_devices()

        if devices_in_db:
            current_device_name = st.selectbox(
                'Gerät auswählen',
                options = devices_in_db, key="sbDevice_reservation")

            if current_device_name in devices_in_db:
                loaded_device = Device.load_data_by_device_name(current_device_name)
                st.write(f"Loaded {loaded_device}")


            with st.form("Device reservation"):
                st.write(loaded_device.device_name)

                #checkbox_val = st.checkbox("Is active?", value=loaded_device.is_active)
                #loaded_device.is_active = checkbox_val
            
                person = st.text_input("Wer reserviert")

                date_start = st.date_input("Start", datetime.date(2019, 7, 6))
                
                
                date_end = st.date_input("Ende", datetime.date(2019, 7, 6))

                reservation_devicename = loaded_device.device_name
                

                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")
                if submitted:
                    new_reservation = Reservation(reservation_devicename,person,date_start,date_end)
                    new_reservation.store_data()
                    st.write("Data stored.")
                    st.rerun()



                #reservation1 = Reservation("Device1", "one@mci.edu", start_time, end_time)