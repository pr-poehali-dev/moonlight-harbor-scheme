"""
Генерация HTML-дайджеста ИТ-департамента Smart Horizon.
Возвращает готовый HTML-файл в виде строки для скачивания на фронтенде.
"""


def build_html() -> str:
    return """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Smart Horizon · ИТ-Дайджест · Выпуск №14</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;500&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:      #070f1c;
    --bg2:     #020810;
    --bg3:     #0c1a2e;
    --cyan:    #00bcd4;
    --cyan2:   rgba(0,188,212,0.15);
    --gray:    #8899aa;
    --white:   #e8f0f8;
    --border:  #142030;
  }

  body {
    background: var(--bg2);
    color: var(--white);
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 14px;
    line-height: 1.6;
  }

  .mono { font-family: 'JetBrains Mono', monospace; }

  /* ── ШАПКА ── */
  .header {
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    padding: 40px 48px 32px;
  }
  .header-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--cyan);
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-bottom: 12px;
  }
  .header h1 {
    font-size: clamp(48px, 8vw, 96px);
    font-weight: 900;
    line-height: 0.9;
    letter-spacing: -0.02em;
    margin-bottom: 16px;
  }
  .header h1 span { color: var(--cyan); }
  .header-sub {
    color: var(--gray);
    font-size: 13px;
    font-weight: 300;
  }
  .header-line {
    height: 1px;
    background: linear-gradient(90deg, var(--cyan), transparent);
    margin: 24px 0 0;
  }

  /* ── МЕТРИКИ ── */
  .metrics {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-bottom: 1px solid var(--border);
  }
  .metric {
    padding: 28px 16px;
    text-align: center;
    border-right: 1px solid var(--border);
    background: var(--bg);
  }
  .metric:last-child { border-right: none; }
  .metric-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 32px;
    font-weight: 700;
    color: var(--cyan);
    line-height: 1;
    margin-bottom: 8px;
    text-shadow: 0 0 20px rgba(0,188,212,0.4);
  }
  .metric-lbl {
    font-size: 11px;
    color: var(--gray);
    text-transform: uppercase;
    letter-spacing: 0.15em;
  }

  /* ── КОНТЕНТ ── */
  .content { padding: 0 48px 48px; }

  /* ── СЕКЦИЯ ── */
  .section { padding-top: 48px; }
  .section-header {
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 4px;
  }
  .section-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: rgba(0,188,212,0.4);
    letter-spacing: 0.2em;
  }
  .section-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--cyan);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }
  .section-hr {
    height: 1px;
    background: var(--border);
    margin: 10px 0 24px;
  }
  .section-desc {
    font-size: 12px;
    color: var(--gray);
    font-weight: 300;
    margin-bottom: 24px;
  }

  /* ── НОВОСТИ ── */
  .news-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1px;
    background: var(--border);
  }
  .news-card {
    background: var(--bg);
    padding: 20px 24px;
    border-left: 2px solid rgba(0,188,212,0.2);
  }
  .news-title {
    font-size: 13px;
    font-weight: 600;
    color: var(--white);
    margin-bottom: 6px;
    line-height: 1.4;
  }
  .news-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: rgba(0,188,212,0.6);
    margin-bottom: 10px;
  }
  .news-body {
    font-size: 12px;
    color: var(--gray);
    line-height: 1.6;
    font-weight: 300;
  }

  /* ── ПРОСТОЕ О СЛОЖНОМ ── */
  .simple-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 32px;
    margin-top: 8px;
  }
  .steps { display: flex; flex-direction: column; gap: 2px; background: var(--border); }
  .step {
    background: var(--bg);
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 14px 18px;
  }
  .step-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: var(--cyan);
    background: rgba(0,188,212,0.1);
    border: 1px solid rgba(0,188,212,0.2);
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 1px;
  }
  .step-text { font-size: 13px; color: var(--gray); line-height: 1.5; }

  .faqs { display: flex; flex-direction: column; gap: 2px; background: var(--border); }
  .faq { background: var(--bg); padding: 14px 18px; }
  .faq-q { font-size: 13px; font-weight: 600; color: var(--white); margin-bottom: 6px; }
  .faq-q::before { content: "? "; color: var(--cyan); font-family: 'JetBrains Mono', monospace; }
  .faq-a { font-size: 12px; color: var(--gray); line-height: 1.5; padding-left: 14px; font-weight: 300; }
  .faq-a::before { content: "→ "; color: rgba(0,188,212,0.5); font-family: 'JetBrains Mono', monospace; }

  .simple-tip {
    margin-top: 20px;
    border-left: 3px solid rgba(0,188,212,0.4);
    padding: 12px 18px;
    background: var(--bg);
    font-size: 12px;
    color: var(--gray);
    font-style: italic;
  }

  /* ── ГЕРОИ ── */
  .hero-card {
    background: var(--bg);
    border: 1px solid var(--border);
    margin-bottom: 2px;
  }
  .hero-top {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    padding: 24px 28px 16px;
    border-bottom: 1px solid var(--border);
  }
  .hero-emoji { font-size: 40px; line-height: 1; }
  .hero-info { flex: 1; }
  .hero-exp {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: rgba(0,188,212,0.5);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .hero-name { font-size: 20px; font-weight: 900; color: var(--white); margin-bottom: 2px; }
  .hero-role { font-size: 13px; color: var(--cyan); font-weight: 500; margin-bottom: 10px; }
  .hero-quote {
    font-size: 13px;
    color: var(--gray);
    font-style: italic;
    border-left: 2px solid rgba(0,188,212,0.3);
    padding-left: 12px;
    line-height: 1.5;
  }
  .hero-body {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1px;
    background: var(--border);
  }
  .hero-col { background: var(--bg); padding: 20px 24px; }
  .hero-col-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--gray);
    text-transform: uppercase;
    letter-spacing: 0.2em;
    margin-bottom: 12px;
  }
  .hero-col ul { list-style: none; display: flex; flex-direction: column; gap: 8px; }
  .hero-col li { font-size: 12px; line-height: 1.5; display: flex; gap: 8px; align-items: flex-start; }
  .hero-col li::before { flex-shrink: 0; margin-top: 1px; }
  .col-day li::before { content: "·"; color: rgba(0,188,212,0.4); }
  .col-day li { color: var(--gray); }
  .col-stones li::before { content: "⚠"; color: rgba(0,188,212,0.5); font-size: 10px; }
  .col-stones li { color: var(--gray); }
  .col-hacks li::before { content: "→"; color: var(--cyan); font-family: 'JetBrains Mono', monospace; }
  .col-hacks li { color: rgba(0,188,212,0.85); }

  .heroes-tip {
    margin-top: 16px;
    border-left: 3px solid rgba(0,188,212,0.4);
    padding: 12px 18px;
    background: var(--bg);
    font-size: 12px;
    color: var(--gray);
    font-style: italic;
  }

  /* ── ФУТЕР ── */
  .footer {
    border-top: 1px solid var(--border);
    padding: 24px 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg2);
  }
  .footer-logo {
    font-size: 48px;
    font-weight: 900;
    color: var(--cyan);
    line-height: 1;
    text-shadow: 0 0 30px rgba(0,188,212,0.3);
    letter-spacing: -0.02em;
  }
  .footer-logo span { color: var(--white); }
  .footer-info { text-align: right; }
  .footer-info p { font-size: 11px; color: var(--gray); font-weight: 300; }
  .footer-info a { color: var(--cyan); text-decoration: none; }

  /* ── КНОПКА ПЕЧАТИ ── */
  .print-bar {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 1000;
    background: rgba(2,8,16,0.95);
    border-bottom: 1px solid var(--border);
    padding: 10px 48px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    backdrop-filter: blur(8px);
  }
  .print-bar-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--gray);
    letter-spacing: 0.15em;
    text-transform: uppercase;
  }
  .print-btn {
    background: var(--cyan);
    color: #000;
    border: none;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 700;
    padding: 9px 24px;
    cursor: pointer;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    transition: opacity 0.15s;
  }
  .print-btn:hover { opacity: 0.85; }

  body { padding-top: 52px; }

  @media print {
    body {
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
      padding-top: 0;
    }
    .print-bar { display: none; }
  }
</style>
</head>
<body>

<!-- ПАНЕЛЬ ПЕЧАТИ -->
<div class="print-bar">
  <span class="print-bar-label">Smart Horizon · ИТ-Дайджест · Выпуск №14</span>
  <button class="print-btn" onclick="window.print()">Сохранить как PDF</button>
</div>

<!-- ШАПКА -->
<div class="header">
  <div class="header-label mono">Smart Horizon · ИТ-Департамент</div>
  <h1>ТЕХНОЛОГИИ.<br><span>ДАЙДЖЕСТ.</span></h1>
  <div class="header-sub">Выпуск № 14 &nbsp;·&nbsp; 8 апреля 2025 &nbsp;·&nbsp; Время чтения: 9 минут</div>
  <div class="header-line"></div>
</div>

<!-- МЕТРИКИ -->
<div class="metrics">
  <div class="metric"><div class="metric-val">99.7%</div><div class="metric-lbl">Uptime платформ</div></div>
  <div class="metric"><div class="metric-val">47</div><div class="metric-lbl">Задач закрыто</div></div>
  <div class="metric"><div class="metric-val">12 сек</div><div class="metric-lbl">Среднее время API</div></div>
  <div class="metric"><div class="metric-val">0</div><div class="metric-lbl">Крит. инцидентов</div></div>
</div>

<!-- КОНТЕНТ -->
<div class="content">

  <!-- 01 ИНФРАСТРУКТУРА -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">01</span>
      <span class="section-title">Инфраструктура</span>
    </div>
    <div class="section-hr"></div>
    <div class="section-desc">Обновления серверной части, облачные миграции и DevOps-практики</div>
    <div class="news-grid">
      <div class="news-card">
        <div class="news-title">Переезд 3 сервисов на Kubernetes завершён без инцидентов</div>
        <div class="news-meta">Downtime: 0 мин · 12 подов в проде · Ingress: nginx 1.25</div>
        <div class="news-body">Команда DevOps перевела auth-gateway, notification-service и report-builder в кластер Kubernetes. HPA настроен на 2–8 реплик. Мониторинг через Prometheus + Grafana, алерты — в Telegram-канал команды.</div>
      </div>
      <div class="news-card">
        <div class="news-title">Расширение дискового пространства основной БД</div>
        <div class="news-meta">+2 ТБ · PostgreSQL 15.4 · Прод-контур</div>
        <div class="news-body">Текущий объём: 4.8 ТБ из 8 ТБ доступных. Запланирована архивация данных старше 3 лет в холодное хранилище S3.</div>
      </div>
      <div class="news-card">
        <div class="news-title">Автоматические бэкапы для всех окружений</div>
        <div class="news-meta">Retention: 30 дней · S3 · Проверка восстановления: еженедельно</div>
        <div class="news-body">Тестовое восстановление занимает 12 минут. RPO: 1 час, RTO: 30 минут. Пайплайн покрывает prod, stage и dev.</div>
      </div>
    </div>
  </div>

  <!-- 02 КИБЕРБЕЗОПАСНОСТЬ -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">02</span>
      <span class="section-title">Кибербезопасность</span>
    </div>
    <div class="section-hr"></div>
    <div class="section-desc">Уязвимости, патчи, аудиты и политики информационной безопасности</div>
    <div class="news-grid">
      <div class="news-card">
        <div class="news-title">Обновлён SSL-сертификат на продуктивном контуре</div>
        <div class="news-meta">Срок: 12 мес · Let's Encrypt · 14 доменов</div>
        <div class="news-body">Авто-обновление через certbot настроено. Следующее плановое обновление: апрель 2026.</div>
      </div>
      <div class="news-card">
        <div class="news-title">Pentest внутренней CRM: результаты</div>
        <div class="news-meta">Найдено: 2 medium, 0 critical · Исполнитель: внутренняя команда ИБ</div>
        <div class="news-body">Выявлены: избыточные права роли «оператор» и отсутствие rate-limit на /api/search. Срок исправления — до 25 апреля.</div>
      </div>
      <div class="news-card">
        <div class="news-title">Введена обязательная двухфакторная аутентификация</div>
        <div class="news-meta">Охват: 98% · Дедлайн: 30 апреля · TOTP / Telegram</div>
        <div class="news-body">12 сотрудников ещё не активировали 2FA. ИТ-отдел вышлет повторное напоминание. Поддерживаемые методы: Google Authenticator, Яндекс.Ключ, Telegram-бот.</div>
      </div>
    </div>
  </div>

  <!-- 03 РАЗРАБОТКА -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">03</span>
      <span class="section-title">Разработка</span>
    </div>
    <div class="section-hr"></div>
    <div class="section-desc">Релизы продуктов, обновления платформ CarMoney и внутренних систем</div>
    <div class="news-grid">
      <div class="news-card">
        <div class="news-title">Релиз CarMoney App v4.2.1</div>
        <div class="news-meta">15 багфиксов · 2 новые функции · iOS 16+ и Android 10+</div>
        <div class="news-body">Новый экран истории платежей с фильтрацией, push-уведомления о статусе заявки. Рейтинг в App Store вырос с 4.2 до 4.5.</div>
      </div>
      <div class="news-card">
        <div class="news-title">Портал сотрудников: новый раздел HR</div>
        <div class="news-meta">В проде с 3 апреля · 200+ активных пользователей за первую неделю</div>
        <div class="news-body">Раздел «Моя команда» с оргструктурой, контактами и графиком отпусков. Интеграция с 1С:Кадры — синхронизация раз в час.</div>
      </div>
      <div class="news-card">
        <div class="news-title">API скоринга ускорен на 40%</div>
        <div class="news-meta">P95 latency: 120 мс → 72 мс · Нагрузка: 3 200 req/мин</div>
        <div class="news-body">Добавлены составные индексы, внедрён Redis-кэш. Среднее время обработки заявки: 1.8 → 1.1 сек.</div>
      </div>
    </div>
  </div>

  <!-- 04 ТРЕНДЫ -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">04</span>
      <span class="section-title">Тренды и регуляторика</span>
    </div>
    <div class="section-hr"></div>
    <div class="section-desc">ИИ, машинное обучение, регуляторика и лучшие практики отрасли</div>
    <div class="news-grid">
      <div class="news-card">
        <div class="news-title">ЦБ РФ: новые требования к ИБ для МФО с Q3 2025</div>
        <div class="news-meta">Положение 821-П · Срок: 1 июля 2025</div>
        <div class="news-body">Обязательный SIEM, логирование привилегированных действий, аудит доступа к ПДн раз в квартал. ИТ-департамент готовит дорожную карту.</div>
      </div>
      <div class="news-card">
        <div class="news-title">Пилот: LLM-ассистент для службы поддержки</div>
        <div class="news-meta">Точность: 81% · 500 тест-запросов · YandexGPT Pro</div>
        <div class="news-body">Ассистент обработал 405 из 500 запросов корректно. Расширение на email-обращения запланировано на май 2025.</div>
      </div>
      <div class="news-card">
        <div class="news-title">FinTech Russia 2025 — итоги конференции</div>
        <div class="news-meta">12–14 марта · Москва · 3 доклада от команды</div>
        <div class="news-body">Темы: open banking API, ML-скоринг в реальном времени, миграция на отечественный стек. Материалы доступны на корпоративном портале.</div>
      </div>
    </div>
  </div>

  <!-- 05 ПРОСТОЕ О СЛОЖНОМ -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">05</span>
      <span class="section-title">Простое о сложном</span>
    </div>
    <div class="section-hr"></div>
    <div class="section-desc">Объясняем ИТ-процессы так, чтобы было понятно всем — без жаргона и сложных схем</div>

    <strong style="color: var(--white); font-size: 15px; display: block; margin-bottom: 16px;">Тема выпуска: как работает сайт? За 4 шага</strong>

    <div class="simple-grid">
      <div class="steps">
        <div class="step"><div class="step-num">1</div><div class="step-text">Вы открываете браузер и вводите адрес сайта — например, carmoney.ru</div></div>
        <div class="step"><div class="step-num">2</div><div class="step-text">Запрос летит через интернет на наш сервер — как письмо на почтовый адрес</div></div>
        <div class="step"><div class="step-num">3</div><div class="step-text">Сервер находит нужную страницу и отправляет её обратно к вам</div></div>
        <div class="step"><div class="step-num">4</div><div class="step-text">Браузер «собирает» страницу из кусочков и показывает готовый сайт</div></div>
      </div>
      <div class="faqs">
        <div class="faq">
          <div class="faq-q">Почему сайт иногда не открывается?</div>
          <div class="faq-a">Сервер временно перегружен или идут технические работы. Как почта — письмо дойдёт, но чуть позже. Обычно достаточно подождать пару минут.</div>
        </div>
        <div class="faq">
          <div class="faq-q">Что такое «обновление системы» из рассылки?</div>
          <div class="faq-a">Это как замена масла в машине: система работает, но мы улучшаем её под капотом — исправляем ошибки, делаем быстрее.</div>
        </div>
        <div class="faq">
          <div class="faq-q">Зачем менять пароль каждые 3 месяца?</div>
          <div class="faq-a">Если злоумышленник узнал пароль, он не сможет долго им пользоваться. Смена пароля — как смена замка.</div>
        </div>
      </div>
    </div>
    <div class="simple-tip">Следующий выпуск: Что такое бэкап и почему без него — как ехать без запаски.</div>
  </div>

  <!-- 06 ЗНАЙ ГЕРОЕВ В ЛИЦО -->
  <div class="section">
    <div class="section-header">
      <span class="section-num mono">06</span>
      <span class="section-title">Знай героев в лицо</span>
    </div>
    <div class="section-hr"></div>
    <div class="section-desc">Кто эти люди, которые держат наши системы живыми? Говорим честно — о буднях, сложностях и лайфхаках</div>

    <!-- Герой 1 -->
    <div class="hero-card">
      <div class="hero-top">
        <div class="hero-emoji">🖥️</div>
        <div class="hero-info">
          <div class="hero-exp mono">7 лет в ИТ</div>
          <div class="hero-name">Алексей Морозов</div>
          <div class="hero-role">Системный администратор</div>
          <div class="hero-quote">«Если утром у вас открылась почта — значит, я не зря не спал ночью.»</div>
        </div>
      </div>
      <div class="hero-body">
        <div class="hero-col col-day">
          <div class="hero-col-label">Типичный день</div>
          <ul>
            <li>08:30 — проверяю графики нагрузки серверов за ночь</li>
            <li>10:00 — обновляю ОС на тестовом окружении</li>
            <li>14:00 — разбираю заявки: нет доступа, не работает принтер</li>
            <li>17:00 — настраиваю мониторинг нового сервиса</li>
          </ul>
        </div>
        <div class="hero-col col-stones">
          <div class="hero-col-label">Подводные камни</div>
          <ul>
            <li>Коллеги думают, сисадмин = починить компьютер. На деле — управление десятками серверов и сетей.</li>
            <li>Самый страшный момент — звонок в 3 ночи: сайт упал. К этому готовишься заранее.</li>
          </ul>
        </div>
        <div class="hero-col col-hacks">
          <div class="hero-col-label">Личные лайфхаки</div>
          <ul>
            <li>Всегда документируй, что сделал. Память подводит, записи — никогда.</li>
            <li>Перед любым изменением делай бэкап. Даже если «там мелочь».</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Герой 2 -->
    <div class="hero-card">
      <div class="hero-top">
        <div class="hero-emoji">📊</div>
        <div class="hero-info">
          <div class="hero-exp mono">4 года в аналитике</div>
          <div class="hero-name">Дарья Соколова</div>
          <div class="hero-role">Аналитик данных</div>
          <div class="hero-quote">«Говорят, я разговариваю с данными — и они мне отвечают.»</div>
        </div>
      </div>
      <div class="hero-body">
        <div class="hero-col col-day">
          <div class="hero-col-label">Типичный день</div>
          <ul>
            <li>09:00 — забираю данные из системы за предыдущий день</li>
            <li>10:30 — строю дашборды для отдела продаж</li>
            <li>13:00 — объясняю продукту, почему упала конверсия</li>
            <li>16:00 — пишу SQL-запросы для отчёта по просрочке</li>
          </ul>
        </div>
        <div class="hero-col col-stones">
          <div class="hero-col-label">Подводные камни</div>
          <ul>
            <li>Данные врут без контекста. 0 — это «нет кредитов» или «ошибка загрузки»?</li>
            <li>Стейкхолдеры хотят один главный показатель. Реальность сложнее.</li>
          </ul>
        </div>
        <div class="hero-col col-hacks">
          <div class="hero-col-label">Личные лайфхаки</div>
          <ul>
            <li>Сначала спроси «зачем нужен этот отчёт» — экономит 80% времени.</li>
            <li>Держи шаблоны частых запросов под рукой. Большинство задач — вариации одного.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Герой 3 -->
    <div class="hero-card">
      <div class="hero-top">
        <div class="hero-emoji">⚙️</div>
        <div class="hero-info">
          <div class="hero-exp mono">5 лет в разработке</div>
          <div class="hero-name">Игорь Петров</div>
          <div class="hero-role">Разработчик бэкенда</div>
          <div class="hero-quote">«Пользователи меня не видят — но чувствуют каждый день.»</div>
        </div>
      </div>
      <div class="hero-body">
        <div class="hero-col col-day">
          <div class="hero-col-label">Типичный день</div>
          <ul>
            <li>09:30 — планёрка: что делали вчера, что сегодня</li>
            <li>10:00 — пишу новую функцию для API скоринга</li>
            <li>13:30 — code review: смотрю код коллег</li>
            <li>15:00 — разбираю баги из трекера</li>
          </ul>
        </div>
        <div class="hero-col col-stones">
          <div class="hero-col-label">Подводные камни</div>
          <ul>
            <li>«Быстро» и «хорошо» всегда в конфликте. Технический долг потом бьёт сильнее.</li>
            <li>Баг, который не воспроизводится локально — самый страшный.</li>
          </ul>
        </div>
        <div class="hero-col col-hacks">
          <div class="hero-col-label">Личные лайфхаки</div>
          <ul>
            <li>Читай сообщение об ошибке до конца. 90% ответов уже там.</li>
            <li>Перед тем как лезть в код — убедись, что понял задачу.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="heroes-tip">Хочешь стать героем следующего выпуска? Напиши в ИТ-отдел — расскажем о твоей профессии всей компании.</div>
  </div>

</div><!-- /content -->

<!-- ФУТЕР -->
<div class="footer">
  <div class="footer-logo">ИТ<span> DIGEST</span></div>
  <div class="footer-info">
    <p>Smart Horizon · ИТ-Департамент</p>
    <p>Выпуск № 14 · 2025</p>
    <p><a href="https://smarthorizon.ru">smarthorizon.ru</a></p>
  </div>
</div>

</body>
</html>"""


def handler(event: dict, context) -> dict:
    """Генерирует HTML-дайджест ИТ-департамента Smart Horizon и возвращает его для скачивания."""
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

    html = build_html()

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
        },
        "body": html,
    }