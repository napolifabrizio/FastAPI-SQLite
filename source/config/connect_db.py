from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.sqlite")
SQLModel.metadata.create_all(engine)