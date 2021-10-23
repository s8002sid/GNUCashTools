using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.IO;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.Text.RegularExpressions;

namespace SCGUI
{
    public partial class Form1 : Form
    {
        Dictionary<String, Data> database;
        private string basePath = @"..\..\..\statementConv\";
        private string mapBasePath = @"..\..\..\statementConv\TTMap\";
        public Form1()
        {
            InitializeComponent();
            database = SCXMLParser.Parse("db.xml");
            FillCBoxName();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            cboxName.SelectedIndex = 0;
            SetSplitterDistance();
        }

        private void cboxBank_SelectedIndexChanged(object sender, EventArgs e)
        {
            FillTextBox();
        }
        private void FillTextBox()
        {
            if (cboxName.Text == "" || cboxBank.Text == "")
            {
                return;
            }
            tboxFile.Text = database[cboxName.Text].bankAndMap[cboxBank.Text].Key;
            tboxATFile.Text = database[cboxName.Text].bankAndMap[cboxBank.Text].Value;
        }
        private void cboxName_SelectedIndexChanged(object sender, EventArgs e)
        {
            FillCBoxBank();
        }
        private void FillCBoxBank()
        {
            if (cboxName.Text == "")
                return;
            Data d = database[cboxName.Text];
            cboxBank.Items.Clear();
            foreach (KeyValuePair<String, KeyValuePair<String, String>> entry in d.bankAndMap)
            {
                cboxBank.Items.Add(entry.Key);
            }
            cboxBank.SelectedIndex = 0;
        }
        private void FillCBoxName()
        {
            foreach (KeyValuePair<String, Data> entry in database)
            {
                cboxName.Items.Add(entry.Key);
            }
            cboxName.SelectedIndex = 0;
        }
        private void SetSplitterDistance()
        {
            //SetEquidistantSplit(splitContainer1);
            SetEquidistantSplit(splitContainer2);
            SetEquidistantSplit(splitContainer3);
        }
        private void SetEquidistantSplit(SplitContainer container)
        {
            container.SplitterDistance = (container.Orientation == Orientation.Vertical ?
               container.Width : container.Height) / 2;
        }
        private void Form1_Resize(object sender, EventArgs e)
        {
            SetSplitterDistance();
        }

        private void tboxFile_TextChanged(object sender, EventArgs e)
        {
            FillDatagrid(dataGridViewTT, tboxFile.Text);
        }
        void WriteGridToFile(DataGridView view, string filePath)
        {
            StreamWriter writer = new StreamWriter(filePath);
            string toWrite = "";
            for (int i = 0; i < view.Rows.Count - 1; i++)
            {
                if (i != 0)
                    toWrite += "\n";
                toWrite += view.Rows[i].Cells[0].Value + "," + view.Rows[i].Cells[1].Value;
            }
            writer.Write(toWrite);
            writer.Close();
        }
        private string GetJsonKeyValue(string key, string value)
        {
            return "\t\"" + key + "\":\"" + value.Replace("\\", "\\\\") + "\"";
        }
        private void btnGenerate_Click(object sender, EventArgs e)
        {
            //Save Map File
            if (tboxFile.Text != "")
            {
                string filePath1 = mapBasePath + tboxFile.Text;
                WriteGridToFile(dataGridViewTT, filePath1);
            }
            if (tboxATFile.Text != "")
            {
                string filePath1 = mapBasePath + tboxATFile.Text;
                WriteGridToFile(dataGridViewAT, filePath1);
            }
            string json = "{\n";
            json += "\"statements\":[\n{\n";
            json += GetJsonKeyValue("excelPath", tboxExcelPath.Text) + ",\n";
            json += GetJsonKeyValue("type", cboxBank.Text) + ",\n";
            json += GetJsonKeyValue("name", cboxName.Text) + ",\n";
            json += "\t\"generate\": [\"gnuCash\"]\n";

            json += "}\n]\n";
            json += "}";

            string jsonFilePath = mapBasePath + "output.json";
            StreamWriter w = new StreamWriter(jsonFilePath);
            w.Write(json);
            w.Close();
            string missedExcelPath = String.Format("{0}\\{1}output\\{2}-{3}-MissedTransaction.csv", Directory.GetCurrentDirectory(), basePath, cboxName.Text, cboxBank.Text);
            string gnuCashExcelPath = String.Format("{0}\\{1}output\\{2}-{3}-GNUCashFormat.csv", Directory.GetCurrentDirectory(), basePath, cboxName.Text, cboxBank.Text);
            if (File.Exists(missedExcelPath)) File.Delete(missedExcelPath);
            if (File.Exists(gnuCashExcelPath)) File.Delete(gnuCashExcelPath);
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = "python.exe";
            start.WorkingDirectory = Directory.GetCurrentDirectory() + "\\"+ basePath;
            start.Arguments = Directory.GetCurrentDirectory()+ "\\" + basePath + "statementConv.py";
            start.UseShellExecute = false;
            start.CreateNoWindow = true;
            start.RedirectStandardOutput = false;
            start.RedirectStandardError = false;
            Process process = Process.Start(start);
            process.WaitForExit();
            if (File.Exists(missedExcelPath))
            {
                StreamReader reader = new StreamReader(missedExcelPath);
                string line;
                int counter = 0;
                dataGridViewMissed.Rows.Clear();
                while ((line = reader.ReadLine()) != null)
                {
                    counter++;
                    if (counter == 1)
                    {
                        continue;
                    }
                    int index = dataGridViewMissed.Rows.Add();
                    string[] splittedStr = line.Split(',');
                    for (int i = 0; i < dataGridViewMissed.Rows[index].Cells.Count; i++)
                    {
                        dataGridViewMissed.Rows[index].Cells[i].Value = splittedStr[i];
                    }
                }
                reader.Close();
            }
            if (File.Exists(gnuCashExcelPath))
            {
                StreamReader reader = new StreamReader(gnuCashExcelPath);
                string line;
                int counter = 0;
                dataGridViewGNU.Rows.Clear();
                Regex CSVParser = new Regex(",(?=(?:[^\"]*\"[^\"]*\")*(?![^\"]*\"))");
                while ((line = reader.ReadLine()) != null)
                {
                    counter++;
                    if (counter == 1)
                    {
                        continue;
                    }
                    int index = dataGridViewGNU.Rows.Add();
                    string[] splittedStr = CSVParser.Split(line);//line.Split(',');
                    dataGridViewGNU.Rows[index].Cells[0].Value = splittedStr[0].Replace("\"","");
                    dataGridViewGNU.Rows[index].Cells[1].Value = splittedStr[1].Replace("\"", "");
                    dataGridViewGNU.Rows[index].Cells[2].Value = splittedStr[3].Replace("\"", "");
                    dataGridViewGNU.Rows[index].Cells[3].Value = splittedStr[4].Replace("\"", "").Replace("0.0","");
                    dataGridViewGNU.Rows[index].Cells[4].Value = splittedStr[5].Replace("\"", "").Replace("0.0", ""); ;
                    dataGridViewGNU.Rows[index].Cells[5].Value = splittedStr[7].Replace("\"", "");
                }
                reader.Close();
            }
        }
        private void FillDatagrid(DataGridView view, string fileName)
        {
            view.Rows.Clear();
            String filePath = mapBasePath + fileName;
            string line;
            try
            {
                StreamReader file =
                    new StreamReader(filePath);
                DataGridViewRow dr;
                while ((line = file.ReadLine()) != null)
                {
                    dr = (DataGridViewRow)view.Rows[0].Clone();
                    dr.Cells[0].Value = line.Split(',')[0];
                    dr.Cells[1].Value = line.Split(',')[1];
                    view.Rows.Add(dr);
                }

                file.Close();
            }
            catch
            {

            }
        }
        private void tboxATFile_TextChanged(object sender, EventArgs e)
        {
            FillDatagrid(dataGridViewAT, tboxATFile.Text);
        }
    }
}
