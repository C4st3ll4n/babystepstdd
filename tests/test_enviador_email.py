import pytest

from enviador import Enviador


def test_criar_enviador_email():
    sender = Enviador()
    assert sender is not None


@pytest.mark.parametrize('destinatario', ['p13dr0h@gmail.com', 'eu@eu.com.br', 'tdd@eu.com'])
def test_remetente(destinatario):
    sender = Enviador()
    result = sender.enviar(
        destinatario,
        'p13tr0@outlook.com',
        "TDD",
        "Primeiro appzineo feito com tdd")
    assert destinatario in result
