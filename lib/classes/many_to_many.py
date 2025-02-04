class Band:
    all_bands = []  # Track all bands
    
    def __init__(self, name, hometown):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Band name must be a non-empty string.")
        if not isinstance(hometown, str) or not hometown.strip():
            raise ValueError("Hometown must be a non-empty string.")
        
        self._name = name
        self._hometown = hometown
        Band.all_bands.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, new_hometown):
        if isinstance(new_hometown, str) and new_hometown.strip():
            self._hometown = new_hometown
        else:
            raise ValueError("Hometown must be a non-empty string.")
    
    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]
    
    def venues(self):
        return list(set(concert.venue for concert in self.concerts()))
    
    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)
    
    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]

class Venue:
    all_venues = []
    
    def __init__(self, name, city):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Venue name must be a non-empty string.")
        if not isinstance(city, str) or not city.strip():
            raise ValueError("City must be a non-empty string.")
        
        self._name = name
        self._city = city
        Venue.all_venues.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, new_city):
        if isinstance(new_city, str) and new_city.strip():
            self._city = new_city
    
    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]
    
    def bands(self):
        return list(set(concert.band for concert in self.concerts()))
    
    def concert_on(self, date):
        return next((concert for concert in self.concerts() if concert.date == date), None)

class Concert:
    all = []  # Track all concerts, matches test expectation
    
    def __init__(self, date, band, venue):
        if isinstance(date, (str, int)):
            date = str(date)
        if not date.strip():
            raise ValueError("Concert date must be a non-empty string.")
        if not isinstance(band, Band):
            raise ValueError("Band must be an instance of the Band class.")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be an instance of the Venue class.")
        
        self._date = date
        self._band = band
        self._venue = venue
        
        # Ensure concerts are added properly to the list
        Concert.all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str) and new_date.strip():
            self._date = new_date
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, new_band):
        if isinstance(new_band, Band):
            self._band = new_band
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, new_venue):
        if isinstance(new_venue, Venue):
            self._venue = new_venue
    
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
