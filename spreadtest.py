import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials

scope = 'https://spreadsheets.google.com/feeds'
json = 'keys/dotspreed-0f70c3397201.json'
sheet_url = 'https://docs.google.com/spreadsheets/d/1vBaQpznNODv-vvIymOm1571s-XFBphwXKG_7mTf5Als/edit#gid=0'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)

gc = gspread.authorize(credentials)
doc = gc.open_by_url(sheet_url)
worksheet = doc.worksheet('시트1')

# cell_data = worksheet.acell('A1').value
#test = worksheet.update_acell('b11',"input test")

cell_range = ['B16:D50']

# 범위만큼 가져오기
status = worksheet.batch_get(cell_range)

print(len(status[0]))

def getPerson():
    new_name_list = []
    
    for i in range(len(status[0])):
        person_info = status[0][i]
        
        if not person_info:
            continue  # 빈 문자열인 경우 스킵
        # 아니면 추가
        new_name_list.append(person_info)
    # 결과 출력    
    # print(new_name_list)
    return new_name_list

def addPerson(name, job, jg):
    
    new_value = getPerson()
    
    new_person = [name, job, jg]
    
    new_value.append(new_person)
    
    # TODO
    # 여기서 문제가 나는 것 같음. 찾아보자
    worksheet.update(cell_range, new_value)
    
    worksheet.format(cell_range, {
    "horizontalAlignment": "CENTER",
    "textFormat": {
      "foregroundColor": {
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      "fontSize": 12,
      "bold": True
     }})
    

    

