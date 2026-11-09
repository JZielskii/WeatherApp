import time
from services.openweather import get_weather
from services.files import save_to_excel, read_excel
from services.dashboard import render

render()



# while True:
#     weather = get_weather()
#     save_to_excel([weather])
#     time.sleep(15)
