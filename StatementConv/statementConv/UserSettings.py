from StatementParser import *;
from TransactionReader import *;
class UserSetting(object):
    def __init__(self, inputFile, accountName, prefix):
        self.outputFileFolder = "output\\"
        self.simpleTransactionFileName = 'SimpleTransaction.csv';
        self.missedTransactionFileName = 'MissedTransaction.csv'
        self.GNUCashFormatFileName = 'GNUCashFormat.csv';
        self.VRFormatFileName = 'VRFormat.csv';
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
        if ('HDFCSec' in accountName):
            self.statementParser = HDFCSecStatementParser();
            if (extension == 'xls'):
                self.reader = HDFCSecExcelReader();
        elif ('HDFC' in accountName):
            self.statementParser = HDFCStatementParser();
            if (extension == 'xls'):
                self.reader = HDFCExcelReader();
        elif (accountName == 'SBI'):
            self.statementParser = SBIStatementParser();
            if (extension == 'xls'):
                self.reader = SBIExcelReader();
        elif (accountName == 'AllahabadBank'):
            self.statementParser = AllahabadBankStatementParser();
            if (extension == 'xls'):
                self.reader = AllahabadBankExcelReader();
        elif (accountName == 'IDBI'):
            self.statementParser = IDBIStatementParser();
            if (extension == 'xls'):
                self.reader = IDBIExcelReader();
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
        elif ('GNU' in accountName):
            self.statementParser = GNUStatementParser();
            if (extension == 'xls'):
                self.reader = ExcelReader();
        elif ('LVBank' in accountName):
            self.statementParser = LVBankStatementParser1();
            if (extension == 'xls'):
                self.reader = ExcelReader();
        elif ('LVB-Saving' in accountName):
            self.statementParser = LVBankStatementParser1();
            if (extension == 'xls'):
                self.reader = LVBankExcelReader();
        elif ('LVB-Current' in accountName):
            self.statementParser = LVBankStatementParser1();
            if (extension == 'xls'):
                self.reader = LVBankExcelReader();
        self.ttMapFName = 'TTMap\\TTMap-' + accountName + '-' + prefix + '.txt';
        if (accountName == 'MF'):
            self.atMapFName = 'TTMap\\ATMap-' + accountName + '-' + prefix + '.txt';
            self.ttMapFName = 'TTMap\\TTMap-' + accountName + '-' + prefix + '.txt';

    def CreatePathName(self):
        self.outputSimpleTransaction = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.simpleTransactionFileName;
        self.outputMissedTransaction = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.missedTransactionFileName;
        self.outputGNUCashFormat = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.GNUCashFormatFileName;
        self.outputVRFormat = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.VRFormatFileName;
        self.ttMapFName = self.settingFolder + self.ttMapFName;
        
        

class SiddharthSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(SiddharthSetting, self).__init__(inputFile, accountName, 'Siddharth');
        if (accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC Bank';
            self.ttMapFName = 'TTMap\\TTMap-HDFC-Siddharth.txt'
        elif(accountName == 'SBI'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:State Bank Of India';
            self.ttMapFName = 'TTMap\\TTMap-SBI-Siddharth.txt'
        elif(accountName == 'MF'):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMap\\TTMap-MF-Siddharth.txt'
            self.atMapFName = 'TTMap\\ATMap-MF-Siddharth.txt'
        self.CreatePathName();

class DadSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(DadSetting, self).__init__(inputFile, accountName, 'Dad');
        if(accountName == 'AllahabadBank'):
            self.fullAccountPath = 'Assets:Current Assets:Saving Account:Allahabad Bank Durg 64099';
            self.ttMapFName = 'TTMap\\TTMap-Allahabad-Dad.txt'
        elif(accountName == 'IDBI'):
            self.fullAccountPath = 'Assets:Current Assets:Saving Account:IDBI Bank 136136';
            self.ttMapFName = 'TTMap\\TTMap-IDBI-Dad.txt'
        elif(accountName == 'MF'):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMap\\TTMap-MF-Dad.txt'
            self.atMapFName = 'TTMap\\ATMap-MF-Dad.txt'
        elif (accountName == 'LVSaving'):
            self.fullAccountPath = 'Assets:Current Assets:Bank Account:LVB - Saving';
            self.ttMapFName = 'TTMap\\TTMap-LVB-Saving-Dad.txt';
            self.atMapFName = 'TTMap\\ATMap-LVB-Saving-Dad.txt';
        elif (accountName == 'LVCurrent'):
            self.fullAccountPath = 'Assets:Current Assets:Bank Account:LVB - Current';
            self.ttMapFName = 'TTMap\\TTMap-LVB-Current-Dad.txt';
            self.atMapFName = 'TTMap\\ATMap-LVB-Current-Dad.txt';
        self.CreatePathName();
    
class ShreyanshSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(ShreyanshSetting, self).__init__(inputFile, accountName, 'Bro');
        
        if (accountName == 'HDFC8072'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC Bank 50100193708072';
            #self.ttMapFName = 'TTMap\\TTMap-HDFC8072-Bro.txt'
        elif (accountName == 'HDFC9771'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC BANK 50100061339771';
            #self.ttMapFName = 'TTMap\\TTMap-HDFC9771-Bro.txt'
        elif(accountName == 'BOB'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:Bank Of Baroda 02495';
            #self.ttMapFName = 'TTMap\\TTMap-BOB-Bro.txt'
        elif(accountName == 'LVB-Current'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:Laxhmi Vilas 1421';
        elif(accountName == 'LVB-Saving'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:Laxhmi Vilas 0319';
        elif(accountName == 'MF'):
            self.fullAccountPath = '';
            #self.ttMapFName = 'TTMap\\TTMap-MF-Bro.txt'
            #self.atMapFName = 'TTMap\\ATMap-MF-Bro.txt'
        self.CreatePathName();

class MomSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(MomSetting, self).__init__(inputFile, accountName, 'Mom');
        if(accountName == 'BOB'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:Bank of Baroda S/B 01446';
            self.ttMapFName = 'TTMap\\TTMap-BOB-Mom.txt';
        elif(accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:H.D.F.C S/B 09151870000121';
            self.ttMapFName = 'TTMap\\TTMap-HDFC-Mom.txt';
        elif(accountName == 'LVB-Saving'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:LVB - Saving';
            self.ttMapFName = 'TTMap\\TTMap-LVB-Saving-Mom.txt';
        elif(accountName == 'LVB-Saving'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:LVB - Current';
            self.ttMapFName = 'TTMap\\TTMap-LVB-Current-Mom.txt';
        self.CreatePathName();

class ShwetaSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(ShwetaSetting, self).__init__(inputFile, accountName, 'Shweta');
        if(accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC Bank';
            self.ttMapFName = 'TTMap\\TTMap-HDFC-Shweta.txt';
        self.CreatePathName();

class DiptiSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(DiptiSetting,self).__init__(inputFile, accountName, 'Dipti');
        if (accountName == 'FINDIA' or accountName == 'MF' ):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMapMFDip.txt';
            self.atMapFName = 'ATMapMFDip.txt';
        if (accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC 2414';
            self.ttMapFName = 'TTMap\\TTMap-HDFC-Dipti.txt'
        if (accountName == 'SBI'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:SBI';
            self.ttMapFName = 'TTMap\\TTMap-SBI-Dipti.txt'
        if (accountName == 'HDFCSec'):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMap\\TTMap-HDFCSec-Dipti.txt'
            self.atMapFName = 'TTMap\\ATMap-HDFCSec-Dipti.txt';
        self.CreatePathName();

class VFSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(VFSetting,self).__init__(inputFile, accountName, 'VF');
        if (accountName == 'LVBank'):
            self.fullAccountPath = 'Assets:Current Assets:Current Account:LVB-Current';
            self.ttMapFName = 'TTLVBankVF.txt';
            self.atMapFName = 'ATMapBankVF.txt';
        self.CreatePathName();

class GNUCashSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(GNUCashSetting, self).__init__(inputFile, accountName, 'GNU');
        if(accountName == 'GNU'):
            self.fullAccountPath='';
            self.ttMapFName = 'TTMapMFGnu.txt';
            self.atMapFName = 'ATMapMFGnu.txt';
        self.CreatePathName();