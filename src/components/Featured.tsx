const topics = [
  {
    tag: "01",
    label: "Инфраструктура",
    desc: "Обновления серверной части, облачные миграции и DevOps-практики",
    news: [
      { title: "Переезд 3 сервисов на Kubernetes", meta: "Downtime: 0 мин · 12 подов в проде" },
      { title: "Расширение дискового пространства БД", meta: "+2 ТБ · PostgreSQL 15.4" },
      { title: "Автобэкапы настроены для всех окружений", meta: "Retention: 30 дней · S3" },
    ],
  },
  {
    tag: "02",
    label: "Кибербезопасность",
    desc: "Уязвимости, патчи, аудиты и политики информационной безопасности",
    news: [
      { title: "Обновлён SSL-сертификат на prod-контуре", meta: "Срок: 12 мес · Let's Encrypt" },
      { title: "Проведён pentest внутренней CRM-системы", meta: "Найдено: 2 medium, 0 critical" },
      { title: "Введена обязательная 2FA для всех сотрудников", meta: "Охват: 98% · Завершить до 30 апр" },
    ],
  },
  {
    tag: "03",
    label: "Разработка",
    desc: "Релизы продуктов, обновления платформ CarMoney и внутренних систем",
    news: [
      { title: "Релиз CarMoney App v4.2.1", meta: "15 фиксов · 2 новых фичи · iOS + Android" },
      { title: "Внутренний портал сотрудников: новый раздел HR", meta: "В проде с 3 апреля" },
      { title: "API скоринга ускорен на 40%", meta: "P95 latency: 120 мс → 72 мс" },
    ],
  },
  {
    tag: "04",
    label: "Тренды",
    desc: "ИИ, машинное обучение, регуляторика и лучшие практики отрасли",
    news: [
      { title: "ЦБ РФ опубликовал новые требования к ИБ МФО", meta: "Срок внедрения: Q3 2025" },
      { title: "Пилот: LLM-ассистент для службы поддержки", meta: "Точность: 81% · 500 тест-запросов" },
      { title: "Конференция FinTech Russia 2025 — итоги", meta: "3 доклада от команды · 12–14 марта" },
    ],
  },
];

export default function Featured() {
  return (
    <div className="min-h-screen bg-[#070f1c] px-6 py-20 lg:py-32 grid-bg">
      <div className="max-w-6xl mx-auto">
        <div className="mb-16 flex items-start gap-6">
          <div className="w-px h-16 bg-cyan-400/40 mt-1 shrink-0" />
          <div>
            <p className="text-mono text-cyan-400 text-xs uppercase tracking-[0.25em] mb-3">Рубрики дайджеста</p>
            <h2 className="text-3xl lg:text-5xl font-black text-white leading-tight">
              Что внутри<br />каждого выпуска
            </h2>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-px bg-white/5">
          {topics.map((t) => (
            <div
              key={t.tag}
              className="bg-[#070f1c] p-8 group hover:bg-[#0c1a2e] transition-colors duration-300"
            >
              <div className="flex items-center justify-between mb-4">
                <span className="text-mono text-cyan-400/40 text-xs tracking-widest">{t.tag}</span>
                <span className="text-mono text-white/20 text-xs">{t.news.length} материала</span>
              </div>
              <h3 className="text-white text-xl font-bold mb-1 group-hover:text-cyan-400 transition-colors duration-300">
                {t.label}
              </h3>
              <p className="text-white/30 text-xs leading-relaxed font-light mb-6">{t.desc}</p>

              <ul className="flex flex-col gap-3">
                {t.news.map((n, i) => (
                  <li key={i} className="border-l border-cyan-400/20 pl-4">
                    <p className="text-white/80 text-sm font-medium leading-snug">{n.title}</p>
                    <p className="text-mono text-cyan-400/50 text-xs mt-1">{n.meta}</p>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-12 flex items-center justify-between border-t border-white/5 pt-8">
          <p className="text-white/30 text-sm font-light">
            Выходит каждую неделю · Smart Horizon ИТ-Департамент
          </p>
          <button className="text-mono text-cyan-400 border border-cyan-400/30 px-6 py-2.5 text-xs uppercase tracking-widest hover:bg-cyan-400/10 transition-all duration-300">
            Читать выпуск →
          </button>
        </div>
      </div>
    </div>
  );
}
