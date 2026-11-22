
import unittest
from decimal import Decimal

from imoveis import Apartamento, Casa, Estudio
from contrato import Contrato


class TestRentSmart(unittest.TestCase):

    def test_apartamento_com_desconto(self):
        imovel = Apartamento(2, True, False)
        self.assertEqual(
            imovel.calcular_aluguel(),
            Decimal("1140.00")
        )

    def test_apartamento_sem_adicionais(self):
        imovel = Apartamento(1, False, True)
        self.assertEqual(
            imovel.calcular_aluguel(),
            Decimal("700.00")
        )

    def test_casa_com_adicionais(self):
        imovel = Casa(2, True)
        self.assertEqual(
            imovel.calcular_aluguel(),
            Decimal("1450.00")
        )

    def test_estudio_com_tres_vagas(self):
        imovel = Estudio(3)
        self.assertEqual(
            imovel.calcular_aluguel(),
            Decimal("1510.00")
        )

    def test_estudio_sem_estacionamento(self):
        imovel = Estudio(0)
        self.assertEqual(
            imovel.calcular_aluguel(),
            Decimal("1200.00")
        )

    def test_parcelamento_quatro_vezes(self):
        contrato = Contrato(4)
        parcelas = contrato.calcular_parcelas()

        self.assertEqual(len(parcelas), 4)
        self.assertEqual(parcelas[0], Decimal("500.00"))
        self.assertEqual(sum(parcelas), Decimal("2000.00"))

    def test_parcelamento_tres_vezes(self):
        contrato = Contrato(3)
        parcelas = contrato.calcular_parcelas()

        self.assertEqual(
            parcelas,
            [
                Decimal("666.67"),
                Decimal("666.67"),
                Decimal("666.66")
            ]
        )

    def test_quartos_invalidos(self):
        with self.assertRaises(ValueError):
            Apartamento(3, False, True)

    def test_parcelamento_invalido(self):
        with self.assertRaises(ValueError):
            Contrato(6)


if __name__ == "__main__":
    unittest.main()
