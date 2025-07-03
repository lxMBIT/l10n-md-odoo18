from odoo.tests.common import TransactionCase

class TestBankImportEdge(TransactionCase):
    def setUp(self):
        super().setUp()
        self.bank_statement = self.env['l10n_md_bank.bank_statement']

    def test_import_csv_edge(self):
        csv_content = 'date,description,amount,currency,partner,reference\n2025-07-01,EUR payment,1000,EUR,Acme,REF100'.encode('utf-8')
        res = self.bank_statement.import_bank_file(csv_content, 'csv')
        assert 'statement_id' in res
        csv_content_dup = 'date,description,amount,currency,partner,reference\n2025-07-01,EUR payment,1000,EUR,Acme,REF100\n2025-07-01,Duplicate,1000,EUR,Acme,REF100'.encode('utf-8')
        res = self.bank_statement.import_bank_file(csv_content_dup, 'csv')
        assert 'error' in res
        csv_content_bad = 'date,description,amount,currency,partner,reference\n2025-13-01,Bad date,100,USD,Bad,BADREF'.encode('utf-8')
        res = self.bank_statement.import_bank_file(csv_content_bad, 'csv')
        assert 'error' in res

    def test_import_sepa_edge(self):
        sepa_content = '''<?xml version="1.0"?><Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.053.001.02"><BkToCstmrStmt><Stmt><Ntry><BookgDt><Dt>2025-07-02</Dt></BookgDt><Amt Ccy="EUR">500</Amt><NtryRef>SEPA100</NtryRef><AddtlNtryInf>SEPA EUR</AddtlNtryInf><NtryDtls><TxDtls><RltdPties><Cdtr><Nm>Beta</Nm></Cdtr></RltdPties></TxDtls></NtryDtls></Ntry></Stmt></BkToCstmrStmt></Document>'''.encode('utf-8')
        res = self.bank_statement.import_bank_file(sepa_content, 'sepa')
        assert 'statement_id' in res
        sepa_content_dup = '''<?xml version="1.0"?><Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.053.001.02"><BkToCstmrStmt><Stmt><Ntry><BookgDt><Dt>2025-07-02</Dt></BookgDt><Amt Ccy="EUR">500</Amt><NtryRef>SEPA100</NtryRef><AddtlNtryInf>Duplicate</AddtlNtryInf><NtryDtls><TxDtls><RltdPties><Cdtr><Nm>Beta</Nm></Cdtr></RltdPties></TxDtls></NtryDtls></Ntry><Ntry><BookgDt><Dt>2025-07-02</Dt></BookgDt><Amt Ccy="EUR">500</Amt><NtryRef>SEPA100</NtryRef><AddtlNtryInf>Duplicate</AddtlNtryInf><NtryDtls><TxDtls><RltdPties><Cdtr><Nm>Beta</Nm></Cdtr></RltdPties></TxDtls></NtryDtls></Ntry></Stmt></BkToCstmrStmt></Document>'''.encode('utf-8')
        res = self.bank_statement.import_bank_file(sepa_content_dup, 'sepa')
        assert 'error' in res
        sepa_content_bad = '''<?xml version="1.0"?><Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.053.001.02"><BkToCstmrStmt><Stmt><Ntry><BookgDt><Dt></Dt></BookgDt><Amt Ccy="USD">200</Amt><NtryRef></NtryRef><AddtlNtryInf>No ref</AddtlNtryInf></Ntry></Stmt></BkToCstmrStmt></Document>'''.encode('utf-8')
        res = self.bank_statement.import_bank_file(sepa_content_bad, 'sepa')
        assert 'error' in res

    def test_import_mt940_edge(self):
        mt940_content = ':20:START\n:61:250703C300,USD\n:86:MT940100'.encode('utf-8')
        res = self.bank_statement.import_bank_file(mt940_content, 'mt940')
        assert 'statement_id' in res
        mt940_content_dup = ':20:START\n:61:250703C300,USD\n:86:MT940100\n:61:250703C300,USD\n:86:MT940100'.encode('utf-8')
        res = self.bank_statement.import_bank_file(mt940_content_dup, 'mt940')
        assert 'error' in res
        mt940_content_bad = ':20:START\n:61:250703Cbad,USD\n:86:BADAMT'.encode('utf-8')
        res = self.bank_statement.import_bank_file(mt940_content_bad, 'mt940')
        assert 'error' in res
