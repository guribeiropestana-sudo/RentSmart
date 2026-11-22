
from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP


class Imovel(ABC):

    @abstractmethod
    def detalhar_aluguel(self):
        pass

    def calcular_aluguel(self):
        return self.detalhar_aluguel()["total"]

    def _montar_detalhes(
        self,
        base,
        quartos=Decimal("0.00"),
        garagem=Decimal("0.00"),
        estacionamento=Decimal("0.00"),
        percentual_desconto=Decimal("0.00")
    ):
        subtotal = base + quartos + garagem + estacionamento

        desconto = (
            subtotal * percentual_desconto
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return {
            "base": base,
            "quartos": quartos,
            "garagem": garagem,
            "estacionamento": estacionamento,
            "subtotal": subtotal,
            "desconto": desconto,
            "total": subtotal - desconto
        }


class Apartamento(Imovel):

    def __init__(self, quartos, garagem, possui_criancas):
        if quartos not in (1, 2):
            raise ValueError("Apartamento deve ter 1 ou 2 quartos.")

        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas

    def detalhar_aluguel(self):
        return self._montar_detalhes(
            base=Decimal("700.00"),
            quartos=Decimal("200.00") if self.quartos == 2 else Decimal("0.00"),
            garagem=Decimal("300.00") if self.garagem else Decimal("0.00"),
            percentual_desconto=(
                Decimal("0.05")
                if not self.possui_criancas
                else Decimal("0.00")
            )
        )


class Casa(Imovel):

    def __init__(self, quartos, garagem):
        if quartos not in (1, 2):
            raise ValueError("Casa deve ter 1 ou 2 quartos.")

        self.quartos = quartos
        self.garagem = garagem

    def detalhar_aluguel(self):
        return self._montar_detalhes(
            base=Decimal("900.00"),
            quartos=Decimal("250.00") if self.quartos == 2 else Decimal("0.00"),
            garagem=Decimal("300.00") if self.garagem else Decimal("0.00")
        )


class Estudio(Imovel):

    def __init__(self, vagas):
        if type(vagas) is not int or vagas < 0 or vagas == 1:
            raise ValueError(
                "Escolha 0 vagas ou o pacote de 2 ou mais vagas."
            )

        self.vagas = vagas

    def detalhar_aluguel(self):
        estacionamento = Decimal("0.00")

        if self.vagas >= 2:
            estacionamento = (
                Decimal("250.00")
                + Decimal("60.00") * (self.vagas - 2)
            )

        return self._montar_detalhes(
            base=Decimal("1200.00"),
            estacionamento=estacionamento
        )
