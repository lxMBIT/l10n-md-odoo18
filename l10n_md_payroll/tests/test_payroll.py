from odoo.tests.common import TransactionCase

class TestMoldovaPayroll(TransactionCase):
    def test_cnas_cnam_rules(self):
        employee = self.env['hr.employee'].create({'name': 'Test Employee'})
        contract = self.env['hr.contract'].create({
            'name': 'Test Contract',
            'employee_id': employee.id,
            'wage': 10000,
            'struct_id': self.env.ref('l10n_md_payroll.hr_payroll_structure_md').id,
        })
        payslip = self.env['hr.payslip'].create({
            'employee_id': employee.id,
            'contract_id': contract.id,
            'struct_id': contract.struct_id.id,
            'date_from': '2025-07-01',
            'date_to': '2025-07-31',
        })
        payslip.compute_sheet()
        cnas_emp = payslip.line_ids.filtered(lambda l: l.code == 'CNAS_EMP')
        cnam_emp = payslip.line_ids.filtered(lambda l: l.code == 'CNAM_EMP')
        self.assertAlmostEqual(cnas_emp.total, 600.0, places=2)
        self.assertAlmostEqual(cnam_emp.total, 900.0, places=2)
