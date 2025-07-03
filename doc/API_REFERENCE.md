# API Reference

## Основные модели
- res.company: IDNO, IBAN, банковские реквизиты
- account.move: счета, интеграция с eFactura
- l10n_md_einvoice.soap: SOAP-клиент для eFactura
- l10n_md_bank.bank_statement: банковские выписки
- hr.payslip: payroll, demo-зарплаты

## Методы
- send_invoice(xml): отправка счета в eFactura
- generate_invoice_xml(...): генерация XML по XSD
- parse_csv_bank_statement, parse_sepa_bank_statement, parse_mt940_bank_statement: парсинг банковских файлов
