import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

#

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método

def test_calcular_media_5_notas():
    aluno = Aluno("Ana", [8.0, 6.0, 7.0, 9.0,10])
    assert aluno.calcular_media() == 8.0
    
def test_situacao_aprovado(aluno_aprovado):
    assert aluno_aprovado.situacao() == "Aprovado"

def test_situacao_reprovado(aluno_reprovado):
    assert aluno_reprovado.situacao() == "Reprovado"

def test_situacao_aprovado_6():
    aluno = Aluno("Lucas", [6.0, 6.0, 6.0, 6.0])
    assert aluno.situacao() == "Aprovado"

def test_maior_nota_9():
    aluno = Aluno("Bia", [5.0, 9.0, 7.0, 3.0])
    assert aluno.maior_nota() == 9.0

def test_maior_nota_7():
    aluno = Aluno("Bia", [5.0, 1.0, 7.0, 3.0])
    assert aluno.maior_nota() == 7.0 

def test_menor_nota():
    aluno = Aluno("Bia", [5.0, 1.0, 7.0, 3.0])
    assert aluno.menor_nota() == 1.0 

def test_media_arredondada_teto():
    aluno = Aluno("Ekko", [10, 10, 9.8, 9.4])
    assert aluno.calcular_media_arredondada() == 10

def test_media_arredondada_piso():
    aluno = Aluno("Bolsonaro",[1, 1, 2, 1.88] )
    assert aluno.calcular_media_arredondada() == 1
 

