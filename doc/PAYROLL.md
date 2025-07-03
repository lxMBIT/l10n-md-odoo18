# Moldova Payroll Extension

## Overview
Модуль l10n_md_payroll расширяет функционал расчёта зарплаты для Молдовы по аналогии с l10n_lt и l10n_pl.

## Salary Rules
- CNAS Employee (6%)
- CNAS Employer (18%)
- CNAM Employee (9%)
- CNAM Employer (0%)

## Reports
- CNAS Report (QWeb)

## Translations
- md.po, ru.po

## Autotests
- Тест расчёта взносов для payslip

## Demo
- payroll_structure_md.xml

## Установка
Добавьте модуль l10n_md_payroll в список установленных.

## Autotests
- Автотесты покрывают загрузку структуры, правил и demo-данных (test_payroll.py, test_payroll_demo.py).
