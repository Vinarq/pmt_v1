import logging
def connection():
    try:
        # from sqlalchemy import *
        from sqlalchemy import schema, types, Table, column, String
        from sqlalchemy.engine import create_engine
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.sql import select
        metadata = schema.MetaData()
        import psycopg2
        engine = create_engine("postgresql://root:markez@localhost:5432/pmt")
        connection = engine.connect()
        engine.echo = True
        metadata.bind = engine
        logging.info('connection to DB successful')
        return engine, metadata, connection
    except Exception, e:
        logging.error('Error connecting to database {0}'.format(e))
        print('connection to DB NOT successful')
        print e
        raise e

