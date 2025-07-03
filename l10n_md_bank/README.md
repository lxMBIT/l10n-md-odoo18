# l10n_md_bank: Импорт/экспорт банковских файлов (CSV, SEPA, MT940) для Odoo 18

## Поддерживаемые форматы
- **CSV**: `date,description,amount,currency,partner,reference`
- **SEPA XML**: pain.053 (ISO 20022)
- **MT940**: SWIFT (текстовый)

## Примеры файлов
### CSV
```
date,description,amount,currency,partner,reference
2025-07-01,EUR payment,1000,EUR,Acme,REF100
2025-07-01,Duplicate,1000,EUR,Acme,REF100  # дубль
2025-13-01,Bad date,100,USD,Bad,BADREF     # ошибка формата
```

### SEPA (фрагмент)
```xml
<Ntry>
  <BookgDt><Dt>2025-07-02</Dt></BookgDt>
  <Amt Ccy="EUR">500</Amt>
  <NtryRef>SEPA100</NtryRef>
  <AddtlNtryInf>SEPA EUR</AddtlNtryInf>
  <NtryDtls><TxDtls><RltdPties><Cdtr><Nm>Beta</Nm></Cdtr></RltdPties></TxDtls></NtryDtls>
</Ntry>
```

### MT940 (фрагмент)
```
:20:START
:61:250703C300,USD
:86:MT940100
:61:250703C300,USD
:86:MT940100  # дубль
:61:250703Cbad,USD
:86:BADAMT     # ошибка формата
```

## Edge-case сценарии
- Валютные операции (EUR, USD)
- Дублирующиеся reference (ошибка)
- Ошибки формата (неверная дата, сумма, пустой reference)

## Использование
- Импорт через метод `import_bank_file(file_content, file_type)`
- Поддержка автоматического создания выписок и строк
- Ошибки возвращаются в виде `{'error': ...}`

## Автотесты
Запуск:
```
odoo --test-enable -d <db> -i l10n_md_bank
```
Покрытие: импорт edge-case файлов для всех форматов, проверка ошибок и успешных сценариев.

## Demo-данные
Включены в `demo/bank_statement_demo.xml` — содержат валютные операции, дубли, ошибки формата для всех форматов.

