import requests
import json

def get_capacity(slot_start, slot_end, playground_id):
    capacity_url = f"https://my.sportpolimi.it/booking/get-remaining-bookings?start={slot_start}&end={slot_end}&playground={playground_id}"
    
    response = requests.get(capacity_url)
    
    if response.status_code == 200:
        capacity_data = json.loads(response.text)
        remaining_capacity = capacity_data["data"]["remaining"]
        return remaining_capacity
    else:
        print(f"Failed to fetch capacity data. Status code: {response.status_code}")
        return 0

def get_slots(start_date_str, end_date_str, playground_id=55):
    url = f"https://my.sportpolimi.it/booking/get-events?filters=%7B%22city%22%3A%22Milano%22%2C%22playgroundType%22%3A%22%22%2C%22sport%22%3A%22%22%7D&external=2&playground_id={playground_id}&start={start_date_str}T00%3A00%3A00%2B01%3A00&end={end_date_str}T23%3A59%59%2B01%3A00"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)

        slots = {}

        for index, slot_data in enumerate(data, start=1):
            slot_start = slot_data["start"]
            slot_end = slot_data["end"]
            slot_disabled = slot_data["disabled"]
            
            if slot_disabled:
                capacity = 0
            else:
                capacity = get_capacity(slot_start, slot_end, playground_id)

            slots[index] = [slot_start, slot_end, capacity]

        return slots
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return {}

if __name__ == "__main__":
    start_date_str = "2023-11-07"
    end_date_str = "2023-11-10"
    playground_id = "55"
    
    slots = get_slots(start_date_str, end_date_str, playground_id)

    # Print the dictionary with slot information
    for index, slot_info in slots.items():
        slot_start, slot_end, capacity = slot_info
        print(f"Slot {index}: Start Time: {slot_start}, End Time: {slot_end}, Capacity: {capacity}")
