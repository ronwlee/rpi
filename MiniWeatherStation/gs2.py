import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Raspberry Pi Weather Station-6831df99334f.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("rpiLog").sheet1
