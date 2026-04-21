const heroes = [
  {
    name: "Алексей Морозов",
    role: "Системный администратор",
    emoji: "🖥️",
    exp: "7 лет в ИТ",
    about:
      "Я слежу за тем, чтобы все серверы работали без перебоев. Если утром у вас открылась почта — значит, я не зря не спал ночью.",
    typical_day: [
      "08:30 — проверяю графики нагрузки серверов за ночь",
      "10:00 — обновляю операционные системы на тестовом окружении",
      "14:00 — разбираю заявки от коллег: «не работает принтер», «нет доступа к папке»",
      "17:00 — настраиваю мониторинг нового сервиса",
    ],
    stones: [
      "Коллеги думают, что сисадмин = «починить компьютер». На деле — это управление десятками серверов и сетей.",
      "Самый страшный момент — звонок в 3 ночи: «сайт упал». К этому готовишься заранее — пишешь инструкции и автоматизируешь.",
    ],
    lifehacks: [
      "Всегда документируй, что сделал. Память подводит, записи — никогда.",
      "Перед любым изменением делай бэкап. Даже если «ну там мелочь».",
    ],
  },
  {
    name: "Дарья Соколова",
    role: "Аналитик данных",
    emoji: "📊",
    exp: "4 года в аналитике",
    about:
      "Я превращаю горы цифр из баз данных в понятные отчёты для бизнеса. Говорят, я «разговариваю» с данными — и они мне отвечают.",
    typical_day: [
      "09:00 — забираю данные из системы за предыдущий день",
      "10:30 — строю дашборды для отдела продаж и кредитования",
      "13:00 — встреча с продуктом: объясняю, почему конверсия упала",
      "16:00 — пишу SQL-запросы для нового отчёта по просрочке",
    ],
    stones: [
      "Данные врут, если не знаешь контекст. Цифра 0 в поле «кредиты» — это «нет кредитов» или «ошибка загрузки»? Нужно всегда уточнять.",
      "Стейкхолдеры хотят «один главный показатель». Но реальность сложнее — приходится объяснять, почему нельзя смотреть только на конверсию.",
    ],
    lifehacks: [
      "Сначала спроси «зачем нужен этот отчёт» — это экономит 80% времени.",
      "Держи шаблоны частых запросов под рукой. Большинство задач — вариации одного и того же.",
    ],
  },
  {
    name: "Игорь Петров",
    role: "Разработчик бэкенда",
    emoji: "⚙️",
    exp: "5 лет в разработке",
    about:
      "Я пишу код, который работает «за кулисами»: обрабатывает заявки, считает скоринг, отправляет уведомления. Пользователи меня не видят — но чувствуют каждый день.",
    typical_day: [
      "09:30 — планёрка команды: что делали вчера, что делаем сегодня, где застряли",
      "10:00 — пишу новую функцию для API скоринга",
      "13:30 — code review: смотрю код коллег и комментирую",
      "15:00 — разбираю баги из трекера — что-то сломалось в проде",
    ],
    stones: [
      "«Быстро сделать» и «сделать хорошо» — всегда в конфликте. Давление дедлайна реально, но технический долг потом бьёт сильнее.",
      "Баг, который не воспроизводится локально — самый страшный. Значит, проблема в окружении, данных или «звёздах сошлись».",
    ],
    lifehacks: [
      "Читай сообщение об ошибке до конца. 90% ответов уже там.",
      "Перед тем как лезть в код — убедись, что понял задачу. Переделывать дороже, чем уточнить.",
    ],
  },
];

export default function Heroes() {
  return (
    <div className="bg-[#070f1c] px-6 py-20 lg:py-32 grid-bg">
      <div className="max-w-6xl mx-auto">

        <div className="mb-16 flex items-start gap-6">
          <div className="w-px h-16 bg-cyan-400/40 mt-1 shrink-0" />
          <div>
            <p className="text-mono text-cyan-400 text-xs uppercase tracking-[0.25em] mb-3">Рубрика выпуска</p>
            <h2 className="text-3xl lg:text-5xl font-black text-white leading-tight">
              Знай героев<br />в лицо
            </h2>
            <p className="text-white/40 text-sm mt-3 font-light max-w-md">
              Кто эти люди, которые держат наши системы живыми? Говорим с ними честно — о буднях, сложностях и секретах профессии
            </p>
          </div>
        </div>

        <div className="flex flex-col gap-px bg-white/5">
          {heroes.map((h, idx) => (
            <div key={idx} className="bg-[#070f1c] hover:bg-[#0b1525] transition-colors duration-300 p-8 lg:p-10">
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

                <div>
                  <div className="text-4xl mb-4">{h.emoji}</div>
                  <p className="text-mono text-cyan-400/50 text-xs tracking-widest uppercase mb-1">{h.exp}</p>
                  <h3 className="text-white text-xl font-black mb-0.5">{h.name}</h3>
                  <p className="text-cyan-400 text-sm font-medium mb-4">{h.role}</p>
                  <p className="text-white/50 text-sm leading-relaxed font-light border-l border-cyan-400/20 pl-4 italic">
                    «{h.about}»
                  </p>
                </div>

                <div>
                  <p className="text-mono text-white/30 text-xs uppercase tracking-widest mb-4">Типичный день</p>
                  <ul className="flex flex-col gap-2.5">
                    {h.typical_day.map((d, i) => (
                      <li key={i} className="flex gap-3 items-start">
                        <div className="w-1 h-1 bg-cyan-400/40 rounded-full mt-2 shrink-0" />
                        <p className="text-white/60 text-sm leading-snug">{d}</p>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="flex flex-col gap-6">
                  <div>
                    <p className="text-mono text-white/30 text-xs uppercase tracking-widest mb-3">Подводные камни</p>
                    <ul className="flex flex-col gap-3">
                      {h.stones.map((s, i) => (
                        <li key={i} className="flex gap-3 items-start">
                          <span className="text-cyan-400/50 text-xs mt-0.5 shrink-0">⚠</span>
                          <p className="text-white/50 text-sm leading-relaxed">{s}</p>
                        </li>
                      ))}
                    </ul>
                  </div>

                  <div>
                    <p className="text-mono text-white/30 text-xs uppercase tracking-widest mb-3">Личные лайфхаки</p>
                    <ul className="flex flex-col gap-2">
                      {h.lifehacks.map((lh, i) => (
                        <li key={i} className="flex gap-3 items-start">
                          <span className="text-cyan-400 text-xs mt-0.5 shrink-0">→</span>
                          <p className="text-cyan-400/80 text-sm leading-relaxed">{lh}</p>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

              </div>
            </div>
          ))}
        </div>

        <div className="mt-12 border border-white/5 p-6 flex items-center gap-4">
          <div className="w-1 h-10 bg-cyan-400/60 shrink-0" />
          <p className="text-white/40 text-sm font-light leading-relaxed">
            <span className="text-white/70 font-medium">Хочешь стать героем следующего выпуска?</span>{" "}
            Напиши в ИТ-отдел — расскажем о твоей профессии всей компании.
          </p>
        </div>

      </div>
    </div>
  );
}
