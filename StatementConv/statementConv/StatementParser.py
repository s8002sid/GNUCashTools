from MyEnum import TTEnum;
from Transaction import Transaction;
from Utility.CSV import CSV;
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
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;
        if (transaction[5] != ''):
            withdrawal = float(transaction[5]);
        if (transaction[6] != ''):
            deposit = float(transaction[6]);
        if (transaction[7] != ''):
            closingBalance = float(transaction[7]);
        return Transaction(sno,             #sno
                           transaction[0],  #date
                           transaction[1],  #transtype
                           transaction[2],  #narration
                           transaction[3],  #refno
                           transaction[4],  #valuedate
                           float(withdrawal),  #withdrawal
                           float(deposit),  #deposit
                           float(closingBalance)   #closingbalance
                           )
