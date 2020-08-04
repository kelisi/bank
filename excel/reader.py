import logging
from openpyxl import Workbook, load_workbook
from .entity.user import User
from .entity.tradeinfo import TradeInfo, CardType

logger = logging.getLogger(__name__)

# read
SHEET_SAVING_CARD = "大额交易"
SHEET_CREDIT_CARD = "信用卡交易"

# create
SHEET_MERGE_CREATE = "合并交易"

TITLE_USER_ID = "身份证号"
TITLE_USER_NAME = "客户姓名"
TITLE_TRADE_DATE = "交易日期"
TITLE_TRADE_AMOUNT = "交易金额"
TITLE_TRADE_TYPE = "交易方式"

FIRST_ROW_READ = [TITLE_USER_ID, TITLE_USER_NAME,
                  TITLE_TRADE_DATE, TITLE_TRADE_AMOUNT, TITLE_TRADE_TYPE]

TITLE_SAVING_TRADE_AMOUNT = "大额交易金额"
TITLE_SAVING_TRADE_TYPE = "大额交易方式"
TITLE_CREDIT_TRADE_AMOUNT = "信用卡交易金额"
TITLE_CREDIT_TRADE_TYPE = "信用卡交易方式"
TITLE_TRADE_DATE_AMOUNT = "当日累计交易额"

FIRST_ROW_WRITE = [TITLE_USER_ID, TITLE_USER_NAME, TITLE_TRADE_DATE, TITLE_SAVING_TRADE_AMOUNT,
                   TITLE_SAVING_TRADE_TYPE, TITLE_CREDIT_TRADE_AMOUNT, TITLE_CREDIT_TRADE_TYPE, TITLE_TRADE_DATE_AMOUNT]


class BankExcelReader():
    file_path = ""
    # 身份证:User
    user_map = {}

    def __init__(self, path):
        logger.debug("read file :%s", path)
        self.file_path = path
        self.work_book = load_workbook(path)
        self.user_map = {}

    def getSavingCardSheet(self):
        return self.work_book[SHEET_SAVING_CARD]

    def getCreditCardSheet(self):
        return self.work_book[SHEET_CREDIT_CARD]

    def __getUser(self, identityId):
        return self.user_map[identityId]

    def __addUser(self, identityId, user):
        self.user_map[identityId] = user

    def __readSheet(self, sheet, cardType):
        first_row = sheet[1]

        for i in range(len(first_row)):
            if first_row[i].value != FIRST_ROW_READ[i]:
                raise Exception("列顺序不匹配")

        for row in sheet[2:sheet.max_row]:
            user_name = row[FIRST_ROW_READ.index(TITLE_USER_NAME)].value
            user_id = row[FIRST_ROW_READ.index(TITLE_USER_ID)].value
            user = None

            if user_id in self.user_map:
                logger.debug("get user:%s", user_id)
                user = self.__getUser(user_id)
            else:
                if cardType == CardType.CARD_TYPE_CREDIT:
                    logger.debug("User[%s] Not in Saving Card Sheet Ignore!", user_id)
                else:
                    user = User(user_name, user_id)
                    self.__addUser(user_id, user)

            trade_time = row[FIRST_ROW_READ.index(TITLE_TRADE_DATE)].value
            trade_amount = row[FIRST_ROW_READ.index(TITLE_TRADE_AMOUNT)].value
            trade_type = row[FIRST_ROW_READ.index(TITLE_TRADE_TYPE)].value

            trade_info = TradeInfo(
                trade_time, trade_amount, trade_type, cardType)

            user.addTradeByTime(trade_time, trade_info)

    def __readSavingCard(self):
        saving_card_sheet = self.getSavingCardSheet()
        self.__readSheet(saving_card_sheet, CardType.CARD_TYPE_SAVING)

    def __readCreditCard(self):
        credit_card_sheet = self.getCreditCardSheet()
        self.__readSheet(credit_card_sheet, CardType.CARD_TYPE_CREDIT)

    def read(self):
        # must read saving card sheet first
        self.__readSavingCard()
        self.__readCreditCard()

        logger.debug("user map:", self.user_map)

    def __writeCell(self, sheet, user):
        for time, trade_list in user.tradeInfoDic.items():
            trade_number = 0
            for i, trade in enumerate(trade_list):
                trade_number = trade_number + trade.amount
                trade_date_amount = None

                if i == len(trade_list)-1:
                    trade_date_amount = trade_number

                if trade.card_type == CardType.CARD_TYPE_SAVING:
                    sheet.append([user.identityId, user.name, time,
                                  trade.amount, trade.trade_type, None, None, trade_date_amount])
                else:
                    sheet.append([user.identityId, user.name, time, None,
                                  None, trade.amount, trade.trade_type, trade_date_amount])

    def write(self):
        # remove before  create merge sheet
        if SHEET_MERGE_CREATE in self.work_book.sheetnames:
            del self.work_book[SHEET_MERGE_CREATE]
        merge_sheet = self.work_book.create_sheet(SHEET_MERGE_CREATE)

        merge_sheet.append(FIRST_ROW_WRITE)

        for user in self.user_map.values():
            self.__writeCell(merge_sheet, user)

        self.work_book.save(self.file_path)
