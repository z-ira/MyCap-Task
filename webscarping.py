import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect


parser = argparser.ArgumentParser()
parser.add_argument("--page_number_MAX",help="Enter the number of pages to parse: ",type = int)
parser.add_argument("--dbname",help="Enter the number of pages to parse: ",type = int)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_number_MAX = args.page_number_MAX
scraped_info_list = []
connect.connect(args.dbname)

for page_number in range(1,page_number_MAX):
    req = requests.get(oyo_url+str(page_number))
    content = req.content
    print(content)

    soup = BeautifulSoup(content,"html.parser")

    all_hotels = soup.find_all("div",{"class" : "hotelCardListing"})

    for hotel in all_hotels :
        hotel_dict = {}
        hotel_dict["name"]= hotel.find("h3",{"class" : "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span",{"itemprop" : "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span",{"class" : "listingPrice__finalPrice"}).text

        #try ..... except block
        try :
            hotel_dict["rating"] = hotel.find("span",{"class" : "hotelRating__ratingSummary"}).text
        except AttributeError :
            hotel_dict["rating"]=None
            
        parent_amenities_element = hotel.find("div",{"class" : "amenityWrapper"})

        amenities_list = []
        for amenity in parent_amenities_element.find_all("div",{"class" : "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span",{"class" : "d-body-smd"}).text.strip())

        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))
        
        # print(hotel_name,hotel_address,hotel_rating,hotel_price,amenities_list)

dataFrame = pandas.DataFrame(scraped_info_list)
print("Creating new csv file ...")
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)
