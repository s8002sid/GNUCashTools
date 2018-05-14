from Statement import Statement;
from ExportStatement import *;
from StatementParser import *;
from UserSettings import *;
import re;
from Utility.Utility import Utility;
from TransactionReader import *;

sidSet = SiddharthSetting('SBI', r'C:\Users\siddjain\Google Drive\Home\Documents\Accounts\Statement\Bank\Sid\SBI_2017-2018.xls');
transactions = sidSet.reader.Read(sidSet.inputFile);
statement=Statement(transactions, sidSet.statementParser, sidSet.fullAccountPath, sidSet.ttMapFName, sidSet.atMapFName);
simpleStatementExporter = SimpleStatementExporter(statement);
nonUpdatedStatementExporter = NonUpdatedStatement(statement);
gnucashFormat = GNUCashStatement(statement);

Utility.WriteStatement(simpleStatementExporter, sidSet.outputSimpleTransaction);
Utility.WriteStatement(nonUpdatedStatementExporter, sidSet.outputMissedTransaction);
Utility.WriteStatement(gnucashFormat, sidSet.outputGNUCashFormat);

statement.WriteWordStat(r"output\WordStat.txt");
