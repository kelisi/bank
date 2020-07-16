from enum import Enum

# 
class SavingCardTradeType(Enum):
    TYPE_TO_CASH = "取现"
    TYPE_CARD = "刷卡"

class CardType(Enum):
    CARD_TYPE_SAVING = "储蓄卡"
    CARD_TYPE_CREDIT = "信用卡"

class TradeInfo(object):
    time = None
    amount = 0
    trade_type = ""
    card_type = None

    def __init__(self, time, amount, tradeType, cardType):
        self.time = time
        self.amount = amount
        self.trade_type = tradeType
        self.card_type = cardType