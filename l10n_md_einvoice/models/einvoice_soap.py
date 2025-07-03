from odoo import models, fields, api
from zeep import Client, Settings
from zeep.transports import Transport
import requests

class EinvoiceSoapClient(models.Model):
    _name = 'l10n_md_einvoice.soap'
    _description = 'eFactura SOAP Integration'

    wsdl_url = fields.Char('WSDL URL', default='https://efactura.sfs.md/ws/InvoiceService.svc?wsdl')
    username = fields.Char('API Username')
    password = fields.Char('API Password')

    def send_invoice(self, invoice_xml, actor_role=1, xml_status=0):
        # SOAP client init
        session = requests.Session()
        session.verify = True
        transport = Transport(session=session, timeout=20)
        settings = Settings(strict=False, xml_huge_tree=True)
        client = Client(wsdl=self.wsdl_url, transport=transport, settings=settings)
        # Auth
        client.set_ns_prefix('wsse', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd')
        client.transport.session.auth = (self.username, self.password)
        # Формируем запрос
        request_id = self.env['ir.sequence'].next_by_code('l10n_md_einvoice.soap.reqid') or 'REQ-0001'
        try:
            result = client.service.PostInvoices(
                RequestId=request_id,
                InvoicesXml=invoice_xml,
                ActorRole=actor_role,
                InvoicesXmlStatus=xml_status
            )
            return result
        except Exception as e:
            return {'error': str(e)}
