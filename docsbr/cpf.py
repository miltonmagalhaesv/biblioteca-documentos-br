"""Utilitários para CPF."""


def somente_numeros(valor: object) -> str:
    """Retorna apenas os algarismos presentes no valor informado."""
    return "".join(caractere for caractere in str(valor) if caractere.isdigit())


def formatar_cpf(valor: object) -> str:
    """Formata uma sequência de 11 algarismos como CPF."""
    numeros = somente_numeros(valor)

    if len(numeros) != 11:
        raise ValueError("O CPF deve conter 11 números.")

    return (
        f"{numeros[:3]}."
        f"{numeros[3:6]}."
        f"{numeros[6:9]}-"
        f"{numeros[9:]}"
    )


def validar_cpf(valor: object) -> bool:
    """Valida o tamanho, a repetição e os dígitos verificadores de um CPF."""
    numeros = somente_numeros(valor)

    if len(numeros) != 11 or numeros == numeros[0] * 11:
        return False

    for tamanho in (9, 10):
        soma = sum(
            int(numero) * peso
            for numero, peso in zip(numeros[:tamanho], range(tamanho + 1, 1, -1))
        )
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(numeros[tamanho]):
            return False

    return True
