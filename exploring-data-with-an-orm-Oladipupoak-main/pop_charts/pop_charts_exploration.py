
from sqlalchemy import String, Integer, Float, Column
from sqlalchemy import select, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class PopCharts(Base):
    __tablename__ = "PopCharts"
    id = Column(Integer, primary_key=True)
    youtube_link = Column(String())
    name = Column(String())
    artist = Column(String())
    time_on_chart = Column(Integer)
    change = Column(Float)
    total_views = Column(Integer)
    num_likes = Column(Integer)
    duration = Column(Integer)
    views_this_week = Column(Integer)


class PopChartsExploration:
    def __init__(self, filename):
        self.engine = create_engine(f'sqlite:///{filename}', echo=False)
        Session = sessionmaker(self.engine)
        self.session = Session()

    
    def save(self):
        self.session.commit()
            
    def get_longest_song(self):
        result = (
            self.session.query(PopCharts)
            .order_by(PopCharts.duration.desc())
            .first())
            
        print(f'Found: {result.artist} - {result.name} {result.duration}')
    def number_of_songs(self):
        result = self.session.query(PopCharts).count()
        print(f'Number of songs in the pop charts database: {result}')

    def most_liked_song(self):
        result = (
            self.session.query(PopCharts)
            .order_by(PopCharts.num_likes.desc())
            .first())
        print(f'Found: {result.artist} - {result.name} {result.num_likes}')
        #* What is the most viewed song?
    def most_viewed_song(self):
        result = (
            self.session.query(PopCharts)
            .order_by(PopCharts.total_views.desc())
            .first())
        print(f'Found: {result.artist} - {result.name} {result.total_views}')
#* What are the 10 top trending songs? (Hint: Find the songs with the largest percentage increase in views this week.)
    def top_trending_songs(self):
        result = (
            self.session.query(PopCharts)
            .order_by(PopCharts.change.desc())
            .limit(10)
            .all())
        print(f'Found: {result.artist} - {result.name} {result.change}')
#* What song that has been ranked in the top 100 for the shortest amount of time?
    def shortest_time_on_chart(self):
        result = (
            self.session.query(PopCharts)
            .order_by(PopCharts.time_on_chart.asc())
            .first())
        print(f'Found: {result.artist} - {result.name} {result.time_on_chart}')






     

        

if __name__ == '__main__':
    popChartsExploration = PopChartsExploration('pop_charts_exploration.db')
    popChartsExploration.get_longest_song()
    