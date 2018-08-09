import xlrd;
import unicodedata;
from Utility.CSV import *;
class TransactionReader(object):
    def Read(self, fileName):
        print('This function must not get called');

class CSVReader(TransactionReader):
    def Read(self, fileName):
        fob = open(fileName, "r");
        lines = fob.readlines();
        fob.close();
        lines = [e.replace('\n', '') for e in lines];
        for i in range(len(lines)):
            lines[i] = CSV.Tokenize(lines[i]);
        del lines[0];
        return lines;

class ExcelReader(TransactionReader):
    def __init__(self):
        self.transactionStartPoint = 1;
        self.transactionEndPoint = 0;

    def Read(self, fileName):
        wbook = xlrd.open_workbook(fileName);
        wsheet = wbook.sheet_by_index(0);
        transactions = [];
        for row in range(wsheet.nrows):
            transaction = [];
            for col in range(wsheet.ncols):
                text = wsheet.cell(row, col).value;
                if (type(text) is unicode):
                    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore');
                if (type(text) is float):
                    text = str(text);
                transaction.append(text);
            transactions.append(transaction);
            
        if (self.transactionStartPoint > 0 and 
            len(transactions) > self.transactionStartPoint):
            del transactions[:self.transactionStartPoint]

        if (self.transactionEndPoint > 0 and
            len(transactions) > self.transactionEndPoint):
            del transactions[(len(transactions)-self.transactionEndPoint):];
                
        return transactions;

class HDFCExcelReader(ExcelReader):
    def __init__(self):
        ExcelReader.__init__(self);
        self.transactionStartPoint = 22;
        self.transactionEndPoint = 18;

class HDFCSecExcelReader(ExcelReader):
    def __init__(self):
        ExcelReader.__init__(self);
        self.transactionStartPoint = 3;
        self.transactionEndPoint = 0;

class SBIExcelReader(ExcelReader):
    def __init__(self):
        ExcelReader.__init__(self);
        self.transactionStartPoint = 21;
        self.transactionEndPoint = 2;

class AllahabadBankExcelReader(ExcelReader):
    def __init__(self):
        ExcelReader.__init__(self);
        self.transactionStartPoint = 22;
        self.transactionEndPoint = 7;

class IDBIExcelReader(ExcelReader):
    def __init__(self):
        ExcelReader.__init__(self);
        self.transactionStartPoint = 7;
        self.transactionEndPoint = 0;

class BOBExcelReader(ExcelReader):
    def __init__(self):
        ExcelReader.__init__(self);
        self.transactionStartPoint = 15;
        self.transactionEndPoint = 3;
class FIndiaExcelReader(ExcelReader):
    def __init__(self):
        ExcelReader.__init__(self);
        self.transactionStartPoint = 2;
        self.transactionEndPoint = 0;