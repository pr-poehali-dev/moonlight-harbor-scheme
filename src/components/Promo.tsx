import { useScroll, useTransform, motion } from "framer-motion";
import { useRef } from "react";

export default function Promo() {
  const container = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: container,
    offset: ["start end", "end start"],
  });
  const y = useTransform(scrollYProgress, [0, 1], ["-10vh", "10vh"]);

  return (
    <div
      ref={container}
      className="relative flex items-center justify-center h-screen overflow-hidden"
      style={{ clipPath: "polygon(0% 0, 100% 0%, 100% 100%, 0 100%)" }}
    >
      <div className="fixed top-[-10vh] left-0 h-[120vh] w-full">
        <motion.div style={{ y }} className="relative w-full h-full">
          <img
            src="/images/spiral-circles.jpg"
            alt="Технологии"
            className="w-full h-full object-cover brightness-[0.2] saturate-0"
          />
          <div className="absolute inset-0 bg-gradient-to-br from-cyan-950/40 via-[#050d1a]/60 to-[#050d1a]/80" />
          <div className="absolute inset-0 grid-bg opacity-80" />
        </motion.div>
      </div>

      <p className="text-mono absolute top-12 left-6 text-cyan-400/60 uppercase z-10 text-xs tracking-[0.3em]">
        Smart Horizon · {new Date().getFullYear()}
      </p>

      <p className="absolute bottom-12 left-6 right-6 text-white text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl max-w-4xl z-10 font-black leading-tight">
        Умные решения для финансового рынка —<br />
        <span className="text-cyan-400">мы строим цифровой горизонт</span>
      </p>
    </div>
  );
}
