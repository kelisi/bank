from enum import Enum

class CardType(Enum):
    CARD_TYPE_SAVING = "储蓄卡"
    CARD_TYPE_CREDIT = "信用卡"

class TradeInfo(object):
    def __init__(self, time, amount, purpose, cardType):
        # 交易时间
        self.time = time
        # 交易金额
        self.amount = amount
        # 资金用途
        self.purpose = purpose
        # 交易用卡
        self.card_type = cardType
        
class SavingCardTradeInfo(TradeInfo):
    def __init__(self, time, amount, purpose, fingerPrint, totalAmount):
        self.time = time
        self.amount = amount
        self.purpose = purpose
        # 大额交易特征代码
        self.finger_print = fingerPrint
        # 交易总数
        self.total_amount = totalAmount
        self.card_type = CARD_TYPE_SAVING
        
class CreditCardTradeInfo(TradeInfo):
    def __init__(self, time, amount, purpose, inOutFlag, transferFlag, storeName, tradeType):
        self.time = time
        self.amount = amount
        self.purpose = purpose
        # 资金收付标识
        self.flag_in_or_out = inOutFlag
        # 现金转账标识
        self.flag_transfer = transferFlag
        self.store_name = storeName
        self.trade_type = tradeT
        self.card_type = CARD_TYPE_SAVING