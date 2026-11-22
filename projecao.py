
import csv
from pathlib import Path
from decimal import Decimal


class ProjecaoLocacao:

    def __init__(self, imovel, contrato):
        self.imovel = imovel
        self.contrato = contrato

    def formatar_valor(self, valor):
        return f"{valor:.2f}".replace(".", ",")

    def gerar_csv(self):
        aluguel = self.imovel.calcular_aluguel()
        parcelas = self.contrato.calcular_parcelas()

        caminho = (
            Path(__file__).resolve().parent
            / "projecao_12_meses.csv"
        )

        with open(
            caminho, "w", newline="", encoding="utf-8-sig"
        ) as arquivo:

            escritor = csv.writer(arquivo, delimiter=";")

            escritor.writerow([
                "Mes",
                "Aluguel (R$)",
                "Parcela da Taxa (R$)",
                "Total Mensal (R$)"
            ])

            for mes in range(1, 13):

                if mes <= len(parcelas):
                    parcela_taxa = parcelas[mes - 1]
                else:
                    parcela_taxa = Decimal("0.00")

                total_mensal = aluguel + parcela_taxa

                escritor.writerow([
                    mes,
                    self.formatar_valor(aluguel),
                    self.formatar_valor(parcela_taxa),
                    self.formatar_valor(total_mensal)
                ])

        return caminho
