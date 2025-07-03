from odoo.tests.common import TransactionCase

class TestBankStatementMD(TransactionCase):
    def test_demo_bank_statement(self):
        statement = self.env['l10n_md_bank.bank_statement'].search([('name', '=', 'MD20250701-001')])
        self.assertTrue(statement, 'Demo bank statement not found')
        self.assertEqual(len(statement.line_ids), 2, 'Demo bank statement should have 2 lines')
        self.assertEqual(statement.line_ids[0].amount, 10000.00)
        self.assertEqual(statement.line_ids[1].amount, -3500.00)
