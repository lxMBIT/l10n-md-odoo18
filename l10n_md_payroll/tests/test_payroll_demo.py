from odoo.tests.common import TransactionCase

class TestMoldovaPayrollDemo(TransactionCase):
    def test_demo_structure_and_rules(self):
        struct = self.env['hr.payroll.structure'].search([('code', '=', 'MD_BASE')], limit=1)
        self.assertTrue(struct, 'Payroll structure MD_BASE not loaded')
        rule_cnas = self.env['hr.salary.rule'].search([('code', '=', 'CNAS_EMP')], limit=1)
        self.assertTrue(rule_cnas, 'CNAS Employee rule not loaded')
        rule_cnam = self.env['hr.salary.rule'].search([('code', '=', 'CNAM_EMP')], limit=1)
        self.assertTrue(rule_cnam, 'CNAM Employee rule not loaded')
