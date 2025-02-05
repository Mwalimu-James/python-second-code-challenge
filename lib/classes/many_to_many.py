class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(hometown, str) or not hometown.strip():
            raise ValueError("Hometown must be a non-empty string.")
        self._name = name
        self._hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        pass  # Ignore modifications.

    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list({concert.venue for concert in self.concerts()})

    def play_in_venue(self, venue, date):
        return Concert(date=date, band=self, venue=venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]

    def __repr__(self):
        return f"Band(name='{self.name}', hometown='{self.hometown}')"


class Concert:
    all = []

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or not date.strip():
            raise ValueError("Date must be a non-empty string.")
        if not isinstance(band, Band):
            raise ValueError("Band must be an instance of Band class.")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be an instance of Venue class.")
        self._date = date
        self._band = band
        self._venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and value.strip():
            self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            print("Invalid value for band; ignoring.")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            print("Invalid value for venue; ignoring.")

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def __repr__(self):
        return f"Concert(date='{self.date}', band={self.band.name}, venue={self.venue.name}')"


class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(city, str) or not city.strip():
            raise ValueError("City must be a non-empty string.")
        self._name = name
        self._city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and value.strip():
            self._city = value

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})

    def __repr__(self):
        return f"Venue(name='{self.name}', city='{self.city}')"