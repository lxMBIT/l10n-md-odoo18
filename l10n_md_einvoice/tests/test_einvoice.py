from odoo.tests.common import TransactionCase

class TestMoldovaEinvoice(TransactionCase):
    def test_demo_invoice_loaded(self):
        invoice = self.env['l10n_md_einvoice.invoice'].search([('name', '=', 'INV-MD-0001')], limit=1)
        self.assertTrue(invoice, 'Demo e-invoice not loaded')
        self.assertEqual(invoice.einvoice_md_id, 'MD-INV-0001')
        self.assertEqual(invoice.amount_total, 1500.00)
        self.assertEqual(invoice.state, 'draft')
