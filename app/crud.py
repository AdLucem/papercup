"""Library to perform Create, Read, Update and Delete functions"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fuzzywuzzy import fuzz, process

from create_database import Base, Paper


def init():

    engine = create_engine('sqlite:///papercup_database.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def clean(session):
    """delete everything in the existing table"""

    papers = session.query(Paper).all()
    for paper in papers:
        session.delete(paper)
    session.commit()


def insert(session, data):
    """Insert the detail of a paper in the Paper table"""

    paper = Paper(title=data['title'], content=data['content'])
    session.add(paper)
    session.commit()


def read_all(session):
    """Read and display the contents of all the papers
    in the database"""

    papers = session.query(Paper).all()
    for paper in papers:
        print(paper.id)
        print(paper.title)
        print(paper.content)
        print("================================")


def fuzzy_query(session, query):

    papers = session.query(Paper).all()
    titles = list(map(lambda x: x.title, papers))

    choices = process.extract(query, titles)

    correct = ""

    for choice in choices:
        if choice[1] < 50:
            break
        else:
            print('Do you want "' + title + '" ? y/n')
            x = input()
            if x.lower() == "y":
                correct = choice
                break

    return correct


def query(session, query):

    query = query.lower()
    title = fuzzy_query(session, query)
    if title == "":
        return None
    else:
        result = session.query(Paper.title == title)
        data = {"title": result.title,
                "content": result.content}
        return data




