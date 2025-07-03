from odoo.tests.common import TransactionCase

class TestI18n(TransactionCase):
    def test_idno_translation(self):
        self.env.user.lang = 'ru_RU'
        field = self.env['ir.model.fields'].search([('model', '=', 'res.company'), ('name', '=', 'idno')], limit=1)
        self.assertTrue(field, 'IDNO field not found')
        label = field.field_description
        self.assertIn('IDNO', label)
