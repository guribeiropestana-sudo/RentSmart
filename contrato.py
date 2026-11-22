
from decimal import Decimal, ROUND_HALF_UP


class Contrato:
    def __init__(self, numero_parcelas):
        if type(numero_parcelas) is not int or not 1 <= numero_parcelas <= 5:
            raise ValueError("O parcelamento deve ser de 1 a 5 vezes.")

        self.taxa_contratual = Decimal("2000.00")
        self.numero_parcelas = numero_parcelas

    def calcular_parcelas(self):
        valor_parcela = (
            self.taxa_contratual / self.numero_parcelas
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        parcelas = [valor_parcela] * (self.numero_parcelas - 1)

        # Ajusta a última parcela para totalizar exatamente R$ 2.000,00
        ultima_parcela = self.taxa_contratual - sum(
            parcelas, Decimal("0.00")
        )

        parcelas.append(ultima_parcela)

        return parcelas
