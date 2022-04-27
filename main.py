from models.modelbrand_ads import Brand, Ads
from package.brand_ads import Brands
db = Brands()
all_brand = db.brand().all_brands()
print(all_brand)
