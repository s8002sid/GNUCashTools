from MyEnum import TTEnum;
from Transaction import Transaction;
from Utility.CSV import CSV;
from datetime import datetime;
from datetime import timedelta;
from Utility.Utility import *;
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
                           Utility.GetDate(transaction[0]),#date
                           '',                          #transtype
                           transaction[2],              #narration
                           transaction[3],              #refno
                           Utility.GetDate(transaction[1]),#valuedate
                           withdrawal,                  #withdrawal
                           deposit,                     #deposit
                           closingBalance,              #closingbalance
                           '',                          #action
                           '',                          #account
                           '1'                          #Price
                           );

class AllahabadBankStatementParser(StatementParser):
    """
    Date
    ValueDate
    Description
    Debit
    Credit
    Balance
    """
    def Parse(self, transaction, sno):
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;
        if (transaction[3].strip() != ''):
            withdrawal = float(transaction[3]);
        if (transaction[4].strip() != ''):
            deposit = float(transaction[4]);
        if (transaction[5].strip() != ''):
            closingBalance = float(transaction[5].replace('CR', ''));
        return Transaction(sno,
                           transaction[0].replace('/', '-'),#date
                           '',                          #transtype
                           transaction[2],              #narration
                           '',                          #refno
                           transaction[1].replace('/', '-'),#valuedate
                           withdrawal,                  #withdrawal
                           deposit,                     #deposit
                           closingBalance,              #closingbalance
                           '',                          #action
                           '',                          #account
                           '1'                          #Price
                           );

class IDBIStatementParser(StatementParser):
    """
    SL No
    Date
    ValueDate
    Description
    ChequeNO
    CR/DR
    TxnType
    Amount
    Balance
    """
    def Parse(self, transaction, sno):
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;
        if (transaction[5].strip() == 'CR'):
            deposit = float(transaction[7]);
        elif (transaction[5].strip() == 'DR'):
            withdrawal = float(transaction[7]);
        if (transaction[8].strip() != ''):
            closingBalance = float(transaction[8]);
        chqNo = '';
        if (transaction[4].strip() != ''):
            chqNo = chqNo + ' Cheque No.: ' + transaction[4].strip();
        return Transaction(sno,
                           Utility.GetDate(transaction[1]),#date
                           '',                          #transtype
                           transaction[3] + chqNo,      #narration
                           '',                          #refno
                           Utility.GetDate(transaction[2]),#valuedate
                           withdrawal,                  #withdrawal
                           deposit,                     #deposit
                           closingBalance,              #closingbalance
                           '',                          #action
                           '',                          #account
                           '1'                          #Price
                           );
class HDFCSecStatementParser(StatementParser):
    """
    Date
    Exchange
    Symbol
    Action
    Order Qty
    DisclQty
    ExecQty
    OrderPrice
    TriggerPrice
    BookType
    Sett. Type
    Terminal ID
    OrderType
    Source
    Product
    Status
    Reason
    HSL Ref No
    Exch Order No
    BasketID
    """
    def Parse(self, transaction, sno):
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;
        narration = '';
        amount = float(transaction[6]);
        if (transaction[3].strip() == 'BUY'):
            deposit = amount;
        elif (transaction[3].strip() == 'SELL'):
            withdrawal = amount;
        narration = 'Exchange: ' + transaction[1] + ' Symbol: ' + transaction[2] + ' HSL Ref No: ' + transaction[17];
        narration += ' Exch Order No: ' + transaction[18] + ' Basket ID: ' + transaction[19] + 'Action: ' + transaction[3];
        return Transaction(sno,
                           Utility.GetDate(transaction[0].split(' ')[0]),#date
                           '', #transtype
                           narration,      #narration
                           '',             #refno
                           Utility.GetDate(transaction[0].split(' ')[0]),#valuedate
                           withdrawal,                  #withdrawal
                           deposit,                     #deposit
                           closingBalance,              #closingbalance
                           transaction[3],              #action
                           narration,                   #account
                           transaction[7]               #Price
                           );

class BOBStatementParser(StatementParser):
    """
    SrNo, Date, Description, Checque No, Debit Amount, Credit Amt, Balance, Value Date
    """

    def Parse(self, transaction, sno):
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;
        if (transaction[4].strip().replace('-','').replace(',','').replace('Cr','') != ''):
            withdrawal = float(transaction[4].replace('-','').replace(',','').replace('Cr',''));
        if (transaction[5].strip().replace('-','').replace(',','').replace('Cr','') != ''):
            deposit = float(transaction[5].replace('-','').replace(',','').replace('Cr',''));
        if (transaction[6].strip().replace('-','').replace(',','').replace('Cr','') != ''):
            closingBalance = float(transaction[6].replace('-','').replace(',','').replace('Cr',''));
        return Transaction(sno,
                           Utility.GetDate(transaction[1]),
                           '',
                           transaction[2],
                           transaction[3],
                           Utility.GetDate(transaction[7]),
                           withdrawal,
                           deposit,
                           closingBalance,
                           '',
                           '',
                           '1');

class LVBankStatementParser(StatementParser):
    """
    TrDate, ValDate, RefNO, TransDisc, D/C, Amount, Running Balance
    """

    def Parse(self, transaction, sno):
        withdrawal = 0.00;
        deposit = 0.00;
        closingBalance = 0.00;

        if (transaction[4].strip() == 'C'):
            deposit = float(transaction[5]);
        elif (transaction[4].strip() == 'D'):
            withdrawal = float(transaction[5]);
        if (deposit < 0):
            withdrawal = -deposit;
            deposite = 0.0;
        elif (withdrawal < 0):
            deposit = -withdrawal;
            withdrawal = 0.0;
        closingBalance = transaction[6];
        #sno, date, transtype, narration, refno, valuedate, withdrawal, deposit, closingbalance, action, account, price
        return Transaction(sno,
                           Utility.GetDate(transaction[1]),
                           '',
                           transaction[3],
                           transaction[2],
                           Utility.GetDate(transaction[0]),
                           withdrawal,
                           deposit,
                           closingBalance,
                           '',
                           '',
                           '1');
                                 

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
        date = Utility.GetDate(transaction[17]);
        description += ' TXN No: ' + transaction[13];
        units = float(transaction[14]);
        amount = float(transaction[15]);
        price = float(transaction[16]);
        description += ' Folio No. ' + transaction[18];
        withdrawal = 0.0;
        deposit = 0.0;
        numShares = float(transaction[14]);
        action = ''
        if (transaction[4].strip() == 'Redeem'):
            withdrawal = numShares;
            action = 'Sell';
        else:
            deposit = numShares;
            action = 'Buy';
        price = amount/numShares;
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

class FIndiaStatementParser(StatementParser):
    def Parse(self, transaction, sno):
        #TransactionRefNo, empty, empty, account, folio number, blank, date, blank, blank, price, unit, amount
        #sno
        date = Utility.GetDate(transaction[6]);
        transType= '';
        description = '';
        description += 'REFNo: ' + transaction[0];
        description += ' Folio: ' + transaction[4];
        refNo = '';
        withdrawal = 0;
        deposit = float(transaction[10]);
        closingBalance = 0;
        action = 'Buy';
        account = transaction[3];
        price = transaction[9];
        return Transaction(sno,
                           date,
                           transType,
                           description,
                           refNo,
                           date,
                           withdrawal,
                           deposit,
                           closingBalance,
                           action,
                           account,
                           price);

class GNUStatementParser(StatementParser):
    def Parse(self, transaction, sno):
        #Date, empty, empty, empty, empty, empty, empty, action, empty, empty, account, empty, unit, empty, empty, price
        #sno
        if (transaction[0].strip() == ''):
            return;
        date = Utility.GetDate(transaction[0]);
        transType= '';
        description = transaction[10];
        refNo = '';
        action = transaction[7];
        deposit = withdrawal = 0;
        if(action.lower() == 'buy'):
            deposit = float(transaction[12]);
        else:
            withdrawal = -float(transaction[12]);
        closingBalance = 0;
        account = transaction[10];
        price = str(self.CalPrice(transaction[15]));
        return Transaction(sno,
                           date,
                           transType,
                           description,
                           refNo,
                           date,
                           withdrawal,
                           deposit,
                           closingBalance,
                           action,
                           account,
                           price);
    def CalPrice(self, price):
        price = price.replace(' ', '');
        tmp = price.split('+');
        if(len(tmp) == 1):
            return float(tmp[0]);
        a=float(tmp[0]);
        tmp = tmp[1].split('/');
        if(len(tmp) == 1):
            return a+float(tmp[0]);
        return a+(float(tmp[0])/float(tmp[1]));