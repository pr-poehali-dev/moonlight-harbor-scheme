interface HeaderProps {
  className?: string;
}

export default function Header({ className }: HeaderProps) {
  return (
    <header className={`absolute top-0 left-0 right-0 z-10 p-6 ${className ?? ""}`}>
      <div className="flex justify-between items-center">
        <div className="flex items-center gap-3">
          <div className="w-6 h-6 border border-cyan-400 rotate-45 flex items-center justify-center">
            <div className="w-2 h-2 bg-cyan-400"></div>
          </div>
          <span className="text-white text-sm uppercase tracking-widest font-medium">Smart Horizon</span>
        </div>
        <nav className="flex gap-8">
          <a
            href="#digest"
            className="text-white/70 hover:text-cyan-400 transition-colors duration-300 uppercase text-xs tracking-widest"
          >
            Дайджест
          </a>
          <a
            href="#subscribe"
            className="text-white/70 hover:text-cyan-400 transition-colors duration-300 uppercase text-xs tracking-widest"
          >
            Подписаться
          </a>
        </nav>
      </div>
    </header>
  );
}
