# Руководство для разработчиков (Developer Guide)

## Структура модулей
- l10n_md: основной модуль, план счетов, налоги, demo-данные
- l10n_md_einvoice: интеграция с eFactura, генерация и отправка счетов, SOAP/REST API
- l10n_md_bank: банковские парсеры (CSV, SEPA, MT940), edge-case сценарии
- l10n_md_payroll: payroll, demo-зарплаты, правила, отчёты

## Основные принципы
- Все модели доступны через views/actions
- Автотесты для всех бизнес-сценариев
- Документация и примеры для каждого подмодуля
- Интеграция с CI/CD и миграциями

## Расширение
- Добавляйте новые модели через генератор pipeline
- Для новых интеграций — создавайте отдельные подмодули
- Все изменения — через pull request и review
