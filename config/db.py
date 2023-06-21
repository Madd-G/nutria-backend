from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://u5325200_alamsyah:Alamsyah15.@srv49.niagahoster.com:3306/u5325200_alamsyah')
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# session = Session()
#
# Base = automap_base()
meta = MetaData()
conn = engine.connect()
