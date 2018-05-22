from MyEnum import TTEnum;
from Transaction import Transaction;
from Utility.CSV import CSV;
from StatementParser import StatementParser;
from Utility.WordStats import *;
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
    def __init__(self, transactions, parser, statementTransType, ttMapFName, atMapFName):
        self.transactions = [];
        Transaction.PopulateMap(ttMapFName, atMapFName);
        for i in range(len(transactions)):
            transaction = parser.Parse(transactions[i], i);
            if (transaction is None):
                continue;
            if (transaction.value[TTEnum.Account] == ''):
                transaction.value[TTEnum.Account] = statementTransType;
            self.transactions.append(transaction);
            self.statementTransType = statementTransType;

    def WriteWordStat(self, fileName):
        analyzer = StatementAnalyzer();
        for i in range(len(self.transactions)):
            if (self.transactions[i].updated == 0):
                analyzer.AddStatement(self.transactions[i].value[TTEnum.Narration]);
        analyzer.WriteSortedWordList(fileName);
