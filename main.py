# variaveis
usuarios = []
postagens = []
proximo_id_usuario = 1
proximo_id_postagem = 1

# funções
def resetar():
    global proximo_id_usuario
    global proximo_id_postagem
    global usuarios
    global postagens
    usuarios.clear()
    postagens.clear()
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def criar_usuario(nome):
    global proximo_id_usuario
    if nome == '':
        raise Exception
    usuario = {
        'id':proximo_id_usuario,
        'nome':nome,
        'seguidores':[],
        'seguindo':[]
    }  
    usuarios.append(usuario)
    proximo_id_usuario += 1


def criar_postagem(usuario, texto):
    global proximo_id_postagem

    if texto == "":
        raise Exception

    try:
        encontrar_usuario_por_id(usuario)
        postagem = {
            'id': proximo_id_postagem,
            'usuario': usuario,
            'mensagem': texto,
            'curtidores':[]
        }
        postagens.append(postagem)
        proximo_id_postagem += 1
    except IndexError as error:
        raise IndexError

    
def seguir_usuario(usuario_seguidor, usuario_a_seguir):
    if usuario_seguidor == usuario_a_seguir:
        raise Exception

    encontrar_usuario_por_id(usuario_seguidor)['seguindo'].append(usuario_a_seguir)
    encontrar_usuario_por_id(usuario_a_seguir)['seguidores'].append(usuario_seguidor)

def curtir_postagem(usuario, postagem):
    if postagem <= 0 or postagem > len(postagens):
        raise IndexError("Postagem inexistente.") 
    postagem_obj = encontrar_postagem_por_id(postagem)
    if usuario in postagem_obj['curtidores']:
     raise Exception("Usuário já curtiu esta postagem.") 
    postagem_obj['curtidores'].append(usuario)

def comentar_postagem(usuario, postagem, texto):
    if postagem <= 0 or postagem > len(postagens):
        raise IndexError("Postagem inexistente.")
    if texto.strip() == "":
        raise ValueError("Texto do comentário não pode ser vazio.")
    
    postagem_obj = encontrar_postagem_por_id(postagem)
    if 'comentarios' not in postagem_obj:
        postagem_obj['comentarios'] = []
    postagem_obj['comentarios'].append({'usuario': usuario, 'texto': texto})

def encontrar_usuario_por_id(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return usuario
    raise IndexError

def encontrar_postagem_por_id(post_id):
    return postagens[post_id - 1]

def excluir_usuario(user_id):
    global usuarios, postagens
    
    # Encontra o usuário a ser excluído
    usuario = encontrar_usuario_por_id(user_id)
    
    # Remove o usuário da lista de usuários
    usuarios[:] = [u for u in usuarios if u['id'] != user_id]

    # Lidar com as postagens associadas ao usuário excluído
    for postagem in postagens[:]:  # Usando o slicing para evitar erro de modificação durante iteração
        if postagem['usuario'] == user_id:
            # Se o usuário excluído for o autor da postagem, transfira a postagem para outro usuário
            if usuarios:  # Verifica se há outros usuários
                postagem['usuario'] = usuarios[0]['id']  # Transfere a postagem para o primeiro usuário restante
            else:
                postagens.remove(postagem)  # Se não houver mais usuários, remove a postagem

        # Limpa as curtidas de postagens associadas ao usuário excluído
        postagem['curtidores'] = [curtidor for curtidor in postagem['curtidores'] if curtidor != user_id]

        # Limpa os comentários do usuário excluído
        if 'comentarios' in postagem:
            postagem['comentarios'] = [comentario for comentario in postagem['comentarios'] if comentario['usuario'] != user_id]

# menu
def exibir_menu():

    while True:
        print("\n--- Menu ---")
        print("1. Criar Usuário")
        print("2. Criar Postagem")
        print("3. Seguir Usuário")
        print("4. Curtir Postagem")
        print("5. Comentar em Postagem")
        print("6. Excluir usuario")
        print("7. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do usuário: ").strip()
            criar_usuario(nome)
            print("Usuário criado com sucesso!")

        elif opcao == "2":
            try:
                user_id = int(input("Digite o ID do autor da postagem: ").strip())
                texto = input("Digite o texto da postagem: ").strip()
                criar_postagem(user_id, texto)
                print("Postagem criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar postagem: {e}")

        elif opcao == "3":
            try:
                user_id = int(input("Digite o seu ID: ").strip())
                target_id = int(input("Digite o ID do usuário que deseja seguir: ").strip())
                seguir_usuario(user_id, target_id)
                print("Usuário seguido com sucesso!")
            except Exception as e:
                print(f"Erro ao seguir usuário: {e}")

        elif opcao == "4":
            try:
                user_id = int(input("Digite o seu ID: ").strip())
                post_id = int(input("Digite o ID da postagem que deseja curtir: ").strip())
                curtir_postagem(user_id, post_id)
                print("Postagem curtida com sucesso!")
            except Exception as e:
                print(f"Erro ao curtir postagem: {e}")

        elif opcao == "5":
            try:
                user_id = int(input("Digite o seu ID: ").strip())
                post_id = int(input("Digite o ID da postagem que deseja comentar: ").strip())
                texto = input("Digite o texto do comentário: ").strip()
                comentar_postagem(user_id, post_id, texto)
                print("Comentário adicionado com sucesso!")
            except Exception as e:
                print(f"Erro ao comentar: {e}")
        
        elif opcao == "6":
            try:
                user_id = int(input("Digite o ID a ser apagado: ").strip())
                excluir_usuario(user_id)
                print("Usuario excluido com sucesso")
            except Exception as e:
                print(f"Erro ao excluir usuario: {e}")
                
        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
