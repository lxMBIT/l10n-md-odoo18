{
    'name': 'Moldova - Accounting',
    'website': 'https://statistica.gov.md/',
    'author': 'Odoo S.A., Moldova Community',
    'icon': '/account/static/description/l10n.png',
    'countries': ['md'],
    'category': 'Accounting/Localizations/Account Charts',
    'version': '1.0',
    'depends': [
        'account',
        'base_vat',
    ],
    'auto_install': False,
    'description': """
Модуль локализации бухгалтерии для Республики Молдова для Odoo 18.
Включает план счетов, налоги, группы, банки, шаблоны отчётов, demo-данные, переводы, национальные реквизиты компаний.
""",
    'data': [
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'data/account_tax_report_data.xml',
        'data/account_tax_report_data_pnl.xml',
        'data/account_tax_report_data_cashflow.xml',
'account_report_balance_md.xml',    'account_report_pnl_md.xml',    'account_report_cashflow_md.xml',
        'data/res.bank.csv',
        'data/template/account.account-md.csv',
        'data/template/account.fiscal.position-md.csv',
        'data/template/account.group-md.csv',
        'data/template/account.journal-md.csv',
        'data/template/account.payment.term-md.csv',
        'data/template/account.tax.group-md.csv',
        'data/template/account.tax-md.csv',
    ],
    'demo': [
        'demo/demo_company.xml',
        'demo/demo_account.xml',
        'demo/demo_tax.xml',
        'demo/demo_bank.xml',
        'demo/demo_invoice_sale.xml',
        'demo/demo_invoice_purchase.xml',
        'demo/demo_tax_social.xml',
    ],
    'license': 'LGPL-3',
}
