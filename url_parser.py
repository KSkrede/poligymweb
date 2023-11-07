import urllib.parse

# The URL-encoded string
url_string = "_csrf-frontend=XlWFLMOrHJRIOsm9ACaMUi7ImT428jG1OSZsax2MshgPMN90jeR2uSkKodltH8d_Q6PBB1ycbvRwaTsze-LFWQ%3D%3D&BookingCalendarForm%5Bid%5D=&BookingCalendarForm%5Bstart_date_time%5D=2024-01-23+10%3A00&BookingCalendarForm%5Bend_date_time%5D=2024-01-23+11%3A30&BookingCalendarForm%5Bplayground_id%5D=55&BookingCalendarForm%5Bstart_time%5D=10%3A00&BookingCalendarForm%5Bend_time%5D=11%3A30"

# Parse the query string into a dictionary
parsed_data = urllib.parse.parse_qs(url_string)

# Extract values for the keys you mentioned
csrfToken = parsed_data.get('_csrf-frontend', [''])[0]
bookingId = parsed_data.get('BookingCalendarForm[id]', [''])[0]

# Print the values
print(f'_csrf-frontend: {csrfToken}')
print(f'BookingCalendarForm[id]: {bookingId}')
