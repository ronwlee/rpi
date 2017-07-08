import gspread

gc = gspread.authorize('Raspberry Pi Weather Station-6831df99334f.json')

wks = gc.open("rpiLog").sheet1
