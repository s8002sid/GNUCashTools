from MyEnum import TTEnum;
from Transaction import Transaction;
from Utility.CSV import CSV;
import re
"""
Statement downloaded from different website contains different format.
Each source from where we can download statement must inherit this class, 
create a Transaction object, do required formating and return it.
"""
class StatementParser:
    """
    Statement parser base class
    @param self pointer to self
    @param transaction list containing one line of transaction
    @param Line number of this transaction
    @return Returns an object of Transaction class
    """
    def Parse(self, transaction, sno):
        print("This function must not get called");
    __Parse = Parse;
    
class HDFCStatementParser(StatementParser):
    """
    transaction contains following entries in order:
    Date
    Narration
    Reference Number
    Value Date
    Withdrawal Amount
    Deposit
    Closing Balance
    """
    def Parse(self, transaction, sno):
        return Transaction(sno,
                           transaction[0],  #date
                           '',              #transtype
                           transaction[1],  #narration
                           transaction[2],  #refno
                           transaction[3],  #valuedate
                           transaction[4],  #withdrawal
                           transaction[5],  #deposit
                           transaction[6]   #closingbalance
                           );

class HDFCEditedStatementParser(StatementParser):
    """
    transaction contains following entries in order:
    Date
    Transaction Type
    Narration
    Reference Number
    Value Date
    Withdrawal Amount
    Deposit
    Closing Balance
    """
    def Parse(self, transaction, sno):
        return Transaction(sno,             #sno
                           transaction[0],  #date
                           transaction[1],  #transtype
                           transaction[2],  #narration
                           transaction[3],  #refno
                           transaction[4],  #valuedate
                           transaction[5],  #withdrawal
                           transaction[6],  #deposit
                           transaction[7]   #closingbalance
                           )
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
    def __init__(self, transactions, parser):
        self.transactions = [];
        transactions = [e.replace('\n', '') for e in transactions];
        for i in range(len(transactions)):
            self.transactions.append(parser.Parse(CSV.Tokenize(transactions[i]), i));

    """
    This function is used for creating Header String
    """
    def HeaderString(self):
        #Header
        x='';
        x+=Transaction.TransTypeName[TTEnum.SNO] + ',';
        x+=Transaction.TransTypeName[TTEnum.Date] + ',';
        x+=Transaction.TransTypeName[TTEnum.TransType] + ',';
        x+=Transaction.TransTypeName[TTEnum.Narration] + ',';
        x+=Transaction.TransTypeName[TTEnum.Refno] + ',';
        x+=Transaction.TransTypeName[TTEnum.ValueDate] + ',';
        x+=Transaction.TransTypeName[TTEnum.Withdrawal] + ',';
        x+=Transaction.TransTypeName[TTEnum.Deposit] + ',';
        x+=Transaction.TransTypeName[TTEnum.ClosingBalance];
        return x;

    """
    This function is used for converting list of transaction in to CSV string list and returns it.
    """
    def ToStringList(self):
        ToWrite=[];
        ToWrite.append(self.HeaderString());
        #Values
        for i in range(len(self.transactions)):
            x = '';
            value = self.transactions[i].value;
            x+= str(value[TTEnum.SNO]) + ',';
            x+=value[TTEnum.Date] + ',';
            x+=value[TTEnum.TransType] + ',';
            x+=value[TTEnum.Narration] + ',';
            x+=value[TTEnum.Refno] + ',';
            x+=value[TTEnum.ValueDate] + ',';
            x+=value[TTEnum.Withdrawal] + ',';
            x+=value[TTEnum.Deposit] + ',';
            x+=value[TTEnum.ClosingBalance];
            ToWrite.append(x);
        return ToWrite;

    """
    This function is used to get all entries for which Transaction Type has not been updated.
    """
    def NotUpdatedTransTypeStringList(self):
        ToWrite = [];
        ToWrite.append(self.HeaderString());
        for i in range(len(self.transactions)):
            x = '';
            value = self.transactions[i].value;
            if (self.transactions[i].updated == 0):
                x+= str(value[TTEnum.SNO]) + ',';
                x+=value[TTEnum.Date] + ',';
                x+=value[TTEnum.TransType] + ',';
                x+=value[TTEnum.Narration] + ',';
                x+=value[TTEnum.Refno] + ',';
                x+=value[TTEnum.ValueDate] + ',';
                x+=value[TTEnum.Withdrawal] + ',';
                x+=value[TTEnum.Deposit] + ',';
                x+=value[TTEnum.ClosingBalance];
                ToWrite.append(x);
        return ToWrite;