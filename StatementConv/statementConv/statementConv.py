from Statement import Statement;
from ExportStatement import *;
from StatementParser import *;
from UserSettings import *;
import re;
from Utility.Utility import Utility;
from TransactionReader import *;
import json;
import os;
#To use this scripts install python 2.7
#Install following modules: emun34, xlrd, python-lambda
#These scripts are not compitable with python 3.x

def ReadTransaction(set, writeHeader):
    transactions = set.reader.Read(set.inputFile);
    statement=Statement(transactions, set.statementParser, set.fullAccountPath, set.ttMapFName, set.atMapFName);
    nonUpdatedStatementExporter = NonUpdatedStatement(statement, writeHeader);
    simpleStatementExporter = SimpleStatementExporter(statement, writeHeader);
    return transactions, statement, nonUpdatedStatementExporter, simpleStatementExporter;

def WriteGNUCTransaction(wordStatFile, set, writeHeader):
    transactions, statement, nonUpdatedStatementExporter, simpleStatementExporter = ReadTransaction(set, writeHeader);
    gnucashFormat = GNUCashStatement(statement, writeHeader);
    Utility.WriteStatement(simpleStatementExporter, set.outputSimpleTransaction);
    Utility.WriteStatement(nonUpdatedStatementExporter, set.outputMissedTransaction);
    Utility.WriteStatement(gnucashFormat, set.outputGNUCashFormat);
    statement.WriteWordStat(wordStatFile);

def WriteVRTransaction(set, writeHeader):
    transactions, statement, nonUpdatedStatementExporter, simpleStatementExporter = ReadTransaction(set, writeHeader);
    vrFormat = ValueResearchStatement(statement, writeHeader);
    Utility.WriteStatement(vrFormat, set.outputVRFormat);

def CheckAndRemoveFile(filePath):
    if (os.path.isfile(filePath)):
        os.remove(filePath);
def GenerateUsingJson(jsonFilePath):
    fob = open(jsonFilePath, "r+");
    jsonData = "\n".join(fob.readlines());
    fob.close();
    parsedJsonData = json.loads(jsonData);
    jsonArrayLen = len(parsedJsonData["statements"]);
    deletedFileStat = [];
    for i in range(len(parsedJsonData["statements"])):
        Transaction.transTypeMap = [];
        Transaction.accountTypeMap = [];
        excelPath = parsedJsonData["statements"][i]["excelPath"];
        type = parsedJsonData["statements"][i]["type"];
        #One of SBI BOB HDFC AllahabadBank LVBank MF
        name = parsedJsonData["statements"][i]["name"];
        genFormat = [];
        if (parsedJsonData["statements"][i].get("generate")):
            genFormat = parsedJsonData["statements"][0]["generate"];
        else:
            genFormat.append('gnuCash')

        settingFunc = DiptiSetting;
        if (name == 'Dipti'):
            settingFunc = DiptiSetting;
        elif (name == 'Siddharth'):
            settingFunc = SiddharthSetting;
        elif (name == 'Mom'):
            settingFunc = MomSetting;
        elif (name == 'Shweta'):
            settingFunc = ShwetaSetting;
        elif (name == 'Dad'):
            settingFunc = DadSetting;
        elif (name == 'VardhamanFinance'):
            settingFunc = VFSetting;
        elif (name == 'Shreyansh'):
            settingFunc = ShreyanshSetting;
        set = settingFunc(type, excelPath);
        wordStatFile = r'output\WordStat' + name + '.txt';
        writeHeader = False;
        if (name not in deletedFileStat):
            CheckAndRemoveFile(os.getcwd() + wordStatFile);
            deletedFileStat.append(name);
            writeHeader = True;
        if (name + type not in deletedFileStat):
            CheckAndRemoveFile(os.getcwd() + '\\'+ set.outputSimpleTransaction);
            CheckAndRemoveFile(os.getcwd() + '\\' + set.outputMissedTransaction);
            CheckAndRemoveFile(os.getcwd() + '\\' + set.outputGNUCashFormat);
            CheckAndRemoveFile(os.getcwd() + '\\' + set.outputVRFormat);
            deletedFileStat.append(name+type);
            writeHeader = True;
        if ('gnuCash' in genFormat):
            WriteGNUCTransaction(wordStatFile, set, writeHeader);
        if ('vrFormat' in genFormat):
            WriteVRTransaction(set, writeHeader);
#jsonFilePath=r'C:\sj\GoogleDrive\Home\Share\Dilip-Share\Document\Account\Statement\MFU\JSON\Transaction.JSON';
jsonFilePath=r'C:\sj\GoogleDrive\Home\Share\Dilip-Share\Document\Account\Statement\Transaction.JSON'
GenerateUsingJson(jsonFilePath);
#Dipti SBI Account Generator
#set = DiptiSetting('SBI', r'C:\Users\siddjain\Google Drive\Home\Share\Dipti-Share\Document\Account\Statement\Bank\SBI_2017-2018.xls');

#Mom BOB Account Generator
#set = MomSetting('BOB', r'C:\Users\siddjain\Google Drive\Home\Share\Chandra-Share\Document\Account\Statement\BOB_2017-2018.xls');

#Mom HDFC Account Generator
#set = MomSetting('HDFC', r'C:\Users\siddjain\Google Drive\Home\Share\Chandra-Share\Document\Account\Statement\2017-2018.xls');

#Shweta HDFC Account Generator
#set = ShwetaSetting('HDFC', r'C:\Users\siddjain\Google Drive\Home\Share\Shweta-Share\Document\Account\Statement\Bank\2017-2018.xls');

#Dad AllahabadBank Setting
#set = DadSetting('AllahabadBank', r'C:\Users\siddjain\Google Drive\Home\Share\Dilip-Share\Document\Account\Statement\Bank\2017-2018-04-08.xls');
#set = DadSetting('AllahabadBank', r'C:\Users\siddjain\Google Drive\Home\Share\Dilip-Share\Document\Account\Statement\Bank\2017-2018-09-01.xls');
#set = DadSetting('AllahabadBank', r'C:\Users\siddjain\Google Drive\Home\Share\Dilip-Share\Document\Account\Statement\Bank\2017-2018-02-03.xls');
#set = VFSetting('LVBank', r'C:\sj\GoogleDrive\Home\Share\Dilip-Share\VardhamanFinance\Document\Account\Bank\Book1.xls');
#WriteGNUCTransaction(r"output\WordStat.txt", set);
#WriteGNUCTransaction(r"output\WordStat.txt", set);

#set = DiptiSetting('HDFC', r'C:\Users\siddjain\Google Drive\Home\Share\Dipti-Share\Document\Account\Statement\Bank\2017-2018.xls');


#sidSet = SiddharthSetting('SBI', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\Bank\Sid\SBI_2017-2018.xls');
#sidSet = SiddharthSetting('MF', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\MutualFund\Sid\NOB_201712.xls');
#sidSet = ShreyanshSetting('BOB', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\Bank\Bro\BOB_2017-2018.xls');


#transactions = sidSet.reader.Read(sidSet.inputFile);
#statement=Statement(transactions, sidSet.statementParser, sidSet.fullAccountPath, sidSet.ttMapFName, sidSet.atMapFName);
#simpleStatementExporter = SimpleStatementExporter(statement);
#nonUpdatedStatementExporter = NonUpdatedStatement(statement);
#gnucashFormat = GNUCashStatement(statement);

#Utility.WriteStatement(simpleStatementExporter, sidSet.outputSimpleTransaction);
#Utility.WriteStatement(nonUpdatedStatementExporter, sidSet.outputMissedTransaction);
#Utility.WriteStatement(gnucashFormat, sidSet.outputGNUCashFormat);

#statement.WriteWordStat(r"output\WordStat.txt");

#sidSet = DiptiSetting('GNU', r'C:\Users\siddjain\Documents\excludingDipti.csv');
#transactions = sidSet.reader.Read(sidSet.inputFile);
#statement=Statement(transactions, sidSet.statementParser, sidSet.fullAccountPath, sidSet.ttMapFName, sidSet.atMapFName);
#statement.WriteWordStat(r"output\WordStat.txt");
#vrStatementExporter = ValueResearchStatement(statement);
#Utility.WriteStatement(vrStatementExporter, r'output\vrStatement.csv');

#nonUpdatedStatementExporter = NonUpdatedStatement(statement);
#Utility.WriteStatement(nonUpdatedStatementExporter, sidSet.outputMissedTransaction);