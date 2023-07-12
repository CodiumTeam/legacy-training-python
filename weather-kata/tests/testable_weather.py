import datetime

from weather import Weather


class TestableWeather(Weather):

    def _find_latitude_and_longitude(self, city):
        return '{"data":[{"latitude":40.429913,"longitude":-3.669245,"type":"locality","name":"Madrid","number":null,"postal_code":null,"street":null,"confidence":1,"region":"Madrid","region_code":"MD","county":null,"locality":"Madrid","administrative_area":null,"neighbourhood":null,"country":"Spain","country_code":"ESP","continent":"Europe","label":"Madrid, Spain","bbox_module":[-3.888962,40.312064,-3.518051,40.643271],"country_module":{"latitude":40.396026611328125,"longitude":-3.550692558288574,"common_name":"Spain","official_name":"Kingdom of Spain","capital":"Madrid","flag":"\ud83c\uddea\ud83c\uddf8","area":505992,"landlocked":false,"independent":true,"global":{"alpha2":"ES","alpha3":"ESP","numeric_code":"724","region":"Europe","subregion":"Southern Europe","region_code":"150","subregion_code":"039","world_region":"EMEA","continent_name":"Europe","continent_code":"EU"},"dial":{"calling_code":"34","national_prefix":null,"international_prefix":"00"},"currencies":[{"symbol":"\u20ac","code":"EUR","name":"Euro","numeric":978,"minor_unit":2}],"languages":{"spa":"Spanish"}},"sun_module":{"rise":{"time":1689137690,"astronomical":1689130490,"civil":1689135752,"nautical":1689133305},"set":{"time":1689191148,"astronomical":1689198348,"civil":1689193085,"nautical":1689195533},"transit":1689164419},"timezone_module":{"name":"Europe\/Madrid","offset_sec":7200,"offset_string":"+02:00"}}]}'

    def _find_prediction(self, latitude, longitude):
        return '{"latitude":40.43,"longitude":-3.67,"generationtime_ms":0.7439851760864258,"utc_offset_seconds":7200,"timezone":"Europe/Berlin","timezone_abbreviation":"CEST","elevation":684.0,"current_weather":{"temperature":32.8,"windspeed":19.4,"winddirection":235.0,"weathercode":3,"is_day":1,"time":"2023-07-12T15:00"},"daily_units":{"time":"iso8601","weathercode":"wmo code","windspeed_10m_max":"km/h"},"daily":{"time":["2023-07-12","2023-07-13","2023-07-14","2023-07-15","2023-07-16","2023-07-17","2023-07-18"],"weathercode":[3,3,0,0,3,2,0],"windspeed_10m_max":[20.0,14.6,22.6,27.6,17.7,9.4,14.4]}}'

    def _now(self):
        return datetime.datetime(2023,7,12)