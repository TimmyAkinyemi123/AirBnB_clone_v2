create State
create State name="California"
create State name="California" + create City state_id="<new state ID>" name="Fremont"
create State name="California" + create City state_id="<new state ID>" name="San_Francisco"
create State name="California" + create City state_id="<new state ID>" name="San_Francisco_is_super_cool" + create User email="my@me.com" password="pwd" first_name="FN" last_name="LN" + create Place city_id="<new city ID>" user_id="<new user ID>" name="My_house" description="no_description_yet" number_rooms=4 number_bathrooms=1 max_guest=3 price_by_night=100 latitude=120.12 longitude=101.4 + show Place <new place ID>
