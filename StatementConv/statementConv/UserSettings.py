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
        elif ('LVSaving' in accountName):
            self.statementParser = LVBankStatementParser1();
            if (extension == 'xls'):
                self.reader = LVBankExcelReader();
        elif ('LVCurrent' in accountName):
            self.statementParser = LVBankStatementParser1();
            if (extension == 'xls'):
                self.reader = LVBankExcelReader();


    def CreatePathName(self):
        self.outputSimpleTransaction = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.simpleTransactionFileName;
        self.outputMissedTransaction = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.missedTransactionFileName;
        self.outputGNUCashFormat = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.GNUCashFormatFileName;
        self.outputVRFormat = self.outputFileFolder + self.prefix + '-' + self.accountName + '-' + self.VRFormatFileName;
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

class DadSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(DadSetting, self).__init__(inputFile, accountName, 'Dad');
        if(accountName == 'AllahabadBank'):
            self.fullAccountPath = 'Assets:Current Assets:Saving Account:Allahabad Bank Durg 64099';
            self.ttMapFName = 'TTMapAllahabadBankDad.txt'
        elif(accountName == 'IDBI'):
            self.fullAccountPath = 'Assets:Current Assets:Saving Account:IDBI Bank 136136';
            self.ttMapFName = 'TTMapIDBIDad.txt'
        elif(accountName == 'MF'):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMapMFDad.txt'
            self.atMapFName = 'ATMapMFDad.txt'
        elif (accountName == 'LVSaving'):
            self.fullAccountPath = 'Assets:Current Assets:Bank Account:LVB - Saving';
            self.ttMapFName = 'TTMapLVSDad.txt';
            self.atMapFName = 'ATMapLVSDad.txt';
        elif (accountName == 'LVCurrent'):
            self.fullAccountPath = 'Assets:Current Assets:Bank Account:LVB - Current';
            self.ttMapFName = 'TTMapLVCDad.txt';
            self.atMapFName = 'ATMapLVCDad.txt';
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
            self.ttMapFName = 'TTMapMFShr.txt'
            self.atMapFName = 'ATMapMFShr.txt'
        self.CreatePathName();

class MomSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(MomSetting, self).__init__(inputFile, accountName, 'Cha');
        if(accountName == 'BOB'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:Bank of Baroda S/B 01446';
            self.ttMapFName = 'TTMapBOBCha.txt';
        elif(accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:H.D.F.C S/B 09151870000121';
            self.ttMapFName = 'TTMapHDFCCha.txt';
        self.CreatePathName();

class ShwetaSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(ShwetaSetting, self).__init__(inputFile, accountName, 'Shw');
        if(accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC Bank';
            self.ttMapFName = 'TTMapHDFCShw.txt';
        self.CreatePathName();

class DiptiSetting(UserSetting):
    def __init__(self, accountName, inputFile):
        super(DiptiSetting,self).__init__(inputFile, accountName, 'Dip');
        if (accountName == 'FINDIA' or accountName == 'MF' ):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMapMFDip.txt';
            self.atMapFName = 'ATMapMFDip.txt';
        if (accountName == 'HDFC'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:HDFC 2414';
            self.ttMapFName = 'TTMapHDFCDip.txt'
        if (accountName == 'SBI'):
            self.fullAccountPath = 'Assets:Current Assets:Savings Account:SBI';
            self.ttMapFName = 'TTMapSBIDip.txt'
        if (accountName == 'HDFCSec'):
            self.fullAccountPath = '';
            self.ttMapFName = 'TTMapHDFCSecDip.txt'
            self.atMapFName = 'ATMapHDFCSecDip.txt';
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