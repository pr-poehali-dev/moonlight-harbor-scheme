const topics = [
  { tag: "01", label: "Инфраструктура", desc: "Обновления серверной части, облачные миграции и DevOps-практики" },
  { tag: "02", label: "Кибербезопасность", desc: "Уязвимости, патчи, аудиты и политики информационной безопасности" },
  { tag: "03", label: "Разработка", desc: "Релизы продуктов, обновления платформ CarMoney и внутренних систем" },
  { tag: "04", label: "Тренды", desc: "ИИ, машинное обучение, регуляторика и лучшие практики отрасли" },
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
              <span className="text-mono text-cyan-400/40 text-xs tracking-widest">{t.tag}</span>
              <h3 className="text-white text-xl font-bold mt-3 mb-2 group-hover:text-cyan-400 transition-colors duration-300">
                {t.label}
              </h3>
              <p className="text-white/40 text-sm leading-relaxed font-light">{t.desc}</p>
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
