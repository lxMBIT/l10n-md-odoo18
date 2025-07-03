from odoo import models

class EinvoiceXmlTemplate(models.AbstractModel):
    _name = 'l10n_md_einvoice.xml_template'
    _description = 'eFactura XML Template Generator'

    def generate_invoice_xml(self, supplier_idno, buyer_idno, seria, number, total, total_tva, items):
        items_xml = '\n'.join([
            f"<Row Code='{item['code']}' Name='{item['name']}' UnitOfMeasure='{item['uom']}' Quantity='{item['qty']}' UnitPriceWithoutTVA='{item['price']}' TotalPriceWithoutTVA='{item['total_no_tva']}' TVA='{item['tva']}' TotalTVA='{item['total_tva']}' TotalPrice='{item['total']}' />"
            for item in items
        ])
        return f'''<Documents>\n  <Document>\n    <SupplierInfo>\n      <Seria>{seria}</Seria>\n      <Number>{number}</Number>\n      <Supplier IDNO='{supplier_idno}' />\n      <Buyer IDNO='{buyer_idno}' />\n      <Total>{total}</Total>\n      <TotalTVA>{total_tva}</TotalTVA>\n      <Merchandises>\n        {items_xml}\n      </Merchandises>\n    </SupplierInfo>\n  </Document>\n</Documents>'''
