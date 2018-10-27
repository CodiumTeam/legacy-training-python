from .context import tripservice

class TestTripService(object):

    def test_xxx(self):
        tripService = tripservice.TripService()
        tripService.getTripsByUser(tripservice.User())
        pass
