from datetime import datetime

date = "Jan 15, 2023 - 12:05:33"
date_conversion = datetime.strptime(date, "%b %d, %Y - %H:%M:%S")
print("Полное название месяца:", date_conversion.strftime("%B"))
print("Форматированная дата:", date_conversion.strftime("%d.%m.%Y, %H:%M"))
