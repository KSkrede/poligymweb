from requests_toolbelt.utils import dump
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from get_slots import get_slots

app = Flask(__name__)
slots = {}

BOOKING_URL = "https://my.sportpolimi.it/booking/book"


def book_slot(startDate, endDate, startTime, endTime, playgroundId=55):
    headers = {
        'Host': 'my.sportpolimi.it',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-CSRF-Token': 'qQs-s-GVIdwRzffUDvIF74ZS2Ed6q1Ei4VC3yWf5jeCbc13VoOZj5HO0sZcjlVSI7hC_Lxv-Am_XEs6WDJK-ow==',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '483',
        'Origin': 'https://my.sportpolimi.it',
        'Connection': 'keep-alive',
        'Referer': 'https://my.sportpolimi.it/booking/calendar?type=athletic_activity&city=Milano',
        'Cookie': 'Cookie: __stripe_mid=d0e3dd35-db0a-46b1-9c7e-e4b83c3ad531f39cf7; cookieconsent_dismissed=yes; advanced-frontend=77ou2ai1i7g1pootrccb7m9ko1; _csrf-frontend=11658b1232d028c6fea9b6ddfe5907364f367c04a5d9bc973a43335d3ac2c631a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%222xcfAsB8byFC-gQghBghaUSM6By_kk3C%22%3B%7D; SimpleSAML=4c568ab5c2df5056df20fb6214eb8ca0; SimpleSAMLAuthToken=_8b555e7d961c7b281fa46ddde4ccbb796b342ed740',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    # Construct the data for booking
    booking_data = {
        '_csrf-frontend': 'qQs-s-GVIdwRzffUDvIF74ZS2Ed6q1Ei4VC3yWf5jeCbc13VoOZj5HO0sZcjlVSI7hC_Lxv-Am_XEs6WDJK-ow==',
        'BookingCalendarForm[id]': '',
        'BookingCalendarForm[start_date_time]': f"{startDate}+{startTime}",
        'BookingCalendarForm[end_date_time]': f"{endDate}+{endTime}",
        'BookingCalendarForm[playground_id]': playgroundId,
        'BookingCalendarForm[start_time]': startTime,
        'BookingCalendarForm[end_time]': endTime,
        'BookingCalendarForm[accepted_booking_terms]': 1,
        'BookingCalendarForm[accepted_additional]': 1,
    }

    response = requests.post(BOOKING_URL, data=booking_data, headers=headers)
    data = dump.dump_response(response)
    print(data.decode('utf-8'))
    if response.status_code == 200:
        return True
    else:
        print(f"Failed to book the slot. Status code: {response.status_code}")
        return False

# tests



def test_book_slot():
    book_slot("2023-11-09", "2023-11-09", "10:00", "11:30")


test_book_slot()
