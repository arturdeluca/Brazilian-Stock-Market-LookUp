from tabulate import tabulate


# ITUB4 FUNCTION
def itub4_lookup():
    while True:
        try:
            qitub4 = input(
                "\nQual das seguintes opções você gostaria de selecionar?\n  Valores de data específica (1)\n  Valor de mês específico (2)\nPor favor, use 1 ou 2 para selecionar a sua opção.\n\n"
            )
            if qitub4 == "1" or qitub4 == "2":
                break

            else:
                raise ValueError

        except ValueError:
            print(
                "\nDesculpe mas essa opção não esta disponível!\n  Por favor, selecione uma opção disponível\n"
            )

        finally:
            if qitub4 == "1":
                while True:
                    try:
                        with open("data/ITUB4_daily_max.csv", "r") as f:
                            date = input(
                                "\nQual data você gostaria de ver?\n  A data mais antiga disponível é '2000-12-21'\nO formato escrito deve ser YYYY-MM-DD\n\n"
                            )

                            for line in f:
                                if line.startswith(date):
                                    line = line.split(",")
                                    table = [
                                        ["Data", line[0]],
                                        ["Aberto", f"$ {line[1]}"],
                                        ["Valor mais Alto", f"$ {line[2]}"],
                                        ["Valor mais Baixo", f"$ {line[3]}"],
                                        ["Fechamento", f"$ {line[4]}"],
                                        ["Volume", f"{int(line[6]):,d}"],
                                    ]
                                    f.close()
                                    return tabulate(table, tablefmt="double_grid")

                    except:
                        pass

            elif qitub4 == "2":
                while True:
                    try:
                        with open("data/ITUB4_monthly_max.csv", "r") as f:
                            date_month = input(
                                "\nQual mês você gostaria de procurar?\n  O primeiro mẽs disponível é '2000-01'\nO formato escrito deve ser YYYY-MM\n"
                            )

                            for line in f:
                                if line.startswith(date_month):
                                    line = line.split(",")
                                    line[1] = float(line[1])
                                    line[4] = float(line[4])
                                    dif = line[4] - line[1]
                                    table = [
                                        ["Ano e Mês", line[0]],
                                        ["Aberto", f"$ {line[1]}"],
                                        ["Valor mais Alto", f"$ {line[2]}"],
                                        ["Valor mais Baixo", f"$ {line[3]}"],
                                        ["Fechamento", f"$ {line[4]}"],
                                        ["Volume", f"{int(line[6]):,d}"],
                                        ["Diferença Diária", f"$ {dif}"],
                                    ]
                                    f.close()
                                    return tabulate(table, tablefmt="double_grid")
                    except:
                        pass


# BBDC4 FUNCTION
def bbdc4_lookup():
    while True:
        try:
            qbbdc4 = input(
                "\nQual das seguintes opções você gostaria de selecionar?\n  Valores de data específica (1)\n  Valor de mês específico (2)\nPor favor, use 1 ou 2 para selecionar a sua opção.\n\n"
            )
            if qbbdc4 == "1" or qbbdc4 == "2":
                break

            else:
                raise ValueError

        except ValueError:
            print(
                "\nDesculpe mas essa opção não esta disponível!\n  Por favor, selecione uma opção disponível\n"
            )

        finally:
            if qbbdc4 == "1":
                while True:
                    try:
                        with open("data/BBDC4_daily_max.csv", "r") as f:
                            date = input(
                                "\nQual data você gostaria de ver?\n  A data mais antiga disponível é '2008-01-02\nO formato escrito deve ser YYYY-MM-DD\n\n"
                            )

                            for line in f:
                                if line.startswith(date):
                                    line = line.split(",")
                                    table = [
                                        ["Data", line[0]],
                                        ["Aberto", f"$ {line[1]}"],
                                        ["Valor mais Alto", f"$ {line[2]}"],
                                        ["Valor mais Baixo", f"$ {line[3]}"],
                                        ["Fechamento", f"$ {line[4]}"],
                                        ["Volume", f"{int(line[6]):,d}"],
                                    ]
                                    f.close()
                                    return tabulate(table, tablefmt="double_grid")

                    except:
                        pass

            elif qbbdc4 == "2":
                while True:
                    try:
                        with open("data/BBDC4_monthly_max.csv", "r") as f:
                            date_month = input(
                                "\n\nQual mês de qual ano você gostaria de procurar?\n  O primeiro mês disponível é '2008-02'\nO formato escrito deve ser YYYY-MM\n"
                            )

                            for line in f:
                                if line.startswith(date_month):
                                    line = line.split(",")
                                    line[1] = float(line[1])
                                    line[4] = float(line[4])
                                    dif = line[4] - line[1]
                                    table = [
                                        ["Mes", line[0]],
                                        ["Aberto", f"$ {line[1]}"],
                                        ["Valor mais Alto", f"$ {line[2]}"],
                                        ["Valor mais Baixo", f"$ {line[3]}"],
                                        ["Fechamento", f"$ {line[4]}"],
                                        ["Volume", f"{int(line[6]):,d}"],
                                        ["Diferença Diária", f"$ {dif}"],
                                    ]
                                    f.close()
                                    return tabulate(table, tablefmt="double_grid")
                    except:
                        pass


# VALE3 FUNCTION
def vale3_lookup():
    while True:
        try:
            qvale3 = input(
                "\nQual das seguintes opções você gostaria de selecionar?\n  Valores de data específica (1)\n  Valor de mês específico (2)\nPor favor, use 1 ou 2 para selecionar a sua opção.\n\n"
            )
            if qvale3 == "1" or qvale3 == "2":
                break

            else:
                raise ValueError

        except ValueError:
            print(
                "\nDesculpe mas essa opção não esta disponível!\n  Por favor, selecione uma opção disponível\n"
            )

        finally:
            if qvale3 == "1":
                while True:
                    try:
                        with open("data/VALE3_daily_max.csv", "r") as f:
                            date = input(
                                "\nQual data você gostaria de ver?\n  A data mais antiga disponível é '2008-01-03\nO formato escrito deve ser YYYY-MM-DD\n\n"
                            )

                            for line in f:
                                if line.startswith(date):
                                    line = line.split(",")
                                    table = [
                                        ["Data", line[0]],
                                        ["Aberto", f"$ {line[1]}"],
                                        ["Valor mais Alto", f"$ {line[2]}"],
                                        ["Valor mais Baixo", f"$ {line[3]}"],
                                        ["Fechamento", f"$ {line[4]}"],
                                        ["Volume", f"{int(line[6]):,d}"],
                                    ]
                                    f.close()
                                    return tabulate(table, tablefmt="double_grid")

                    except:
                        pass

            elif qvale3 == "2":
                while True:
                    try:
                        with open("data/VALE3_monthly_max.csv", "r") as f:
                            date_month = input(
                                "\nQual mês de qual ano você gostaria de procurar?\n  O primeiro mês disponível é '2000-02'\nO formato escrito deve ser YYYY-MM\n"
                            )

                            for line in f:
                                if line.startswith(date_month):
                                    line = line.split(",")
                                    line[1] = float(line[1])
                                    line[4] = float(line[4])
                                    dif = line[4] - line[1]
                                    table = [
                                        ["Mês", line[0]],
                                        ["Aberto", f"$ {line[1]}"],
                                        ["Valor mais Alto", f"$ {line[2]}"],
                                        ["Valor mais Baixo", f"$ {line[3]}"],
                                        ["Fechamento", f"$ {line[4]}"],
                                        ["Volume", f"{int(line[6]):,d}"],
                                        ["Diferença Diária", f"$ {dif}"],
                                    ]
                                    f.close()
                                    return tabulate(table, tablefmt="double_grid")
                    except:
                        pass


def main():
    while True:
        try:
            q = input(
                "\nQuais das seguintes ações você gostaria de ver?\n  BBDC4\n  ITUB4\n  VALE3\n\nPressione CTRL C para sair\n\n"
            ).lower()

            if q == "itub4":
                print(itub4_lookup())

            elif q == "bbdc4":
                print(bbdc4_lookup())

            elif q == "vale3":
                print(vale3_lookup())

            else:
                raise ValueError

        except ValueError:
            print("\nOpção não disponível\n")

        except KeyboardInterrupt:
            print("\n\nSuccesful System Exit\n")
            break


if __name__ == "__main__":
    main()
