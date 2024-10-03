import requests

url = "https://oregonstateparks.reserveamerica.com/camping/devils-lake-state-recreation-area/r/campgroundDetails.do?contractCode=OR&parkId=402130"

response = requests.get(url, verify=False)

# Get all cookies
cookies = response.cookies

# Access a specific cookie
cookie_value = response.cookies.get('cookie_name')

# Print all cookies
for cookie in cookies:
    print(cookie.name, cookie.value)
