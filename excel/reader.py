import logging
from openpyxl import Workbook, load_workbook
from .entity.user import User

logger = logging.getLogger(__name__)

SHEET_SAVING_CARD = "大额交易"
SHEET_CREDIT_CARD = "信用卡交易"

FIRST_ROW = ["身份证号", "客户姓名", "交易日期", "交易金额", "交易方式"]


class BankExcelReader():
    file_path = ""
    # 身份证:User
    user_map = {}

    def __init__(self, path):
        logger.debug("read file :%s", path)
        self.file_path = path
        self.work_book = load_workbook(path)

    def getSavingCardSheet(self):
        return self.work_book[SHEET_SAVING_CARD]

    def getCreditCardSheet(self):
        return self.work_book[SHEET_CREDIT_CARD]

    def __readSavingCard(self):
        saving_card_sheet = self.getSavingCardSheet()

        first_row = saving_card_sheet[1]

        for i in range(len(first_row)):
            if first_row[i].value != FIRST_ROW[i]:
                raise Exception("列顺序不匹配")

        for row in saving_card_sheet[2:]:
            user = User()
            pass
            # for row in saving_card_sheet.rows:
            #     for cell in row:
            #         logger.debug(cell.value)
            # pass

    def __readCreditCard(self):
        pass

    def read(self):
        self.__readSavingCard()
        self.__readCreditCard()
