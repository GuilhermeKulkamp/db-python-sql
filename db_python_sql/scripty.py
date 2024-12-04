import os # incluido apenas para limpar a tela do console
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

# configurando a engine do DB
engine = create_engine("sqlite:///db/database.db")

# configurando a sessão
Session = sessionmaker(engine)

# criando a tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

# insere um registro
def insert_usuario(nome_usuario, tipo_usuario):
    session = Session()
    try:
        if all([nome_usuario, tipo_usuario]):
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f'Usuário {nome_usuario} cadastrado com sucesso!')
        else:
            print('É obrigatório informar nome e tipo')
    except Exception as e:
        session.rollback()
        print(f'Erro ao cadastrar usuário {nome_usuario}: {e}')
    finally:
        session.close
        
# pesquisar por usuários
def select_usuarios(nome_usuario=''):
    session = Session()
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario)
        else:
            dados = session.query(Usuario).all()
        # aqui deveria retornar o resultado
        for i in dados:
            print(f'Usuário {i.nome} - Tipo: {i.tipo} - id: {i.id}')
    except Exception as e:
        print(f'Erro ao consultar usuário. Erro: {e}')
        # não precisa session.rollback() pois não foi alterado nenhum registro
    finally:
        session.close

# alterar registro
def update_usuario(id_usuario, nome_usuario, tipo_usuario):
    session = Session()
    try:
        if all([id_usuario, nome_usuario, tipo_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            usuario.nome = nome_usuario
            usuario.tipo = tipo_usuario
            session.commit()
            print(f'Usuário {nome_usuario} alterado com sucesso')
        else:
            print('É obrigatório informar o Id, nome e tipo do usuário')
    except Exception as e:
        print(f'Erro ao tentar alterar usuário: {e}')
    finally:
        session.close()
    
# excluir registro
def delete_usuario(id_usuario):
    session = Session()
    try:
        if all([id_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f'Usuário ID {id_usuario} deletado')
        else:
            print('É obrigatório informar o ID')
    except Exception as e:
        print(f'Erro ao tentar deletar usuário ID {id_usuario}: {e}')
    finally:
        session.close()
    

if __name__ == '__main__':
    os.system('clear')
    Base.metadata.create_all(engine)
#    insert_usuario('guilherme', 'Admin')
    select_usuarios('')
#    update_usuario(1,'Guilherme K','Super')
#    delete_usuario(4)
