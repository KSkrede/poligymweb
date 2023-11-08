import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from get_slots import get_slots

app = Flask(__name__)
slots = {}

# Define the base URL for booking
BOOKING_URL = "https://my.sportpolimi.it/booking/book"


def book_slot(startDate, endDate, startTime, endTime, playgroundId=55):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Construct the data for booking
    booking_data = {
        '_csrf-frontend': "XlWFLMOrHJRIOsm9ACaMUi7ImT428jG1OSZsax2MshgPMN90jeR2uSkKodltH8d_Q6PBB1ycbvRwaTsze-LFWQ==",
        'BookingCalendarForm[id]': "",
        'BookingCalendarForm[start_date_time]': f"{startDate}+{startTime}",
        'BookingCalendarForm[end_date_time]': f"{endDate}+{endTime}",
        'BookingCalendarForm[playground_id]': playgroundId,
        'BookingCalendarForm[start_time]': startTime,
        'BookingCalendarForm[end_time]': endTime,
        'BookingCalendarForm[accepted_booking_terms]': 1,
        'BookingCalendarForm[accepted_additional]': 1,
    }
    print(booking_data)

    response = requests.post(BOOKING_URL, data=booking_data, headers=headers)
    print(response)
    if response.status_code == 200:
        return True
    else:
        print(f"Failed to book the slot. Status code: {response.status_code}")
        return False

# Rest of your existing code

@app.route('/')
def index():
    return render_template('index.html', slots=slots)

@app.route('/fetch_slots', methods=['POST'])
def fetch_slots():
    start_date_str = "2023-11-08"
    end_date_str = "2023-11-08"
    playground_id = "55"
    
    global slots
    slots = get_slots(start_date_str, end_date_str, playground_id)
    
    return render_template('index.html', slots=slots)

@app.route('/book_slot', methods=['POST'])
def book_slot_handler():
    # Retrieve the booking data from the request
    startDate = request.form.get('BookingCalendarForm[start_date]')
    endDate = request.form.get('BookingCalendarForm[end_date]')
    startTime = request.form.get('BookingCalendarForm[start_time]')
    endTime = request.form.get('BookingCalendarForm[end_time]')

    # Attempt to book the slot using the correct function
    if book_slot(startDate, endDate, startTime, endTime):
        return "Slot booked successfully!"
    else:
        return "Failed to book the slot."

if __name__ == '__main__':
    app.run(debug=True)
