from odoo.tests.common import TransactionCase

class TestEinvoiceSoapDemo(TransactionCase):
    def test_send_invoice_demo(self):
        xml_gen = self.env['l10n_md_einvoice.xml_template']
        xml = xml_gen.generate_invoice_xml(
            supplier_idno='1002600001257',
            buyer_idno='1002600003815',
            seria='EAA',
            number='000005424',
            total='124434.04',
            total_tva='22444.04',
            items=[{
                'code': '122414', 'name': 'Medicamente', 'uom': 'buc.', 'qty': 4, 'price': 142.4, 'total_no_tva': 1335.4, 'tva': 20, 'total_tva': 100, 'total': 10035.5
            }]
        )
        client = self.env['l10n_md_einvoice.soap']
        # В демо-режиме не отправляем реальный запрос, только проверяем формирование XML и структуру клиента
        self.assertIn('<Documents>', xml)
        self.assertTrue(hasattr(client, 'send_invoice'))
