"""
Генерация PDF-дайджеста ИТ-департамента Smart Horizon.
Возвращает PDF-файл в base64 для скачивания на фронтенде.
"""

import base64
import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT


DARK_BG = colors.HexColor("#070f1c")
CYAN = colors.HexColor("#00bcd4")
LIGHT_GRAY = colors.HexColor("#8899aa")
WHITE = colors.HexColor("#e8f0f8")
BORDER = colors.HexColor("#142030")


def build_pdf() -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=20*mm,
        rightMargin=20*mm,
        topMargin=18*mm,
        bottomMargin=18*mm,
    )

    styles = getSampleStyleSheet()

    style_label = ParagraphStyle("label", fontSize=7, textColor=CYAN, spaceAfter=2, leading=10, fontName="Helvetica")
    style_h1 = ParagraphStyle("h1", fontSize=28, textColor=WHITE, spaceAfter=4, leading=32, fontName="Helvetica-Bold")
    style_subtitle = ParagraphStyle("subtitle", fontSize=10, textColor=LIGHT_GRAY, spaceAfter=6, leading=14, fontName="Helvetica")
    style_section = ParagraphStyle("section", fontSize=13, textColor=CYAN, spaceAfter=4, spaceBefore=10, leading=16, fontName="Helvetica-Bold")
    style_news_title = ParagraphStyle("news_title", fontSize=10, textColor=WHITE, spaceAfter=2, leading=13, fontName="Helvetica-Bold")
    style_news_meta = ParagraphStyle("news_meta", fontSize=8, textColor=CYAN, spaceAfter=6, leading=11, fontName="Helvetica")
    style_news_body = ParagraphStyle("news_body", fontSize=9, textColor=LIGHT_GRAY, spaceAfter=8, leading=13, fontName="Helvetica")
    style_footer = ParagraphStyle("footer", fontSize=7, textColor=LIGHT_GRAY, alignment=TA_CENTER, fontName="Helvetica")
    style_metric_val = ParagraphStyle("metric_val", fontSize=20, textColor=CYAN, alignment=TA_CENTER, fontName="Helvetica-Bold", leading=24)
    style_metric_lbl = ParagraphStyle("metric_lbl", fontSize=7, textColor=LIGHT_GRAY, alignment=TA_CENTER, fontName="Helvetica", leading=10)

    story = []

    # ── HEADER ──────────────────────────────────────────────────────────
    story.append(Paragraph("SMART HORIZON · ИТ-ДЕПАРТАМЕНТ", style_label))
    story.append(Paragraph("ДАЙДЖЕСТ", style_h1))
    story.append(Paragraph("Выпуск № 14 · 8 апреля 2025 · Время чтения: 6 минут", style_subtitle))
    story.append(HRFlowable(width="100%", thickness=1, color=CYAN, spaceAfter=10))

    # ── METRICS ROW ─────────────────────────────────────────────────────
    metrics = [
        [Paragraph("99.7%", style_metric_val), Paragraph("47", style_metric_val),
         Paragraph("12 сек", style_metric_val), Paragraph("0", style_metric_val)],
        [Paragraph("Uptime платформ", style_metric_lbl), Paragraph("Задач закрыто", style_metric_lbl),
         Paragraph("Среднее время API", style_metric_lbl), Paragraph("Крит. инцидентов", style_metric_lbl)],
    ]
    t = Table(metrics, colWidths=["25%", "25%", "25%", "25%"])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    # ── SECTIONS ────────────────────────────────────────────────────────
    sections = [
        {
            "num": "01",
            "title": "Инфраструктура",
            "news": [
                {
                    "title": "Переезд 3 сервисов на Kubernetes завершён без инцидентов",
                    "meta": "Downtime: 0 мин · 12 подов в проде · Ingress: nginx 1.25",
                    "body": "Команда DevOps успешно перевела сервисы auth-gateway, notification-service и "
                            "report-builder в кластер Kubernetes. HPA настроен на диапазон 2–8 реплик. "
                            "Мониторинг через Prometheus + Grafana, алерты подключены в Telegram-канал команды.",
                },
                {
                    "title": "Расширение дискового пространства основной БД",
                    "meta": "+2 ТБ · PostgreSQL 15.4 · Прод-контур",
                    "body": "В связи с ростом объёма транзакций CarMoney выполнено расширение дискового "
                            "пространства. Текущий объём: 4.8 ТБ из 8 ТБ доступных. Запланирована архивация "
                            "данных старше 3 лет в холодное хранилище S3.",
                },
                {
                    "title": "Автоматические бэкапы настроены для всех окружений",
                    "meta": "Retention: 30 дней · S3 · Проверка восстановления: еженедельно",
                    "body": "Настроен единый пайплайн резервного копирования для prod, stage и dev окружений. "
                            "Тестовое восстановление занимает в среднем 12 минут. RPO: 1 час, RTO: 30 минут.",
                },
            ],
        },
        {
            "num": "02",
            "title": "Кибербезопасность",
            "news": [
                {
                    "title": "Обновлён SSL-сертификат на продуктивном контуре",
                    "meta": "Срок действия: 12 мес · Let's Encrypt · 14 доменов",
                    "body": "Плановая ротация сертификатов выполнена для всех публичных endpoint'ов. "
                            "Настроен авто-обновление через certbot. Следующее плановое обновление: апрель 2026.",
                },
                {
                    "title": "Pentest внутренней CRM-системы: результаты",
                    "meta": "Найдено: 2 уязвимости medium, 0 critical · Исполнитель: внутренняя команда ИБ",
                    "body": "Выявлены: избыточные права у роли «оператор» на чтение финансовых отчётов, "
                            "отсутствие rate-limit на endpoint /api/search. Оба пункта внесены в backlog "
                            "с приоритетом P1, срок исправления — до 25 апреля.",
                },
                {
                    "title": "Введена обязательная двухфакторная аутентификация",
                    "meta": "Охват: 98% сотрудников · Дедлайн: 30 апреля · TOTP / Telegram",
                    "body": "С 1 апреля 2FA обязательна для всех корпоративных аккаунтов. "
                            "12 сотрудников ещё не активировали — ИТ-отдел вышлет повторное напоминание. "
                            "Поддерживаемые методы: Google Authenticator, Яндекс.Ключ, Telegram-бот.",
                },
            ],
        },
        {
            "num": "03",
            "title": "Разработка",
            "news": [
                {
                    "title": "Релиз CarMoney App v4.2.1",
                    "meta": "15 багфиксов · 2 новые функции · iOS 16+ и Android 10+",
                    "body": "Ключевые изменения: новый экран истории платежей с фильтрацией, "
                            "push-уведомления о статусе заявки. Исправлен критический баг с зависанием "
                            "при оплате через СБП. Рейтинг в App Store вырос с 4.2 до 4.5.",
                },
                {
                    "title": "Внутренний портал сотрудников: новый раздел HR",
                    "meta": "В проде с 3 апреля · 200+ активных пользователей за первую неделю",
                    "body": "Запущен раздел «Моя команда» с оргструктурой, контактами и графиком отпусков. "
                            "Интеграция с 1С:Кадры — данные синхронизируются раз в час. "
                            "Следующий этап: онлайн-заявки на отпуск и справки.",
                },
                {
                    "title": "API скоринга ускорен на 40%",
                    "meta": "P95 latency: 120 мс → 72 мс · Нагрузка: 3 200 req/мин",
                    "body": "Оптимизированы SQL-запросы к таблице заявок (добавлены составные индексы), "
                            "внедрён Redis-кэш для справочных данных. Среднее время обработки заявки "
                            "на скоринг сократилось с 1.8 до 1.1 секунды.",
                },
            ],
        },
        {
            "num": "04",
            "title": "Тренды и регуляторика",
            "news": [
                {
                    "title": "ЦБ РФ: новые требования к ИБ для МФО вступают в силу в Q3 2025",
                    "meta": "Документ: Положение 821-П · Срок внедрения: 1 июля 2025",
                    "body": "Ключевые требования: обязательный SIEM, логирование всех привилегированных "
                            "действий, аудит доступа к персональным данным не реже раза в квартал. "
                            "ИТ-департамент готовит дорожную карту соответствия.",
                },
                {
                    "title": "Пилот: LLM-ассистент для службы поддержки",
                    "meta": "Точность ответов: 81% · 500 тестовых запросов · Модель: YandexGPT Pro",
                    "body": "За 2 недели пилота ассистент корректно обработал 405 из 500 запросов. "
                            "Среднее время ответа: 2.3 сек. Планируется расширение на входящие обращения "
                            "по email с мая 2025. Экономия: ~30% времени операторов первой линии.",
                },
                {
                    "title": "FinTech Russia 2025 — итоги конференции",
                    "meta": "12–14 марта · Москва · 3 доклада от команды Smart Horizon",
                    "body": "Команда представила доклады по теме open banking API, ML-скоринга в реальном "
                            "времени и опыту миграции на отечественный стек. Получено 18 новых контактов "
                            "от потенциальных партнёров. Материалы докладов доступны на корпоративном портале.",
                },
            ],
        },
    ]

    for section in sections:
        story.append(Paragraph(f"{section['num']} · {section['title'].upper()}", style_section))
        story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6))
        for item in section["news"]:
            story.append(Paragraph(item["title"], style_news_title))
            story.append(Paragraph(item["meta"], style_news_meta))
            story.append(Paragraph(item["body"], style_news_body))
        story.append(Spacer(1, 4))

    # ── FOOTER ──────────────────────────────────────────────────────────
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6))
    story.append(Paragraph(
        "Smart Horizon · ИТ-Департамент · Дайджест выходит еженедельно · smarthorizon.ru",
        style_footer,
    ))

    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(DARK_BG)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    return buffer.getvalue()


def handler(event: dict, context) -> dict:
    """Генерирует PDF-дайджест ИТ-департамента Smart Horizon и возвращает его в base64."""
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Max-Age": "86400",
            },
            "body": "",
        }

    pdf_bytes = build_pdf()
    pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
        },
        "body": pdf_b64,
        "isBase64Encoded": False,
    }
