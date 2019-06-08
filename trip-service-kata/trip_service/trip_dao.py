
from .dependend_class_call_during_unit_test_exception import DependendClassCallDuringUnitTestException

class TripDAO:
  @staticmethod
  def findTripsByUser(user):
    raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked on an unit test.")

