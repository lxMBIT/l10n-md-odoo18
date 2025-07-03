from odoo.tests.common import TransactionCase

class TestEinvoiceDemo(TransactionCase):
    def test_demo_invoice(self):
        invoice = self.env['account.move'].search([('name', '=', 'EINV/2025/001')])
        self.assertTrue(invoice, 'Demo e-invoice not found')
        self.assertEqual(invoice.amount_total, 10000.00)
