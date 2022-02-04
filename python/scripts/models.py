from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __repr__(self):
        return "<Tournament(title='{}')>" \
            .format(self.title)

class Teams(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    #match = relationship("Matches", back_populates="teams")

    def __repr__(self):
        return "<Teams(name='{}')>" \
            .format(self.name)

class Matches(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    idLocalTeam = Column(Integer, ForeignKey('teams.id'))
    idVisitorTeam = Column(Integer, ForeignKey('teams.id'))
    goalLocalTeam = Column(Integer)
    goalVisitorTeam = Column(Integer)

    teamLocal = relationship("Teams", foreign_keys=[idLocalTeam])
    teamVisitor = relationship("Teams", foreign_keys=[idVisitorTeam])

    def __repr__(self):
        return "<Teams(idLocalTeam={}, idVisitorTeam={}, goalLocalTeam={}, goalVisitorTeam={})>" \
            .format(self.idLocalTeam, self.idLocalTeam, self.goalLocalTeam, self.goalVisitorTeam)
