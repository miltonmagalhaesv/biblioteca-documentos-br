# Biblioteca Documentos BR

Biblioteca Python criada para a atividade de DevOps. Ela remove a formatação,
formata e valida números de CPF.

## Requisitos

- Python 3.8 ou superior

## Utilização

Clone o repositório e execute o Python na raiz do projeto:

```python
from docsbr import formatar_cpf, somente_numeros, validar_cpf

print(somente_numeros("529.982.247-25"))
print(formatar_cpf("52998224725"))
print(validar_cpf("529.982.247-25"))
```

Saída esperada:

```text
52998224725
529.982.247-25
True
```

`formatar_cpf` gera `ValueError` quando o valor não contém 11 algarismos.
`validar_cpf` retorna `True` para um CPF válido e `False` para um CPF inválido.

## Executar os testes

Na raiz do projeto:

```bash
python3 -m unittest discover -s tests -v
```

## Funções

- `somente_numeros(valor)`: remove pontos, hífens e outros caracteres.
- `formatar_cpf(valor)`: aplica a máscara `000.000.000-00`.
- `validar_cpf(valor)`: confere os dígitos verificadores do CPF.

## Licença

Projeto educacional desenvolvido para a disciplina de DevOps.
