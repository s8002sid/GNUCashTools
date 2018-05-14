from StatementParser import *;
from TransactionReader import *;
class UserSetting(object):
    def __init__(self, inputFile, accountName, prefix):
        self.outputFileFolder = "output\\"
        self.simpleTransactionFileName = 'SimpleTransaction.csv';
        self.missedTransactionFileName = 'MissedTransaction.csv'
        self.GNUCashFormatFileName = 'GNUCashFormat.csv';
        self.settingFolder = '.\\';
        self.inputfileFolder = '';
        self.inputFileName = '';
        self.ttMapFName = '';
        self.atMapFName = ''
        self.fullAccountPath = '';
        self.inputFile = inputFile;
        self.accountName = accountName;
        self.prefix = prefix;
        if (accountName == 'HDFC'):
            self.statementParser = HDFCStatementParser();
            tmp = inputFile.split('.');
            if (len(tmp) == 1 or tmp[1] == ''):
                raise ValueError("File doesnot have extension");
            extension = tmp[1];
            if (extension == 'xls'):
                self.reader = HDFCExcelReader();
            elif (extension == 'csv'):
                self.reader = CSVReader();
        if (accountName == 'SBI'):
            self.statementParser = SBIStatementParser();
            tmp = inputFile.split('.');
            if (len(tmp) == 1 or tmp[1] == ''):
                raise ValueError("File doesnot have extension");
            extension = tmp[1];
            if (extension == 'xls'):
                self.reader = SBIExcelReader();
            elif (extension == 'csv'):
                self.reader = CSVReader();


    def CreatePathName(self):
        self.outputSimpleTransaction = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.simpleTransactionFileName;
        self.outputMissedTransaction = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.missedTransactionFileName;
        self.outputGNUCashFormat = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.GNUCashFormatFileName;
        self.ttMapFName = self.settingFolder + self.ttMapFName;
        
        

class SiddharthSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(SiddharthSetting, self).__init__(inputFile, accountName, 'Sid');
        
        if (accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC Bank';
            self.ttMapFName = 'TTMapHDFCSid.txt'
        elif(accountName == 'SBI'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:State Bank Of India';
            self.ttMapFName = 'TTMapSBISid.txt'
        elif(accountName == 'MF'):
            self.fullAccountPath = 'Assets:Investment:Mutual Fund';
            self.ttMapFName = 'TTMapMFSid.txt'
            self.atMapFName = 'ATMapMFSid.txt'
        self.CreatePathName();
    

