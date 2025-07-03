{
    'name': 'Moldova Payroll',
    'version': '1.0.0',
    'category': 'Payroll',
    'summary': 'Payroll rules and reports for Moldova',
    'author': 'lxMBIT',
    'website': 'https://github.com/lxMBIT/l10n-md-odoo18',
    'depends': ['base', 'hr_payroll'],
    'data': [
        'data/payroll_structure_md.xml',
        'report/report_payroll_cnas.xml',
    ],
    'demo': [],
    'test': [
        'tests/test_payroll.py',
    ],
    'i18n': [
        'i18n/md.po',
        'i18n/ru.po',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': 'Payroll rules, reports, translations and tests for Moldova. See doc/PAYROLL.md.'
}
