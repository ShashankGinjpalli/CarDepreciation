class listing_obj:
    def __init__(self, make, title, year, price, mileage, condition, specifications, date_collected, zipcode):
        self.make = make
        self.title = title
        self.year = year
        self.price = price
        self.mileage = mileage
        self.condition = condition
        self.specifications = specifications
        self.date_collected = date_collected
        self.zipcode = zipcode

    def to_dict(self):
        return {'make': self.make, 'title': self.title, 'year': self.year, 'price': self.price, 'mileage': self.mileage, 'condition': self.condition, 'specifications': self.specifications, 'date_collected': self.date_collected, 'zipcode': self.zipcode}
