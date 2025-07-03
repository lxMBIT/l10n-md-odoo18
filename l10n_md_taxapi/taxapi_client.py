import requests
from odoo import models, fields, api

class TaxAPIClient(models.Model):
    _name = 'l10n_md_taxapi.client'
    _description = 'Tax Authority API Integration'

    url = fields.Char('API URL', default='https://api.tax.md/v1/declarations')
    token = fields.Char('API Token')

    def send_declaration(self, declaration_data):
        headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        try:
            resp = requests.post(self.url, json=declaration_data, headers=headers, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {'error': str(e)}
