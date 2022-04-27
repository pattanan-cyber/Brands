from models.modelbrand_ads import Brand, Ads
from package.brand_ads import Brands

db = Brands()
sol = db.brand().name_eqaul('GOOGLE')

print(sol)
