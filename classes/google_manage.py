import gspread

import os
import dotenv

from ast import literal_eval  # распаршивает строку в дикт


dotenv.load_dotenv()

class GoogleSheetManager:
    CREDENTIALS = os.getenv("CREDENTIALS")  # ебанутый словарь с какой-то хуйнёи гугловской
    _key = os.getenv("GOOGLE_SHEET_KEY")
    gc = gspread.service_account_from_dict(literal_eval(CREDENTIALS))
    worksheet = gc.open_by_key(_key)

    def __init__(self):
        self.sheet_p2p = self.worksheet.get_worksheet(0)
        self.sheet_sbp = self.worksheet.get_worksheet(1)

    def get_data(self, p2p_or_sbp: str):
        if p2p_or_sbp.lower() == "sbp":
            return self.sheet_sbp.get('')[1:]
        return self.sheet_p2p.get('')[1:]

    def update_data(self, p2p_or_sbp: str, data_: dict) -> None:
        example_list = list(data_.values())
        if p2p_or_sbp.lower() == 'sbp':
            self.sheet_sbp.append_rows([example_list])
            return
        self.sheet_p2p.append_rows([example_list])

    def delete_data(self, p2p_or_sbp: str, string_num: int) -> None:
        if p2p_or_sbp == 'sbp':
            self.sheet_sbp.delete_rows(string_num)
            return
        self.sheet_p2p.delete_rows(string_num)
