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
          alt="Mountain landscape"
          className="w-full h-full object-cover"
        />
      </motion.div>

      <div className="relative z-10 text-center text-white">
        <p className="text-sm uppercase tracking-widest mb-4 opacity-70">ИТ-Департамент</p>
        <h1 className="text-5xl md:text-7xl lg:text-8xl font-bold tracking-tight mb-6">
          ДАЙДЖЕСТ
        </h1>
        <p className="text-lg md:text-xl max-w-2xl mx-auto px-6 opacity-90">
          Всё важное из мира технологий — собрано, осмыслено и доставлено вашей команде
        </p>
      </div>
    </div>
  );
}