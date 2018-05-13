from MyEnum import TTEnum;
from Transaction import Transaction;
from Utility.CSV import CSV;
from StatementParser import StatementParser;
import re
"""
Statement class provides functionality for storing all transaction of a perticular account.
"""
class Statement:
    """
    __init__ constructor take a multiple transactions as input, 
    get it converted to Transaction objects and store it.
    @param self current instance of Statement class
    @param transactions All transaction in CSV format
    @param parser Concrete object of child of Parser class
    """
    def __init__(self, transactions, parser, statementTransType, ttMapFName):
        self.transactions = [];
        Transaction.PopulateTTMap(ttMapFName);
        for i in range(len(transactions)):
            self.transactions.append(parser.Parse(transactions[i], i));
            self.statementTransType = statementTransType;