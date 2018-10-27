from trip_dao import TripDAO
from user_session import UserSession
from user_not_logged_in_exception import UserNotLoggedInException

class TripService:
  def getTripsByUser(self, user):
    logged_user = UserSession.getInstance().getLoggedUser()
    isFriend = False
    tripList = []
    if logged_user:
      for friend in user.getFriends():
        if friend is logged_user:
          isFriend = True
          break
      if isFriend:
        tripList = TripDAO.findTripsByUser(user)
      return tripList
    else:
      raise UserNotLoggedInException()


