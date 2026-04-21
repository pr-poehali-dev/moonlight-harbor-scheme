import Header from "@/components/Header";
import Hero from "@/components/Hero";
import Featured from "@/components/Featured";
import SimpleIT from "@/components/SimpleIT";
import Heroes from "@/components/Heroes";
import Promo from "@/components/Promo";
import Footer from "@/components/Footer";

const Index = () => {
  return (
    <main className="min-h-screen">
      <Header />
      <Hero />
      <Featured />
      <SimpleIT />
      <Heroes />
      <Promo />
      <Footer />
    </main>
  );
};

export default Index;