# display curr days with format MM/DD/YYYY
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%m/%d/%Y")
print(formatted_date)
