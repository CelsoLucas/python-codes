from datetime import datetime
import delorean


data_especifica = datetime(2024, 11, 12, 14, 00)


d2 = delorean.Delorean(datetime=data_especifica, timezone='America/Campo_Grande')


d2_utc = d2.shift('UTC')


print("Data e hora específica em UTC:", d2_utc)