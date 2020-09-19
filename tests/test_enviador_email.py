import pytest

from enviador import Enviador, EmailInvalido


def test_criar_enviador_email():
    sender = Enviador()
    assert sender is not None


@pytest.mark.parametrize('remetente',
                         ['p13dr0h@gmail.com',
                          'eu@eu.com.br',
                          'tdd@eu.com'])
def test_remetente(remetente):
    sender = Enviador()
    result = sender.enviar(
        remetente,
        'p13tr0@outlook.com',
        "TDD",
        "Primeiro appzineo feito com tdd")
    assert remetente in result


@pytest.mark.parametrize('remetente',
                         ['---',
                          'eu   ',
                          'tdd', ''])
def test_remetente_invalido(remetente):
    sender = Enviador()
    with pytest.raises(EmailInvalido):
        r = sender.enviar(
            remetente,
            'p13tr0@outlook.com',
            "TDD",
            "Primeiro appzineo feito com tdd")
