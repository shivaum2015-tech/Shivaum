class India():
    def capital(self):
        print("New Dehli is the capital of India.")

    def language(self):
        print("Hindi is the most spoken language in India.")

    def type(self):
        print ("India is a developing country.")
class USA():
    def capital(self):
        print ("Washington D.C is the capital of the USA.")

    def language(self):
        print ("English is the most spoken language in the USA.")

    def type(self):
        print ("USA is a developed country")

obj_ind = India()
obdj_usa =USA()

for country in (obj_ind, obdj_usa):
    country.capital()
    country.language()
    country.type()