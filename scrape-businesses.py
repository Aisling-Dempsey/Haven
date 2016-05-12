from helper import yelp_api
from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

def build_csv(city, state):
    """Takes string of "city, state" as argument and builds csv of applicable information for db seeding
    in format of: yelp_id|name|address_1|address_2|city|state_code|zipcode|phone|lat|long|categories """
    city_state = "%s, %s" % (city, state)
    #returns number of results for city_state
    # result_count = yelp_api.search_query(location= city_state)['total']

    # creates a csv in format outlined above

    with open(city+".csv", 'a') as f:
        categories = ['active', 'arts', 'auto', 'beautysvc', 'education', 'eventservices', 'financialservices', 'food',
                      'health', 'homeservices', 'hotelstravel', 'localflavor', 'localservices', 'massmedia',
                      'nightlife', 'pets', 'professional', 'publicservicesgovt', 'realestate', 'religiousorgs',
                      'restaurants', 'shopping']
        line = 0
        for category in categories:
            offset = 0
            result_count = yelp_api.search_query(location=city_state, category_fiter=category)['total']
            while offset < result_count and offset <1000:

                results = yelp_api.search_query(location=city_state, category_filter=category, offset=offset)

                for business in results['businesses']:

                    try:
                        info = []
                        # id
                        info.append(unicode(business['id']))
                        # name
                        info.append(unicode(business['name']))

                        # address lines 1 and 2
                        if business['location'].get('address'):
                            info.append(str(business['location']['address'][0]))
                            if len(business['location']['address']) > 1:
                                info.append(str(business['location']['address'][1]))

                            else: info.append("")

                        else:
                            info.append("")
                            info.append("")

                        # city
                        info.append(str(business['location']['city']))
                        # state code
                        info.append(str(business['location']['state_code']))
                        # zip code
                        info.append(str(business['location']['postal_code']))

                        # phone
                        if business.get('phone'):
                            info.append(str(business['phone']))
                        else:
                            info.append("")

                        # latitude and longitude
                        if business['location'].get('coordinate'):
                            info.append(str(business['location']['coordinate']['latitude']))
                            info.append(str(business['location']['coordinate']['longitude']))
                        else:
                            info.append("")
                            info.append("")

                        # list of categories
                        if business.get('categories'):
                            info.append(str((business['categories'])))
                        else:
                            info.append("")
                        # converts info list to pipe separated
                        data_string = "|".join(info)
                        data_string += "\n"
                        # try:
                        #     # have tried this with the addition of "str.encode('utf8')
                        f.write(data_string)
                        line += 1
                        print line
                        print category
                    except:
                        pass
                offset += 20

build_csv(argv[1], argv[2])