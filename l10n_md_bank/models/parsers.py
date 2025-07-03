
import csv
from datetime import datetime
from odoo import _

class BankFileParseError(Exception):
    pass

def parse_csv_bank_statement(file_content):
    """
    Парсер CSV банковской выписки. Ожидает поля: date, description, amount, currency, partner, reference
    Поддержка edge-case: валютные операции, дубли, ошибки формата
    Возвращает: dict с ключами для создания BankStatementMD и BankStatementLineMD
    """
    lines = []
    seen_refs = set()
    reader = csv.DictReader(file_content.decode('utf-8').splitlines())
    for row in reader:
        try:
            # Проверка формата даты
            date = datetime.strptime(row['date'], '%Y-%m-%d').date()
            amount = float(row['amount'])
            currency = row.get('currency', 'MDL')
            reference = row.get('reference', '')
            # Проверка на дубли
            if reference in seen_refs:
                raise BankFileParseError(_('Duplicate reference: %s') % reference)
            seen_refs.add(reference)
            lines.append({
                'date': date,
                'description': row.get('description', ''),
                'amount': amount,
                'currency': currency,
                'partner_name': row.get('partner', ''),
                'reference': reference,
            })
        except Exception as e:
            raise BankFileParseError(_('Format error in row: %s, error: %s') % (row, e))
    return lines

import xml.etree.ElementTree as ET
from datetime import datetime
from odoo import _

class BankFileParseError(Exception):
    pass

def parse_sepa_bank_statement(file_content):
    """
    Парсер SEPA XML банковской выписки (pain.053). Поддержка edge-case: валютные операции, дубли, ошибки формата.
    Возвращает: list dict для создания BankStatementLineMD
    """
    lines = []
    seen_refs = set()
    try:
        root = ET.fromstring(file_content.decode('utf-8'))
        ns = {'ns': 'urn:iso:std:iso:20022:tech:xsd:pain.053.001.02'}
        for entry in root.findall('.//ns:Ntry', ns):
            date = entry.findtext('ns:BookgDt/ns:Dt', default='', namespaces=ns)
            if not date:
                raise BankFileParseError(_('Missing date in entry'))
            date = datetime.strptime(date, '%Y-%m-%d').date()
            amount = float(entry.findtext('ns:Amt', default='0', namespaces=ns))
            currency = entry.find('ns:Amt', ns).attrib.get('Ccy', 'MDL')
            reference = entry.findtext('ns:NtryRef', default='', namespaces=ns)
            if reference in seen_refs:
                raise BankFileParseError(_('Duplicate reference: %s') % reference)
            seen_refs.add(reference)
            description = entry.findtext('ns:AddtlNtryInf', default='', namespaces=ns)
            partner = entry.findtext('ns:NtryDtls/ns:TxDtls/ns:RltdPties/ns:Cdtr/ns:Nm', default='', namespaces=ns)
            lines.append({
                'date': date,
                'description': description,
                'amount': amount,
                'currency': currency,
                'partner_name': partner,
                'reference': reference,
            })
    except Exception as e:
        raise BankFileParseError(_('SEPA format error: %s') % e)
    return lines

import re
from datetime import datetime
from odoo import _

class BankFileParseError(Exception):
    pass

def parse_mt940_bank_statement(file_content):
    """
    Примитивный парсер MT940. Поддержка edge-case: валютные операции, дубли, ошибки формата.
    Возвращает: list dict для создания BankStatementLineMD
    """
    lines = []
    seen_refs = set()
    content = file_content.decode('utf-8')
    statements = re.split(r'(?=^:20:)', content, flags=re.MULTILINE)
    for statement in statements:
        if not statement.strip():
            continue
        try:
            date_match = re.search(r':61:(\d{6})', statement)
            if not date_match:
                raise BankFileParseError(_('Missing :61: date'))
            date = datetime.strptime(date_match.group(1), '%y%m%d').date()
            amount_match = re.search(r':61:\d{6}(C|D)([\d,]+)', statement)
            if not amount_match:
                raise BankFileParseError(_('Missing amount in :61:'))
            sign = 1 if amount_match.group(1) == 'C' else -1
            amount = sign * float(amount_match.group(2).replace(',', '.'))
            currency_match = re.search(r':61:.*?([A-Z]{3})', statement)
            currency = currency_match.group(1) if currency_match else 'MDL'
            ref_match = re.search(r':86:(.+)', statement)
            reference = ref_match.group(1).strip() if ref_match else ''
            if reference in seen_refs:
                raise BankFileParseError(_('Duplicate reference: %s') % reference)
            seen_refs.add(reference)
            description = reference
            lines.append({
                'date': date,
                'description': description,
                'amount': amount,
                'currency': currency,
                'partner_name': '',
                'reference': reference,
            })
        except Exception as e:
            raise BankFileParseError(_('MT940 format error: %s') % e)
    return lines
