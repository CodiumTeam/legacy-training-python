from .dependend_class_call_during_unit_test_exception import DependendClassCallDuringUnitTestException

class UserSession(object):
  _instance = None
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(UserSession, cls).__new__(cls, *args, **kwargs)
    return cls._instance
  
  @staticmethod
  def getInstance():
    return UserSession()  

  def getLoggedUser(self):
    raise DependendClassCallDuringUnitTestException(
      "UserSession.getLoggedUser() should not be called in an unit test"
    )

