import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials


scope = 'https://spreadsheets.google.com/feeds'
json = 'keys/dotspreed-0f70c3397201.json'

f = open('keys\sheetURL.txt','r')
sheet_url = f.readline()
f.close()

credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)


# TODO 
# 하드코딩 수정하기

gc = gspread.authorize(credentials)
doc = gc.open_by_url(sheet_url)
worksheet = doc.worksheet('시트1')

start_col = 'B'
start_row = 16
end_col = 'D'
end_row = 50

cell_range = '{}{}:{}{}'.format(start_col,start_row,end_col,end_row)

total_rows = end_row - start_row + 1



def getDate():
    date_dict = {}

    cell_list = worksheet.range('날짜')

    for cell in cell_list :
        if len(cell.value) > 0 :
            date_dict[cell.address] = cell.value

    print(date_dict)
    return date_dict 

def getPerson():
    status = worksheet.batch_get(cell_range)
    new_name_list = []
    
    for i in range(len(status[0])):
        person_info = status[0][i]
        
        if not person_info:
            continue  # 빈 문자열인 경우 스킵
        # 아니면 추가
        new_name_list.append(person_info)

    return new_name_list

def addPersonToDot(name, job, jg):

    # TODO 
    # 하드코딩 수정하기
    new_cell_list = []
    cell_list = worksheet.range('돚거단1')
 
    i = 0

    while(i < len(cell_list)):
        if len(cell_list[i].value)>0:
            new_cell_list.append([cell_list[i].value, cell_list[i+1].value, cell_list[i+2].value])

        i+=3
    
    # 업데이트할 값 리스트에 추가
    new_cell_list.append([name, job, jg])


    while len(new_cell_list) < total_rows:
        # demention 맞춰주기
        new_cell_list.append(['','',''])

    worksheet.update('돚거단1', new_cell_list,raw=False)

    
    worksheet.format(cell_range, {
    "horizontalAlignment": "CENTER",
    "textFormat": {
        "foregroundColor": {
            "red": 0.0,
            "green": 0.0,
            "blue": 0.0
        },
      "fontSize": 10,
      "bold": True,
      "fontFamily": "Nato Sans KR"
     }
    })
    
def getNumberWeek(week):

    date_dict = getDate()

    key = None  # 일치하는 키를 저장할 변수
    for k, value in date_dict.items():
        if "요일" in value and value.split(" ")[-1][0] == week:
            key = k
            break
    
    if key == None:
        return "해당 요일에 거점이 없습니다."

    col = key[:1]
    total_label = '{}{}'.format(col, 14) 
    # TODO
    # 하드코딩 수정하기
    total_number = worksheet.acell(total_label).value

    return total_number
