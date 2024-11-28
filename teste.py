import pytest
from main import *

def testaCriarUsuarioValido():
    resetar()
    criar_usuario("Juan")
    assert usuarios[0] == {
        'id':1, 'nome':'Juan',
         'seguidores':[], 'seguindo':[]}

def testaCriarUsuarioSemNome():
    resetar()
    with pytest.raises(Exception) as error:
        criar_usuario("")

def testaCriarPostagemValida():
    resetar()
    criar_usuario("Maria")
    criar_postagem(1, "Olá Mundo")

    assert postagens[0] == {
        'id':1, 'usuario':1, 'mensagem': 'Olá Mundo',
        'curtidores':[]
    }

def testCriarPostagemTextoEmBranco():
    resetar()
    criar_usuario('arthur')
    with pytest.raises(Exception) as error:
        criar_postagem(1,"")

def testaRetornaUsuarioPorId():
    resetar()
    criar_usuario('juan')
    criar_usuario('gleison')
    usuario = encontrar_usuario_por_id(2)
    assert usuario == {
        'id':2,
        'nome':'gleison',
        'seguidores':[],
        'seguindo':[]
    }

def testaUsuariosInseridosNaLista():
    resetar()
    criar_usuario('jose')
    criar_usuario('maria')
    listaEsperada = [{
        'id':1, 'nome':'jose', 'seguidores':[], 'seguindo':[]
    },{
        'id':2, 'nome':'maria', 'seguidores':[], 'seguindo':[]
    }]

    assert usuarios == listaEsperada

def testaCriarPostagemUsuarioInexistente():
    resetar()
    with pytest.raises(IndexError) as error:
        criar_postagem(1,'relou')

def testaSeguirUsuarioExistente():
    resetar()
    criar_usuario('gleison')
    criar_usuario('karen')
    seguir_usuario(1,2)

    assert usuarios[0]['seguindo'] == [2]
    assert usuarios[1]['seguidores'] == [1]

def testaSeguirUsuarioInexistente():
    resetar()
    criar_usuario('gleison')
    with pytest.raises(Exception) as error:
        seguir_usuario(1,4)

def testaSeguirMesmoUsuario():
    resetar()
    criar_usuario('gleison')
    with pytest.raises(Exception) as error:
        seguir_usuario(1,1)

def testaCurtirPostagemValida():
    resetar()
    criar_usuario('gleison')
    criar_usuario('jose')
    criar_postagem(1, 'Acorda povo!')
    curtir_postagem(2, 1)

    assert postagens[0]['curtidores'] == [2]
    
def testaCurtirPostagemNovamente():
    resetar()
    criar_usuario('gleison')
    criar_usuario('jose')
    criar_postagem(1, 'Adoro testar!')
    curtir_postagem(2, 1)
    with pytest.raises(Exception) as error:
        curtir_postagem(2, 1)
    assert str(error.value) == "Usuário já curtiu esta postagem."
    assert postagens[0]['curtidores'] == [2]

def test_comentar_em_postagem():
    criar_usuario("Juan")
    criar_postagem(1, "Primeira postagem!")
    comentar_postagem(1, 1, "Ótimo post!") 
    assert 'comentarios' in postagens[0]  
    assert postagens[0]['comentarios'] == [{'usuario': 1, 'texto': "Ótimo post!"}] 

def test_comentar_texto_vazio():
    criar_usuario("Juan")
    criar_postagem(1, "Postagem com comentários.")
    with pytest.raises(ValueError):
        comentar_postagem(1, 1, "") 

def test_comentar_postagem_inexistente():
    criar_usuario("Juan")
    with pytest.raises(IndexError):
        comentar_postagem(1, 999, "Comentário") 

import pytest
from main import *  # Importa todas as funções do seu script principal (main.py)

# Usando uma fixture do pytest para garantir que a função resetar seja chamada antes de cada teste.
@pytest.fixture(autouse=True)
def setup():
    resetar()  # Chama a função resetar antes de cada teste

def test_excluir_usuario():
    resetar() 
    criar_usuario('Gleison')  
    criar_usuario('Jose')     
    criar_postagem(1, 'Postagem do Gleison')
    criar_postagem(2, 'Postagem do Jose')
    curtir_postagem(1, 2)
    curtir_postagem(2, 1)
    comentar_postagem(1, 2, "Comentário do Gleison")
    comentar_postagem(2, 1, "Comentário do Jose")
    
    excluir_usuario(1)  # Exclui o usuário Gleison (id=1)
    
    # Verificar se o usuário Gleison foi excluído e se as postagens de Gleison foram removidas
    assert len(usuarios) == 1  # Só deve restar o usuário Jose
    assert usuarios[0]['id'] == 2  # O usuário restante deve ser o Jose
    
    print("lista de postagens " + str(postagens) + "tam " + str(len(postagens)))
    
    assert len(postagens) == 1  # Só deve restar uma postagem (a de Jose)
    assert postagens[0]['usuario'] == 2  # A postagem restante deve ser de Jose
    assert postagens[0]['curtidores'] == []  # Não deve haver curtidores na postagem de Jose
    assert 'comentarios' in postagens[0]  # A postagem de Jose ainda deve ter comentários
    assert all(comentario['usuario'] != 1 for comentario in postagens[0]['comentarios'])  # Não deve haver comentários de Gleison

