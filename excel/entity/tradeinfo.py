from enum import Enum

# 
class SavingCardTradeType(Enum):
    TYPE_TO_CASH = "取现"
    TYPE_CARD = "刷卡"

class TradeInfo(object):
    time = None
    amount = 0
    type = None

    pass