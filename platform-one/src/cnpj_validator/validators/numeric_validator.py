"""
Validador Numérico de CNPJ
Responsável pela validação da estrutura numérica e dígitos verificadores
"""

import re

class NumericCNPJValidator:
    """
    Classe responsável pela validação numérica de CNPJ.
    Verifica formato, tamanho e dígitos verificadores.
    """

    @staticmethod
    def remove_formatting(cnpj: str) -> str:
        """
        Remove formatação do CNPJ (pontos, traços e barras).
        Args:
            cnpj: String com CNPJ formatado ou não
        Returns:
            String contendo apenas os números do CNPJ
        """
        if not isinstance(cnpj, str):
            return ""
        return re.sub(r'[^0-9]', '', cnpj)

    @staticmethod
    def validate_length(cnpj: str) -> bool:
        """
        Valida se o CNPJ possui exatamente 14 dígitos.
        Args:
            cnpj: String com CNPJ sem formatação
        Returns:
            True se possui 14 dígitos, False caso contrário
        """
        return len(cnpj) == 14

    @staticmethod
    def validate_all_same_digits(cnpj: str) -> bool:
        """
        Verifica se todos os dígitos são iguais (CNPJs inválidos conhecidos).
        Exemplos: 00000000000000, 11111111111111, etc.
        Args:
            cnpj: String com CNPJ sem formatação
        Returns:
            True se todos os dígitos são iguais, False caso contrário
        """
        return cnpj == cnpj[0] * len(cnpj) if cnpj else False

    @staticmethod
    def calculate_check_digits(cnpj: str) -> str:
        """
        Calcula os dígitos verificadores do CNPJ.
        Args:
            cnpj: String com os 12 primeiros dígitos do CNPJ
        Returns:
            String com os dois dígitos verificadores
        """
        if len(cnpj) != 12 or not cnpj.isdigit():
            return ""
        def calc_digit(cnpj, weights):
            s = sum(int(d) * w for d, w in zip(cnpj, weights))
            r = s % 11
            return '0' if r < 2 else str(11 - r)
        weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        weights_second = [6] + weights_first
        d1 = calc_digit(cnpj, weights_first)
        d2 = calc_digit(cnpj + d1, weights_second)
        return d1 + d2

    @staticmethod
    def validate_check_digits(cnpj: str) -> bool:
        """
        Valida os dígitos verificadores do CNPJ.
        Args:
            cnpj: String com CNPJ sem formatação
        Returns:
            True se os dígitos verificadores são válidos, False caso contrário
        """
        if len(cnpj) != 14 or not cnpj.isdigit():
            return False
        return cnpj[-2:] == NumericCNPJValidator.calculate_check_digits(cnpj[:12])

    @staticmethod
    def validate(cnpj: str) -> dict:
        """
        Valida um CNPJ completo.
        Args:
            cnpj: String com CNPJ formatado ou não
        Returns:
            Dicionário com resultado da validação
        """
        cnpj_clean = NumericCNPJValidator.remove_formatting(cnpj)
        errors = []
        if not NumericCNPJValidator.validate_length(cnpj_clean):
            errors.append("CNPJ deve ter 14 dígitos")
        if NumericCNPJValidator.validate_all_same_digits(cnpj_clean):
            errors.append("CNPJ com todos os dígitos iguais é inválido")
        if not NumericCNPJValidator.validate_check_digits(cnpj_clean):
            errors.append("Dígitos verificadores inválidos")
        return {
            'valid': not errors,
            'errors': errors,
            'cnpj_clean': cnpj_clean
        }

    @staticmethod
    def format_cnpj(cnpj: str) -> str:
        """
        Formata o CNPJ para o padrão XX.XXX.XXX/XXXX-XX.
        Args:
            cnpj: String com CNPJ sem formatação
        Returns:
            String formatada ou original se inválida
        """
        cnpj_clean = NumericCNPJValidator.remove_formatting(cnpj)
        if len(cnpj_clean) != 14:
            return cnpj
        return f"{cnpj_clean[:2]}.{cnpj_clean[2:5]}.{cnpj_clean[5:8]}/{cnpj_clean[8:12]}-{cnpj_clean[12:]}"
