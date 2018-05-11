from MyEnum import TTEnum;
from Transaction import Transaction;
class StatementParser:
    def Parse(self, transaction, sno):
        print("This function must not get called");
    def RemoveCommaFromNarration(self, transaction):
        print("This function must not get called");
    __Parse = Parse;
    __RemoveCommaFromNarration = RemoveCommaFromNarration;
    
class HDFCStatementParser(StatementParser):
    def Parse(self, transaction, sno):
        return Transaction(sno,
                           transaction[0].replace('/', '-'),  #date
                           '',              #transtype
                           transaction[1],  #narration
                           transaction[2],  #refno
                           transaction[3].replace('/', '-'),  #valuedate
                           transaction[4],  #withdrawal
                           transaction[5],  #deposit
                           transaction[6]   #closingbalance
                           );
    def RemoveCommaFromNarration(self, transaction):
        if (len(transaction) == 8):
            transaction

class HDFCEditedStatementParser(StatementParser):
    def Parse(self, transaction, sno):
        return Transaction(sno,             #sno
                           transaction[0].replace('/', '-'),  #date
                           transaction[1],  #transtype
                           transaction[2],  #narration
                           transaction[3],  #refno
                           transaction[4].replace('/', '-'),  #valuedate
                           transaction[5],  #withdrawal
                           transaction[6],  #deposit
                           transaction[7]   #closingbalance
                           )
class Statement:
    def __init__(self, transactions, parser):
        self.transactions = [];
        transactions = [e.replace('\n', '').split(',') for e in transactions];
        for i in range(len(transactions)):
            self.transactions.append(parser.Parse(transactions[i], i));
    
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