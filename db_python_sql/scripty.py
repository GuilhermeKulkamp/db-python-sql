import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer

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
        


if __name__ == '__main__':
    os.system('clear')
    Base.metadata.create_all(engine)
    insert_usuario('guilherme', 'Admin')


