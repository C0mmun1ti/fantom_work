import gspread



gc = gspread.service_account_from_dict(credentials)

worksheet = gc.open_by_key('1LsfI1hI0r1Ynzg3upcQRcyGhrVeam4zxFdshNefldNk')

sheet_p2p = worksheet.get_worksheet(0)
sheet_sbp = worksheet.get_worksheet(1)


example_list = [['33 years old', 'John Apple', '1012', 'friend'], ['18 years old', 'George Eperon', '1013', 'unknown'], ['21 years old', 'Jesper Lokosir', '1014', 'friend']]
sheet_p2p.append_rows(example_list)
from time import sleep

sleep(15)
print(sheet_p2p.get('A1:G1'))
print(sheet_sbp.get('A1:G1'))