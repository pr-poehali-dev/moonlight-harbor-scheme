export default function Footer() {
  return (
    <div
      className="relative h-[400px] sm:h-[600px] lg:h-[800px] max-h-[800px]"
      style={{ clipPath: "polygon(0% 0, 100% 0%, 100% 100%, 0 100%)" }}
    >
      <div className="relative h-[calc(100vh+400px)] sm:h-[calc(100vh+600px)] lg:h-[calc(100vh+800px)] -top-[100vh]">
        <div className="h-[400px] sm:h-[600px] lg:h-[800px] sticky top-[calc(100vh-400px)] sm:top-[calc(100vh-600px)] lg:top-[calc(100vh-800px)]">
          <div className="bg-[#020810] py-4 sm:py-6 lg:py-8 px-6 sm:px-10 h-full w-full flex flex-col justify-between border-t border-cyan-400/20 grid-bg">

            <div className="flex shrink-0 gap-12 sm:gap-16 lg:gap-24">
              <div className="flex flex-col gap-1 sm:gap-2">
                <h3 className="mb-2 text-mono text-cyan-400/50 text-xs uppercase tracking-widest">Рубрики</h3>
                <a href="#infra" className="text-white/60 hover:text-cyan-400 transition-colors duration-300 text-sm">Инфраструктура</a>
                <a href="#security" className="text-white/60 hover:text-cyan-400 transition-colors duration-300 text-sm">Безопасность</a>
                <a href="#releases" className="text-white/60 hover:text-cyan-400 transition-colors duration-300 text-sm">Релизы</a>
              </div>
              <div className="flex flex-col gap-1 sm:gap-2">
                <h3 className="mb-2 text-mono text-cyan-400/50 text-xs uppercase tracking-widest">Дайджест</h3>
                <a href="#archive" className="text-white/60 hover:text-cyan-400 transition-colors duration-300 text-sm">Архив выпусков</a>
                <a href="#subscribe" className="text-white/60 hover:text-cyan-400 transition-colors duration-300 text-sm">Подписаться</a>
                <a href="https://smarthorizon.ru" target="_blank" rel="noreferrer" className="text-white/60 hover:text-cyan-400 transition-colors duration-300 text-sm">smarthorizon.ru</a>
              </div>
            </div>

            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-4 sm:gap-0">
              <h1 className="text-[14vw] sm:text-[12vw] lg:text-[10vw] leading-[0.85] mt-4 sm:mt-6 lg:mt-10 font-black tracking-tight glow-cyan text-cyan-400">
                SMART<br className="hidden lg:block" /><span className="text-white"> HORIZON</span>
              </h1>
              <div className="flex flex-col items-end gap-1">
                <p className="text-mono text-white/30 text-xs tracking-widest">ИТ-ДАЙДЖЕСТ</p>
                <p className="text-white/20 text-xs">{new Date().getFullYear()} Smart Horizon</p>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}
