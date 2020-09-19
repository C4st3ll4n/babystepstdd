import pytest

from enviador import Enviador
from spam.main import EnviadorSpam


def test_envio_spam():
    sender = EnviadorSpam(sessao, Enviador())
    sender.enviarEmails('p13dr0h@gmail.com', "TDD", "Babysteps com TDD")
