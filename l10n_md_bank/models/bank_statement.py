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

from .parsers import parse_csv_bank_statement, parse_sepa_bank_statement, parse_mt940_bank_statement, BankFileParseError
from odoo import models, api, _

class BankStatementMD(models.Model):
    _inherit = 'l10n_md_bank.bank_statement'

    @api.model
    def import_bank_file(self, file_content, file_type):
        """
        Импорт банковского файла (CSV, SEPA, MT940) с поддержкой edge-case.
        file_type: 'csv', 'sepa', 'mt940'
        """
        try:
            if file_type == 'csv':
                lines = parse_csv_bank_statement(file_content)
            elif file_type == 'sepa':
                lines = parse_sepa_bank_statement(file_content)
            elif file_type == 'mt940':
                lines = parse_mt940_bank_statement(file_content)
            else:
                raise BankFileParseError(_('Unknown file type: %s') % file_type)
        except BankFileParseError as e:
            return {'error': str(e)}
        # Пример создания выписки и строк
        statement = self.create({
            'name': _('Imported Statement'),
            'date': lines[0]['date'] if lines else False,
            'bank_account': 'DEMO',
            'currency_id': False,
            'line_ids': [(0, 0, {
                'date': l['date'],
                'description': l['description'],
                'amount': l['amount'],
                'partner_name': l['partner_name'],
                'reference': l['reference'],
            }) for l in lines]
        })
        return {'statement_id': statement.id, 'lines': len(lines)}
