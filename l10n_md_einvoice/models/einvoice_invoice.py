
from odoo import models, fields

class L10nMdEinvoiceInvoice(models.Model):
    _name = 'l10n_md_einvoice.invoice'
    _description = 'Moldova E-Invoice'

    name = fields.Char(string='Invoice Number', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    date_invoice = fields.Date(string='Invoice Date', required=True)
    amount_total = fields.Monetary(string='Total Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')
    einvoice_xml = fields.Binary(string='E-Invoice XML')
    einvoice_md_id = fields.Char(string='e-invoice.md ID')
