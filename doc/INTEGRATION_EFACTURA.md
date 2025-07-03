# Интеграция с eFactura (SIA e-invoice.md)

## Протокол
- SOAP поверх HTTPS (SSL)
- Формат обмена: XML по XSD-схемам

## Настройка
1. Создайте пользователя API с ролью "Директор" в интерфейсе eFactura
2. Получите WSDL-URL, логин и пароль
3. В настройках Odoo заполните поля wsdl_url, username, password в модели l10n_md_einvoice.soap

## Пример использования
- Сформируйте XML с помощью l10n_md_einvoice.xml_template
- Отправьте через метод send_invoice SOAP-клиента
- Обрабатывайте статусы (1 — принято, 2 — успешно, 3 — ошибка)

## Пример кода
```
xml = env[l10n_md_einvoice.xml_template].generate_invoice_xml(...)
result = env[l10n_md_einvoice.soap].send_invoice(xml)
```

## Ошибки и статусы
- 1 — принято к исполнению
- 2 — успешно
- 3 — ошибка (см. поле error)

## Ограничения
- Не более 5000 запросов/час
- Все поля должны соответствовать XSD-схеме

## Тестирование
- Используйте автотест l10n_md_einvoice/tests/test_einvoice_soap_demo.py

