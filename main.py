
from imoveis import Apartamento, Casa, Estudio
from contrato import Contrato
from projecao import ProjecaoLocacao

def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def pedir_numero(mensagem, opcoes_validas):
    while True:
        try:
            numero = int(input(mensagem))

            if numero in opcoes_validas:
                return numero

            print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Digite um número válido.")


def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (S/N): ").strip().lower()

        if resposta in ("s", "sim"):
            return True

        if resposta in ("n", "nao", "não"):
            return False

        print("Resposta inválida. Digite S ou N.")


def escolher_quartos():
    return pedir_numero(
        "Quantidade de quartos (1 ou 2): ",
        (1, 2)
    )


def escolher_vagas():
    while True:
        try:
            vagas = int(input(
                "Quantidade de vagas (0 ou a partir de 2): "
            ))

            if vagas == 0 or vagas >= 2:
                return vagas

            print("Escolha 0 vagas ou pelo menos 2 vagas.")

        except ValueError:
            print("Digite um número válido.")


def criar_imovel(opcao):
    if opcao == 1:
        print("\n--- APARTAMENTO ---")

        quartos = escolher_quartos()
        garagem = perguntar_sim_nao("Deseja garagem?")
        criancas = perguntar_sim_nao("Possui crianças?")

        return Apartamento(quartos, garagem, criancas)

    elif opcao == 2:
        print("\n--- CASA ---")

        quartos = escolher_quartos()
        garagem = perguntar_sim_nao("Deseja garagem?")

        return Casa(quartos, garagem)

    elif opcao == 3:
        print("\n--- ESTÚDIO ---")

        vagas = escolher_vagas()

        return Estudio(vagas)


def mostrar_menu():
    print("\n================================")
    print("        SISTEMA RENTSMART       ")
    print("================================")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")
    print("0 - Sair")
    print("================================")


def main():
    while True:
        mostrar_menu()

        opcao = pedir_numero(
            "Escolha uma opção: ",
            (0, 1, 2, 3)
        )

        if opcao == 0:
            print("\nEncerrando o RentSmart...")
            break


        imovel = criar_imovel(opcao)
        aluguel = imovel.calcular_aluguel()

        print("\n--- TAXA CONTRATUAL ---")
        print("Taxa de contrato: R$ 2.000,00")

        numero_parcelas = pedir_numero(
            "Em quantas vezes deseja pagar? (1 a 5): ",
            (1, 2, 3, 4, 5)
        )

        contrato = Contrato(numero_parcelas)
        parcelas = contrato.calcular_parcelas()

        detalhes = imovel.detalhar_aluguel()

        print("\n================================")
        print("      ORÇAMENTO RENTSMART       ")
        print("================================")

        print(f"Tipo de imóvel: {type(imovel).__name__}")
        print("--------------------------------")

        print(f"Aluguel-base: {formatar_moeda(detalhes['base'])}")

        if detalhes["quartos"] > 0:
            print(
                f"Adicional de quartos: "
                f"{formatar_moeda(detalhes['quartos'])}"
            )

        if detalhes["garagem"] > 0:
            print(
                f"Garagem: {formatar_moeda(detalhes['garagem'])}"
            )

        if detalhes["estacionamento"] > 0:
            print(
                f"Estacionamento: "
                f"{formatar_moeda(detalhes['estacionamento'])}"
            )

        print(f"Subtotal: {formatar_moeda(detalhes['subtotal'])}")

        if detalhes["desconto"] > 0:
            print(
                f"Desconto (5%): - "
                f"{formatar_moeda(detalhes['desconto'])}"
            )

        print("--------------------------------")
        print(f"ALUGUEL MENSAL: {formatar_moeda(aluguel)}")

        print("\n--- TAXA CONTRATUAL ---")
        print(
            f"Valor da taxa: "
            f"{formatar_moeda(contrato.taxa_contratual)}"
        )
        print(f"Parcelamento: {contrato.numero_parcelas}x")

        for numero, valor in enumerate(parcelas, start=1):
            print(
                f"Parcela {numero}: {formatar_moeda(valor)}"
            )

        print("--------------------------------")
        print(
            f"TOTAL DO PRIMEIRO MÊS: "
            f"{formatar_moeda(aluguel + parcelas[0])}"
        )

        print("--------------------------------")
        print("O aluguel e a taxa são custos separados.")
        print("================================")

        print("\n--- GERANDO PROJEÇÃO DE 12 MESES ---")

        projecao = ProjecaoLocacao(imovel, contrato)

        arquivo_csv = projecao.gerar_csv()

        print("Arquivo CSV gerado com sucesso!")
        print(f"Local: {arquivo_csv}")
        print("Projeção financeira de 12 meses concluída.")


        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
