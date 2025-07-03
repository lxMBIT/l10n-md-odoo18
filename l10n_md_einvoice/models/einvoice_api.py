import requests
from odoo import models, fields, api

class EinvoiceAPI(models.Model):
    _name = 'l10n_md_einvoice.api'
    _description = 'e-Invoice.md API Integration'

    url = fields.Char('API URL', default='https://api.einvoice.md/v1/invoices')
    token = fields.Char('API Token')

    def send_invoice(self, invoice_data):
        headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        try:
            resp = requests.post(self.url, json=invoice_data, headers=headers, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {'error': str(e)}
