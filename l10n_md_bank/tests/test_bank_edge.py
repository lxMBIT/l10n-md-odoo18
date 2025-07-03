from odoo.tests.common import TransactionCase

class TestBankEdge(TransactionCase):
    def test_invalid_format(self):
        res = self.env['l10n_md_bank.bank_statement'].create({
            'name': 'BAD/2025/001',
            'date': '2025-07-01',
            'bank_account': 'INVALID',
            'currency_id': self.env.ref('base.MDL').id,
            'line_ids': [(0, 0, {'date': '2025-07-01', 'description': 'Ошибка', 'amount': 100, 'partner_name': 'X', 'reference': 'REF'})]
        })
        self.assertIn('MD', res.bank_account or '', 'IBAN должен начинаться с MD')

    def test_duplicate_statement(self):
        s1 = self.env['l10n_md_bank.bank_statement'].create({'name': 'DUP/2025/001', 'date': '2025-07-01', 'bank_account': 'MD24AG00000002210001300415', 'currency_id': self.env.ref('base.MDL').id})
        with self.assertRaises(Exception):
            self.env['l10n_md_bank.bank_statement'].create({'name': 'DUP/2025/001', 'date': '2025-07-01', 'bank_account': 'MD24AG00000002210001300415', 'currency_id': self.env.ref('base.MDL').id})

    def test_currency_operation(self):
        res = self.env['l10n_md_bank.bank_statement'].create({
            'name': 'CUR/2025/001',
            'date': '2025-07-01',
            'bank_account': 'MD24AG00000002210001300415',
            'currency_id': self.env.ref('base.USD').id,
            'line_ids': [(0, 0, {'date': '2025-07-01', 'description': 'USD операция', 'amount': 500, 'partner_name': 'Y', 'reference': 'USDREF'})]
        })
        self.assertEqual(res.currency_id.name, 'USD')
