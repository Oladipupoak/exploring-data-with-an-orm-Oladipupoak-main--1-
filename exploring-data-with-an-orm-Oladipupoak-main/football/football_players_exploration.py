from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy import select, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Player(Base):
    __tablename__ = "Players"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    name_normalized = Column(String())
    caps = Column(Integer)
    goals = Column(Integer)
    most_recent_year_played = Column(Integer)
    position = Column(String())
    year_born = Column(Integer)
    club = Column(String())
    club_nationality = Column(String())
    played_in_latest = Column(String())
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    
class Country(Base):
    __tablename__ = "Countries"
    country_id = Column(Integer, primary_key=True)
    county_name = Column(String())


class FootballPlayersExploration:
    def __init__(self, filename):
        self.engine = create_engine(f'sqlite:///{filename}', echo=False)
        Session = sessionmaker(self.engine)
        self.session = Session()

    
    def save(self):
        self.session.commit()
            
    def get_most_goals(self):
        result = (
            self.session.query(Player)
            .order_by(Player.goals.desc())
            .first())
            
        print(f'Found: {result.name} - {result.goals}')

    def get_country_most_goals(self):
        result= (
            self.session.query(Player)
            .join(Country)
            .order_by(Player.goals.desc())
            .first())
        
        print(f'Found: {result.name} - {result.goals} - {result.country_id}')
    
    #* What 10 players have the most caps?
    def get_most_caps(self):
        result = (
            self.session.query(Player)
            .order_by(Player.caps.desc())
            .limit(10)
            .all())
        for player in result:
            print(f'Found: {player.name} - {player.caps}')

    def get_country_most_goals_by_players(self):
        result= (
            self.session.query(Player)
            .join(Country)
            .group_by(Player.country_id)
            .order_by(Player.goals.desc())
            .first())
        
        print(f'Found: {result.name} - {result.goals} - {result.country_id}')



        

if __name__ == '__main__':
    footballPlayersExploration = FootballPlayersExploration('football_players_exploration.db')
    footballPlayersExploration.get_most_goals()
    