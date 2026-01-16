import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import qrcode # <-- YENİ EKLENDİ

class Visualizer:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        static_path = os.path.join(self.base_dir, "static")
        if not os.path.exists(static_path): os.makedirs(static_path)
            
        self.static_dir = os.path.join(static_path, "charts")
        if not os.path.exists(self.static_dir): os.makedirs(self.static_dir)

    def create_element_chart(self, element_scores: dict, filename_prefix="chart"):
        try:
            labels = list(element_scores.keys())
            values = list(element_scores.values())
            colors = ['#ef4444', '#10b981', '#3b82f6', '#6366f1'] 

            plt.figure(figsize=(6, 3))
            bars = plt.bar(labels, values, color=colors, width=0.6)
            
            plt.title('ELEMENT DENGESİ', fontsize=12, fontweight='bold', color='#334155', pad=15)
            plt.grid(axis='y', linestyle='--', alpha=0.3)
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{int(height)}', ha='center', va='bottom', fontweight='bold')

            filepath = os.path.join(self.static_dir, f"{filename_prefix}_elements.png")
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            return filepath
        except Exception as e:
            print(f"Grafik Hatası: {e}")
            return None

    def create_chakra_radar(self, chakra_data: dict, filename_prefix="chart"):
        try:
            categories = [f"{i}.Çakra" for i in range(1, 9)]
            values = [chakra_data.get(i, 0) for i in range(1, 9)]
            values += values[:1]
            angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
            angles += angles[:1]
            
            plt.figure(figsize=(4, 4))
            ax = plt.subplot(111, polar=True)
            plt.xticks(angles[:-1], categories, color='grey', size=8)
            ax.plot(angles, values, linewidth=2, linestyle='solid', color='#d4af37')
            ax.fill(angles, values, '#d4af37', alpha=0.2)
            plt.title("ÇAKRA HARİTASI", size=10, fontweight='bold', y=1.1)
            
            filepath = os.path.join(self.static_dir, f"{filename_prefix}_chakra.png")
            plt.savefig(filepath, dpi=100, bbox_inches='tight')
            plt.close()
            return filepath
        except Exception as e:
            print(f"Radar Hatası: {e}")
            return None

    # --- YENİ FONKSİYON: QR KOD ÜRETİCİ ---
    def create_qr(self, url: str, filename_prefix="qr"):
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=2)
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            filepath = os.path.join(self.static_dir, f"{filename_prefix}_qr.png")
            img.save(filepath)
            return filepath
        except Exception as e:
            print(f"QR Hatası: {e}")
            return None