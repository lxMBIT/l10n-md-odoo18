{
    'name': 'Moldova E-Invoice Integration',
    'version': '1.0.0',
    'category': 'Accounting',
    'summary': 'Integration with Moldova e-invoice.md',
    'author': 'lxMBIT',
    'website': 'https://github.com/lxMBIT/l10n-md-odoo18',
    'depends': ['base', 'account'],
    'data': [
        'views/api_autogen_views.xml',
        'views/xml_template_autogen_views.xml',
        'views/invoice_autogen_views.xml',
        'views/soap_autogen_views.xml',
        'views/einvoice_send_wizard_view.xml',
        'views/account_move_button_einvoice.xml',
        'demo/einvoice_invoice_demo.xml',
    ],
    'demo': [
        'demo/einvoice_invoice_demo.xml',
    ],
    'test': [
        'tests/test_einvoice.py',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': 'Integration with Moldova e-invoice.md. See doc/EINVOICE_API.md for API details.'
}
