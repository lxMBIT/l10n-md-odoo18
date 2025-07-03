{
    'name': 'Moldova E-Invoice Integration',
    'version': '1.0.0',
    'category': 'Accounting',
    'summary': 'Integration with Moldova e-invoice.md',
    'author': 'lxMBIT',
    'website': 'https://github.com/lxMBIT/l10n-md-odoo18',
    'depends': ['base', 'account'],
    'data': [
        'demo/einvoice_invoice_demo.xml',
    ],
    'demo': [
        'demo/einvoice_invoice_demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': 'Integration with Moldova e-invoice.md. See doc/EINVOICE_API.md for API details.'
}
