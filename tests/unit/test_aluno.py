import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno
from aluno.aluno import contador_aprovados



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

def test_contar_aprovados_todos():
    maria = Aluno("Maria", [8, 9, 7, 8])   #maprovado
    ekko  = Aluno("Ekko",  [7, 6, 9, 8])   #aprovado
    lucas = Aluno("Lucas", [6, 6, 6, 6])   #aprovado
    alunos = [maria, ekko, lucas]
    assert contador_aprovados(alunos) == 3

def test_contar_aprovados_nenhum():
    joao  = Aluno("João",  [4, 3, 5, 4])   #reprovado
    pedro = Aluno("Pedro", [2, 3, 1, 4])   #reprovado
    alunos = [joao, pedro]
    assert contador_aprovados(alunos) == 0

def test_contar_aprovados_e_reprovados():
    lucas = Aluno("Lucas", [6.0, 6.0, 6.0, 6.0])  #média 6.0 → aprovado
    ekko  = Aluno("Ekko",  [6.0, 5.0, 8.0, 10.0]) #média 7.25 → aprovado
    maria = Aluno("Maria", [6.0, 1.0, 6.0, 3.0])  # média 4.0 → reprovado
    alunos = [lucas, ekko, maria]
    assert contador_aprovados(alunos) == 2

def test_contar_aprovados_vazio():
    assert contador_aprovados([]) == 0
 
##testes reprovacao por falta

def test_situacao_final_reprovado_por_falta():
    maria = Aluno("Maria", notas=[8, 9, 7, 8], faltas=8) 
    assert maria.situacao_final(total_aulas=20) == "Reprovado por falta"

def test_situacao_final_aprovado():
    maria = Aluno("Maria", notas=[8, 9, 7, 8], faltas=2) 
    assert maria.situacao_final(total_aulas=40) == "Aprovado"

def test_situacao_final_reprovado_por_nota():
    joao = Aluno("João", notas=[4, 3, 5, 4], faltas=2) 
    assert joao.situacao_final(total_aulas=40) == "Reprovado por nota"

def test_situacao_final_exatamente_25_porcento():
    joao = Aluno("João", notas=[4, 3, 5, 4], faltas=2) 
    assert joao.situacao_final(total_aulas=8) == "Reprovado por nota"

def test_situacao_final_pouco_acima_25_porcento():
    maria = Aluno("Maria", notas=[8, 9, 7, 8], faltas=2)
    assert maria.situacao_final(total_aulas=7) == "Reprovado por falta"
