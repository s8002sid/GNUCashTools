﻿from Statement import *;
from Transaction import *;
from MyEnum import *;
from Utility.Utility import *;
"""
This file contain statement exporter functions.
"""
"""
Base class of statement exporter.
"""
class StatementExporter:
    def __init__(self, statement, writeHeader):
        self.statement = statement;
        self.writeHeader = writeHeader;

    """
    Inheriting class must provide String list representation for exporting statement.
    """
    def ToString(self):
        print("This function should never get called.");

"""
Simple Statement Exporter
"""
class SimpleStatementExporter(StatementExporter):
    def WriteHeader(self):
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
    def DoWriteIthTransaction(self, i):
        return 1;
    def ToString(self):
        ToWrite=[];
        if (self.writeHeader):
            ToWrite.append(self.WriteHeader());
        else:
            ToWrite.append("");
        #Values
        for i in range(len(self.statement.transactions)):
            if (self.DoWriteIthTransaction(i) == 1):
                x = '';
                value = self.statement.transactions[i].value;
                x+= str(value[TTEnum.SNO]) + ',';
                x+=value[TTEnum.Date] + ',';
                x+=value[TTEnum.TransType] + ',';
                x+=value[TTEnum.Narration] + ',';
                x+=value[TTEnum.Refno] + ',';
                x+=value[TTEnum.ValueDate] + ',';
                x+=str(value[TTEnum.Withdrawal]) + ',';
                x+=str(value[TTEnum.Deposit]) + ',';
                x+=str(value[TTEnum.ClosingBalance]);
                ToWrite.append(x);
        return ToWrite;

"""
If this class is used for exporting statement then output will contain transaction whose transtype field has not been updated.
"""
class NonUpdatedStatement(SimpleStatementExporter):
    def DoWriteIthTransaction(self, i):
        if(self.statement.transactions[i].updated == 1):
            return 0;
        return 1;

"""
Export statement in GNUCash understandable format
"""
class GNUCashStatement(StatementExporter):
    def ToString(self):
        ToWrite = [];
        #Write Header
        x="";
        if (self.writeHeader):
            x+= "Date,";
            x+= "Description,";
            x+= "Transaction Commodity,";
            x+= "Account,";
            x+= "Deposit,";
            x+= "Withdrawal,";
            x+= "Price,"
            x+= "TransferAccount,"
            x+= "Action"
        ToWrite.append(x);
        for i in range(len(self.statement.transactions)):
            value = self.statement.transactions[i].value;
            deposit = '"' + Utility.NumberToCurrency(value[TTEnum.Deposit]) + '"';
            withdrawal = '"' + Utility.NumberToCurrency(value[TTEnum.Withdrawal]) + '"';
            x="";
            x+= value[TTEnum.Date] + ",";
            x+= value[TTEnum.Narration] + ",";      #Description
            x+= "CURRENCY::INR,";                   #Commodity/Currency
            x+= value[TTEnum.Account] + ',';        #Full Account Name
            x+= deposit + ',';                      #Deposit
            x+= withdrawal + ',';                   #Withdrawal
            x+= value[TTEnum.Price] + ',';          #Rate/Price
            x+= value[TTEnum.TransType] + ',';      #TransferAccount
            x+= value[TTEnum.Action];               #Action;
            ToWrite.append(x);
        return ToWrite;

class ValueResearchStatement(StatementExporter):
    def ToString(self):
        ToWrite = [];
        x="";
        if (self.writeHeader):
            x+= "Date of transaction,";
            x+= "Fund name,";
            x+= "Number of units transacted,";
            x+= "Transaction type"
        ToWrite.append(x);
        for i in range(len(self.statement.transactions)):
            value = self.statement.transactions[i].value;
            x="";             
            x+= value[TTEnum.Date] + ",";
            x+= value[TTEnum.Account] + ",";
            x+= str(value[TTEnum.Withdrawal] + value[TTEnum.Deposit]) + ',';
            x+= value[TTEnum.Action];
            ToWrite.append(x);
        return ToWrite;