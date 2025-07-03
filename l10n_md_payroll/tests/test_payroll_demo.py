from odoo.tests.common import TransactionCase

class TestPayrollDemo(TransactionCase):
    def test_demo_payslip(self):
        payslip = self.env['hr.payslip'].search([('number', '=', 'PSL/2025/001')])
        self.assertTrue(payslip, 'Demo payslip not found')
        self.assertGreater(payslip.total, 0)
