from MyEnum import TTEnum;
from Transaction import Transaction;
from Utility.CSV import CSV;
from datetime import datetime;
from datetime import timedelta;
"""
Statement downloaded from different website contains different format.
Each source from where we can download statement must inherit this class, 
create a Transaction object, do required formating and return it.
"""
class StatementParser(object):
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
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;
        if (transaction[4] != ''):
            withdrawal = float(transaction[4]);
        if (transaction[5] != ''):
            deposit = float(transaction[5]);
        if (transaction[6] != ''):
            closingBalance = float(transaction[6]);
        return Transaction(sno,
                           transaction[0],  #date
                           '',              #transtype
                           transaction[1],  #narration
                           transaction[2],  #refno
                           transaction[3],  #valuedate
                           withdrawal,      #withdrawal
                           deposit,         #deposit
                           closingBalance,  #closingbalance
                           '',              #action
                           '',              #account
                           '1'              #Price
                           );

class SBIStatementParser(StatementParser):
    """
    Date
    ValueDate
    Description
    Reference Number
    Debit
    Credit
    Balance
    """
    startDate=datetime(1899,12,30);
    def GetDate(self, dateStr):
        dateDelta = timedelta(int(dateStr.split('.')[0]));
        date = self.startDate + dateDelta;
        return date.strftime('%d-%m-%Y');
    def Parse(self, transaction, sno):
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;
        if (transaction[4].strip() != ''):
            withdrawal = float(transaction[4]);
        if (transaction[5].strip() != ''):
            deposit = float(transaction[5]);
        if (transaction[6].strip() != ''):
            closingBalance = float(transaction[6]);
        return Transaction(sno,
                           self.GetDate(transaction[0]),#date
                           '',                          #transtype
                           transaction[2],              #narration
                           transaction[3],              #refno
                           self.GetDate(transaction[1]),#valuedate
                           withdrawal,                  #withdrawal
                           deposit,                     #deposit
                           closingBalance,              #closingbalance
                           '',                          #action
                           '',                          #account
                           '1'                          #Price
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
                           float(closingBalance),   #closingbalance
                           '',              #action
                           '',              #account
                           '1'              #Price
                           )
class MFStatementParser(StatementParser):
    """

    """
    def Parse(self, transaction, sno):
        description = '';
        description+= 'CANNo: ' + transaction[0];
        description+= ' GRON: ' + transaction[2];
        schemeName = transaction[7];
        date = transaction[12].split(' ')[0];
        description += ' TXN No: ' + transaction[13];
        units = float(transaction[14]);
        amount = float(transaction[15]);
        price = float(transaction[16]);
        description += ' Folio No. ' + transaction[18];
        withdrawal = 0.0;
        deposit = 0.0;
        action = ''
        if (transaction[4].strip() == 'Redeem'):
            withdrawal = amount;
            action = 'Sell';
        else:
            deposit = amount;
            action = 'Buy';

        if (transaction[19].strip() != ''):
            description += '/' + transaction[19]
        return Transaction(sno,             #Sno
                           date,            #Date
                           '',              #TransType
                           description,     #Narration
                           '',              #Refno
                           date,            #ValueDate
                           withdrawal,      #Withdrawal
                           deposit,         #Deposit   
                           0.0,             #ClosingBalance
                           action,          #Action
                           transaction[7],  #Account
                           str(price));     #Price

