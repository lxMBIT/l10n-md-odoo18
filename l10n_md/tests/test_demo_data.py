
from odoo.tests.common import TransactionCase

class TestMoldovaDemoData(TransactionCase):
    def test_demo_company_exists(self):
        company = self.env['res.company'].search([('idno', '=', '1002600043210')], limit=1)
        self.assertTrue(company, 'Demo Moldova company not found')
    def test_demo_invoice_sale_exists(self):
        invoice = self.env['account.move'].search([('move_type', '=', 'out_invoice')], limit=1)
        self.assertTrue(invoice, 'Demo sale invoice not found')
    def test_demo_invoice_purchase_exists(self):
        invoice = self.env['account.move'].search([('move_type', '=', 'in_invoice')], limit=1)
        self.assertTrue(invoice, 'Demo purchase invoice not found')
