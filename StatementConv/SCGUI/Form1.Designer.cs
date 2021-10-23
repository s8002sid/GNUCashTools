namespace SCGUI
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.label1 = new System.Windows.Forms.Label();
            this.tboxExcelPath = new System.Windows.Forms.TextBox();
            this.tboxATFile = new System.Windows.Forms.TextBox();
            this.tboxFile = new System.Windows.Forms.TextBox();
            this.btnGenerate = new System.Windows.Forms.Button();
            this.cboxBank = new System.Windows.Forms.ComboBox();
            this.cboxName = new System.Windows.Forms.ComboBox();
            this.splitContainer2 = new System.Windows.Forms.SplitContainer();
            this.splitContainer3 = new System.Windows.Forms.SplitContainer();
            this.dataGridViewTT = new System.Windows.Forms.DataGridView();
            this.MatchString = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Account = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewAT = new System.Windows.Forms.DataGridView();
            this.dataGridViewMissed = new System.Windows.Forms.DataGridView();
            this.Sno = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Date = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.TransType = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Narration = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Reference = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ValueDate = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Withdrawal = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Deposit = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ClosingBalance = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.dataGridViewGNU = new System.Windows.Forms.DataGridView();
            this.gnuDate = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.gnuDescription = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.gnuAccount = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.gnuDeposit = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.gnuWithdrawal = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.gnuTransferAccount = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.MatchString1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Account1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).BeginInit();
            this.splitContainer2.Panel1.SuspendLayout();
            this.splitContainer2.Panel2.SuspendLayout();
            this.splitContainer2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer3)).BeginInit();
            this.splitContainer3.Panel1.SuspendLayout();
            this.splitContainer3.Panel2.SuspendLayout();
            this.splitContainer3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewTT)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewAT)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewMissed)).BeginInit();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewGNU)).BeginInit();
            this.SuspendLayout();
            // 
            // splitContainer1
            // 
            this.splitContainer1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.FixedPanel = System.Windows.Forms.FixedPanel.Panel1;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            this.splitContainer1.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.label1);
            this.splitContainer1.Panel1.Controls.Add(this.tboxExcelPath);
            this.splitContainer1.Panel1.Controls.Add(this.tboxATFile);
            this.splitContainer1.Panel1.Controls.Add(this.tboxFile);
            this.splitContainer1.Panel1.Controls.Add(this.btnGenerate);
            this.splitContainer1.Panel1.Controls.Add(this.cboxBank);
            this.splitContainer1.Panel1.Controls.Add(this.cboxName);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.splitContainer2);
            this.splitContainer1.Size = new System.Drawing.Size(987, 483);
            this.splitContainer1.SplitterDistance = 74;
            this.splitContainer1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(27, 41);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 17);
            this.label1.TabIndex = 7;
            this.label1.Text = "CSV Path";
            // 
            // tboxExcelPath
            // 
            this.tboxExcelPath.Location = new System.Drawing.Point(101, 38);
            this.tboxExcelPath.Name = "tboxExcelPath";
            this.tboxExcelPath.Size = new System.Drawing.Size(831, 22);
            this.tboxExcelPath.TabIndex = 6;
            // 
            // tboxATFile
            // 
            this.tboxATFile.Location = new System.Drawing.Point(582, 7);
            this.tboxATFile.Name = "tboxATFile";
            this.tboxATFile.ReadOnly = true;
            this.tboxATFile.Size = new System.Drawing.Size(198, 22);
            this.tboxATFile.TabIndex = 5;
            this.tboxATFile.TextChanged += new System.EventHandler(this.tboxATFile_TextChanged);
            // 
            // tboxFile
            // 
            this.tboxFile.Location = new System.Drawing.Point(384, 8);
            this.tboxFile.Name = "tboxFile";
            this.tboxFile.ReadOnly = true;
            this.tboxFile.Size = new System.Drawing.Size(192, 22);
            this.tboxFile.TabIndex = 4;
            this.tboxFile.TextChanged += new System.EventHandler(this.tboxFile_TextChanged);
            // 
            // btnGenerate
            // 
            this.btnGenerate.Location = new System.Drawing.Point(802, 8);
            this.btnGenerate.Name = "btnGenerate";
            this.btnGenerate.Size = new System.Drawing.Size(130, 23);
            this.btnGenerate.TabIndex = 3;
            this.btnGenerate.Text = "Generate";
            this.btnGenerate.UseVisualStyleBackColor = true;
            this.btnGenerate.Click += new System.EventHandler(this.btnGenerate_Click);
            // 
            // cboxBank
            // 
            this.cboxBank.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboxBank.FormattingEnabled = true;
            this.cboxBank.Location = new System.Drawing.Point(199, 7);
            this.cboxBank.Name = "cboxBank";
            this.cboxBank.Size = new System.Drawing.Size(179, 24);
            this.cboxBank.TabIndex = 1;
            this.cboxBank.SelectedIndexChanged += new System.EventHandler(this.cboxBank_SelectedIndexChanged);
            // 
            // cboxName
            // 
            this.cboxName.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboxName.FormattingEnabled = true;
            this.cboxName.Location = new System.Drawing.Point(14, 7);
            this.cboxName.Name = "cboxName";
            this.cboxName.Size = new System.Drawing.Size(179, 24);
            this.cboxName.TabIndex = 0;
            this.cboxName.SelectedIndexChanged += new System.EventHandler(this.cboxName_SelectedIndexChanged);
            // 
            // splitContainer2
            // 
            this.splitContainer2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer2.Location = new System.Drawing.Point(0, 0);
            this.splitContainer2.Name = "splitContainer2";
            this.splitContainer2.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer2.Panel1
            // 
            this.splitContainer2.Panel1.Controls.Add(this.splitContainer3);
            // 
            // splitContainer2.Panel2
            // 
            this.splitContainer2.Panel2.Controls.Add(this.tabControl1);
            this.splitContainer2.Size = new System.Drawing.Size(985, 403);
            this.splitContainer2.SplitterDistance = 200;
            this.splitContainer2.TabIndex = 0;
            // 
            // splitContainer3
            // 
            this.splitContainer3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer3.Location = new System.Drawing.Point(0, 0);
            this.splitContainer3.Name = "splitContainer3";
            // 
            // splitContainer3.Panel1
            // 
            this.splitContainer3.Panel1.Controls.Add(this.dataGridViewTT);
            // 
            // splitContainer3.Panel2
            // 
            this.splitContainer3.Panel2.Controls.Add(this.dataGridViewAT);
            this.splitContainer3.Size = new System.Drawing.Size(985, 200);
            this.splitContainer3.SplitterDistance = 485;
            this.splitContainer3.TabIndex = 0;
            // 
            // dataGridViewTT
            // 
            this.dataGridViewTT.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewTT.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.MatchString,
            this.Account});
            this.dataGridViewTT.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dataGridViewTT.Location = new System.Drawing.Point(0, 0);
            this.dataGridViewTT.Name = "dataGridViewTT";
            this.dataGridViewTT.RowTemplate.Height = 24;
            this.dataGridViewTT.Size = new System.Drawing.Size(485, 200);
            this.dataGridViewTT.TabIndex = 0;
            // 
            // MatchString
            // 
            this.MatchString.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.MatchString.HeaderText = "MatchString";
            this.MatchString.Name = "MatchString";
            this.MatchString.Width = 112;
            // 
            // Account
            // 
            this.Account.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Account.HeaderText = "Account";
            this.Account.Name = "Account";
            this.Account.Width = 88;
            // 
            // dataGridViewAT
            // 
            this.dataGridViewAT.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewAT.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.MatchString1,
            this.Account1});
            this.dataGridViewAT.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dataGridViewAT.Location = new System.Drawing.Point(0, 0);
            this.dataGridViewAT.Name = "dataGridViewAT";
            this.dataGridViewAT.RowTemplate.Height = 24;
            this.dataGridViewAT.Size = new System.Drawing.Size(496, 200);
            this.dataGridViewAT.TabIndex = 0;
            // 
            // dataGridViewMissed
            // 
            this.dataGridViewMissed.AllowUserToAddRows = false;
            this.dataGridViewMissed.AllowUserToDeleteRows = false;
            this.dataGridViewMissed.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewMissed.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Sno,
            this.Date,
            this.TransType,
            this.Narration,
            this.Reference,
            this.ValueDate,
            this.Withdrawal,
            this.Deposit,
            this.ClosingBalance});
            this.dataGridViewMissed.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dataGridViewMissed.Location = new System.Drawing.Point(3, 3);
            this.dataGridViewMissed.Name = "dataGridViewMissed";
            this.dataGridViewMissed.RowTemplate.Height = 24;
            this.dataGridViewMissed.Size = new System.Drawing.Size(971, 164);
            this.dataGridViewMissed.TabIndex = 0;
            // 
            // Sno
            // 
            this.Sno.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Sno.HeaderText = "Sno";
            this.Sno.Name = "Sno";
            this.Sno.ReadOnly = true;
            this.Sno.Width = 62;
            // 
            // Date
            // 
            this.Date.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Date.HeaderText = "Date";
            this.Date.Name = "Date";
            this.Date.ReadOnly = true;
            this.Date.Width = 67;
            // 
            // TransType
            // 
            this.TransType.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.TransType.HeaderText = "TransType";
            this.TransType.Name = "TransType";
            this.TransType.ReadOnly = true;
            this.TransType.Width = 106;
            // 
            // Narration
            // 
            this.Narration.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Narration.HeaderText = "Narration";
            this.Narration.Name = "Narration";
            this.Narration.ReadOnly = true;
            this.Narration.Width = 96;
            // 
            // Reference
            // 
            this.Reference.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Reference.HeaderText = "Reference";
            this.Reference.Name = "Reference";
            this.Reference.ReadOnly = true;
            this.Reference.Width = 103;
            // 
            // ValueDate
            // 
            this.ValueDate.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.ValueDate.HeaderText = "ValueDate";
            this.ValueDate.Name = "ValueDate";
            this.ValueDate.ReadOnly = true;
            this.ValueDate.Width = 103;
            // 
            // Withdrawal
            // 
            this.Withdrawal.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Withdrawal.HeaderText = "Withdrawal";
            this.Withdrawal.Name = "Withdrawal";
            this.Withdrawal.ReadOnly = true;
            this.Withdrawal.Width = 106;
            // 
            // Deposit
            // 
            this.Deposit.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Deposit.HeaderText = "Deposit";
            this.Deposit.Name = "Deposit";
            this.Deposit.ReadOnly = true;
            this.Deposit.Width = 85;
            // 
            // ClosingBalance
            // 
            this.ClosingBalance.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.ClosingBalance.HeaderText = "ClosingBalance";
            this.ClosingBalance.Name = "ClosingBalance";
            this.ClosingBalance.ReadOnly = true;
            this.ClosingBalance.Width = 134;
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl1.Location = new System.Drawing.Point(0, 0);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(985, 199);
            this.tabControl1.TabIndex = 1;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.dataGridViewMissed);
            this.tabPage1.Location = new System.Drawing.Point(4, 25);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(977, 170);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "MissedTransaction";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.dataGridViewGNU);
            this.tabPage2.Location = new System.Drawing.Point(4, 25);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(977, 170);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "GNUCash Transaction";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // dataGridViewGNU
            // 
            this.dataGridViewGNU.AllowUserToAddRows = false;
            this.dataGridViewGNU.AllowUserToDeleteRows = false;
            this.dataGridViewGNU.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewGNU.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.gnuDate,
            this.gnuDescription,
            this.gnuAccount,
            this.gnuDeposit,
            this.gnuWithdrawal,
            this.gnuTransferAccount});
            this.dataGridViewGNU.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dataGridViewGNU.Location = new System.Drawing.Point(3, 3);
            this.dataGridViewGNU.Name = "dataGridViewGNU";
            this.dataGridViewGNU.RowTemplate.Height = 24;
            this.dataGridViewGNU.Size = new System.Drawing.Size(971, 164);
            this.dataGridViewGNU.TabIndex = 0;
            // 
            // gnuDate
            // 
            this.gnuDate.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.gnuDate.HeaderText = "Date";
            this.gnuDate.Name = "gnuDate";
            this.gnuDate.Width = 67;
            // 
            // gnuDescription
            // 
            this.gnuDescription.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.gnuDescription.HeaderText = "Description";
            this.gnuDescription.Name = "gnuDescription";
            this.gnuDescription.Width = 108;
            // 
            // gnuAccount
            // 
            this.gnuAccount.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.gnuAccount.HeaderText = "Account";
            this.gnuAccount.Name = "gnuAccount";
            this.gnuAccount.Width = 88;
            // 
            // gnuDeposit
            // 
            this.gnuDeposit.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.gnuDeposit.HeaderText = "Deposit";
            this.gnuDeposit.Name = "gnuDeposit";
            this.gnuDeposit.Width = 85;
            // 
            // gnuWithdrawal
            // 
            this.gnuWithdrawal.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.gnuWithdrawal.HeaderText = "Withdrawal";
            this.gnuWithdrawal.Name = "gnuWithdrawal";
            this.gnuWithdrawal.Width = 106;
            // 
            // gnuTransferAccount
            // 
            this.gnuTransferAccount.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.gnuTransferAccount.HeaderText = "TransferAccount";
            this.gnuTransferAccount.Name = "gnuTransferAccount";
            this.gnuTransferAccount.Width = 142;
            // 
            // MatchString1
            // 
            this.MatchString1.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.MatchString1.HeaderText = "MatchString";
            this.MatchString1.Name = "MatchString1";
            this.MatchString1.Width = 112;
            // 
            // Account1
            // 
            this.Account1.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells;
            this.Account1.HeaderText = "Account";
            this.Account1.Name = "Account1";
            this.Account1.Width = 88;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(987, 483);
            this.Controls.Add(this.splitContainer1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel1.PerformLayout();
            this.splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.splitContainer2.Panel1.ResumeLayout(false);
            this.splitContainer2.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).EndInit();
            this.splitContainer2.ResumeLayout(false);
            this.splitContainer3.Panel1.ResumeLayout(false);
            this.splitContainer3.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer3)).EndInit();
            this.splitContainer3.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewTT)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewAT)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewMissed)).EndInit();
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewGNU)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.Button btnGenerate;
        private System.Windows.Forms.ComboBox cboxBank;
        private System.Windows.Forms.ComboBox cboxName;
        private System.Windows.Forms.SplitContainer splitContainer2;
        private System.Windows.Forms.SplitContainer splitContainer3;
        private System.Windows.Forms.DataGridView dataGridViewTT;
        private System.Windows.Forms.DataGridView dataGridViewAT;
        private System.Windows.Forms.DataGridView dataGridViewMissed;
        private System.Windows.Forms.TextBox tboxFile;
        private System.Windows.Forms.TextBox tboxATFile;
        private System.Windows.Forms.DataGridViewTextBoxColumn MatchString;
        private System.Windows.Forms.DataGridViewTextBoxColumn Account;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tboxExcelPath;
        private System.Windows.Forms.DataGridViewTextBoxColumn Sno;
        private System.Windows.Forms.DataGridViewTextBoxColumn Date;
        private System.Windows.Forms.DataGridViewTextBoxColumn TransType;
        private System.Windows.Forms.DataGridViewTextBoxColumn Narration;
        private System.Windows.Forms.DataGridViewTextBoxColumn Reference;
        private System.Windows.Forms.DataGridViewTextBoxColumn ValueDate;
        private System.Windows.Forms.DataGridViewTextBoxColumn Withdrawal;
        private System.Windows.Forms.DataGridViewTextBoxColumn Deposit;
        private System.Windows.Forms.DataGridViewTextBoxColumn ClosingBalance;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.DataGridView dataGridViewGNU;
        private System.Windows.Forms.DataGridViewTextBoxColumn gnuDate;
        private System.Windows.Forms.DataGridViewTextBoxColumn gnuDescription;
        private System.Windows.Forms.DataGridViewTextBoxColumn gnuAccount;
        private System.Windows.Forms.DataGridViewTextBoxColumn gnuDeposit;
        private System.Windows.Forms.DataGridViewTextBoxColumn gnuWithdrawal;
        private System.Windows.Forms.DataGridViewTextBoxColumn gnuTransferAccount;
        private System.Windows.Forms.DataGridViewTextBoxColumn MatchString1;
        private System.Windows.Forms.DataGridViewTextBoxColumn Account1;
    }
}

