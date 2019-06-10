
from .trip import Trip

class User:
  
  def __init__(self):
    self.trips = []
    self.friends = []
  
  def getFriends(self):
    return self.friends
  
  def addFriend(self, user):
    self.friends.add(user)

  def addTrip(self, trip):
    self.trips.add(trip)
  
  def trips(self):
    return self.trips

