const steps = [
  { num: "1", text: "Вы открываете браузер и пишете адрес сайта — например, carmoney.ru" },
  { num: "2", text: "Запрос летит через интернет на наш сервер — как письмо на почтовый адрес" },
  { num: "3", text: "Сервер находит нужную страницу и отправляет её обратно к вам" },
  { num: "4", text: "Браузер «собирает» страницу из кусочков и показывает вам готовый сайт" },
];

const faqs = [
  {
    q: "Почему сайт иногда «не открывается»?",
    a: "Скорее всего, сервер временно перегружен или на нём проводятся работы. Как почта — письмо дойдёт, но чуть позже. Обычно достаточно подождать пару минут.",
  },
  {
    q: "Что такое «обновление системы», о котором пишут в рассылке?",
    a: "Это как замена масла в машине: система работает, но мы улучшаем её под капотом — исправляем мелкие ошибки и делаем её быстрее. В это время часть функций может быть недоступна.",
  },
  {
    q: "Зачем менять пароль каждые 3 месяца?",
    a: "Если злоумышленник узнал ваш старый пароль, он не сможет долго им пользоваться. Смена пароля — как смена замка: даже если ключ утёк, дверь снова защищена.",
  },
];

export default function SimpleIT() {
  return (
    <div className="bg-[#020810] px-6 py-20 lg:py-32">
      <div className="max-w-6xl mx-auto">

        <div className="mb-16 flex items-start gap-6">
          <div className="w-px h-16 bg-cyan-400/40 mt-1 shrink-0" />
          <div>
            <p className="text-mono text-cyan-400 text-xs uppercase tracking-[0.25em] mb-3">Рубрика выпуска</p>
            <h2 className="text-3xl lg:text-5xl font-black text-white leading-tight">
              Простое<br />о сложном
            </h2>
            <p className="text-white/40 text-sm mt-3 font-light max-w-md">
              Объясняем ИТ-процессы так, чтобы было понятно всем — без жаргона и сложных схем
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 mb-16">
          <div>
            <p className="text-mono text-cyan-400/60 text-xs uppercase tracking-widest mb-4">Тема этого выпуска</p>
            <h3 className="text-white text-2xl font-black mb-4 leading-tight">
              Как работает сайт?<br />
              <span className="text-cyan-400">За 4 шага</span>
            </h3>
            <p className="text-white/40 text-sm leading-relaxed font-light mb-8">
              Каждый день мы заходим на десятки сайтов и приложений. Но что происходит
              между нажатием кнопки и появлением страницы? Рассказываем на пальцах.
            </p>

            <div className="flex flex-col gap-4">
              {steps.map((s) => (
                <div key={s.num} className="flex gap-4 items-start">
                  <div className="shrink-0 w-8 h-8 border border-cyan-400/30 flex items-center justify-center">
                    <span className="text-mono text-cyan-400 text-xs font-bold">{s.num}</span>
                  </div>
                  <p className="text-white/70 text-sm leading-relaxed pt-1">{s.text}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="flex flex-col gap-px bg-white/5">
            {faqs.map((f, i) => (
              <div key={i} className="bg-[#020810] hover:bg-[#0c1a2e] transition-colors duration-300 p-6">
                <div className="flex gap-3 items-start mb-2">
                  <span className="text-mono text-cyan-400 text-xs font-bold shrink-0 mt-0.5">?</span>
                  <p className="text-white text-sm font-semibold leading-snug">{f.q}</p>
                </div>
                <div className="flex gap-3 items-start pl-0">
                  <span className="text-mono text-cyan-400/40 text-xs font-bold shrink-0 mt-0.5 ml-5">→</span>
                  <p className="text-white/50 text-sm leading-relaxed font-light">{f.a}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="border border-white/5 p-6 flex items-center gap-4">
          <div className="w-1 h-10 bg-cyan-400/60 shrink-0" />
          <p className="text-white/40 text-sm font-light leading-relaxed">
            <span className="text-white/70 font-medium">Следующий выпуск:</span>{" "}
            Что такое бэкап и почему без него как ехать без запаски — просто и с примерами из жизни.
          </p>
        </div>

      </div>
    </div>
  );
}
