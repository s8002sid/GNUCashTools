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
        tmp = inputFile.split('.');
        if (len(tmp) == 1 or tmp[1] == ''):
                raise ValueError("File doesnot have extension");
        extension = tmp[1];
        if (extension == 'csv'):
            self.reader = CSVReader();

        if ('HDFC' in accountName):
            self.statementParser = HDFCStatementParser();
            if (extension == 'xls'):
                self.reader = HDFCExcelReader();
            
        elif (accountName == 'SBI'):
            self.statementParser = SBIStatementParser();
            if (extension == 'xls'):
                self.reader = SBIExcelReader();
        elif (accountName == 'SBI'):
            self.statementParser = SBIStatementParser();
            if (extension == 'xls'):
                self.reader = SBIExcelReader();
        elif (accountName == 'MF'):
            self.statementParser = MFStatementParser();
            if (extension == 'xls'):
                self.reader = ExcelReader();
        elif ('BOB' in accountName):
            self.statementParser = BOBStatementParser();
            if (extension == 'xls'):
                self.reader = BOBExcelReader();
        elif ('FINDIA' in accountName):
            self.statementParser = FIndiaStatementParser();
            if (extension == 'xls'):
                self.reader = FIndiaExcelReader();



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
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMapMFSid.txt'
            self.atMapFName = 'ATMapMFSid.txt'
        self.CreatePathName();
    
class ShreyanshSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(ShreyanshSetting, self).__init__(inputFile, accountName, 'Shr');
        
        if (accountName == 'HDFC8072'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC Bank 50100193708072';
            self.ttMapFName = 'TTMapHDFC8072Shr.txt'
        elif (accountName == 'HDFC9771'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC BANK 50100061339771';
            self.ttMapFName = 'TTMapHDFC9771Shr.txt'
        elif(accountName == 'SBI'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:State Bank Of India';
            self.ttMapFName = 'TTMapSBISid.txt'
        elif(accountName == 'BOB'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:Bank Of Baroda 02495';
            self.ttMapFName = 'TTMapBOBShr.txt'
        elif(accountName == 'MF'):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMapMFSid.txt'
            self.atMapFName = 'ATMapMFSid.txt'
        self.CreatePathName();

class DiptiSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(DiptiSetting,self).__init__(inputFile, accountName, 'Dip');
        if (accountName == 'FINDIA'):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMapMFDip.txt';
            self.atMapFName = 'ATMapMFDip.txt';
        self.CreatePathName();