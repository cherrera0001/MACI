"""
Generador dinámico de Matriz de Confusión
==========================================

Uso:
    python matriz_confusion_generador.py --tp 39 --tn 72 --fp 0 --fn 3

O desde Python:
    from matriz_confusion_generador import ConfusionMatrixVisualizer
    viz = ConfusionMatrixVisualizer(tp=39, tn=72, fp=0, fn=3)
    viz.mostrar_metricas()
    viz.graficar()
    viz.exportar_json()
"""

import json
import argparse
from dataclasses import dataclass
from typing import Dict, Tuple, Optional
import numpy as np

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("⚠️  matplotlib y seaborn no disponibles. Instalá con: pip install matplotlib seaborn")


@dataclass
class ConfusionMatrixVisualizer:
    """Generador dinámico de matriz de confusión y métricas."""

    tp: int  # True Positive
    tn: int  # True Negative
    fp: int  # False Positive
    fn: int  # False Negative
    nombre_positivo: str = "Positivo"
    nombre_negativo: str = "Negativo"
    nombre_modelo: str = "Modelo de Clasificación"

    def __post_init__(self):
        """Validar datos después de inicialización."""
        if any(x < 0 for x in [self.tp, self.tn, self.fp, self.fn]):
            raise ValueError("TP, TN, FP, FN deben ser >= 0")

        self.total = self.tp + self.tn + self.fp + self.fn
        if self.total == 0:
            raise ValueError("Total de observaciones es 0")

    # ==================== MÉTRICAS BÁSICAS ====================

    def accuracy(self) -> float:
        """Exactitud: proporción total de predicciones correctas."""
        return (self.tp + self.tn) / self.total

    def precision(self) -> float:
        """Precisión: de los que predice positivo, cuántos realmente lo son."""
        denom = self.tp + self.fp
        return self.tp / denom if denom > 0 else 0

    def recall(self) -> float:
        """Recall/Sensibilidad: de los positivos reales, cuántos detecta."""
        denom = self.tp + self.fn
        return self.tp / denom if denom > 0 else 0

    def specificity(self) -> float:
        """Especificidad: de los negativos reales, cuántos detecta."""
        denom = self.tn + self.fp
        return self.tn / denom if denom > 0 else 0

    def f1_score(self) -> float:
        """F1-Score: media armónica de precision y recall."""
        p = self.precision()
        r = self.recall()
        if (p + r) == 0:
            return 0
        return 2 * (p * r) / (p + r)

    # ==================== MÉTRICAS DE ERROR ====================

    def false_positive_rate(self) -> float:
        """Tasa de falsos positivos (FPR)."""
        denom = self.fp + self.tn
        return self.fp / denom if denom > 0 else 0

    def false_negative_rate(self) -> float:
        """Tasa de falsos negativos (FNR)."""
        denom = self.fn + self.tp
        return self.fn / denom if denom > 0 else 0

    def false_discovery_rate(self) -> float:
        """Tasa de descubrimiento falso (FDR)."""
        denom = self.fp + self.tp
        return self.fp / denom if denom > 0 else 0

    def false_omission_rate(self) -> float:
        """Tasa de omisión falsa (FOR)."""
        denom = self.fn + self.tn
        return self.fn / denom if denom > 0 else 0

    # ==================== MÉTRICAS DERIVADAS ====================

    def balanced_accuracy(self) -> float:
        """Balanced Accuracy: promedio de recall y specificity."""
        return (self.recall() + self.specificity()) / 2

    def matthews_correlation_coefficient(self) -> float:
        """MCC: correlación entre predicción y realidad (-1 a 1)."""
        denom = ((self.tp + self.fp) * (self.tp + self.fn) *
                 (self.tn + self.fp) * (self.tn + self.fn)) ** 0.5

        if denom == 0:
            return 0

        return ((self.tp * self.tn - self.fp * self.fn) / denom)

    def positive_predictive_value(self) -> float:
        """PPV: probabilidad de que un positivo predicho sea realmente positivo."""
        return self.precision()

    def negative_predictive_value(self) -> float:
        """NPV: probabilidad de que un negativo predicho sea realmente negativo."""
        denom = self.tn + self.fn
        return self.tn / denom if denom > 0 else 0

    # ==================== PRESENTACIÓN ====================

    def mostrar_matriz(self) -> None:
        """Mostrar matriz de confusión en formato texto."""
        print("\n" + "="*60)
        print(f"MATRIZ DE CONFUSIÓN - {self.nombre_modelo}")
        print("="*60)
        print(f"\n{'':25} | {self.nombre_positivo:>10} | {self.nombre_negativo:>10}")
        print("-" * 60)
        print(f"{'Verdad: ' + self.nombre_positivo:25} | {self.tp:>10} | {self.fn:>10}")
        print(f"{'Verdad: ' + self.nombre_negativo:25} | {self.fp:>10} | {self.tn:>10}")
        print("-" * 60)
        print(f"{'TOTAL':25} | {self.tp + self.fp:>10} | {self.fn + self.tn:>10} | {self.total:>10}")

    def mostrar_metricas(self) -> None:
        """Mostrar todas las métricas calculadas."""
        print("\n" + "="*60)
        print("MÉTRICAS DE CLASIFICACIÓN")
        print("="*60)

        metricas = {
            "MÉTRICAS BÁSICAS": {
                "Accuracy (Exactitud)": f"{self.accuracy():.4f}",
                "Precision": f"{self.precision():.4f}",
                "Recall (Sensibilidad)": f"{self.recall():.4f}",
                "Specificity": f"{self.specificity():.4f}",
                "F1-Score": f"{self.f1_score():.4f}",
            },
            "MÉTRICAS DE ERROR": {
                "False Positive Rate (FPR)": f"{self.false_positive_rate():.4f}",
                "False Negative Rate (FNR)": f"{self.false_negative_rate():.4f}",
                "False Discovery Rate (FDR)": f"{self.false_discovery_rate():.4f}",
                "False Omission Rate (FOR)": f"{self.false_omission_rate():.4f}",
            },
            "MÉTRICAS DERIVADAS": {
                "Balanced Accuracy": f"{self.balanced_accuracy():.4f}",
                "Matthews Correlation Coeff.": f"{self.matthews_correlation_coefficient():.4f}",
                "Positive Predictive Value": f"{self.positive_predictive_value():.4f}",
                "Negative Predictive Value": f"{self.negative_predictive_value():.4f}",
            }
        }

        for categoria, metrica_dict in metricas.items():
            print(f"\n{categoria}")
            print("-" * 60)
            for nombre, valor in metrica_dict.items():
                print(f"  {nombre:.<40} {valor:>10}")

    def resumen_ejecutivo(self) -> Dict:
        """Retornar resumen de métricas clave como diccionario."""
        return {
            "matriz": {
                "TP": self.tp,
                "TN": self.tn,
                "FP": self.fp,
                "FN": self.fn,
                "total": self.total,
                "correctas": self.tp + self.tn,
                "incorrectas": self.fp + self.fn,
            },
            "metricas_principales": {
                "accuracy": round(self.accuracy(), 4),
                "precision": round(self.precision(), 4),
                "recall": round(self.recall(), 4),
                "specificity": round(self.specificity(), 4),
                "f1_score": round(self.f1_score(), 4),
                "balanced_accuracy": round(self.balanced_accuracy(), 4),
            },
            "metricas_error": {
                "fpr": round(self.false_positive_rate(), 4),
                "fnr": round(self.false_negative_rate(), 4),
                "fdr": round(self.false_discovery_rate(), 4),
                "for": round(self.false_omission_rate(), 4),
            }
        }

    # ==================== VISUALIZACIÓN ====================

    def graficar(self, guardar: Optional[str] = None) -> None:
        """Generar gráficos de matriz de confusión."""
        if not MATPLOTLIB_AVAILABLE:
            print("❌ matplotlib no disponible. Instala con: pip install matplotlib seaborn")
            return

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Heatmap
        matriz = np.array([[self.tp, self.fn],
                          [self.fp, self.tn]])
        labels = np.array([[f"TP\n{self.tp}", f"FN\n{self.fn}"],
                          [f"FP\n{self.fp}", f"TN\n{self.tn}"]])

        sns.heatmap(matriz, annot=labels, fmt='', cmap='RdYlGn',
                   xticklabels=[self.nombre_positivo, self.nombre_negativo],
                   yticklabels=[self.nombre_positivo, self.nombre_negativo],
                   ax=axes[0], cbar_kws={'label': 'Cantidad'},
                   vmin=0, vmax=max(self.tp, self.tn, self.fp, self.fn))
        axes[0].set_title('Matriz de Confusión', fontsize=14, fontweight='bold')
        axes[0].set_ylabel('Verdad', fontweight='bold')
        axes[0].set_xlabel('Predicción', fontweight='bold')

        # Métricas
        metricas_nombres = ['Accuracy', 'Precision', 'Recall', 'Specificity', 'F1-Score']
        metricas_valores = [
            self.accuracy(),
            self.precision(),
            self.recall(),
            self.specificity(),
            self.f1_score()
        ]

        colores = ['#2ecc71' if v >= 0.8 else '#f39c12' if v >= 0.6 else '#e74c3c'
                  for v in metricas_valores]

        axes[1].barh(metricas_nombres, metricas_valores, color=colores)
        axes[1].set_xlim(0, 1)
        axes[1].set_xlabel('Valor', fontweight='bold')
        axes[1].set_title('Métricas Principales', fontsize=14, fontweight='bold')
        axes[1].grid(axis='x', alpha=0.3)

        # Agregar valores en las barras
        for i, v in enumerate(metricas_valores):
            axes[1].text(v + 0.02, i, f'{v:.3f}', va='center', fontweight='bold')

        plt.suptitle(f'{self.nombre_modelo}', fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()

        if guardar:
            plt.savefig(guardar, dpi=300, bbox_inches='tight')
            print(f"✅ Gráfico guardado en: {guardar}")

        plt.show()

    def exportar_json(self, ruta: str) -> None:
        """Exportar resultados como JSON."""
        resultado = self.resumen_ejecutivo()
        resultado["modelo"] = self.nombre_modelo
        resultado["clase_positiva"] = self.nombre_positivo
        resultado["clase_negativa"] = self.nombre_negativo

        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=2, ensure_ascii=False)
        print(f"✅ JSON exportado a: {ruta}")

    def exportar_csv(self, ruta: str) -> None:
        """Exportar matriz como CSV."""
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(f",{self.nombre_positivo},{self.nombre_negativo}\n")
            f.write(f"Verdad: {self.nombre_positivo},{self.tp},{self.fn}\n")
            f.write(f"Verdad: {self.nombre_negativo},{self.fp},{self.tn}\n")
        print(f"✅ CSV exportado a: {ruta}")


# ==================== EJEMPLOS ====================

def ejemplo_cancer_mama() -> ConfusionMatrixVisualizer:
    """Ejemplo: Cáncer de mama (Hito 2)."""
    return ConfusionMatrixVisualizer(
        tp=39, tn=72, fp=0, fn=3,
        nombre_positivo="Maligno",
        nombre_negativo="Benigno",
        nombre_modelo="Random Forest - Diagnóstico Cáncer de Mama (114 test)"
    )


def ejemplo_covid() -> ConfusionMatrixVisualizer:
    """Ejemplo: COVID-19 (100 pacientes)."""
    return ConfusionMatrixVisualizer(
        tp=38, tn=50, fp=5, fn=7,
        nombre_positivo="COVID+",
        nombre_negativo="COVID-",
        nombre_modelo="Test COVID-19 (100 pacientes)"
    )


def ejemplo_doctor_1000() -> ConfusionMatrixVisualizer:
    """Ejemplo: Doctor con 1000 pacientes (~37% positivos)."""
    # Si 1000 pacientes, 370 positivos, 630 negativos
    # Asumiendo recall 0.93 y FPR 0.05
    tp = int(370 * 0.93)  # 344
    fn = 370 - tp         # 26
    fp = int(630 * 0.05)  # 31
    tn = 630 - fp         # 599

    return ConfusionMatrixVisualizer(
        tp=tp, tn=tn, fp=fp, fn=fn,
        nombre_positivo="Enfermo",
        nombre_negativo="Sano",
        nombre_modelo="Diagnóstico Médico (1000 pacientes)"
    )


# ==================== CLI ====================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generador dinámico de Matriz de Confusión",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python matriz_confusion_generador.py --tp 39 --tn 72 --fp 0 --fn 3
  python matriz_confusion_generador.py --ejemplo cancer
  python matriz_confusion_generador.py --ejemplo covid
  python matriz_confusion_generador.py --ejemplo doctor_1000
        """
    )

    parser.add_argument('--tp', type=int, help='True Positives')
    parser.add_argument('--tn', type=int, help='True Negatives')
    parser.add_argument('--fp', type=int, help='False Positives')
    parser.add_argument('--fn', type=int, help='False Negatives')
    parser.add_argument('--ejemplo', choices=['cancer', 'covid', 'doctor_1000'],
                       help='Cargar ejemplo predefinido')
    parser.add_argument('--graficar', action='store_true', help='Mostrar gráficos')
    parser.add_argument('--guardar-json', type=str, help='Guardar resultados como JSON')
    parser.add_argument('--guardar-csv', type=str, help='Guardar matriz como CSV')

    args = parser.parse_args()

    # Seleccionar ejemplo
    if args.ejemplo == 'cancer':
        viz = ejemplo_cancer_mama()
    elif args.ejemplo == 'covid':
        viz = ejemplo_covid()
    elif args.ejemplo == 'doctor_1000':
        viz = ejemplo_doctor_1000()
    elif all(x is not None for x in [args.tp, args.tn, args.fp, args.fn]):
        viz = ConfusionMatrixVisualizer(tp=args.tp, tn=args.tn, fp=args.fp, fn=args.fn)
    else:
        # Por defecto: cáncer de mama
        viz = ejemplo_cancer_mama()

    # Mostrar resultados
    viz.mostrar_matriz()
    viz.mostrar_metricas()

    # Exportar si se solicita
    if args.guardar_json:
        viz.exportar_json(args.guardar_json)

    if args.guardar_csv:
        viz.exportar_csv(args.guardar_csv)

    if args.graficar:
        viz.graficar()
