import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'keys/dotspreed-0f70c3397201.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
gc = gspread.authorize(credentials)
sheet_url = 'https://docs.google.com/spreadsheets/d/1vBaQpznNODv-vvIymOm1571s-XFBphwXKG_7mTf5Als/edit#gid=0'
doc = gc.open_by_url(sheet_url)
worksheet = doc.worksheet('시트1')
cell_data = worksheet.acell('A1').value
print(cell_data)