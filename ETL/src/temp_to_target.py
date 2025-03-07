from ETL.to_target.country import *
from ETL.to_target.region import *
from ETL.to_target.customer import *
from ETL.to_target.category import *
from ETL.to_target.product import *
from ETL.to_target.subcategory import *
from ETL.to_target.sales import *
from ETL.to_target.location import *
def main():
    load_country_to_tgt()
    load_region_to_tgt()
    load_customer_to_tgt()
    load_category_to_tgt()
    load_subcategory_to_tgt()
    load_product_to_tgt()
    load_location_to_tgt()
    load_sales_to_tgt()
if __name__ == '__main__':
    main()