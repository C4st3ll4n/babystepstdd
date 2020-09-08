import pytest

from spam.db import Conexao
from spam.models.modelos import Usuario


@pytest.fixture
def conexao():
    # Setup
    c_obj = Conexao()
    yield c_obj
    # Tear down
    c_obj.fechar()


@pytest.fixture
def sessao(conexao):
    s_obj = conexao.sessao()
    yield s_obj
    s_obj.fechar()
    s_obj.rollback()


def test_salvar_usuario(sessao):
    u = Usuario(name='Pedro')
    sessao.salvar(u)
    assert isinstance(u.id, int)


def test_listar_usuario(sessao):
    users = [Usuario(name='Pedro'), Usuario(name='Henrique')]
    for u in users:
        sessao.salvar(u)
    assert users == sessao.listar()

