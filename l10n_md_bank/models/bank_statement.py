from odoo import models, fields

class BankStatementMD(models.Model):
    _name = 'l10n_md_bank.bank_statement'
    _description = 'Bank Statement Moldova'

    name = fields.Char('Statement Reference', required=True)
    date = fields.Date('Date', required=True)
    bank_account = fields.Char('Bank Account (IBAN)', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    line_ids = fields.One2many('l10n_md_bank.bank_statement.line', 'statement_id', string='Lines')

class BankStatementLineMD(models.Model):
    _name = 'l10n_md_bank.bank_statement.line'
    _description = 'Bank Statement Line Moldova'

    statement_id = fields.Many2one('l10n_md_bank.bank_statement', string='Statement', required=True)
    date = fields.Date('Date', required=True)
    description = fields.Char('Description')
    amount = fields.Float('Amount', required=True)
    partner_name = fields.Char('Partner')
    reference = fields.Char('Reference')
