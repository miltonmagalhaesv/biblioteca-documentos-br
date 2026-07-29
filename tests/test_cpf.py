import unittest

from docsbr import formatar_cpf, somente_numeros, validar_cpf


class TestCpf(unittest.TestCase):
    def test_remove_formatacao(self):
        self.assertEqual(somente_numeros("529.982.247-25"), "52998224725")

    def test_formata_cpf(self):
        self.assertEqual(formatar_cpf("52998224725"), "529.982.247-25")

    def test_rejeita_tamanho_incorreto_na_formatacao(self):
        with self.assertRaises(ValueError):
            formatar_cpf("123")

    def test_valida_cpf_correto(self):
        self.assertTrue(validar_cpf("529.982.247-25"))

    def test_rejeita_cpf_incorreto(self):
        self.assertFalse(validar_cpf("123.456.789-00"))

    def test_rejeita_numeros_repetidos(self):
        self.assertFalse(validar_cpf("111.111.111-11"))


if __name__ == "__main__":
    unittest.main()
