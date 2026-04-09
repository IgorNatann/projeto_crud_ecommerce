from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria Conexão com o SQLlite em Memória
URI = 'sqlite:///data/database_exemplo_1.db'

engine = create_engine(URI, echo=True)

print('Conexão estabelecida com sucesso!')

#ORM - Object Relational Mapping
Base = declarative_base()

# Herdado da classe Base para criar a tabela de usuários
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

print("Tabela Criada com SQLite estabelecida.") 

#  Criando uma sessão para interagir com o banco de dados, efetua insert utilizando commit e encerra.

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='João', idade=28)
session.add(novo_usuario)
session.commit()

print("Usuário inserido com sucesso.")

usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")