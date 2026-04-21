import { useScroll, useTransform, motion } from "framer-motion";
import { useRef } from "react";

export default function Hero() {
  const container = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: container,
    offset: ["start start", "end start"],
  });
  const y = useTransform(scrollYProgress, [0, 1], ["0vh", "50vh"]);

  return (
    <div
      ref={container}
      className="relative flex items-center justify-center h-screen overflow-hidden"
    >
      <motion.div
        style={{ y }}
        className="absolute inset-0 w-full h-full"
      >
        <img
          src="/images/mountain-landscape.jpg"
          alt="Горизонт"
          className="w-full h-full object-cover brightness-[0.35]"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[#050d1a]/60 via-transparent to-[#050d1a]/80" />
        <div className="absolute inset-0 grid-bg opacity-60" />
      </motion.div>

      <div className="relative z-10 text-center text-white px-6">
        <p className="text-mono text-cyan-400 text-xs uppercase tracking-[0.3em] mb-6 opacity-90">
          Smart Horizon · ИТ-Департамент
        </p>
        <h1 className="text-5xl md:text-7xl lg:text-8xl font-black tracking-tight mb-6 leading-none">
          <span className="block text-white">ТЕХНОЛОГИИ.</span>
          <span className="block glow-cyan text-cyan-400">ДАЙДЖЕСТ.</span>
        </h1>
        <p className="text-base md:text-lg max-w-xl mx-auto text-white/60 leading-relaxed font-light">
          Еженедельный обзор ИТ-событий компании — инфраструктура, безопасность, релизы и тренды
        </p>
        <div className="mt-10 flex items-center justify-center gap-4">
          <div className="w-8 h-px bg-cyan-400/50"></div>
          <span className="text-mono text-cyan-400/60 text-xs tracking-widest">SCROLL</span>
          <div className="w-8 h-px bg-cyan-400/50"></div>
        </div>
      </div>
    </div>
  );
}
