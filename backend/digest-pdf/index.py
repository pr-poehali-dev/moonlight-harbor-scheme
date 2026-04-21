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
from reportlab.lib.enums import TA_CENTER

DARK_BG = colors.HexColor("#070f1c")
DARK_BG2 = colors.HexColor("#020810")
CYAN = colors.HexColor("#00bcd4")
CYAN_DIM = colors.HexColor("#006070")
LIGHT_GRAY = colors.HexColor("#8899aa")
WHITE = colors.HexColor("#e8f0f8")
BORDER = colors.HexColor("#142030")


def make_styles():
    s = {}
    s["label"]      = ParagraphStyle("label",      fontSize=7,  textColor=CYAN,       spaceAfter=2,  leading=10, fontName="Helvetica")
    s["h1"]         = ParagraphStyle("h1",          fontSize=28, textColor=WHITE,      spaceAfter=4,  leading=32, fontName="Helvetica-Bold")
    s["subtitle"]   = ParagraphStyle("subtitle",    fontSize=10, textColor=LIGHT_GRAY, spaceAfter=6,  leading=14, fontName="Helvetica")
    s["section"]    = ParagraphStyle("section",     fontSize=13, textColor=CYAN,       spaceAfter=4,  spaceBefore=14, leading=16, fontName="Helvetica-Bold")
    s["subsection"] = ParagraphStyle("subsection",  fontSize=9,  textColor=LIGHT_GRAY, spaceAfter=3,  leading=12, fontName="Helvetica")
    s["news_title"] = ParagraphStyle("news_title",  fontSize=10, textColor=WHITE,      spaceAfter=2,  leading=13, fontName="Helvetica-Bold")
    s["news_meta"]  = ParagraphStyle("news_meta",   fontSize=8,  textColor=CYAN,       spaceAfter=4,  leading=11, fontName="Helvetica")
    s["news_body"]  = ParagraphStyle("news_body",   fontSize=9,  textColor=LIGHT_GRAY, spaceAfter=10, leading=13, fontName="Helvetica")
    s["step_num"]   = ParagraphStyle("step_num",    fontSize=9,  textColor=CYAN,       spaceAfter=0,  leading=12, fontName="Helvetica-Bold")
    s["step_text"]  = ParagraphStyle("step_text",   fontSize=9,  textColor=LIGHT_GRAY, spaceAfter=6,  leading=13, fontName="Helvetica")
    s["faq_q"]      = ParagraphStyle("faq_q",       fontSize=9,  textColor=WHITE,      spaceAfter=2,  leading=12, fontName="Helvetica-Bold")
    s["faq_a"]      = ParagraphStyle("faq_a",       fontSize=9,  textColor=LIGHT_GRAY, spaceAfter=8,  leading=13, fontName="Helvetica")
    s["hero_name"]  = ParagraphStyle("hero_name",   fontSize=12, textColor=WHITE,      spaceAfter=1,  leading=14, fontName="Helvetica-Bold")
    s["hero_role"]  = ParagraphStyle("hero_role",   fontSize=9,  textColor=CYAN,       spaceAfter=4,  leading=12, fontName="Helvetica")
    s["hero_quote"] = ParagraphStyle("hero_quote",  fontSize=9,  textColor=LIGHT_GRAY, spaceAfter=6,  leading=13, fontName="Helvetica-Oblique")
    s["hero_label"] = ParagraphStyle("hero_label",  fontSize=7,  textColor=LIGHT_GRAY, spaceAfter=3,  leading=10, fontName="Helvetica")
    s["hero_item"]  = ParagraphStyle("hero_item",   fontSize=9,  textColor=LIGHT_GRAY, spaceAfter=4,  leading=13, fontName="Helvetica")
    s["hero_hack"]  = ParagraphStyle("hero_hack",   fontSize=9,  textColor=CYAN,       spaceAfter=4,  leading=13, fontName="Helvetica")
    s["tip"]        = ParagraphStyle("tip",         fontSize=9,  textColor=LIGHT_GRAY, spaceAfter=4,  leading=13, fontName="Helvetica-Oblique")
    s["footer"]     = ParagraphStyle("footer",      fontSize=7,  textColor=LIGHT_GRAY, alignment=TA_CENTER, fontName="Helvetica")
    s["metric_val"] = ParagraphStyle("metric_val",  fontSize=20, textColor=CYAN,       alignment=TA_CENTER, fontName="Helvetica-Bold", leading=24)
    s["metric_lbl"] = ParagraphStyle("metric_lbl",  fontSize=7,  textColor=LIGHT_GRAY, alignment=TA_CENTER, fontName="Helvetica", leading=10)
    return s


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
    S = make_styles()
    story = []

    # ── HEADER ──────────────────────────────────────────────────────────
    story.append(Paragraph("SMART HORIZON · ИТ-ДЕПАРТАМЕНТ", S["label"]))
    story.append(Paragraph("ДАЙДЖЕСТ", S["h1"]))
    story.append(Paragraph("Выпуск № 14 · 8 апреля 2025 · Время чтения: 9 минут", S["subtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=CYAN, spaceAfter=10))

    # ── METRICS ─────────────────────────────────────────────────────────
    metrics = [
        [Paragraph("99.7%", S["metric_val"]), Paragraph("47", S["metric_val"]),
         Paragraph("12 сек", S["metric_val"]), Paragraph("0", S["metric_val"])],
        [Paragraph("Uptime платформ", S["metric_lbl"]), Paragraph("Задач закрыто", S["metric_lbl"]),
         Paragraph("Среднее время API", S["metric_lbl"]), Paragraph("Крит. инцидентов", S["metric_lbl"])],
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
    story.append(Spacer(1, 14))

    # ── РУБРИКИ НОВОСТЕЙ ────────────────────────────────────────────────
    sections = [
        {
            "num": "01", "title": "Инфраструктура",
            "news": [
                {"title": "Переезд 3 сервисов на Kubernetes завершён без инцидентов",
                 "meta": "Downtime: 0 мин · 12 подов в проде · Ingress: nginx 1.25",
                 "body": "Команда DevOps перевела auth-gateway, notification-service и report-builder в кластер "
                         "Kubernetes. HPA настроен на 2-8 реплик. Мониторинг через Prometheus + Grafana."},
                {"title": "Расширение дискового пространства основной БД",
                 "meta": "+2 ТБ · PostgreSQL 15.4 · Прод-контур",
                 "body": "Текущий объём: 4.8 ТБ из 8 ТБ. Запланирована архивация данных старше 3 лет в S3."},
                {"title": "Автоматические бэкапы настроены для всех окружений",
                 "meta": "Retention: 30 дней · S3 · Проверка восстановления: еженедельно",
                 "body": "Тестовое восстановление занимает 12 минут. RPO: 1 час, RTO: 30 минут."},
            ],
        },
        {
            "num": "02", "title": "Кибербезопасность",
            "news": [
                {"title": "Обновлён SSL-сертификат на продуктивном контуре",
                 "meta": "Срок действия: 12 мес · Let's Encrypt · 14 доменов",
                 "body": "Авто-обновление через certbot настроено. Следующее обновление: апрель 2026."},
                {"title": "Pentest внутренней CRM-системы: результаты",
                 "meta": "Найдено: 2 medium, 0 critical · Исполнитель: внутренняя команда ИБ",
                 "body": "Выявлены: избыточные права роли «оператор» и отсутствие rate-limit на /api/search. "
                         "Срок исправления — до 25 апреля."},
                {"title": "Введена обязательная двухфакторная аутентификация",
                 "meta": "Охват: 98% · Дедлайн: 30 апреля · Google Authenticator / Telegram",
                 "body": "12 сотрудников ещё не активировали 2FA — ИТ-отдел направит повторное напоминание."},
            ],
        },
        {
            "num": "03", "title": "Разработка",
            "news": [
                {"title": "Релиз CarMoney App v4.2.1",
                 "meta": "15 багфиксов · 2 новые функции · iOS 16+ и Android 10+",
                 "body": "Новый экран истории платежей, push-уведомления о статусе заявки. "
                         "Рейтинг в App Store вырос с 4.2 до 4.5."},
                {"title": "Внутренний портал сотрудников: новый раздел HR",
                 "meta": "В проде с 3 апреля · 200+ активных пользователей за первую неделю",
                 "body": "Раздел «Моя команда» с оргструктурой и графиком отпусков. "
                         "Следующий этап: онлайн-заявки на отпуск."},
                {"title": "API скоринга ускорен на 40%",
                 "meta": "P95 latency: 120 мс → 72 мс · Нагрузка: 3 200 req/мин",
                 "body": "Добавлены составные индексы, внедрён Redis-кэш. "
                         "Среднее время обработки заявки: 1.8 → 1.1 сек."},
            ],
        },
        {
            "num": "04", "title": "Тренды и регуляторика",
            "news": [
                {"title": "ЦБ РФ: новые требования к ИБ для МФО с Q3 2025",
                 "meta": "Положение 821-П · Срок: 1 июля 2025",
                 "body": "Обязательный SIEM, логирование привилегированных действий, аудит доступа к ПДн. "
                         "ИТ-департамент готовит дорожную карту."},
                {"title": "Пилот: LLM-ассистент для службы поддержки",
                 "meta": "Точность: 81% · 500 тестовых запросов · YandexGPT Pro",
                 "body": "Ассистент обработал 405 из 500 запросов корректно. "
                         "Расширение на email-обращения запланировано на май 2025."},
                {"title": "FinTech Russia 2025 — итоги",
                 "meta": "12-14 марта · Москва · 3 доклада от команды Smart Horizon",
                 "body": "Темы: open banking API, ML-скоринг в реальном времени, миграция на отечественный стек. "
                         "Материалы доступны на корпоративном портале."},
            ],
        },
    ]

    for section in sections:
        story.append(Paragraph(f"{section['num']} · {section['title'].upper()}", S["section"]))
        story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6))
        for item in section["news"]:
            story.append(Paragraph(item["title"], S["news_title"]))
            story.append(Paragraph(item["meta"], S["news_meta"]))
            story.append(Paragraph(item["body"], S["news_body"]))

    # ── ПРОСТОЕ О СЛОЖНОМ ───────────────────────────────────────────────
    story.append(Paragraph("05 · ПРОСТОЕ О СЛОЖНОМ", S["section"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6))
    story.append(Paragraph(
        "Тема выпуска: Как работает сайт? За 4 шага",
        S["news_title"],
    ))
    story.append(Paragraph(
        "Каждый день мы заходим на десятки сайтов. Но что происходит между нажатием кнопки "
        "и появлением страницы? Рассказываем на пальцах — без технического жаргона.",
        S["news_body"],
    ))

    steps = [
        ("Шаг 1", "Вы открываете браузер и вводите адрес сайта — например, carmoney.ru"),
        ("Шаг 2", "Запрос летит через интернет на наш сервер — как письмо на почтовый адрес"),
        ("Шаг 3", "Сервер находит нужную страницу и отправляет её обратно к вам"),
        ("Шаг 4", "Браузер «собирает» страницу из кусочков и показывает готовый сайт"),
    ]
    steps_data = [[Paragraph(num, S["step_num"]), Paragraph(text, S["step_text"])] for num, text in steps]
    steps_table = Table(steps_data, colWidths=["18%", "82%"])
    steps_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(steps_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Вопросы, которые вы не решались задать:", S["news_meta"]))
    faqs = [
        ("Почему сайт иногда не открывается?",
         "Скорее всего, сервер временно перегружен или идут технические работы. Как почта — письмо дойдёт, "
         "но чуть позже. Обычно достаточно подождать пару минут."),
        ("Что такое «обновление системы» из рассылки?",
         "Это как замена масла в машине: система работает, но мы улучшаем её под капотом — исправляем "
         "ошибки и делаем быстрее. В это время часть функций может быть недоступна."),
        ("Зачем менять пароль каждые 3 месяца?",
         "Если злоумышленник узнал старый пароль, он не сможет долго им пользоваться. Смена пароля — "
         "как смена замка: даже если ключ утёк, дверь снова защищена."),
    ]
    for q, a in faqs:
        story.append(Paragraph(f"? {q}", S["faq_q"]))
        story.append(Paragraph(f"→ {a}", S["faq_a"]))

    story.append(Paragraph(
        "Следующий выпуск: Что такое бэкап и почему без него — как ехать без запаски.",
        S["tip"],
    ))

    # ── ЗНАЙ ГЕРОЕВ В ЛИЦО ──────────────────────────────────────────────
    story.append(Paragraph("06 · ЗНАЙ ГЕРОЕВ В ЛИЦО", S["section"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6))
    story.append(Paragraph(
        "Кто эти люди, которые держат наши системы живыми? Говорим с ними честно — "
        "о буднях, сложностях и личных секретах профессии.",
        S["news_body"],
    ))

    heroes = [
        {
            "name": "Алексей Морозов",
            "role": "Системный администратор · 7 лет в ИТ",
            "quote": "Если утром у вас открылась почта — значит, я не зря не спал ночью.",
            "day": [
                "08:30 — проверяю графики нагрузки серверов за ночь",
                "10:00 — обновляю ОС на тестовом окружении",
                "14:00 — разбираю заявки коллег: нет доступа, не работает принтер",
                "17:00 — настраиваю мониторинг нового сервиса",
            ],
            "stones": [
                "Коллеги думают, сисадмин = починить компьютер. На деле — управление десятками серверов.",
                "Самый страшный момент — звонок в 3 ночи: сайт упал. К этому готовишься заранее.",
            ],
            "hacks": [
                "Всегда документируй, что сделал. Память подводит, записи — никогда.",
                "Перед любым изменением делай бэкап. Даже если «там мелочь».",
            ],
        },
        {
            "name": "Дарья Соколова",
            "role": "Аналитик данных · 4 года в аналитике",
            "quote": "Говорят, я разговариваю с данными — и они мне отвечают.",
            "day": [
                "09:00 — забираю данные из системы за предыдущий день",
                "10:30 — строю дашборды для отдела продаж",
                "13:00 — объясняю продукту, почему упала конверсия",
                "16:00 — пишу SQL-запросы для отчёта по просрочке",
            ],
            "stones": [
                "Данные врут, если не знаешь контекст. 0 — это «нет кредитов» или «ошибка загрузки»?",
                "Стейкхолдеры хотят один главный показатель. Реальность сложнее.",
            ],
            "hacks": [
                "Сначала спроси «зачем нужен этот отчёт» — экономит 80% времени.",
                "Держи шаблоны частых запросов под рукой. Большинство задач — вариации одного.",
            ],
        },
        {
            "name": "Игорь Петров",
            "role": "Разработчик бэкенда · 5 лет в разработке",
            "quote": "Пользователи меня не видят — но чувствуют каждый день.",
            "day": [
                "09:30 — планёрка: что делали вчера, что сегодня, где застряли",
                "10:00 — пишу новую функцию для API скоринга",
                "13:30 — code review: смотрю код коллег",
                "15:00 — разбираю баги из трекера",
            ],
            "stones": [
                "«Быстро» и «хорошо» всегда в конфликте. Технический долг потом бьёт сильнее.",
                "Баг, который не воспроизводится локально — самый страшный.",
            ],
            "hacks": [
                "Читай сообщение об ошибке до конца. 90% ответов уже там.",
                "Перед тем как лезть в код — убедись, что понял задачу.",
            ],
        },
    ]

    for hero in heroes:
        story.append(Paragraph(hero["name"], S["hero_name"]))
        story.append(Paragraph(hero["role"], S["hero_role"]))
        story.append(Paragraph(f"«{hero['quote']}»", S["hero_quote"]))

        col_w = ["33%", "33%", "34%"]
        header_row = [
            Paragraph("ТИПИЧНЫЙ ДЕНЬ", S["hero_label"]),
            Paragraph("ПОДВОДНЫЕ КАМНИ", S["hero_label"]),
            Paragraph("ЛИЧНЫЕ ЛАЙФХАКИ", S["hero_label"]),
        ]
        max_rows = max(len(hero["day"]), len(hero["stones"]), len(hero["hacks"]))
        data = [header_row]
        for i in range(max_rows):
            row = [
                Paragraph(f"• {hero['day'][i]}", S["hero_item"]) if i < len(hero["day"]) else Paragraph("", S["hero_item"]),
                Paragraph(f"⚠ {hero['stones'][i]}", S["hero_item"]) if i < len(hero["stones"]) else Paragraph("", S["hero_item"]),
                Paragraph(f"→ {hero['hacks'][i]}", S["hero_hack"]) if i < len(hero["hacks"]) else Paragraph("", S["hero_hack"]),
            ]
            data.append(row)

        hero_table = Table(data, colWidths=col_w)
        hero_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), DARK_BG),
            ("BACKGROUND", (0, 0), (-1, 0), DARK_BG2),
            ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        story.append(hero_table)
        story.append(Spacer(1, 10))

    story.append(Paragraph(
        "Хочешь стать героем следующего выпуска? Напиши в ИТ-отдел — расскажем о твоей профессии всей компании.",
        S["tip"],
    ))

    # ── FOOTER ──────────────────────────────────────────────────────────
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=6))
    story.append(Paragraph(
        "Smart Horizon · ИТ-Департамент · Дайджест выходит еженедельно · smarthorizon.ru",
        S["footer"],
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
