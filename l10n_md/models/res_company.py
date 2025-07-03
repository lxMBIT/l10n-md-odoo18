from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'
    idno = fields.Char(string='IDNO (Moldova)')
    iban = fields.Char(string='IBAN')
