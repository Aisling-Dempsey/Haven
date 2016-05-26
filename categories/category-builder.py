import json
def get_usable_pairings(categories):
    with open("categories.json", 'w') as f:
        cat_pairs = {}
        for category in categories:
                print type(category['parents'])
                print category['title']
                if len(category['parents']) == 1:
                    cat_pairs[category['title']] = {'parent_cat': category['parents'][0]}
                    print cat_pairs[category['title']]

                elif len(category['parents']) > 1:
                    cat_pairs[category['title']] = {'parent_cat': category['parents'][0]}
                    cat_pairs[category['title']]['second_parent_cat'] = category['parents'][1]

        json_string = json.dumps(cat_pairs)
        f.write(json_string)



categories =[{
        "alias": "airportlounges",
        "parents": [
            "bars"
        ],
        "title": "Airport Lounges"
    },
    {
        "alias": "airports",
        "parents": [
            "hotelstravel"
        ],
        "title": "Airports"
    },
    {
        "alias": "airportterminals",
        "parents": [
            "airports"
        ],
        "title": "Airport Terminals"
    },
    {
        "alias": "airsoft",
        "parents": [
            "active"
        ],
        "title": "Airsoft"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "alentejo",
        "parents": [
            "portuguese"
        ],
        "title": "Alentejo"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "algarve",
        "parents": [
            "portuguese"
        ],
        "title": "Algarve"
    },
    {
        "alias": "allergist",
        "parents": [
            "physicians"
        ],
        "title": "Allergists"
    },
    {
        "country_whitelist": [
            "FR",
            "DE"
        ],
        "alias": "alsatian",
        "parents": [
            "french"
        ],
        "title": "Alsatian"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "altoatesine",
        "parents": [
            "italian"
        ],
        "title": "Altoatesine"
    },
    {
        "alias": "amateursportsteams",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "active"
        ],
        "title": "Amateur Sports Teams"
    },
    {
        "alias": "amusementparks",
        "parents": [
            "active"
        ],
        "title": "Amusement Parks"
    },
    {
        "country_whitelist": [
            "IT",
            "ES"
        ],
        "alias": "andalusian",
        "parents": [
            "restaurants"
        ],
        "title": "Andalusian"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "AU",
            "SE",
            "PT",
            "IT",
            "US"
        ],
        "alias": "anesthesiologists",
        "parents": [
            "physicians"
        ],
        "title": "Anesthesiologists"
    },
    {
        "alias": "animalshelters",
        "parents": [
            "pets"
        ],
        "title": "Animal Shelters"
    },
    {
        "alias": "antiques",
        "parents": [
            "shopping"
        ],
        "title": "Antiques"
    },
    {
        "alias": "apartments",
        "parents": [
            "realestate"
        ],
        "title": "Apartments"
    },
    {
        "alias": "appliances",
        "parents": [
            "homeandgarden"
        ],
        "title": "Appliances"
    },
    {
        "alias": "appraisalservices",
        "parents": [
            "localservices"
        ],
        "title": "Appraisal Services"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "apulian",
        "parents": [
            "italian"
        ],
        "title": "Apulian"
    },
    {
        "alias": "aquariums",
        "parents": [
            "active"
        ],
        "title": "Aquariums"
    },
    {
        "alias": "aquariumservices",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "petservices"
        ],
        "title": "Aquarium Services"
    },
    {
        "alias": "arabian",
        "country_blacklist": [
            "DK"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Arabian"
    },
    {
        "country_whitelist": [
            "BR"
        ],
        "alias": "arabpizza",
        "parents": [
            "arabian"
        ],
        "title": "Arab Pizza"
    },
    {
        "alias": "arcades",
        "parents": [
            "arts"
        ],
        "title": "Arcades"
    },
    {
        "alias": "archery",
        "parents": [
            "active"
        ],
        "title": "Archery"
    },
    {
        "alias": "architects",
        "parents": [
            "professional"
        ],
        "title": "Architects"
    },
    {
        "alias": "architecturaltours",
        "parents": [
            "tours"
        ],
        "title": "Architectural Tours"
    },
    {
        "alias": "argentine",
        "country_blacklist": [
            "FI"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Argentine"
    },
    {
        "country_whitelist": [
            "ES",
            "BE",
            "FR",
            "TR",
            "IT",
            "US",
            "CZ",
            "AR",
            "GB",
            "PL"
        ],
        "alias": "armenian",
        "parents": [
            "restaurants"
        ],
        "title": "Armenian"
    },
    {
        "country_whitelist": [
            "ES"
        ],
        "alias": "arroceria_paella",
        "parents": [
            "spanish"
        ],
        "title": "Arroceria / Paella"
    },
    {
        "alias": "artclasses",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "education"
        ],
        "title": "Art Classes"
    },
    {
        "alias": "artrestoration",
        "parents": [
            "localservices"
        ],
        "title": "Art Restoration"
    },
    {
        "alias": "arts",
        "parents": [],
        "title": "Arts & Entertainment"
    },
    {
        "alias": "artsandcrafts",
        "parents": [
            "shopping"
        ],
        "title": "Arts & Crafts"
    },
    {
        "alias": "artschools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Art Schools"
    },
    {
        "country_whitelist": [
            "HK",
            "SE",
            "SG",
            "JP",
            "IT",
            "US"
        ],
        "alias": "artspacerentals",
        "parents": [
            "realestate"
        ],
        "title": "Art Space Rentals"
    },
    {
        "alias": "artsupplies",
        "parents": [
            "artsandcrafts"
        ],
        "title": "Art Supplies"
    },
    {
        "alias": "arttours",
        "parents": [
            "tours"
        ],
        "title": "Art Tours"
    },
    {
        "alias": "asianfusion",
        "parents": [
            "restaurants"
        ],
        "title": "Asian Fusion"
    },
    {
        "alias": "assistedliving",
        "parents": [
            "health"
        ],
        "title": "Assisted Living Facilities"
    },
    {
        "country_whitelist": [
            "ES"
        ],
        "alias": "asturian",
        "parents": [
            "restaurants"
        ],
        "title": "Asturian"
    },
    {
        "country_whitelist": [
            "ES",
            "CH",
            "DK",
            "NO",
            "DE",
            "IT",
            "US",
            "AT",
            "SE"
        ],
        "alias": "attractionfarms",
        "parents": [
            "farms"
        ],
        "title": "Attraction Farms"
    },
    {
        "country_whitelist": [
            "FI",
            "SE",
            "US",
            "NO"
        ],
        "alias": "atvrentals",
        "parents": [
            "active"
        ],
        "title": "ATV Rentals/Tours"
    },
    {
        "alias": "auctionhouses",
        "country_blacklist": [
            "CH",
            "CL",
            "CA",
            "DE",
            "JP",
            "HK",
            "AR",
            "AT",
            "SG",
            "IE",
            "TW",
            "TR",
            "NZ",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Auction Houses"
    },
    {
        "alias": "audiologist",
        "country_blacklist": [
            "CZ",
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Audiologist"
    },
    {
        "alias": "australian",
        "country_blacklist": [
            "DK",
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Australian"
    },
    {
        "alias": "austrian",
        "country_blacklist": [
            "DK",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Austrian"
    },
    {
        "country_whitelist": [
            "SE",
            "NO"
        ],
        "alias": "authorized_postal_representative",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Authorized Postal Representative"
    },
    {
        "alias": "auto",
        "parents": [],
        "title": "Automotive"
    },
    {
        "alias": "auto_detailing",
        "country_blacklist": [
            "AU",
            "BR",
            "ES"
        ],
        "parents": [
            "auto"
        ],
        "title": "Auto Detailing"
    },
    {
        "country_whitelist": [
            "CZ",
            "SG",
            "PT",
            "US"
        ],
        "alias": "autocustomization",
        "parents": [
            "auto"
        ],
        "title": "Auto Customization"
    },
    {
        "country_whitelist": [
            "NO",
            "DE",
            "DK",
            "US",
            "SE"
        ],
        "alias": "autodamageassessment",
        "parents": [
            "auto"
        ],
        "title": "Car Inspectors"
    },
    {
        "country_whitelist": [
            "CZ",
            "IT",
            "BR"
        ],
        "alias": "autoelectric",
        "parents": [
            "auto"
        ],
        "title": "Auto Electric Services"
    },
    {
        "alias": "autoglass",
        "country_blacklist": [
            "ES"
        ],
        "parents": [
            "auto"
        ],
        "title": "Auto Glass Services"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "DK",
            "NO",
            "JP",
            "TR",
            "IT",
            "US",
            "CZ",
            "AU",
            "ES",
            "BR",
            "SE"
        ],
        "alias": "autoinsurance",
        "parents": [
            "insurance"
        ],
        "title": "Auto Insurance"
    },
    {
        "country_whitelist": [
            "PT",
            "CA",
            "TR",
            "IT",
            "US",
            "CZ",
            "AU",
            "SG"
        ],
        "alias": "autoloanproviders",
        "parents": [
            "auto"
        ],
        "title": "Auto Loan Providers"
    },
    {
        "alias": "autopartssupplies",
        "parents": [
            "auto"
        ],
        "title": "Auto Parts & Supplies"
    },
    {
        "alias": "autorepair",
        "parents": [
            "auto"
        ],
        "title": "Auto Repair"
    },
    {
        "alias": "autoupholstery",
        "parents": [
            "auto"
        ],
        "title": "Auto Upholstery"
    },
    {
        "country_whitelist": [
            "FR"
        ],
        "alias": "auvergnat",
        "parents": [
            "french"
        ],
        "title": "Auvergnat"
    },
    {
        "alias": "awnings",
        "parents": [
            "localservices"
        ],
        "title": "Awnings"
    },
    {
        "alias": "ayurveda",
        "parents": [
            "health"
        ],
        "title": "Ayurveda"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "azores",
        "parents": [
            "portuguese"
        ],
        "title": "Azores"
    },
    {
        "alias": "baby_gear",
        "parents": [
            "shopping"
        ],
        "title": "Baby Gear & Furniture"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "backshop",
        "parents": [
            "food"
        ],
        "title": "Backshop"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "baden",
        "parents": [
            "german"
        ],
        "title": "Baden"
    },
    {
        "alias": "badminton",
        "country_blacklist": [
            "NZ",
            "SG",
            "BR",
            "ES",
            "PL"
        ],
        "parents": [
            "active"
        ],
        "title": "Badminton"
    },
    {
        "alias": "bagels",
        "country_blacklist": [
            "AU",
            "ES"
        ],
        "parents": [
            "food"
        ],
        "title": "Bagels"
    },
    {
        "country_whitelist": [
            "PT",
            "NO",
            "DE",
            "TR",
            "IT",
            "CZ",
            "MX",
            "SE"
        ],
        "alias": "baguettes",
        "parents": [
            "restaurants"
        ],
        "title": "Baguettes"
    },
    {
        "country_whitelist": [
            "PT",
            "US"
        ],
        "alias": "bailbondsmen",
        "parents": [
            "localservices"
        ],
        "title": "Bail Bondsmen"
    },
    {
        "alias": "bakeries",
        "parents": [
            "food"
        ],
        "title": "Bakeries"
    },
    {
        "alias": "bangladeshi",
        "country_blacklist": [
            "ES",
            "TR",
            "DK",
            "PT",
            "MX"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Bangladeshi"
    },
    {
        "alias": "bankruptcy",
        "parents": [
            "lawyers"
        ],
        "title": "Bankruptcy Law"
    },
    {
        "alias": "banks",
        "parents": [
            "financialservices"
        ],
        "title": "Banks & Credit Unions"
    },
    {
        "alias": "barbers",
        "parents": [
            "beautysvc"
        ],
        "title": "Barbers"
    },
    {
        "country_whitelist": [
            "CZ",
            "AU",
            "PT",
            "US"
        ],
        "alias": "barreclasses",
        "parents": [
            "fitness"
        ],
        "title": "Barre Classes"
    },
    {
        "alias": "bars",
        "parents": [
            "nightlife"
        ],
        "title": "Bars"
    },
    {
        "alias": "bartenders",
        "country_blacklist": [
            "CH",
            "NO",
            "IE",
            "SG",
            "TR",
            "JP",
            "HK",
            "NZ",
            "AT",
            "TW",
            "FI",
            "PH",
            "MY",
            "PL",
            "GB"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Bartenders"
    },
    {
        "alias": "bartendingschools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Bartending Schools"
    },
    {
        "alias": "baseballfields",
        "country_blacklist": [
            "FR"
        ],
        "parents": [
            "active"
        ],
        "title": "Baseball Fields"
    },
    {
        "alias": "basketballcourts",
        "country_blacklist": [
            "NL",
            "GB",
            "BR",
            "CA",
            "IE",
            "SE",
            "PL"
        ],
        "parents": [
            "active"
        ],
        "title": "Basketball Courts"
    },
    {
        "alias": "basque",
        "country_blacklist": [
            "CZ",
            "AU",
            "DK",
            "PT",
            "SG",
            "TR"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Basque"
    },
    {
        "country_whitelist": [
            "CZ",
            "PT",
            "NO",
            "FI",
            "DE",
            "JP",
            "SE"
        ],
        "alias": "bathing_area",
        "parents": [
            "active"
        ],
        "title": "Bathing Area"
    },
    {
        "alias": "batterystores",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Battery Stores"
    },
    {
        "country_whitelist": [
            "JP",
            "SG",
            "US",
            "TW"
        ],
        "alias": "battingcages",
        "parents": [
            "active"
        ],
        "title": "Batting Cages"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT"
        ],
        "alias": "bavarian",
        "parents": [
            "restaurants"
        ],
        "title": "Bavarian"
    },
    {
        "alias": "bbq",
        "country_blacklist": [
            "AU",
            "BR"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Barbeque"
    },
    {
        "alias": "beachbars",
        "country_blacklist": [
            "BE",
            "HK",
            "IE",
            "JP",
            "CA",
            "TR",
            "US",
            "CZ",
            "NZ",
            "GB",
            "TW",
            "FI",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "bars"
        ],
        "title": "Beach Bars"
    },
    {
        "alias": "beachequipmentrental",
        "parents": [
            "active"
        ],
        "title": "Beach Equipment Rentals"
    },
    {
        "alias": "beaches",
        "parents": [
            "active"
        ],
        "title": "Beaches"
    },
    {
        "country_whitelist": [
            "DK",
            "NO",
            "DE",
            "JP",
            "CZ",
            "AU",
            "AT",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "alias": "beachvolleyball",
        "parents": [
            "active"
        ],
        "title": "Beach Volleyball"
    },
    {
        "alias": "beautysvc",
        "parents": [],
        "title": "Beauty & Spas"
    },
    {
        "alias": "bedbreakfast",
        "country_blacklist": [
            "SG"
        ],
        "parents": [
            "hotelstravel"
        ],
        "title": "Bed & Breakfast"
    },
    {
        "alias": "beer_and_wine",
        "parents": [
            "food"
        ],
        "title": "Beer, Wine & Spirits"
    },
    {
        "alias": "beerbar",
        "country_blacklist": [
            "CH",
            "NL",
            "IE",
            "TW",
            "CA",
            "DE",
            "TR",
            "IT",
            "AT",
            "PH",
            "MY",
            "PL",
            "GB"
        ],
        "parents": [
            "bars"
        ],
        "title": "Beer Bar"
    },
    {
        "country_whitelist": [
            "CZ",
            "CH",
            "DE",
            "AT"
        ],
        "alias": "beergarden",
        "parents": [
            "restaurants"
        ],
        "title": "Beer Garden"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "NO",
            "JP",
            "IT",
            "US",
            "PL",
            "CZ",
            "AU",
            "GB",
            "IE",
            "MX",
            "SE"
        ],
        "alias": "beergardens",
        "parents": [
            "nightlife"
        ],
        "title": "Beer Gardens"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT"
        ],
        "alias": "beerhall",
        "parents": [
            "restaurants"
        ],
        "title": "Beer Hall"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "beira",
        "parents": [
            "portuguese"
        ],
        "title": "Beira"
    },
    {
        "country_whitelist": [
            "AT"
        ],
        "alias": "beisl",
        "parents": [
            "restaurants"
        ],
        "title": "Beisl"
    },
    {
        "alias": "belgian",
        "country_blacklist": [
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Belgian"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "bento",
        "parents": [
            "food"
        ],
        "title": "Bento"
    },
    {
        "country_whitelist": [
            "FR"
        ],
        "alias": "berrichon",
        "parents": [
            "french"
        ],
        "title": "Berrichon"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "DK",
            "PT",
            "NO",
            "DE",
            "IT",
            "US",
            "CZ",
            "AT",
            "SG",
            "ES"
        ],
        "alias": "bespoke",
        "parents": [
            "shopping"
        ],
        "title": "Bespoke Clothing"
    },
    {
        "alias": "bettingcenters",
        "country_blacklist": [
            "FR",
            "NO",
            "CA",
            "US",
            "NZ",
            "BR",
            "FI",
            "SG"
        ],
        "parents": [
            "arts"
        ],
        "title": "Betting Centers"
    },
    {
        "country_whitelist": [
            "CH",
            "PT",
            "CL",
            "DE",
            "TR",
            "IT",
            "AU",
            "AT",
            "ES"
        ],
        "alias": "beverage_stores",
        "parents": [
            "food"
        ],
        "title": "Beverage Store"
    },
    {
        "alias": "bicyclepaths",
        "country_blacklist": [
            "BE",
            "FR",
            "CH",
            "NL",
            "TW",
            "CA",
            "DE",
            "TR",
            "IT",
            "US",
            "HK",
            "AT",
            "PH",
            "MY"
        ],
        "parents": [
            "active"
        ],
        "title": "Bicycle Paths"
    },
    {
        "country_whitelist": [
            "DK"
        ],
        "alias": "bicycles",
        "parents": [],
        "title": "Bicycles"
    },
    {
        "alias": "bike_repair_maintenance",
        "parents": [
            "localservices"
        ],
        "title": "Bike Repair/Maintenance"
    },
    {
        "country_whitelist": [
            "DK",
            "PT"
        ],
        "alias": "bikeassociations",
        "parents": [
            "bicycles"
        ],
        "title": "Bike Associations"
    },
    {
        "alias": "bikerentals",
        "parents": [
            "active"
        ],
        "title": "Bike Rentals"
    },
    {
        "country_whitelist": [
            "DK",
            "PT"
        ],
        "alias": "bikerepair",
        "parents": [
            "bicycles"
        ],
        "title": "Bike Repair"
    },
    {
        "alias": "bikes",
        "parents": [
            "sportgoods"
        ],
        "title": "Bikes"
    },
    {
        "alias": "bikesharing",
        "parents": [
            "transport"
        ],
        "title": "Bike Sharing"
    },
    {
        "country_whitelist": [
            "DK",
            "PT"
        ],
        "alias": "bikeshop",
        "parents": [
            "bicycles"
        ],
        "title": "Bike Shop"
    },
    {
        "country_whitelist": [
            "ES",
            "DK",
            "CL",
            "NO",
            "IT",
            "US",
            "NZ",
            "AR",
            "AU",
            "GB",
            "BR",
            "FI",
            "IE",
            "MX",
            "SE"
        ],
        "alias": "bingo",
        "parents": [
            "arts"
        ],
        "title": "Bingo Halls"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "DK",
            "NO",
            "DE",
            "IT",
            "US",
            "ES",
            "SG",
            "SE"
        ],
        "alias": "birdshops",
        "parents": [
            "petstore"
        ],
        "title": "Bird Shops"
    },
    {
        "alias": "bistros",
        "country_blacklist": [
            "CA",
            "ES",
            "US"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Bistros"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "blacksea",
        "parents": [
            "restaurants"
        ],
        "title": "Black Sea"
    },
    {
        "alias": "blinds",
        "parents": [
            "homeservices"
        ],
        "title": "Shades & Blinds"
    },
    {
        "alias": "blooddonation",
        "country_blacklist": [
            "BE",
            "NL",
            "PT",
            "IE",
            "SG",
            "CA",
            "HK",
            "GB",
            "TW",
            "FI",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "health"
        ],
        "title": "Blood & Plasma Donation Centers"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "blowfish",
        "parents": [
            "japanese"
        ],
        "title": "Blowfish"
    },
    {
        "country_whitelist": [
            "FR",
            "PT",
            "CA",
            "TR",
            "US",
            "CZ",
            "AU",
            "GB",
            "IE"
        ],
        "alias": "blowoutservices",
        "parents": [
            "hair"
        ],
        "title": "Blow Dry/Out Services"
    },
    {
        "alias": "boatcharters",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Boat Charters"
    },
    {
        "country_whitelist": [
            "ES",
            "DK",
            "PT",
            "NO",
            "IE",
            "DE",
            "US",
            "CZ",
            "GB",
            "SE",
            "SG",
            "MX",
            "PL"
        ],
        "alias": "boatdealers",
        "parents": [
            "auto"
        ],
        "title": "Boat Dealers"
    },
    {
        "alias": "boating",
        "parents": [
            "active"
        ],
        "title": "Boating"
    },
    {
        "alias": "boatrepair",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "professional"
        ],
        "title": "Boat Repair"
    },
    {
        "alias": "bodyshops",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "auto"
        ],
        "title": "Body Shops"
    },
    {
        "alias": "bookbinding",
        "parents": [
            "localservices"
        ],
        "title": "Bookbinding"
    },
    {
        "alias": "bookstores",
        "parents": [
            "media"
        ],
        "title": "Bookstores"
    },
    {
        "country_whitelist": [
            "NZ",
            "AU",
            "ES",
            "PT",
            "SE",
            "IT",
            "US"
        ],
        "alias": "bootcamps",
        "parents": [
            "fitness"
        ],
        "title": "Boot Camps"
    },
    {
        "country_whitelist": [
            "FR"
        ],
        "alias": "bourguignon",
        "parents": [
            "french"
        ],
        "title": "Bourguignon"
    },
    {
        "alias": "bowling",
        "parents": [
            "active"
        ],
        "title": "Bowling"
    },
    {
        "alias": "boxing",
        "country_blacklist": [
            "ES",
            "DK",
            "NO",
            "TR",
            "AU",
            "PL",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "parents": [
            "fitness"
        ],
        "title": "Boxing"
    },
    {
        "alias": "brasseries",
        "country_blacklist": [
            "AR",
            "MX"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Brasseries"
    },
    {
        "alias": "brazilian",
        "parents": [
            "restaurants"
        ],
        "title": "Brazilian"
    },
    {
        "country_whitelist": [
            "BR"
        ],
        "alias": "brazilianempanadas",
        "parents": [
            "brazilian"
        ],
        "title": "Brazilian Empanadas"
    },
    {
        "alias": "breakfast_brunch",
        "parents": [
            "restaurants"
        ],
        "title": "Breakfast & Brunch"
    },
    {
        "alias": "breweries",
        "parents": [
            "food"
        ],
        "title": "Breweries"
    },
    {
        "alias": "brewingsupplies",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Brewing Supplies"
    },
    {
        "alias": "bridal",
        "parents": [
            "shopping"
        ],
        "title": "Bridal"
    },
    {
        "alias": "british",
        "country_blacklist": [
            "FI"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "British"
    },
    {
        "alias": "bubbletea",
        "country_blacklist": [
            "CH",
            "NL",
            "PT",
            "CA",
            "TR",
            "IT",
            "NZ",
            "AR",
            "AT",
            "BR",
            "MX",
            "ES"
        ],
        "parents": [
            "food"
        ],
        "title": "Bubble Tea"
    },
    {
        "alias": "buddhist_temples",
        "parents": [
            "religiousorgs"
        ],
        "title": "Buddhist Temples"
    },
    {
        "alias": "buffets",
        "parents": [
            "restaurants"
        ],
        "title": "Buffets"
    },
    {
        "alias": "buildingsupplies",
        "parents": [
            "homeservices"
        ],
        "title": "Building Supplies"
    },
    {
        "alias": "bulgarian",
        "country_blacklist": [
            "NL",
            "DK",
            "PT",
            "NO",
            "CA",
            "TR",
            "US",
            "NZ",
            "BR",
            "SG",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Bulgarian"
    },
    {
        "country_whitelist": [
            "AU"
        ],
        "alias": "bulkbilling",
        "parents": [
            "medcenters"
        ],
        "title": "Bulk Billing"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "CL",
            "NO",
            "JP",
            "CZ",
            "NZ",
            "AR",
            "BR",
            "MX",
            "ES"
        ],
        "alias": "bungeejumping",
        "parents": [
            "active"
        ],
        "title": "Bungee Jumping"
    },
    {
        "alias": "burgers",
        "parents": [
            "restaurants"
        ],
        "title": "Burgers"
    },
    {
        "alias": "burmese",
        "country_blacklist": [
            "CZ",
            "DK",
            "PT",
            "FI",
            "TR",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Burmese"
    },
    {
        "alias": "buses",
        "parents": [
            "transport"
        ],
        "title": "Buses"
    },
    {
        "country_whitelist": [
            "ES",
            "FR",
            "CH",
            "DK",
            "PT",
            "NO",
            "CA",
            "DE",
            "JP",
            "IT",
            "US",
            "AU",
            "AT",
            "BR",
            "SE"
        ],
        "alias": "businessconsulting",
        "parents": [
            "professional"
        ],
        "title": "Business Consulting"
    },
    {
        "country_whitelist": [
            "CZ",
            "GB",
            "PT",
            "CA",
            "IE",
            "US"
        ],
        "alias": "businesslawyers",
        "parents": [
            "lawyers"
        ],
        "title": "Business Law"
    },
    {
        "country_whitelist": [
            "DK",
            "CL",
            "NO",
            "IT",
            "AR",
            "BR",
            "MX",
            "ES"
        ],
        "alias": "busrental",
        "parents": [
            "localservices"
        ],
        "title": "Bus Rental"
    },
    {
        "alias": "bustours",
        "parents": [
            "tours"
        ],
        "title": "Bus Tours"
    },
    {
        "alias": "butcher",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "food"
        ],
        "title": "Butcher"
    },
    {
        "alias": "c_and_mh",
        "parents": [
            "health"
        ],
        "title": "Counseling & Mental Health"
    },
    {
        "alias": "cabaret",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "arts"
        ],
        "title": "Cabaret"
    },
    {
        "alias": "cabinetry",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Cabinetry"
    },
    {
        "country_whitelist": [
            "FR",
            "CH",
            "JP",
            "DE",
            "TR",
            "IT",
            "US",
            "CZ",
            "NZ",
            "AT",
            "BR"
        ],
        "alias": "cablecars",
        "parents": [
            "transport"
        ],
        "title": "Cable Cars"
    },
    {
        "alias": "cafes",
        "country_blacklist": [
            "AR",
            "MX",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Cafes"
    },
    {
        "alias": "cafeteria",
        "country_blacklist": [
            "FR",
            "IE",
            "CA",
            "CZ",
            "NZ",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Cafeteria"
    },
    {
        "alias": "cajun",
        "country_blacklist": [
            "AU",
            "SG",
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Cajun/Creole"
    },
    {
        "alias": "cakeshop",
        "country_blacklist": [
            "CL",
            "CA",
            "TR",
            "US",
            "HK",
            "AR",
            "ES",
            "FI",
            "PL"
        ],
        "parents": [
            "food"
        ],
        "title": "Patisserie/Cake Shop"
    },
    {
        "country_whitelist": [
            "IT",
            "US"
        ],
        "alias": "calabrian",
        "parents": [
            "italian"
        ],
        "title": "Calabrian"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "ES",
            "BR",
            "IT",
            "US"
        ],
        "alias": "calligraphy",
        "parents": [
            "localservices"
        ],
        "title": "Calligraphy"
    },
    {
        "alias": "cambodian",
        "country_blacklist": [
            "CZ",
            "DK",
            "PT",
            "FI",
            "TR",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Cambodian"
    },
    {
        "alias": "campgrounds",
        "parents": [
            "hotelstravel"
        ],
        "title": "Campgrounds"
    },
    {
        "alias": "candy",
        "parents": [
            "gourmet"
        ],
        "title": "Candy Stores"
    },
    {
        "country_whitelist": [
            "NL",
            "GB",
            "IE",
            "CA",
            "TR",
            "US",
            "PL"
        ],
        "alias": "cannabis_clinics",
        "parents": [
            "health"
        ],
        "title": "Cannabis Clinics"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "cannabisdispensaries",
        "parents": [
            "shopping"
        ],
        "title": "Cannabis Dispensaries"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "cannabisreferrals",
        "parents": [
            "health"
        ],
        "title": "Medical Cannabis Referrals"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "cannabistours",
        "parents": [
            "cannabis_clinics"
        ],
        "title": "Cannabis Tours"
    },
    {
        "country_whitelist": [
            "CH",
            "DK",
            "NO",
            "DE",
            "JP",
            "IT",
            "CZ",
            "AT",
            "PL"
        ],
        "alias": "canteen",
        "parents": [
            "restaurants"
        ],
        "title": "Canteen"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "MY",
            "TW",
            "JP",
            "IT",
            "US",
            "HK",
            "NZ",
            "AR",
            "AU",
            "GB",
            "SG",
            "SE"
        ],
        "alias": "cantonese",
        "parents": [
            "chinese"
        ],
        "title": "Cantonese"
    },
    {
        "alias": "car_dealers",
        "parents": [
            "auto"
        ],
        "title": "Car Dealers"
    },
    {
        "country_whitelist": [
            "NZ",
            "AR",
            "AU",
            "US"
        ],
        "alias": "carbrokers",
        "parents": [
            "auto"
        ],
        "title": "Car Brokers"
    },
    {
        "country_whitelist": [
            "CZ",
            "NZ",
            "AU",
            "BR",
            "SG",
            "US"
        ],
        "alias": "carbuyers",
        "parents": [
            "auto"
        ],
        "title": "Car Buyers"
    },
    {
        "alias": "cardioclasses",
        "parents": [
            "fitness"
        ],
        "title": "Cardio Classes"
    },
    {
        "alias": "cardiology",
        "parents": [
            "physicians"
        ],
        "title": "Cardiologists"
    },
    {
        "alias": "careercounseling",
        "parents": [
            "professional"
        ],
        "title": "Career Counseling"
    },
    {
        "alias": "caribbean",
        "country_blacklist": [
            "FI",
            "TR",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Caribbean"
    },
    {
        "country_whitelist": [
            "ES",
            "DK",
            "NO",
            "IT",
            "US",
            "PL",
            "BR",
            "SG",
            "SE"
        ],
        "alias": "caricatures",
        "parents": [
            "eventservices"
        ],
        "title": "Caricatures"
    },
    {
        "alias": "carousels",
        "parents": [
            "active"
        ],
        "title": "Carousels"
    },
    {
        "alias": "carpenters",
        "country_blacklist": [
            "TR"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Carpenters"
    },
    {
        "alias": "carpet_cleaning",
        "parents": [
            "localservices"
        ],
        "title": "Carpet Cleaning"
    },
    {
        "alias": "carpeting",
        "parents": [
            "homeservices"
        ],
        "title": "Carpeting"
    },
    {
        "alias": "carpetinstallation",
        "parents": [
            "homeservices"
        ],
        "title": "Carpet Installation"
    },
    {
        "alias": "carrental",
        "parents": [
            "hotelstravel"
        ],
        "title": "Car Rental"
    },
    {
        "alias": "carshares",
        "country_blacklist": [
            "BE",
            "NL",
            "PT",
            "HK",
            "JP",
            "TR",
            "CZ",
            "MY",
            "BR",
            "TW",
            "FI",
            "PH",
            "SG",
            "PL"
        ],
        "parents": [
            "auto"
        ],
        "title": "Car Share Services"
    },
    {
        "alias": "carwash",
        "parents": [
            "auto"
        ],
        "title": "Car Wash"
    },
    {
        "alias": "casinos",
        "country_blacklist": [
            "HK",
            "JP"
        ],
        "parents": [
            "arts"
        ],
        "title": "Casinos"
    },
    {
        "country_whitelist": [
            "ES",
            "BE",
            "FR",
            "CH",
            "PT",
            "NO",
            "DE",
            "JP",
            "IT",
            "CZ",
            "AT",
            "FI",
            "SE",
            "GB"
        ],
        "alias": "castles",
        "parents": [
            "arts"
        ],
        "title": "Castles"
    },
    {
        "country_whitelist": [
            "ES",
            "FR",
            "TR",
            "IT",
            "US"
        ],
        "alias": "catalan",
        "parents": [
            "restaurants"
        ],
        "title": "Catalan"
    },
    {
        "alias": "catering",
        "parents": [
            "eventservices"
        ],
        "title": "Caterers"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "NO",
            "TW",
            "JP",
            "IT",
            "US",
            "HK",
            "AU",
            "ES",
            "BR",
            "CZ",
            "SG",
            "SE"
        ],
        "alias": "cellphoneaccessories",
        "parents": [
            "shopping"
        ],
        "title": "Mobile Phone Accessories"
    },
    {
        "country_whitelist": [
            "BR"
        ],
        "alias": "centralbrazilian",
        "parents": [
            "brazilian"
        ],
        "title": "Central Brazilian"
    },
    {
        "country_whitelist": [
            "FR",
            "CH",
            "DK",
            "CZ",
            "CA",
            "DE",
            "US",
            "PL",
            "HK",
            "NZ",
            "AT",
            "NO",
            "SG",
            "SE"
        ],
        "alias": "challengecourses",
        "parents": [
            "active"
        ],
        "title": "Challenge Courses"
    },
    {
        "alias": "champagne_bars",
        "country_blacklist": [
            "AU"
        ],
        "parents": [
            "bars"
        ],
        "title": "Champagne Bars"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "cheekufta",
        "parents": [
            "turkish"
        ],
        "title": "Chee Kufta"
    },
    {
        "alias": "cheese",
        "parents": [
            "gourmet"
        ],
        "title": "Cheese Shops"
    },
    {
        "country_whitelist": [
            "NL",
            "GB",
            "AU",
            "CA",
            "IE",
            "US",
            "PL"
        ],
        "alias": "cheesesteaks",
        "parents": [
            "restaurants"
        ],
        "title": "Cheesesteaks"
    },
    {
        "alias": "cheesetastingclasses",
        "parents": [
            "tastingclasses"
        ],
        "title": "Cheese Tasting Classes"
    },
    {
        "country_whitelist": [
            "IE",
            "TW",
            "CA",
            "DE",
            "TR",
            "US",
            "PL",
            "HK",
            "AR",
            "AT",
            "BR",
            "SG",
            "MX",
            "SE",
            "GB"
        ],
        "alias": "chicken_wings",
        "parents": [
            "restaurants"
        ],
        "title": "Chicken Wings"
    },
    {
        "alias": "chickenshop",
        "country_blacklist": [
            "CZ",
            "MX",
            "CL"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Chicken Shop"
    },
    {
        "country_whitelist": [
            "ES",
            "FR",
            "DK",
            "NO",
            "IT",
            "US",
            "AU",
            "GB",
            "BR",
            "IE",
            "SE"
        ],
        "alias": "childbirthedu",
        "parents": [
            "specialtyschools"
        ],
        "title": "Childbirth Education"
    },
    {
        "alias": "childcare",
        "parents": [
            "localservices"
        ],
        "title": "Child Care & Day Care"
    },
    {
        "alias": "childcloth",
        "parents": [
            "fashion"
        ],
        "title": "Children's Clothing"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "childproofing",
        "parents": [
            "homeservices"
        ],
        "title": "Childproofing"
    },
    {
        "country_whitelist": [
            "FI",
            "FR",
            "BR",
            "CL"
        ],
        "alias": "chilean",
        "parents": [
            "restaurants"
        ],
        "title": "Chilean"
    },
    {
        "alias": "chimneysweeps",
        "country_blacklist": [
            "AR",
            "MX"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Chimney Sweeps"
    },
    {
        "alias": "chinese",
        "parents": [
            "restaurants"
        ],
        "title": "Chinese"
    },
    {
        "country_whitelist": [
            "ES",
            "PT"
        ],
        "alias": "chinesebazaar",
        "parents": [
            "shopping"
        ],
        "title": "Chinese Bazaar"
    },
    {
        "alias": "chiropractors",
        "parents": [
            "health"
        ],
        "title": "Chiropractors"
    },
    {
        "alias": "chocolate",
        "parents": [
            "gourmet"
        ],
        "title": "Chocolatiers & Shops"
    },
    {
        "alias": "choirs",
        "country_blacklist": [
            "BE",
            "NL",
            "CA",
            "US",
            "CZ",
            "NZ",
            "BR",
            "SG",
            "PL"
        ],
        "parents": [
            "arts"
        ],
        "title": "Choirs"
    },
    {
        "alias": "christmastrees",
        "parents": [
            "homeandgarden"
        ],
        "title": "Christmas Trees"
    },
    {
        "alias": "churches",
        "parents": [
            "religiousorgs"
        ],
        "title": "Churches"
    },
    {
        "country_whitelist": [
            "ES",
            "AR",
            "MX",
            "PT",
            "CL"
        ],
        "alias": "churros",
        "parents": [
            "food"
        ],
        "title": "Churros"
    },
    {
        "alias": "cideries",
        "country_blacklist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "NO",
            "JP",
            "TR",
            "IT"
        ],
        "parents": [
            "food"
        ],
        "title": "Cideries"
    },
    {
        "country_whitelist": [
            "FI",
            "FR",
            "MX",
            "PT"
        ],
        "alias": "circusschools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Circus Schools"
    },
    {
        "alias": "climbing",
        "parents": [
            "active"
        ],
        "title": "Climbing"
    },
    {
        "alias": "clockrepair",
        "country_blacklist": [
            "CL",
            "AR",
            "JP",
            "MX",
            "IT"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Clock Repair"
    },
    {
        "alias": "clothingrental",
        "parents": [
            "fashion"
        ],
        "title": "Clothing Rental"
    },
    {
        "alias": "clowns",
        "country_blacklist": [
            "NO",
            "TR",
            "CZ",
            "PL",
            "SE",
            "FI",
            "SG",
            "ES"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Clowns"
    },
    {
        "alias": "cocktailbars",
        "parents": [
            "bars"
        ],
        "title": "Cocktail Bars"
    },
    {
        "alias": "coffee",
        "parents": [
            "food"
        ],
        "title": "Coffee & Tea"
    },
    {
        "alias": "coffeeroasteries",
        "parents": [
            "food"
        ],
        "title": "Coffee Roasteries"
    },
    {
        "country_whitelist": [
            "NL",
            "PT"
        ],
        "alias": "coffeeshops",
        "parents": [
            "nightlife"
        ],
        "title": "Coffeeshops"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "NL",
            "DK",
            "NO",
            "IE",
            "DE",
            "TR",
            "PL",
            "AT",
            "SG",
            "SE",
            "GB"
        ],
        "alias": "coffeeteasupplies",
        "parents": [
            "food"
        ],
        "title": "Coffee & Tea Supplies"
    },
    {
        "country_whitelist": [
            "PT",
            "US"
        ],
        "alias": "collegecounseling",
        "parents": [
            "education"
        ],
        "title": "College Counseling"
    },
    {
        "alias": "collegeuniv",
        "parents": [
            "education"
        ],
        "title": "Colleges & Universities"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CL",
            "CA",
            "US",
            "AR",
            "FI",
            "MX",
            "ES"
        ],
        "alias": "colombian",
        "parents": [
            "latin"
        ],
        "title": "Colombian"
    },
    {
        "country_whitelist": [
            "AU",
            "US"
        ],
        "alias": "colonics",
        "parents": [
            "health"
        ],
        "title": "Colonics"
    },
    {
        "alias": "comedyclubs",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "nightlife"
        ],
        "title": "Comedy Clubs"
    },
    {
        "country_whitelist": [
            "AR",
            "DK",
            "FI",
            "CA",
            "JP",
            "MX",
            "US"
        ],
        "alias": "comfortfood",
        "parents": [
            "restaurants"
        ],
        "title": "Comfort Food"
    },
    {
        "alias": "comicbooks",
        "parents": [
            "media"
        ],
        "title": "Comic Books"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "PT",
            "CA",
            "DE",
            "US",
            "AU",
            "BR"
        ],
        "alias": "commercialrealestate",
        "parents": [
            "realestate"
        ],
        "title": "Commercial Real Estate"
    },
    {
        "alias": "commissionedartists",
        "country_blacklist": [
            "FR"
        ],
        "parents": [
            "professional"
        ],
        "title": "Commissioned Artists"
    },
    {
        "alias": "communitybookbox",
        "country_blacklist": [
            "FR",
            "CL",
            "JP",
            "IT",
            "AR",
            "PH",
            "MY",
            "MX",
            "ES"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Community Book Box"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "CA",
            "US",
            "CZ",
            "GB",
            "BR",
            "IE",
            "SE"
        ],
        "alias": "communitycenters",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Community Centers"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "NO",
            "DE",
            "US",
            "AU",
            "ES",
            "SG",
            "SE"
        ],
        "alias": "communitygardens",
        "parents": [
            "localservices"
        ],
        "title": "Community Gardens"
    },
    {
        "alias": "computers",
        "parents": [
            "shopping"
        ],
        "title": "Computers"
    },
    {
        "alias": "concept_shops",
        "country_blacklist": [
            "ES",
            "CL",
            "JP",
            "CA",
            "TR",
            "IT",
            "US",
            "HK",
            "NZ",
            "AR",
            "PL",
            "BR",
            "SG",
            "SE"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Concept Shops"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "conciergemedicine",
        "parents": [
            "health"
        ],
        "title": "Concierge Medicine"
    },
    {
        "country_whitelist": [
            "HK",
            "SG",
            "MY",
            "TW"
        ],
        "alias": "congee",
        "parents": [
            "chinese"
        ],
        "title": "Congee"
    },
    {
        "alias": "contractlaw",
        "country_blacklist": [
            "FR"
        ],
        "parents": [
            "lawyers"
        ],
        "title": "Contract Law"
    },
    {
        "alias": "contractors",
        "parents": [
            "homeservices"
        ],
        "title": "Contractors"
    },
    {
        "alias": "convenience",
        "country_blacklist": [
            "FI"
        ],
        "parents": [
            "food"
        ],
        "title": "Convenience Stores"
    },
    {
        "country_whitelist": [
            "HK",
            "SG",
            "JP",
            "TW"
        ],
        "alias": "conveyorsushi",
        "parents": [
            "japanese"
        ],
        "title": "Conveyor Belt Sushi"
    },
    {
        "alias": "cookingclasses",
        "parents": [
            "artsandcrafts"
        ],
        "title": "Cooking Classes"
    },
    {
        "alias": "cookingschools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Cooking Schools"
    },
    {
        "alias": "copyshops",
        "parents": [
            "localservices"
        ],
        "title": "Printing Services"
    },
    {
        "country_whitelist": [
            "BE",
            "FR"
        ],
        "alias": "corsican",
        "parents": [
            "restaurants"
        ],
        "title": "Corsican"
    },
    {
        "alias": "cosmeticdentists",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "dentists"
        ],
        "title": "Cosmetic Dentists"
    },
    {
        "alias": "cosmetics",
        "parents": [
            "shopping",
            "beautysvc"
        ],
        "title": "Cosmetics & Beauty Supply"
    },
    {
        "alias": "cosmeticsurgeons",
        "parents": [
            "physicians"
        ],
        "title": "Cosmetic Surgeons"
    },
    {
        "alias": "cosmetology_schools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Cosmetology Schools"
    },
    {
        "alias": "costumes",
        "parents": [
            "artsandcrafts"
        ],
        "title": "Costumes"
    },
    {
        "alias": "countertopinstall",
        "country_blacklist": [
            "CZ",
            "FR",
            "CH",
            "AT",
            "DE",
            "IT"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Countertop Installation"
    },
    {
        "country_whitelist": [
            "CL",
            "TW",
            "JP",
            "IT",
            "US",
            "HK",
            "AR",
            "BR",
            "SG",
            "MX",
            "ES"
        ],
        "alias": "countryclubs",
        "parents": [
            "arts"
        ],
        "title": "Country Clubs"
    },
    {
        "country_whitelist": [
            "SE",
            "US"
        ],
        "alias": "countrydancehalls",
        "parents": [
            "nightlife"
        ],
        "title": "Country Dance Halls"
    },
    {
        "alias": "couriers",
        "parents": [
            "localservices"
        ],
        "title": "Couriers & Delivery Services"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "NL",
            "PT",
            "NO",
            "DE",
            "IT",
            "US",
            "CZ",
            "AU",
            "AT"
        ],
        "alias": "courthouses",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Courthouses"
    },
    {
        "country_whitelist": [
            "AU",
            "SE",
            "US",
            "PT"
        ],
        "alias": "cprclasses",
        "parents": [
            "specialtyschools"
        ],
        "title": "CPR Classes"
    },
    {
        "country_whitelist": [
            "ES",
            "BE",
            "CH",
            "NL",
            "DE",
            "IT",
            "US",
            "PL",
            "BR",
            "SE",
            "AT"
        ],
        "alias": "craneservices",
        "parents": [
            "localservices"
        ],
        "title": "Crane Services"
    },
    {
        "alias": "creperies",
        "parents": [
            "restaurants"
        ],
        "title": "Creperies"
    },
    {
        "alias": "criminaldefense",
        "parents": [
            "lawyers"
        ],
        "title": "Criminal Defense Law"
    },
    {
        "country_whitelist": [
            "FR",
            "CH",
            "DE",
            "AT",
            "US"
        ],
        "alias": "csa",
        "parents": [
            "food"
        ],
        "title": "CSA"
    },
    {
        "alias": "cuban",
        "country_blacklist": [
            "SG",
            "TR",
            "DK"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Cuban"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "cucinacampana",
        "parents": [
            "italian"
        ],
        "title": "Cucina campana"
    },
    {
        "alias": "culturalcenter",
        "country_blacklist": [
            "CH",
            "NL",
            "CA",
            "DE",
            "TR",
            "NZ",
            "AT",
            "BR",
            "IE"
        ],
        "parents": [
            "arts"
        ],
        "title": "Cultural Center"
    },
    {
        "alias": "cupcakes",
        "country_blacklist": [
            "CZ",
            "CA",
            "TR",
            "ES"
        ],
        "parents": [
            "food"
        ],
        "title": "Cupcakes"
    },
    {
        "alias": "currencyexchange",
        "parents": [
            "financialservices"
        ],
        "title": "Currency Exchange"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT"
        ],
        "alias": "currysausage",
        "parents": [
            "restaurants"
        ],
        "title": "Curry Sausage"
    },
    {
        "alias": "custommerchandise",
        "parents": [
            "shopping"
        ],
        "title": "Customized Merchandise"
    },
    {
        "alias": "cyclingclasses",
        "country_blacklist": [
            "NZ",
            "AR",
            "BR",
            "PT",
            "CA",
            "IE",
            "MX"
        ],
        "parents": [
            "active"
        ],
        "title": "Cycling Classes"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT"
        ],
        "alias": "cypriot",
        "parents": [
            "restaurants"
        ],
        "title": "Cypriot"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "DK",
            "NO",
            "CA",
            "DE",
            "IT",
            "US",
            "PL",
            "CZ",
            "AU",
            "GB",
            "FI",
            "IE",
            "SE"
        ],
        "alias": "czech",
        "parents": [
            "restaurants"
        ],
        "title": "Czech"
    },
    {
        "country_whitelist": [
            "AR",
            "MX",
            "PT"
        ],
        "alias": "czechslovakian",
        "parents": [
            "restaurants"
        ],
        "title": "Czech/Slovakian"
    },
    {
        "country_whitelist": [
            "NZ",
            "AU",
            "PT",
            "SG",
            "TR",
            "US"
        ],
        "alias": "damagerestoration",
        "parents": [
            "homeservices"
        ],
        "title": "Damage Restoration"
    },
    {
        "alias": "dance_schools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Dance Schools"
    },
    {
        "alias": "danceclubs",
        "parents": [
            "nightlife"
        ],
        "title": "Dance Clubs"
    },
    {
        "country_whitelist": [
            "FI"
        ],
        "alias": "dancerestaurants",
        "parents": [
            "nightlife"
        ],
        "title": "Dance Restaurants"
    },
    {
        "alias": "dancestudio",
        "parents": [
            "fitness"
        ],
        "title": "Dance Studios"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "SE",
            "NO"
        ],
        "alias": "danish",
        "parents": [
            "restaurants"
        ],
        "title": "Danish"
    },
    {
        "country_whitelist": [
            "ES",
            "BE",
            "FR",
            "CH",
            "DK",
            "PT",
            "NO",
            "CA",
            "DE",
            "IT",
            "US",
            "CZ",
            "AU",
            "AT",
            "SE"
        ],
        "alias": "datarecovery",
        "parents": [
            "itservices"
        ],
        "title": "Data Recovery"
    },
    {
        "alias": "daycamps",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "active"
        ],
        "title": "Day Camps"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "debtrelief",
        "parents": [
            "financialservices"
        ],
        "title": "Debt Relief Services"
    },
    {
        "alias": "decksrailing",
        "parents": [
            "homeservices"
        ],
        "title": "Decks & Railing"
    },
    {
        "alias": "delicatessen",
        "country_blacklist": [
            "IT",
            "US"
        ],
        "parents": [
            "food"
        ],
        "title": "Delicatessen"
    },
    {
        "alias": "delis",
        "country_blacklist": [
            "CH",
            "AT",
            "PT",
            "CL",
            "DE",
            "IT",
            "SE"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Delis"
    },
    {
        "country_whitelist": [
            "ES",
            "AU",
            "IT",
            "US"
        ],
        "alias": "demolitionservices",
        "parents": [
            "homeservices"
        ],
        "title": "Demolition Services"
    },
    {
        "country_whitelist": [
            "CA"
        ],
        "alias": "dentalhygeiniststorefront",
        "parents": [
            "dentalhygienists"
        ],
        "title": "Storefront Clinics"
    },
    {
        "country_whitelist": [
            "NL",
            "DK",
            "PT",
            "NO",
            "CA",
            "DE",
            "US"
        ],
        "alias": "dentalhygienists",
        "parents": [
            "health"
        ],
        "title": "Dental Hygienists"
    },
    {
        "country_whitelist": [
            "CA"
        ],
        "alias": "dentalhygienistsmobile",
        "parents": [
            "dentalhygienists"
        ],
        "title": "Mobile Clinics"
    },
    {
        "alias": "dentists",
        "parents": [
            "health"
        ],
        "title": "Dentists"
    },
    {
        "alias": "departmentsofmotorvehicles",
        "country_blacklist": [
            "BE",
            "FR"
        ],
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Departments of Motor Vehicles"
    },
    {
        "alias": "deptstores",
        "parents": [
            "fashion",
            "shopping"
        ],
        "title": "Department Stores"
    },
    {
        "alias": "dermatology",
        "parents": [
            "physicians"
        ],
        "title": "Dermatologists"
    },
    {
        "alias": "desserts",
        "parents": [
            "food"
        ],
        "title": "Desserts"
    },
    {
        "country_whitelist": [
            "FR",
            "PT",
            "CA",
            "US",
            "AU",
            "GB",
            "BR",
            "IE",
            "MX"
        ],
        "alias": "diagnosticimaging",
        "parents": [
            "diagnosticservices"
        ],
        "title": "Diagnostic Imaging"
    },
    {
        "alias": "diagnosticservices",
        "parents": [
            "health"
        ],
        "title": "Diagnostic Services"
    },
    {
        "country_whitelist": [
            "AR",
            "ES",
            "CL",
            "TR",
            "IT",
            "US",
            "MX"
        ],
        "alias": "dialysisclinics",
        "parents": [
            "health"
        ],
        "title": "Dialysis Clinics"
    },
    {
        "alias": "dietitians",
        "parents": [
            "health"
        ],
        "title": "Dietitians"
    },
    {
        "alias": "dimsum",
        "country_blacklist": [
            "TR",
            "BR",
            "PT"
        ],
        "parents": [
            "chinese"
        ],
        "title": "Dim Sum"
    },
    {
        "alias": "diners",
        "country_blacklist": [
            "CZ",
            "AU",
            "SE",
            "FI"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Diners"
    },
    {
        "alias": "dinnertheater",
        "country_blacklist": [
            "BE",
            "FR",
            "JP",
            "IT",
            "NL"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Dinner Theater"
    },
    {
        "alias": "discgolf",
        "country_blacklist": [
            "CZ",
            "AU",
            "SG",
            "DK"
        ],
        "parents": [
            "active"
        ],
        "title": "Disc Golf"
    },
    {
        "alias": "discountstore",
        "parents": [
            "shopping"
        ],
        "title": "Discount Store"
    },
    {
        "alias": "distilleries",
        "parents": [
            "food"
        ],
        "title": "Distilleries"
    },
    {
        "alias": "divebars",
        "country_blacklist": [
            "CZ",
            "FR",
            "AU"
        ],
        "parents": [
            "bars"
        ],
        "title": "Dive Bars"
    },
    {
        "country_whitelist": [
            "CH",
            "CL",
            "DE",
            "JP",
            "IT",
            "US",
            "NZ",
            "AR",
            "AU",
            "AT",
            "BR",
            "MX",
            "ES"
        ],
        "alias": "diveshops",
        "parents": [
            "sportgoods"
        ],
        "title": "Dive Shops"
    },
    {
        "alias": "diving",
        "parents": [
            "active"
        ],
        "title": "Diving"
    },
    {
        "alias": "divorce",
        "parents": [
            "lawyers"
        ],
        "title": "Divorce & Family Law"
    },
    {
        "alias": "diyfood",
        "country_blacklist": [
            "ES",
            "FR",
            "CH",
            "CL",
            "NO",
            "DE",
            "IT",
            "CZ",
            "NZ",
            "AT",
            "FI",
            "SE"
        ],
        "parents": [
            "food"
        ],
        "title": "Do-It-Yourself Food"
    },
    {
        "alias": "djs",
        "parents": [
            "eventservices"
        ],
        "title": "DJs"
    },
    {
        "alias": "dog_parks",
        "parents": [
            "parks"
        ],
        "title": "Dog Parks"
    },
    {
        "alias": "dogwalkers",
        "parents": [
            "petservices"
        ],
        "title": "Dog Walkers"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "dolmusstation",
        "parents": [
            "transport"
        ],
        "title": "Dolmus Station"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "dominican",
        "parents": [
            "caribbean"
        ],
        "title": "Dominican"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "DK",
            "CZ",
            "CA",
            "TR",
            "PL"
        ],
        "alias": "donairs",
        "parents": [
            "food"
        ],
        "title": "Donairs"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "donburi",
        "parents": [
            "japanese"
        ],
        "title": "Donburi"
    },
    {
        "alias": "donuts",
        "country_blacklist": [
            "ES"
        ],
        "parents": [
            "food"
        ],
        "title": "Donuts"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "PT",
            "IT",
            "US",
            "CZ",
            "NZ",
            "BR",
            "PL"
        ],
        "alias": "doorsales",
        "parents": [
            "homeservices"
        ],
        "title": "Door Sales/Installation"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "IT",
            "PT",
            "US"
        ],
        "alias": "doulas",
        "parents": [
            "health"
        ],
        "title": "Doulas"
    },
    {
        "alias": "dramaschools",
        "country_blacklist": [
            "CA",
            "CZ",
            "AU",
            "GB",
            "FI",
            "IE",
            "NL",
            "PT",
            "HK",
            "TW",
            "TR",
            "US",
            "NZ",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "specialtyschools"
        ],
        "title": "Drama Schools"
    },
    {
        "alias": "driveintheater",
        "country_blacklist": [
            "FR",
            "AR",
            "MX",
            "CL"
        ],
        "parents": [
            "movietheaters"
        ],
        "title": "Drive-In Theater"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "drivethrubars",
        "parents": [
            "bars"
        ],
        "title": "Drive-Thru Bars"
    },
    {
        "alias": "driving_schools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Driving Schools"
    },
    {
        "alias": "drugstores",
        "country_blacklist": [
            "FR",
            "AR",
            "NO",
            "CL",
            "TR",
            "MX",
            "SE"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Drugstores"
    },
    {
        "alias": "drycleaninglaundry",
        "parents": [
            "localservices"
        ],
        "title": "Dry Cleaning & Laundry"
    },
    {
        "alias": "drywall",
        "country_blacklist": [
            "HK",
            "JP"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Drywall Installation & Repair"
    },
    {
        "country_whitelist": [
            "CA",
            "DE",
            "US"
        ],
        "alias": "duilawyers",
        "parents": [
            "lawyers"
        ],
        "title": "DUI Law"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "dumplings",
        "parents": [
            "restaurants"
        ],
        "title": "Dumplings"
    },
    {
        "alias": "dutyfreeshops",
        "parents": [
            "shopping"
        ],
        "title": "Duty-Free Shops"
    },
    {
        "alias": "earnosethroat",
        "parents": [
            "physicians"
        ],
        "title": "Ear Nose & Throat"
    },
    {
        "country_whitelist": [
            "FR",
            "AU"
        ],
        "alias": "eastern_european",
        "parents": [
            "restaurants"
        ],
        "title": "Eastern European"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "easterngerman",
        "parents": [
            "german"
        ],
        "title": "Eastern German"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "easternmexican",
        "parents": [
            "mexican"
        ],
        "title": "Eastern Mexican"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "PT",
            "CL",
            "DE",
            "IT",
            "US",
            "NO",
            "AR",
            "BR",
            "MX",
            "ES"
        ],
        "alias": "editorialservices",
        "parents": [
            "professional"
        ],
        "title": "Editorial Services"
    },
    {
        "alias": "education",
        "parents": [],
        "title": "Education"
    },
    {
        "alias": "educationservices",
        "country_blacklist": [
            "BR"
        ],
        "parents": [
            "education"
        ],
        "title": "Educational Services"
    },
    {
        "country_whitelist": [
            "BE",
            "CA",
            "FR",
            "US",
            "IT"
        ],
        "alias": "egyptian",
        "parents": [
            "mideastern"
        ],
        "title": "Egyptian"
    },
    {
        "alias": "eldercareplanning",
        "parents": [
            "localservices"
        ],
        "title": "Elder Care Planning"
    },
    {
        "alias": "electricians",
        "parents": [
            "homeservices"
        ],
        "title": "Electricians"
    },
    {
        "alias": "electronics",
        "parents": [
            "shopping"
        ],
        "title": "Electronics"
    },
    {
        "alias": "electronicsrepair",
        "parents": [
            "localservices"
        ],
        "title": "Electronics Repair"
    },
    {
        "alias": "elementaryschools",
        "parents": [
            "education"
        ],
        "title": "Elementary Schools"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT"
        ],
        "alias": "eltern_cafes",
        "parents": [
            "food",
            "restaurants"
        ],
        "title": "Parent Cafes"
    },
    {
        "alias": "embassy",
        "country_blacklist": [
            "TR"
        ],
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Embassy"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "CL",
            "NO",
            "IT",
            "US",
            "CZ",
            "AR",
            "ES",
            "BR",
            "MX",
            "SE"
        ],
        "alias": "embroideryandcrochet",
        "parents": [
            "artsandcrafts"
        ],
        "title": "Embroidery & Crochet"
    },
    {
        "alias": "emergencymedicine",
        "parents": [
            "physicians"
        ],
        "title": "Emergency Medicine"
    },
    {
        "country_whitelist": [
            "SE",
            "US"
        ],
        "alias": "emergencyrooms",
        "parents": [
            "health"
        ],
        "title": "Emergency Rooms"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "emilian",
        "parents": [
            "italian"
        ],
        "title": "Emilian"
    },
    {
        "country_whitelist": [
            "AR",
            "ES",
            "US",
            "CL"
        ],
        "alias": "empanadas",
        "parents": [
            "food"
        ],
        "title": "Empanadas"
    },
    {
        "alias": "employmentagencies",
        "parents": [
            "professional"
        ],
        "title": "Employment Agencies"
    },
    {
        "alias": "employmentlawyers",
        "parents": [
            "lawyers"
        ],
        "title": "Employment Law"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT",
            "ES",
            "SE"
        ],
        "alias": "emstraining",
        "parents": [
            "fitness"
        ],
        "title": "EMS Training"
    },
    {
        "alias": "endocrinologists",
        "country_blacklist": [
            "PT",
            "IE",
            "TW",
            "CA",
            "JP",
            "PL",
            "HK",
            "NZ",
            "AU",
            "GB",
            "FI",
            "SG",
            "SE"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Endocrinologists"
    },
    {
        "alias": "endodontists",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "dentists"
        ],
        "title": "Endodontists"
    },
    {
        "alias": "engraving",
        "parents": [
            "localservices"
        ],
        "title": "Engraving"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "entertainmentlaw",
        "parents": [
            "lawyers"
        ],
        "title": "Entertainment Law"
    },
    {
        "alias": "eroticmassage",
        "country_blacklist": [
            "DK",
            "CL",
            "JP",
            "NO",
            "TR",
            "US",
            "HK",
            "TW",
            "FI",
            "PH",
            "MY",
            "SE"
        ],
        "parents": [
            "beautysvc"
        ],
        "title": "Erotic Massage"
    },
    {
        "alias": "escapegames",
        "parents": [
            "active"
        ],
        "title": "Escape Games"
    },
    {
        "alias": "estateliquidation",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "realestate"
        ],
        "title": "Estate Liquidation"
    },
    {
        "alias": "estatephotography",
        "country_blacklist": [
            "FR",
            "JP",
            "IT"
        ],
        "parents": [
            "realestatesvcs"
        ],
        "title": "Real Estate Photography"
    },
    {
        "alias": "estateplanning",
        "country_blacklist": [
            "SE",
            "NO"
        ],
        "parents": [
            "lawyers"
        ],
        "title": "Estate Planning Law"
    },
    {
        "alias": "ethicgrocery",
        "country_blacklist": [
            "BE",
            "FR",
            "CH",
            "NL",
            "JP",
            "DE",
            "TR",
            "US",
            "CZ",
            "AT",
            "PH",
            "MY"
        ],
        "parents": [
            "food"
        ],
        "title": "Ethic Grocery"
    },
    {
        "alias": "ethiopian",
        "country_blacklist": [
            "CZ",
            "DK",
            "PT",
            "SG",
            "TR",
            "MX",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Ethiopian"
    },
    {
        "alias": "ethnicgrocery",
        "parents": [
            "food"
        ],
        "title": "Ethnic Grocery"
    },
    {
        "alias": "ethnicmarkets",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "gourmet"
        ],
        "title": "Ethnic Food"
    },
    {
        "alias": "eventphotography",
        "parents": [
            "photographers"
        ],
        "title": "Event Photography"
    },
    {
        "alias": "eventplanning",
        "parents": [
            "eventservices"
        ],
        "title": "Party & Event Planning"
    },
    {
        "alias": "eventservices",
        "parents": [],
        "title": "Event Planning & Services"
    },
    {
        "country_whitelist": [
            "DE",
            "PT",
            "SE",
            "NO"
        ],
        "alias": "experiences",
        "parents": [
            "active"
        ],
        "title": "Experiences"
    },
    {
        "alias": "eyelashservice",
        "country_blacklist": [
            "IT"
        ],
        "parents": [
            "beautysvc"
        ],
        "title": "Eyelash Service"
    },
    {
        "alias": "fabricstores",
        "parents": [
            "artsandcrafts"
        ],
        "title": "Fabric Stores"
    },
    {
        "country_whitelist": [
            "CZ",
            "NZ",
            "AU",
            "BR",
            "US"
        ],
        "alias": "facepainting",
        "parents": [
            "eventservices"
        ],
        "title": "Face Painting"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "fado_houses",
        "parents": [
            "portuguese"
        ],
        "title": "Fado Houses"
    },
    {
        "alias": "falafel",
        "country_blacklist": [
            "AR",
            "MX",
            "PT"
        ],
        "parents": [
            "mediterranean"
        ],
        "title": "Falafel"
    },
    {
        "alias": "familydr",
        "country_blacklist": [
            "BR"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Family Practice"
    },
    {
        "alias": "farmequipmentrepair",
        "parents": [
            "localservices"
        ],
        "title": "Farm Equipment Repair"
    },
    {
        "alias": "farmersmarket",
        "parents": [
            "food"
        ],
        "title": "Farmers Market"
    },
    {
        "alias": "farmingequipment",
        "parents": [
            "shopping"
        ],
        "title": "Farming Equipment"
    },
    {
        "alias": "farms",
        "parents": [
            "arts"
        ],
        "title": "Farms"
    },
    {
        "alias": "fashion",
        "parents": [
            "shopping"
        ],
        "title": "Fashion"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "fasil",
        "parents": [
            "nightlife"
        ],
        "title": "Fasil Music"
    },
    {
        "alias": "fencesgates",
        "parents": [
            "homeservices"
        ],
        "title": "Fences & Gates"
    },
    {
        "alias": "fencing",
        "parents": [
            "active"
        ],
        "title": "Fencing Clubs"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "JP",
            "DE",
            "TR",
            "IT",
            "HK",
            "NZ",
            "ES",
            "FI",
            "SG",
            "SE"
        ],
        "alias": "ferries",
        "parents": [
            "transport"
        ],
        "title": "Ferries"
    },
    {
        "alias": "fertility",
        "parents": [
            "physicians"
        ],
        "title": "Fertility"
    },
    {
        "alias": "festivals",
        "parents": [
            "arts"
        ],
        "title": "Festivals"
    },
    {
        "alias": "filipino",
        "country_blacklist": [
            "CZ",
            "TR",
            "DK",
            "FI"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Filipino"
    },
    {
        "alias": "financialadvising",
        "parents": [
            "financialservices"
        ],
        "title": "Financial Advising"
    },
    {
        "alias": "financialservices",
        "parents": [],
        "title": "Financial Services"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "firearmtraining",
        "parents": [
            "specialtyschools"
        ],
        "title": "Firearm Training"
    },
    {
        "alias": "firedepartments",
        "country_blacklist": [
            "NZ",
            "GB",
            "BR",
            "SG",
            "CA",
            "IE"
        ],
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Fire Departments"
    },
    {
        "alias": "fireplace",
        "parents": [
            "homeservices"
        ],
        "title": "Fireplace Services"
    },
    {
        "alias": "fireprotection",
        "parents": [
            "homeservices"
        ],
        "title": "Fire Protection Services"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "SE",
            "NO",
            "FI",
            "US"
        ],
        "alias": "firewood",
        "parents": [
            "homeservices"
        ],
        "title": "Firewood"
    },
    {
        "country_whitelist": [
            "CZ",
            "PT",
            "US"
        ],
        "alias": "fireworks",
        "parents": [
            "shopping"
        ],
        "title": "Fireworks"
    },
    {
        "alias": "firstaidclasses",
        "country_blacklist": [
            "BE",
            "FR",
            "NL",
            "BR",
            "IE",
            "SG",
            "NZ"
        ],
        "parents": [
            "specialtyschools"
        ],
        "title": "First Aid Classes"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "fischbroetchen",
        "parents": [
            "restaurants"
        ],
        "title": "Fischbroetchen"
    },
    {
        "alias": "fishing",
        "parents": [
            "active"
        ],
        "title": "Fishing"
    },
    {
        "country_whitelist": [
            "AU",
            "DK",
            "PT",
            "NO",
            "FI",
            "DE",
            "SE"
        ],
        "alias": "fishmonger",
        "parents": [
            "food"
        ],
        "title": "Fishmonger"
    },
    {
        "alias": "fishnchips",
        "country_blacklist": [
            "BR",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Fish & Chips"
    },
    {
        "alias": "fitness",
        "parents": [
            "active"
        ],
        "title": "Fitness & Instruction"
    },
    {
        "alias": "fitnessequipment",
        "parents": [
            "shopping"
        ],
        "title": "Fitness/Exercise Equipment"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT",
            "PL",
            "DK"
        ],
        "alias": "flatbread",
        "parents": [
            "restaurants"
        ],
        "title": "Flatbread"
    },
    {
        "alias": "fleamarkets",
        "parents": [
            "shopping"
        ],
        "title": "Flea Markets"
    },
    {
        "country_whitelist": [
            "FR"
        ],
        "alias": "flemish",
        "parents": [
            "belgian"
        ],
        "title": "Flemish"
    },
    {
        "alias": "flightinstruction",
        "parents": [
            "specialtyschools"
        ],
        "title": "Flight Instruction"
    },
    {
        "alias": "floatspa",
        "country_blacklist": [
            "FR",
            "JP",
            "IT"
        ],
        "parents": [
            "health"
        ],
        "title": "Float Spa"
    },
    {
        "alias": "flooring",
        "parents": [
            "homeservices"
        ],
        "title": "Flooring"
    },
    {
        "alias": "florists",
        "parents": [
            "flowers"
        ],
        "title": "Florists"
    },
    {
        "alias": "flowers",
        "parents": [
            "shopping"
        ],
        "title": "Flowers & Gifts"
    },
    {
        "alias": "flyboarding",
        "parents": [
            "active"
        ],
        "title": "Flyboarding"
    },
    {
        "alias": "fondue",
        "country_blacklist": [
            "CZ",
            "DK",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Fondue"
    },
    {
        "alias": "food",
        "parents": [],
        "title": "Food"
    },
    {
        "country_whitelist": [
            "DK",
            "NO",
            "IE",
            "SG",
            "CA",
            "JP",
            "US",
            "CZ",
            "NZ",
            "AU",
            "GB",
            "HK",
            "PH",
            "MY",
            "SE"
        ],
        "alias": "food_court",
        "parents": [
            "restaurants"
        ],
        "title": "Food Court"
    },
    {
        "alias": "foodbanks",
        "parents": [
            "nonprofit"
        ],
        "title": "Food Banks"
    },
    {
        "alias": "fooddeliveryservices",
        "parents": [
            "food"
        ],
        "title": "Food Delivery Services"
    },
    {
        "country_whitelist": [
            "SG",
            "PT",
            "US"
        ],
        "alias": "foodsafety",
        "parents": [
            "specialtyschools"
        ],
        "title": "Food Safety Training"
    },
    {
        "alias": "foodstands",
        "parents": [
            "restaurants"
        ],
        "title": "Food Stands"
    },
    {
        "alias": "foodtours",
        "parents": [
            "tours"
        ],
        "title": "Food Tours"
    },
    {
        "alias": "foodtrucks",
        "country_blacklist": [
            "SG"
        ],
        "parents": [
            "food"
        ],
        "title": "Food Trucks"
    },
    {
        "alias": "football",
        "parents": [
            "active"
        ],
        "title": "Soccer"
    },
    {
        "alias": "formalwear",
        "country_blacklist": [
            "CH",
            "IE",
            "JP",
            "TR",
            "IT",
            "PL",
            "HK",
            "GB",
            "TW",
            "FI",
            "PH",
            "MY",
            "SE"
        ],
        "parents": [
            "fashion"
        ],
        "title": "Formal Wear"
    },
    {
        "alias": "framing",
        "parents": [
            "artsandcrafts"
        ],
        "title": "Framing"
    },
    {
        "alias": "freediving",
        "parents": [
            "diving"
        ],
        "title": "Free Diving"
    },
    {
        "country_whitelist": [
            "AR",
            "MX",
            "ES",
            "CL"
        ],
        "alias": "freiduria",
        "parents": [
            "restaurants"
        ],
        "title": "Freiduria"
    },
    {
        "alias": "french",
        "parents": [
            "restaurants"
        ],
        "title": "French"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "AU",
            "IT",
            "PL"
        ],
        "alias": "friterie",
        "parents": [
            "food"
        ],
        "title": "Friterie"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "friulan",
        "parents": [
            "italian"
        ],
        "title": "Friulan"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "GB",
            "SG",
            "IT",
            "ES"
        ],
        "alias": "frozenfood",
        "parents": [
            "gourmet"
        ],
        "title": "Frozen Food"
    },
    {
        "country_whitelist": [
            "ES",
            "DK",
            "SE",
            "NO",
            "MX",
            "US"
        ],
        "alias": "fueldocks",
        "parents": [
            "auto"
        ],
        "title": "Fuel Docks"
    },
    {
        "alias": "funeralservices",
        "parents": [
            "localservices"
        ],
        "title": "Funeral Services & Cemeteries"
    },
    {
        "country_whitelist": [
            "CZ",
            "CH",
            "DE",
            "AT",
            "PT"
        ],
        "alias": "funfair",
        "parents": [
            "festivals"
        ],
        "title": "Fun Fair"
    },
    {
        "alias": "furclothing",
        "parents": [
            "fashion"
        ],
        "title": "Fur Clothing"
    },
    {
        "alias": "furniture",
        "parents": [
            "homeandgarden"
        ],
        "title": "Furniture Stores"
    },
    {
        "alias": "furnitureassembly",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Furniture Assembly"
    },
    {
        "alias": "furniturerepair",
        "parents": [
            "localservices"
        ],
        "title": "Furniture Repair"
    },
    {
        "country_whitelist": [
            "HK",
            "SG",
            "MY",
            "TW"
        ],
        "alias": "fuzhou",
        "parents": [
            "chinese"
        ],
        "title": "Fuzhou"
    },
    {
        "country_whitelist": [
            "ES",
            "PT"
        ],
        "alias": "galician",
        "parents": [
            "restaurants"
        ],
        "title": "Galician"
    },
    {
        "alias": "galleries",
        "parents": [
            "arts",
            "shopping"
        ],
        "title": "Art Galleries"
    },
    {
        "country_whitelist": [
            "CA",
            "AR",
            "MX",
            "US",
            "CL"
        ],
        "alias": "gametruckrental",
        "parents": [
            "eventservices"
        ],
        "title": "Game Truck Rental"
    },
    {
        "alias": "garage_door_services",
        "country_blacklist": [
            "CH",
            "PT",
            "CL",
            "JP",
            "DE",
            "TR",
            "MY",
            "PL",
            "HK",
            "AR",
            "AT",
            "TW",
            "PH",
            "SG",
            "SE"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Garage Door Services"
    },
    {
        "alias": "gardeners",
        "parents": [
            "homeservices"
        ],
        "title": "Gardeners"
    },
    {
        "alias": "gardening",
        "parents": [
            "homeandgarden"
        ],
        "title": "Nurseries & Gardening"
    },
    {
        "alias": "gardens",
        "parents": [
            "arts"
        ],
        "title": "Botanical Gardens"
    },
    {
        "alias": "gastroenterologist",
        "parents": [
            "physicians"
        ],
        "title": "Gastroenterologist"
    },
    {
        "alias": "gastropubs",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Gastropubs"
    },
    {
        "alias": "gaybars",
        "parents": [
            "bars"
        ],
        "title": "Gay Bars"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "IT",
            "US",
            "AU",
            "PH",
            "SG",
            "SE"
        ],
        "alias": "gelato",
        "parents": [
            "food"
        ],
        "title": "Gelato"
    },
    {
        "alias": "general_litigation",
        "parents": [
            "lawyers"
        ],
        "title": "General Litigation"
    },
    {
        "alias": "generaldentistry",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "dentists"
        ],
        "title": "General Dentistry"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT",
            "PT"
        ],
        "alias": "generalfestivals",
        "parents": [
            "festivals"
        ],
        "title": "General Festivals"
    },
    {
        "alias": "geneticists",
        "parents": [
            "physicians"
        ],
        "title": "Geneticists"
    },
    {
        "country_whitelist": [
            "CZ",
            "GB",
            "PL"
        ],
        "alias": "georgian",
        "parents": [
            "restaurants"
        ],
        "title": "Georgian"
    },
    {
        "alias": "german",
        "parents": [
            "restaurants"
        ],
        "title": "German"
    },
    {
        "alias": "gerontologist",
        "parents": [
            "physicians"
        ],
        "title": "Gerontologists"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "giblets",
        "parents": [
            "restaurants"
        ],
        "title": "Giblets"
    },
    {
        "alias": "giftshops",
        "country_blacklist": [
            "SG",
            "TR",
            "PL"
        ],
        "parents": [
            "flowers"
        ],
        "title": "Gift Shops"
    },
    {
        "alias": "glassandmirrors",
        "country_blacklist": [
            "TR",
            "AU",
            "IE",
            "GB"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Glass & Mirrors"
    },
    {
        "country_whitelist": [
            "CH",
            "AT",
            "PT",
            "NO",
            "DE",
            "SE"
        ],
        "alias": "gliding",
        "parents": [
            "active"
        ],
        "title": "Gliding"
    },
    {
        "country_whitelist": [
            "CZ",
            "CH",
            "DE",
            "AT",
            "SE"
        ],
        "alias": "gluhwein",
        "parents": [
            "food"
        ],
        "title": "Mulled Wine"
    },
    {
        "alias": "gluten_free",
        "parents": [
            "restaurants"
        ],
        "title": "Gluten-Free"
    },
    {
        "alias": "gokarts",
        "parents": [
            "active"
        ],
        "title": "Go Karts"
    },
    {
        "country_whitelist": [
            "ES",
            "BE",
            "FR",
            "CH",
            "NL",
            "PT",
            "CA",
            "DE",
            "IT",
            "US",
            "AT",
            "BR",
            "SE"
        ],
        "alias": "goldbuyers",
        "parents": [
            "shopping"
        ],
        "title": "Gold Buyers"
    },
    {
        "alias": "golf",
        "parents": [
            "active"
        ],
        "title": "Golf"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "golfcartrentals",
        "parents": [
            "eventservices"
        ],
        "title": "Golf Cart Rentals"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "AU",
            "CA",
            "DE",
            "US"
        ],
        "alias": "golfequipment",
        "parents": [
            "sportgoods"
        ],
        "title": "Golf Equipment"
    },
    {
        "country_whitelist": [
            "ES",
            "BE",
            "FR",
            "NL",
            "DK",
            "NO",
            "JP",
            "IT",
            "US",
            "NZ",
            "AU",
            "GB",
            "SE"
        ],
        "alias": "golflessons",
        "parents": [
            "fitness"
        ],
        "title": "Golf Lessons"
    },
    {
        "alias": "golfshops",
        "country_blacklist": [
            "IE",
            "CA",
            "SG",
            "NZ",
            "BR"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Golf Equipment Shops"
    },
    {
        "alias": "gourmet",
        "parents": [
            "food"
        ],
        "title": "Specialty Food"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "gozleme",
        "parents": [
            "turkish"
        ],
        "title": "Gozleme"
    },
    {
        "alias": "graphicdesign",
        "parents": [
            "professional"
        ],
        "title": "Graphic Design"
    },
    {
        "alias": "greek",
        "parents": [
            "restaurants"
        ],
        "title": "Greek"
    },
    {
        "alias": "grocery",
        "parents": [
            "food"
        ],
        "title": "Grocery"
    },
    {
        "alias": "groomer",
        "parents": [
            "petservices"
        ],
        "title": "Pet Groomers"
    },
    {
        "alias": "guesthouses",
        "country_blacklist": [
            "SG",
            "DK"
        ],
        "parents": [
            "hotelstravel"
        ],
        "title": "Guest Houses"
    },
    {
        "alias": "guitarstores",
        "parents": [
            "musicinstrumentservices"
        ],
        "title": "Guitar Stores"
    },
    {
        "alias": "gun_ranges",
        "country_blacklist": [
            "BE",
            "FR",
            "CH",
            "AT",
            "BR",
            "SG"
        ],
        "parents": [
            "active"
        ],
        "title": "Gun/Rifle Ranges"
    },
    {
        "country_whitelist": [
            "CH",
            "PT",
            "CL",
            "CA",
            "DE",
            "US",
            "AR",
            "AT",
            "PH",
            "MY",
            "MX",
            "PL"
        ],
        "alias": "guns_and_ammo",
        "parents": [
            "shopping"
        ],
        "title": "Guns & Ammo"
    },
    {
        "alias": "gutterservices",
        "country_blacklist": [
            "AR",
            "MX",
            "PT"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Gutter Services"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "CA",
            "US",
            "CZ",
            "NZ",
            "BR",
            "MX"
        ],
        "alias": "gymnastics",
        "parents": [
            "active"
        ],
        "title": "Gymnastics"
    },
    {
        "alias": "gyms",
        "parents": [
            "fitness"
        ],
        "title": "Gyms"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "gyudon",
        "parents": [
            "donburi"
        ],
        "title": "Gyudon"
    },
    {
        "alias": "habilitativeservices",
        "parents": [
            "health"
        ],
        "title": "Habilitative Services"
    },
    {
        "country_whitelist": [
            "HK",
            "PH",
            "SG",
            "MY",
            "US"
        ],
        "alias": "hainan",
        "parents": [
            "chinese"
        ],
        "title": "Hainan"
    },
    {
        "alias": "hair",
        "parents": [
            "beautysvc"
        ],
        "title": "Hair Salons"
    },
    {
        "alias": "hair_extensions",
        "country_blacklist": [
            "BE",
            "NL",
            "CL",
            "TR",
            "IT",
            "HK",
            "AR",
            "PL"
        ],
        "parents": [
            "hair",
            "beautysvc"
        ],
        "title": "Hair Extensions"
    },
    {
        "alias": "hairloss",
        "parents": [
            "beautysvc"
        ],
        "title": "Hair Loss Centers"
    },
    {
        "alias": "hairremoval",
        "parents": [
            "beautysvc"
        ],
        "title": "Hair Removal"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "US",
            "CZ",
            "AU",
            "SG",
            "SE"
        ],
        "alias": "hairstylists",
        "parents": [
            "hair"
        ],
        "title": "Hair Stylists"
    },
    {
        "country_whitelist": [
            "CA",
            "US"
        ],
        "alias": "haitian",
        "parents": [
            "caribbean"
        ],
        "title": "Haitian"
    },
    {
        "country_whitelist": [
            "HK",
            "TW",
            "CA",
            "SG",
            "MY",
            "PH"
        ],
        "alias": "hakka",
        "parents": [
            "chinese"
        ],
        "title": "Hakka"
    },
    {
        "alias": "halal",
        "country_blacklist": [
            "TR",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Halal"
    },
    {
        "alias": "halotherapy",
        "country_blacklist": [
            "FR"
        ],
        "parents": [
            "health"
        ],
        "title": "Halotherapy"
    },
    {
        "alias": "handball",
        "country_blacklist": [
            "CA",
            "DE",
            "HK",
            "AU",
            "GB",
            "SG",
            "IE",
            "PT",
            "CZ",
            "TW",
            "TR",
            "US",
            "NZ",
            "PH",
            "MY",
            "MX"
        ],
        "parents": [
            "active"
        ],
        "title": "Handball"
    },
    {
        "country_whitelist": [
            "TW",
            "BR"
        ],
        "alias": "handrolls",
        "parents": [
            "japanese"
        ],
        "title": "Hand Rolls"
    },
    {
        "alias": "handyman",
        "parents": [
            "homeservices"
        ],
        "title": "Handyman"
    },
    {
        "alias": "hanggliding",
        "country_blacklist": [
            "NL",
            "DK",
            "CZ",
            "IE",
            "TW",
            "CA",
            "DE",
            "TR",
            "HK",
            "GB",
            "FI",
            "PH",
            "MY",
            "PL",
            "SG"
        ],
        "parents": [
            "active"
        ],
        "title": "Hang Gliding"
    },
    {
        "alias": "hardware",
        "parents": [
            "homeandgarden"
        ],
        "title": "Hardware Stores"
    },
    {
        "alias": "hats",
        "country_blacklist": [
            "CH",
            "NL",
            "CL",
            "JP",
            "TR",
            "PL",
            "HK",
            "AR",
            "AT",
            "IE",
            "SE",
            "GB"
        ],
        "parents": [
            "fashion"
        ],
        "title": "Hats"
    },
    {
        "alias": "hauntedhouses",
        "parents": [
            "arts"
        ],
        "title": "Haunted Houses"
    },
    {
        "alias": "hawaiian",
        "country_blacklist": [
            "CZ",
            "AU",
            "TR",
            "DK",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Hawaiian"
    },
    {
        "country_whitelist": [
            "HK",
            "PH",
            "SG",
            "MY",
            "TW"
        ],
        "alias": "hawkercentre",
        "parents": [
            "food"
        ],
        "title": "Hawker Centre"
    },
    {
        "alias": "headshops",
        "parents": [
            "shopping"
        ],
        "title": "Head Shops"
    },
    {
        "alias": "health",
        "parents": [],
        "title": "Health & Medical"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "PT",
            "DE",
            "US",
            "CZ",
            "NZ",
            "AU",
            "BR",
            "SG",
            "MX"
        ],
        "alias": "healthinsurance",
        "parents": [
            "health"
        ],
        "title": "Health Insurance Offices"
    },
    {
        "alias": "healthmarkets",
        "parents": [
            "gourmet"
        ],
        "title": "Health Markets"
    },
    {
        "alias": "healthretreats",
        "country_blacklist": [
            "CZ",
            "AR",
            "MX"
        ],
        "parents": [
            "hotelstravel"
        ],
        "title": "Health Retreats"
    },
    {
        "alias": "healthtrainers",
        "parents": [
            "fitness"
        ],
        "title": "Trainers"
    },
    {
        "country_whitelist": [
            "FR",
            "CH",
            "DK",
            "PT",
            "NO",
            "DE",
            "AT",
            "BR",
            "FI",
            "PL"
        ],
        "alias": "hearing_aids",
        "parents": [
            "health"
        ],
        "title": "Hearing Aids"
    },
    {
        "alias": "hearingaidproviders",
        "country_blacklist": [
            "ES",
            "CZ",
            "JP",
            "TR",
            "HK",
            "NZ",
            "AU",
            "GB",
            "IE",
            "SE"
        ],
        "parents": [
            "health"
        ],
        "title": "Hearing Aid Providers"
    },
    {
        "country_whitelist": [
            "HK",
            "SG",
            "MY",
            "TW"
        ],
        "alias": "henghwa",
        "parents": [
            "chinese"
        ],
        "title": "Henghwa"
    },
    {
        "country_whitelist": [
            "FR",
            "AU",
            "BR",
            "NZ",
            "IT",
            "US"
        ],
        "alias": "hennaartists",
        "parents": [
            "eventservices"
        ],
        "title": "Henna Artists"
    },
    {
        "alias": "hepatologists",
        "parents": [
            "physicians"
        ],
        "title": "Hepatologists"
    },
    {
        "alias": "herbsandspices",
        "parents": [
            "gourmet"
        ],
        "title": "Herbs & Spices"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "hessian",
        "parents": [
            "german"
        ],
        "title": "Hessian"
    },
    {
        "country_whitelist": [
            "AT"
        ],
        "alias": "heuriger",
        "parents": [
            "restaurants"
        ],
        "title": "Heuriger"
    },
    {
        "alias": "hifi",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "shopping"
        ],
        "title": "High Fidelity Audio Equipment"
    },
    {
        "alias": "highschools",
        "parents": [
            "education"
        ],
        "title": "Middle Schools & High Schools"
    },
    {
        "alias": "hiking",
        "parents": [
            "active"
        ],
        "title": "Hiking"
    },
    {
        "alias": "himalayan",
        "parents": [
            "restaurants"
        ],
        "title": "Himalayan/Nepalese"
    },
    {
        "alias": "hindu_temples",
        "parents": [
            "religiousorgs"
        ],
        "title": "Hindu Temples"
    },
    {
        "alias": "historicaltours",
        "parents": [
            "tours"
        ],
        "title": "Historical Tours"
    },
    {
        "country_whitelist": [
            "HK"
        ],
        "alias": "hkcafe",
        "parents": [
            "restaurants"
        ],
        "title": "Hong Kong Style Cafe"
    },
    {
        "alias": "hobbyshops",
        "parents": [
            "shopping"
        ],
        "title": "Hobby Shops"
    },
    {
        "country_whitelist": [
            "HK",
            "SG",
            "MY",
            "TW"
        ],
        "alias": "hokkien",
        "parents": [
            "chinese"
        ],
        "title": "Hokkien"
    },
    {
        "alias": "holidaydecorations",
        "parents": [
            "homeandgarden"
        ],
        "title": "Holiday Decorations"
    },
    {
        "alias": "home_inspectors",
        "parents": [
            "homeservices"
        ],
        "title": "Home Inspectors"
    },
    {
        "country_whitelist": [
            "CA",
            "US"
        ],
        "alias": "home_organization",
        "parents": [
            "homeservices"
        ],
        "title": "Home Organization"
    },
    {
        "alias": "homeandgarden",
        "parents": [
            "shopping"
        ],
        "title": "Home & Garden"
    },
    {
        "alias": "homeappliancerepair",
        "parents": [
            "localservices"
        ],
        "title": "Appliances & Repair"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "homeautomation",
        "parents": [
            "homeservices"
        ],
        "title": "Home Automation"
    },
    {
        "alias": "homecleaning",
        "parents": [
            "homeservices"
        ],
        "title": "Home Cleaning"
    },
    {
        "alias": "homedecor",
        "parents": [
            "homeandgarden"
        ],
        "title": "Home Decor"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "NL",
            "DE",
            "US",
            "AT",
            "SE"
        ],
        "alias": "homeenergyauditors",
        "parents": [
            "homeservices"
        ],
        "title": "Home Energy Auditors"
    },
    {
        "alias": "homehealthcare",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "health"
        ],
        "title": "Home Health Care"
    },
    {
        "alias": "homeinsurance",
        "parents": [
            "insurance"
        ],
        "title": "Home & Rental Insurance"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "homemadefood",
        "parents": [
            "turkish"
        ],
        "title": "Homemade Food"
    },
    {
        "country_whitelist": [
            "ES",
            "NO",
            "SE",
            "US",
            "DK"
        ],
        "alias": "homenetworkinstall",
        "parents": [
            "homeservices"
        ],
        "title": "Home Network Installation"
    },
    {
        "alias": "homeopathic",
        "country_blacklist": [
            "PT",
            "CZ",
            "IE",
            "TW",
            "CA",
            "TR",
            "US",
            "HK",
            "NZ",
            "AU",
            "GB",
            "SG",
            "PL"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Homeopathic"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "homeownerassociation",
        "parents": [
            "realestate"
        ],
        "title": "Homeowner Association"
    },
    {
        "alias": "homeservices",
        "parents": [],
        "title": "Home Services"
    },
    {
        "alias": "homestaging",
        "country_blacklist": [
            "CH",
            "PT",
            "DE",
            "IT",
            "CZ",
            "AT",
            "BR",
            "ES"
        ],
        "parents": [
            "realestate"
        ],
        "title": "Home Staging"
    },
    {
        "alias": "hometheatreinstallation",
        "country_blacklist": [
            "CZ",
            "DK"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Home Theatre Installation"
    },
    {
        "country_whitelist": [
            "PT",
            "US"
        ],
        "alias": "homewindowtinting",
        "parents": [
            "homeservices"
        ],
        "title": "Home Window Tinting"
    },
    {
        "country_whitelist": [
            "FR",
            "FI",
            "DE",
            "TR",
            "IT",
            "SE"
        ],
        "alias": "honey",
        "parents": [
            "food"
        ],
        "title": "Honey"
    },
    {
        "alias": "hookah_bars",
        "country_blacklist": [
            "AU",
            "PT",
            "CL"
        ],
        "parents": [
            "bars"
        ],
        "title": "Hookah Bars"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "NO",
            "CA",
            "DE",
            "US",
            "CZ",
            "SE"
        ],
        "alias": "horse_boarding",
        "parents": [
            "pets"
        ],
        "title": "Horse Boarding"
    },
    {
        "alias": "horsebackriding",
        "parents": [
            "active"
        ],
        "title": "Horseback Riding"
    },
    {
        "country_whitelist": [
            "FR",
            "NL",
            "DK",
            "NO",
            "DE",
            "IT",
            "US",
            "CZ",
            "ES",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "alias": "horsequipment",
        "parents": [
            "shopping"
        ],
        "title": "Horse Equipment Shops"
    },
    {
        "alias": "horseracing",
        "country_blacklist": [
            "BE",
            "FR",
            "CA",
            "IT",
            "HK",
            "GB",
            "BR",
            "SG",
            "IE",
            "ES",
            "NL",
            "TW",
            "NZ",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "active"
        ],
        "title": "Horse Racing"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "horumon",
        "parents": [
            "japanese"
        ],
        "title": "Horumon"
    },
    {
        "alias": "hospice",
        "parents": [
            "health"
        ],
        "title": "Hospice"
    },
    {
        "alias": "hospitalists",
        "country_blacklist": [
            "CL",
            "AR",
            "JP",
            "MX",
            "IT"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Hospitalists"
    },
    {
        "alias": "hospitals",
        "parents": [
            "health"
        ],
        "title": "Hospitals"
    },
    {
        "alias": "hostels",
        "parents": [
            "hotelstravel"
        ],
        "title": "Hostels"
    },
    {
        "alias": "hot_air_balloons",
        "country_blacklist": [
            "CA",
            "SG",
            "NZ",
            "BR"
        ],
        "parents": [
            "active"
        ],
        "title": "Hot Air Balloons"
    },
    {
        "alias": "hotdog",
        "parents": [
            "restaurants"
        ],
        "title": "Hot Dogs"
    },
    {
        "alias": "hotdogs",
        "parents": [
            "restaurants"
        ],
        "title": "Fast Food"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "FI",
            "BR",
            "SE"
        ],
        "alias": "hotel_bar",
        "parents": [
            "bars"
        ],
        "title": "Hotel bar"
    },
    {
        "alias": "hotels",
        "parents": [
            "hotelstravel",
            "eventservices"
        ],
        "title": "Hotels"
    },
    {
        "alias": "hotelstravel",
        "parents": [],
        "title": "Hotels & Travel"
    },
    {
        "country_whitelist": [
            "FR",
            "TW",
            "CA",
            "JP",
            "US",
            "HK",
            "MY",
            "BR",
            "PH",
            "SG",
            "SE"
        ],
        "alias": "hotpot",
        "parents": [
            "restaurants"
        ],
        "title": "Hot Pot"
    },
    {
        "country_whitelist": [
            "AU",
            "NZ",
            "JP",
            "BR",
            "TW"
        ],
        "alias": "hotsprings",
        "parents": [
            "beautysvc"
        ],
        "title": "Hot Springs"
    },
    {
        "alias": "hottubandpool",
        "parents": [
            "homeandgarden"
        ],
        "title": "Hot Tub & Pool"
    },
    {
        "country_whitelist": [
            "AU",
            "IT",
            "US"
        ],
        "alias": "housesitters",
        "parents": [
            "homeservices"
        ],
        "title": "House Sitters"
    },
    {
        "alias": "housingcooperatives",
        "country_blacklist": [
            "CL",
            "AR",
            "MX",
            "IT"
        ],
        "parents": [
            "realestate"
        ],
        "title": "Housing Cooperatives"
    },
    {
        "country_whitelist": [
            "HK",
            "FR",
            "SG",
            "MY",
            "TW"
        ],
        "alias": "hunan",
        "parents": [
            "chinese"
        ],
        "title": "Hunan"
    },
    {
        "alias": "hungarian",
        "country_blacklist": [
            "DK",
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Hungarian"
    },
    {
        "alias": "huntingfishingsupplies",
        "parents": [
            "sportgoods"
        ],
        "title": "Hunting & Fishing Supplies"
    },
    {
        "alias": "hvac",
        "parents": [
            "homeservices"
        ],
        "title": "Heating & Air Conditioning/HVAC"
    },
    {
        "alias": "hydrotherapy",
        "parents": [
            "health"
        ],
        "title": "Hydrotherapy"
    },
    {
        "alias": "hypnosis",
        "country_blacklist": [
            "ES",
            "NL",
            "CZ",
            "TR",
            "HK",
            "GB",
            "IE",
            "PL"
        ],
        "parents": [
            "health"
        ],
        "title": "Hypnosis/Hypnotherapy"
    },
    {
        "country_whitelist": [
            "CA",
            "PT",
            "US"
        ],
        "alias": "iberian",
        "parents": [
            "restaurants"
        ],
        "title": "Iberian"
    },
    {
        "alias": "icecream",
        "parents": [
            "food"
        ],
        "title": "Ice Cream & Frozen Yogurt"
    },
    {
        "alias": "immigrationlawyers",
        "parents": [
            "lawyers"
        ],
        "title": "Immigration Law"
    },
    {
        "alias": "immunodermatologists",
        "country_blacklist": [
            "FR",
            "JP"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Immunodermatologists"
    },
    {
        "alias": "indonesian",
        "country_blacklist": [
            "MX",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Indonesian"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "DE",
            "JP",
            "IT",
            "CZ",
            "NZ",
            "AU",
            "ES",
            "SE"
        ],
        "alias": "indoor_playcenter",
        "parents": [
            "active"
        ],
        "title": "Indoor Playcentre"
    },
    {
        "alias": "indoorlandscaping",
        "country_blacklist": [
            "IT"
        ],
        "parents": [
            "professional"
        ],
        "title": "Indoor Landscaping"
    },
    {
        "alias": "indpak",
        "parents": [
            "restaurants"
        ],
        "title": "Indian"
    },
    {
        "alias": "infectiousdisease",
        "parents": [
            "physicians"
        ],
        "title": "Infectious Disease Specialists"
    },
    {
        "alias": "insulationinstallation",
        "parents": [
            "homeservices"
        ],
        "title": "Insulation Installation"
    },
    {
        "alias": "insurance",
        "parents": [
            "financialservices"
        ],
        "title": "Insurance"
    },
    {
        "alias": "interiordesign",
        "parents": [
            "homeservices"
        ],
        "title": "Interior Design"
    },
    {
        "alias": "internalmed",
        "country_blacklist": [
            "BR"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Internal Medicine"
    },
    {
        "alias": "international",
        "country_blacklist": [
            "ES",
            "BE",
            "NL",
            "IE",
            "TR",
            "IT",
            "US",
            "CZ",
            "GB",
            "SE",
            "FI",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "International"
    },
    {
        "country_whitelist": [
            "AR",
            "BR",
            "CL",
            "IT",
            "ES",
            "MX"
        ],
        "alias": "internetbooth",
        "parents": [
            "localservices"
        ],
        "title": "Internet Booths & Calling Centers"
    },
    {
        "alias": "internetcafe",
        "parents": [
            "food"
        ],
        "title": "Internet Cafes"
    },
    {
        "alias": "investing",
        "parents": [
            "financialservices"
        ],
        "title": "Investing"
    },
    {
        "country_whitelist": [
            "CZ",
            "US"
        ],
        "alias": "iplaw",
        "parents": [
            "lawyers"
        ],
        "title": "IP & Internet Law"
    },
    {
        "alias": "irish",
        "parents": [
            "restaurants"
        ],
        "title": "Irish"
    },
    {
        "alias": "irish_pubs",
        "parents": [
            "bars"
        ],
        "title": "Irish Pub"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "irrigation",
        "parents": [
            "homeservices"
        ],
        "title": "Irrigation"
    },
    {
        "country_whitelist": [
            "SE"
        ],
        "alias": "island_pub",
        "parents": [
            "restaurants"
        ],
        "title": "Island Pub"
    },
    {
        "alias": "isps",
        "parents": [
            "professional",
            "homeservices"
        ],
        "title": "Internet Service Providers"
    },
    {
        "country_whitelist": [
            "CZ",
            "CH",
            "DE",
            "AT"
        ],
        "alias": "israeli",
        "parents": [
            "restaurants"
        ],
        "title": "Israeli"
    },
    {
        "alias": "italian",
        "parents": [
            "restaurants"
        ],
        "title": "Italian"
    },
    {
        "alias": "itservices",
        "parents": [
            "localservices"
        ],
        "title": "IT Services & Computer Repair"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "ivhydration",
        "parents": [
            "health"
        ],
        "title": "IV Hydration"
    },
    {
        "country_whitelist": [
            "NZ",
            "AU",
            "BR",
            "TW",
            "SG",
            "JP",
            "MX"
        ],
        "alias": "izakaya",
        "parents": [
            "japanese"
        ],
        "title": "Izakaya"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "jaliscan",
        "parents": [
            "mexican"
        ],
        "title": "Jaliscan"
    },
    {
        "country_whitelist": [
            "HK",
            "SG",
            "JP",
            "TW"
        ],
        "alias": "japacurry",
        "parents": [
            "japanese"
        ],
        "title": "Japanese Curry"
    },
    {
        "alias": "japanese",
        "parents": [
            "restaurants"
        ],
        "title": "Japanese"
    },
    {
        "alias": "jazzandblues",
        "parents": [
            "arts",
            "nightlife"
        ],
        "title": "Jazz & Blues"
    },
    {
        "alias": "jetskis",
        "parents": [
            "active"
        ],
        "title": "Jet Skis"
    },
    {
        "alias": "jewelry",
        "parents": [
            "shopping"
        ],
        "title": "Jewelry"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "PT",
            "JP",
            "CA",
            "TR",
            "IT",
            "US",
            "CZ",
            "AU",
            "ES",
            "PL"
        ],
        "alias": "jewelryrepair",
        "parents": [
            "localservices"
        ],
        "title": "Jewelry Repair"
    },
    {
        "country_whitelist": [
            "DE",
            "IT",
            "PL"
        ],
        "alias": "jewish",
        "parents": [
            "restaurants"
        ],
        "title": "Jewish"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "jpsweets",
        "parents": [
            "food"
        ],
        "title": "Japanese Sweets"
    },
    {
        "alias": "juicebars",
        "parents": [
            "food"
        ],
        "title": "Juice Bars & Smoothies"
    },
    {
        "alias": "junkremovalandhauling",
        "parents": [
            "localservices"
        ],
        "title": "Junk Removal & Hauling"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "kaiseki",
        "parents": [
            "japanese"
        ],
        "title": "Kaiseki"
    },
    {
        "alias": "karaoke",
        "parents": [
            "nightlife"
        ],
        "title": "Karaoke"
    },
    {
        "alias": "kebab",
        "country_blacklist": [
            "CA",
            "NL",
            "GB",
            "US",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Kebab"
    },
    {
        "alias": "kids_activities",
        "country_blacklist": [
            "CA",
            "SG"
        ],
        "parents": [
            "active"
        ],
        "title": "Kids Activities"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "kimonos",
        "parents": [
            "fashion"
        ],
        "title": "Kimonos"
    },
    {
        "alias": "kiosk",
        "country_blacklist": [
            "FR",
            "IE",
            "CA",
            "IT",
            "US",
            "HK",
            "NZ",
            "GB",
            "BR",
            "SG"
        ],
        "parents": [
            "food",
            "shopping"
        ],
        "title": "Kiosk"
    },
    {
        "alias": "kitchenandbath",
        "parents": [
            "homeandgarden"
        ],
        "title": "Kitchen & Bath"
    },
    {
        "country_whitelist": [
            "GB",
            "US"
        ],
        "alias": "kitchenincubators",
        "parents": [
            "realestate"
        ],
        "title": "Kitchen Incubators"
    },
    {
        "alias": "kiteboarding",
        "country_blacklist": [
            "BE",
            "CH",
            "CZ",
            "CA",
            "IT",
            "HK",
            "AT",
            "PL",
            "GB"
        ],
        "parents": [
            "active"
        ],
        "title": "Kiteboarding"
    },
    {
        "country_whitelist": [
            "ES",
            "CL",
            "IT",
            "US",
            "CZ",
            "AU",
            "GB",
            "BR",
            "SE"
        ],
        "alias": "knifesharpening",
        "parents": [
            "localservices"
        ],
        "title": "Knife Sharpening"
    },
    {
        "alias": "knittingsupplies",
        "parents": [
            "shopping"
        ],
        "title": "Knitting Supplies"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "kombucha",
        "parents": [
            "food"
        ],
        "title": "Kombucha"
    },
    {
        "country_whitelist": [
            "MY",
            "SG"
        ],
        "alias": "kopitiam",
        "parents": [
            "restaurants"
        ],
        "title": "Kopitiam"
    },
    {
        "alias": "korean",
        "parents": [
            "restaurants"
        ],
        "title": "Korean"
    },
    {
        "alias": "kosher",
        "country_blacklist": [
            "TR",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Kosher"
    },
    {
        "country_whitelist": [
            "SE",
            "NO"
        ],
        "alias": "kurdish",
        "parents": [
            "restaurants"
        ],
        "title": "Kurdish"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "kushikatsu",
        "parents": [
            "japanese"
        ],
        "title": "Kushikatsu"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "PT",
            "IT",
            "US",
            "AU",
            "BR",
            "MX"
        ],
        "alias": "laboratorytesting",
        "parents": [
            "diagnosticservices"
        ],
        "title": "Laboratory Testing"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "IT",
            "PT",
            "US"
        ],
        "alias": "lactationservices",
        "parents": [
            "health"
        ],
        "title": "Lactation Services"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "lahmacun",
        "parents": [
            "turkish"
        ],
        "title": "Lahmacun"
    },
    {
        "alias": "lakes",
        "parents": [
            "active"
        ],
        "title": "Lakes"
    },
    {
        "alias": "lancenters",
        "country_blacklist": [
            "PH",
            "MY",
            "IT"
        ],
        "parents": [
            "arts"
        ],
        "title": "LAN Centers"
    },
    {
        "alias": "landmarks",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Landmarks & Historical Buildings"
    },
    {
        "alias": "landscapearchitects",
        "parents": [
            "homeservices"
        ],
        "title": "Landscape Architects"
    },
    {
        "alias": "landscaping",
        "country_blacklist": [
            "DK",
            "ES"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Landscaping"
    },
    {
        "alias": "landsurveying",
        "country_blacklist": [
            "JP"
        ],
        "parents": [
            "realestatesvcs"
        ],
        "title": "Land Surveying"
    },
    {
        "alias": "language_schools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Language Schools"
    },
    {
        "country_whitelist": [
            "AU"
        ],
        "alias": "laos",
        "parents": [
            "restaurants"
        ],
        "title": "Laos"
    },
    {
        "alias": "laotian",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Laotian"
    },
    {
        "alias": "laser_hair_removal",
        "parents": [
            "hairremoval"
        ],
        "title": "Laser Hair Removal"
    },
    {
        "alias": "laserlasikeyes",
        "parents": [
            "health"
        ],
        "title": "Laser Eye Surgery/Lasik"
    },
    {
        "alias": "lasertag",
        "country_blacklist": [
            "IE",
            "BR"
        ],
        "parents": [
            "active"
        ],
        "title": "Laser Tag"
    },
    {
        "alias": "latin",
        "parents": [
            "restaurants"
        ],
        "title": "Latin American"
    },
    {
        "country_whitelist": [
            "NZ",
            "AU",
            "PT",
            "NO",
            "FI",
            "SE"
        ],
        "alias": "lawn_bowling",
        "parents": [
            "active"
        ],
        "title": "Lawn Bowling"
    },
    {
        "alias": "lawyers",
        "parents": [
            "professional"
        ],
        "title": "Lawyers"
    },
    {
        "alias": "leather",
        "parents": [
            "fashion"
        ],
        "title": "Leather Goods"
    },
    {
        "alias": "lebanese",
        "country_blacklist": [
            "HK",
            "AR",
            "JP"
        ],
        "parents": [
            "mideastern"
        ],
        "title": "Lebanese"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "PT",
            "CA",
            "TR",
            "IT",
            "US",
            "CZ",
            "NZ",
            "AU",
            "BR",
            "SG"
        ],
        "alias": "legalservices",
        "parents": [
            "professional"
        ],
        "title": "Legal Services"
    },
    {
        "alias": "leisure_centers",
        "country_blacklist": [
            "DK"
        ],
        "parents": [
            "active"
        ],
        "title": "Leisure Centers"
    },
    {
        "alias": "libraries",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Libraries"
    },
    {
        "alias": "liceservices",
        "country_blacklist": [
            "CL",
            "DE",
            "JP",
            "CZ",
            "AR",
            "HK",
            "FI",
            "MX"
        ],
        "parents": [
            "health"
        ],
        "title": "Lice Services"
    },
    {
        "alias": "lifecoach",
        "parents": [
            "professional"
        ],
        "title": "Life Coach"
    },
    {
        "country_whitelist": [
            "ES",
            "DK",
            "NO",
            "IE",
            "TR",
            "JP",
            "IT",
            "US",
            "CZ",
            "NZ",
            "AU",
            "GB",
            "BR",
            "SG",
            "SE"
        ],
        "alias": "lifeinsurance",
        "parents": [
            "insurance"
        ],
        "title": "Life Insurance"
    },
    {
        "alias": "lighting",
        "parents": [
            "homeservices"
        ],
        "title": "Lighting Fixtures & Equipment"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "ligurian",
        "parents": [
            "italian"
        ],
        "title": "Ligurian"
    },
    {
        "alias": "limos",
        "parents": [
            "transport"
        ],
        "title": "Limos"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "PT",
            "DE",
            "IT",
            "CZ",
            "AT"
        ],
        "alias": "linens",
        "parents": [
            "homeandgarden"
        ],
        "title": "Linens"
    },
    {
        "alias": "lingerie",
        "parents": [
            "fashion"
        ],
        "title": "Lingerie"
    },
    {
        "alias": "livestocksupply",
        "parents": [
            "shopping"
        ],
        "title": "Livestock Feed & Supply"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "NO",
            "DE",
            "JP",
            "IT",
            "US",
            "ES",
            "SG",
            "SE"
        ],
        "alias": "localfishstores",
        "parents": [
            "petstore"
        ],
        "title": "Local Fish Stores"
    },
    {
        "alias": "localflavor",
        "parents": [],
        "title": "Local Flavor"
    },
    {
        "alias": "localservices",
        "parents": [],
        "title": "Local Services"
    },
    {
        "alias": "locksmiths",
        "parents": [
            "homeservices"
        ],
        "title": "Keys & Locksmiths"
    },
    {
        "alias": "lounges",
        "parents": [
            "bars"
        ],
        "title": "Lounges"
    },
    {
        "alias": "luggage",
        "parents": [
            "shopping"
        ],
        "title": "Luggage"
    },
    {
        "alias": "luggagestorage",
        "parents": [
            "travelservices"
        ],
        "title": "Luggage Storage"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "lumbard",
        "parents": [
            "italian"
        ],
        "title": "Lumbard"
    },
    {
        "country_whitelist": [
            "BE",
            "FR"
        ],
        "alias": "lyonnais",
        "parents": [
            "restaurants"
        ],
        "title": "Lyonnais"
    },
    {
        "alias": "macarons",
        "country_blacklist": [
            "PH",
            "MY",
            "IT"
        ],
        "parents": [
            "gourmet"
        ],
        "title": "Macarons"
    },
    {
        "alias": "machinerental",
        "parents": [
            "localservices"
        ],
        "title": "Machine & Tool Rental"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "madeira",
        "parents": [
            "portuguese"
        ],
        "title": "Madeira"
    },
    {
        "alias": "magicians",
        "country_blacklist": [
            "PL",
            "SE",
            "NO",
            "FI",
            "SG",
            "TR",
            "ES"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Magicians"
    },
    {
        "alias": "mags",
        "parents": [
            "media"
        ],
        "title": "Newspapers & Magazines"
    },
    {
        "country_whitelist": [
            "HK",
            "JP"
        ],
        "alias": "mahjong",
        "parents": [
            "arts"
        ],
        "title": "Mah Jong Halls"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "mailboxcenters",
        "parents": [
            "localservices"
        ],
        "title": "Mailbox Centers"
    },
    {
        "alias": "makeupartists",
        "parents": [
            "beautysvc"
        ],
        "title": "Makeup Artists"
    },
    {
        "alias": "malaysian",
        "country_blacklist": [
            "CZ",
            "TR",
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Malaysian"
    },
    {
        "country_whitelist": [
            "AU",
            "MY"
        ],
        "alias": "mamak",
        "parents": [
            "malaysian"
        ],
        "title": "Mamak"
    },
    {
        "country_whitelist": [
            "CH",
            "PT",
            "NO",
            "DE",
            "TR",
            "AT",
            "SE",
            "GB"
        ],
        "alias": "marchingbands",
        "parents": [
            "arts"
        ],
        "title": "Marching Bands"
    },
    {
        "country_whitelist": [
            "ES",
            "FR",
            "DK",
            "CL",
            "NO",
            "TR",
            "IT",
            "US",
            "NZ",
            "AR",
            "GB",
            "BR",
            "IE",
            "MX",
            "SE"
        ],
        "alias": "marinas",
        "parents": [
            "auto"
        ],
        "title": "Marinas"
    },
    {
        "alias": "marketing",
        "parents": [
            "professional"
        ],
        "title": "Marketing"
    },
    {
        "alias": "markets",
        "parents": [
            "gourmet"
        ],
        "title": "Fruits & Veggies"
    },
    {
        "country_whitelist": [
            "CH",
            "DK",
            "PT",
            "NO",
            "DE",
            "IT",
            "CZ",
            "AT",
            "IE",
            "GB"
        ],
        "alias": "marketstalls",
        "parents": [
            "shopping"
        ],
        "title": "Market Stalls"
    },
    {
        "alias": "martialarts",
        "parents": [
            "fitness"
        ],
        "title": "Martial Arts"
    },
    {
        "alias": "masonry_concrete",
        "country_blacklist": [
            "BE",
            "NZ",
            "NL",
            "GB",
            "BR",
            "IE",
            "SG"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Masonry/Concrete"
    },
    {
        "alias": "massage",
        "parents": [
            "beautysvc"
        ],
        "title": "Massage"
    },
    {
        "alias": "massage_schools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Massage Schools"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "DK",
            "PT",
            "NO",
            "CA",
            "JP",
            "IT",
            "US",
            "AU",
            "GB",
            "BR"
        ],
        "alias": "massage_therapy",
        "parents": [
            "health"
        ],
        "title": "Massage Therapy"
    },
    {
        "alias": "massmedia",
        "parents": [],
        "title": "Mass Media"
    },
    {
        "country_whitelist": [
            "US",
            "FR",
            "CA",
            "PT",
            "DK"
        ],
        "alias": "matchmakers",
        "parents": [
            "professional"
        ],
        "title": "Matchmakers"
    },
    {
        "country_whitelist": [
            "CL",
            "AR",
            "MX",
            "ES",
            "IT"
        ],
        "alias": "materialeelettrico",
        "parents": [
            "homeandgarden"
        ],
        "title": "Materiale elettrico"
    },
    {
        "alias": "maternity",
        "parents": [
            "fashion"
        ],
        "title": "Maternity Wear"
    },
    {
        "alias": "mattresses",
        "parents": [
            "homeandgarden"
        ],
        "title": "Mattresses"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "meatballs",
        "parents": [
            "restaurants"
        ],
        "title": "Meatballs"
    },
    {
        "alias": "meats",
        "parents": [
            "gourmet"
        ],
        "title": "Meat Shops"
    },
    {
        "alias": "medcenters",
        "parents": [
            "health"
        ],
        "title": "Medical Centers"
    },
    {
        "alias": "media",
        "parents": [
            "shopping"
        ],
        "title": "Books, Mags, Music & Video"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT",
            "US",
            "IT"
        ],
        "alias": "mediators",
        "parents": [
            "professional"
        ],
        "title": "Mediators"
    },
    {
        "country_whitelist": [
            "CH",
            "AU",
            "AT",
            "NO",
            "DE",
            "SE"
        ],
        "alias": "medicalfoot",
        "parents": [
            "health"
        ],
        "title": "Medical Foot Care"
    },
    {
        "alias": "medicallaw",
        "parents": [
            "lawyers"
        ],
        "title": "Medical Law"
    },
    {
        "alias": "medicalspa",
        "parents": [
            "health",
            "beautysvc"
        ],
        "title": "Medical Spas"
    },
    {
        "alias": "medicalsupplies",
        "country_blacklist": [
            "BE",
            "NL",
            "CL",
            "TR",
            "AR",
            "FI",
            "MX",
            "SE"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Medical Supplies"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "PT",
            "IT",
            "US",
            "AU",
            "BR",
            "SG"
        ],
        "alias": "medicaltransportation",
        "parents": [
            "health"
        ],
        "title": "Medical Transportation"
    },
    {
        "alias": "meditationcenters",
        "country_blacklist": [
            "AR",
            "MX"
        ],
        "parents": [
            "fitness"
        ],
        "title": "Meditation Centers"
    },
    {
        "alias": "mediterranean",
        "parents": [
            "restaurants"
        ],
        "title": "Mediterranean"
    },
    {
        "alias": "menscloth",
        "parents": [
            "fashion"
        ],
        "title": "Men's Clothing"
    },
    {
        "country_whitelist": [
            "CZ",
            "AU",
            "DK",
            "PT",
            "NO",
            "CL",
            "US"
        ],
        "alias": "menshair",
        "parents": [
            "hair"
        ],
        "title": "Men's Hair Salons"
    },
    {
        "alias": "metalfabricators",
        "country_blacklist": [
            "AR",
            "MX",
            "SE"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Metal Fabricators"
    },
    {
        "alias": "mexican",
        "parents": [
            "restaurants"
        ],
        "title": "Mexican"
    },
    {
        "alias": "mideastern",
        "country_blacklist": [
            "BR"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Middle Eastern"
    },
    {
        "alias": "midwives",
        "parents": [
            "health"
        ],
        "title": "Midwives"
    },
    {
        "country_whitelist": [
            "AU",
            "PL"
        ],
        "alias": "milkbars",
        "parents": [
            "restaurants"
        ],
        "title": "Milk Bars"
    },
    {
        "country_whitelist": [
            "GB"
        ],
        "alias": "milkshakebars",
        "parents": [
            "food"
        ],
        "title": "Milkshake Bars"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "minho",
        "parents": [
            "portuguese"
        ],
        "title": "Minho"
    },
    {
        "alias": "mini_golf",
        "country_blacklist": [
            "IT"
        ],
        "parents": [
            "active"
        ],
        "title": "Mini Golf"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "mobiledentrepair",
        "parents": [
            "auto"
        ],
        "title": "Mobile Dent Repair"
    },
    {
        "alias": "mobilehomes",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "realestate"
        ],
        "title": "Mobile Home Dealers"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "mobileparks",
        "parents": [
            "realestate"
        ],
        "title": "Mobile Home Parks"
    },
    {
        "alias": "mobilephonerepair",
        "parents": [
            "itservices"
        ],
        "title": "Mobile Phone Repair"
    },
    {
        "alias": "mobilephones",
        "parents": [
            "shopping"
        ],
        "title": "Mobile Phones"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "mobilityequipment",
        "parents": [
            "auto"
        ],
        "title": "Mobility Equipment Sales & Services"
    },
    {
        "country_whitelist": [
            "AU"
        ],
        "alias": "modern_australian",
        "parents": [
            "restaurants"
        ],
        "title": "Modern Australian"
    },
    {
        "alias": "modern_european",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Modern European"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "mohels",
        "parents": [
            "eventservices"
        ],
        "title": "Mohels"
    },
    {
        "alias": "mongolian",
        "country_blacklist": [
            "FI",
            "TR",
            "DK",
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Mongolian"
    },
    {
        "alias": "montessori",
        "parents": [
            "education"
        ],
        "title": "Montessori Schools"
    },
    {
        "alias": "moroccan",
        "country_blacklist": [
            "TR"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Moroccan"
    },
    {
        "alias": "mortgagebrokers",
        "country_blacklist": [
            "BR",
            "DK",
            "ES"
        ],
        "parents": [
            "realestate"
        ],
        "title": "Mortgage Brokers"
    },
    {
        "alias": "mosques",
        "parents": [
            "religiousorgs"
        ],
        "title": "Mosques"
    },
    {
        "country_whitelist": [
            "ES",
            "TW",
            "IT",
            "US",
            "SE"
        ],
        "alias": "motodealers",
        "parents": [
            "auto"
        ],
        "title": "Motorsport Vehicle Dealers"
    },
    {
        "country_whitelist": [
            "FR",
            "PT",
            "NO",
            "DE",
            "IT",
            "US",
            "CZ",
            "NZ",
            "AU",
            "BR",
            "FI",
            "SG",
            "MX",
            "ES"
        ],
        "alias": "motorcycle_rental",
        "parents": [
            "hotelstravel"
        ],
        "title": "Motorcycle Rental"
    },
    {
        "alias": "motorcycledealers",
        "country_blacklist": [
            "BR"
        ],
        "parents": [
            "auto"
        ],
        "title": "Motorcycle Dealers"
    },
    {
        "alias": "motorcyclerepair",
        "parents": [
            "auto"
        ],
        "title": "Motorcycle Repair"
    },
    {
        "alias": "motorcyclinggear",
        "country_blacklist": [
            "CA",
            "IE",
            "NZ",
            "BR",
            "GB"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Motorcycle Gear"
    },
    {
        "country_whitelist": [
            "ES",
            "TW",
            "IT",
            "US",
            "SE"
        ],
        "alias": "motorepairs",
        "parents": [
            "auto"
        ],
        "title": "Motorsport Vehicle Repairs"
    },
    {
        "alias": "mountainbiking",
        "parents": [
            "active"
        ],
        "title": "Mountain Biking"
    },
    {
        "country_whitelist": [
            "FR",
            "CH",
            "CL",
            "DE",
            "IT",
            "US",
            "PL",
            "CZ",
            "NZ",
            "AR",
            "AT",
            "NO",
            "SE"
        ],
        "alias": "mountainhuts",
        "parents": [
            "hotels"
        ],
        "title": "Mountain Huts"
    },
    {
        "alias": "movers",
        "parents": [
            "homeservices"
        ],
        "title": "Movers"
    },
    {
        "alias": "movietheaters",
        "parents": [
            "arts"
        ],
        "title": "Cinema"
    },
    {
        "alias": "museums",
        "parents": [
            "arts"
        ],
        "title": "Museums"
    },
    {
        "alias": "musicalinstrumentsandteachers",
        "parents": [
            "shopping"
        ],
        "title": "Musical Instruments & Teachers"
    },
    {
        "alias": "musicians",
        "country_blacklist": [
            "TR",
            "ES",
            "PL"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Musicians"
    },
    {
        "alias": "musicinstrumentservices",
        "parents": [
            "localservices"
        ],
        "title": "Musical Instrument Services"
    },
    {
        "alias": "musicproduction",
        "parents": [
            "professional"
        ],
        "title": "Music Production Services"
    },
    {
        "alias": "musicvenues",
        "parents": [
            "arts",
            "nightlife"
        ],
        "title": "Music Venues"
    },
    {
        "alias": "musicvideo",
        "parents": [
            "media"
        ],
        "title": "Music & DVDs"
    },
    {
        "alias": "nailtechnicians",
        "country_blacklist": [
            "FR",
            "CH",
            "AT",
            "BR",
            "JP",
            "DE",
            "TR"
        ],
        "parents": [
            "othersalons"
        ],
        "title": "Nail Technicians"
    },
    {
        "alias": "nannys",
        "country_blacklist": [
            "ES",
            "CA",
            "PL",
            "BR",
            "FI",
            "IE",
            "SE",
            "GB"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Nanny Services"
    },
    {
        "country_whitelist": [
            "FR",
            "IT"
        ],
        "alias": "napoletana",
        "parents": [
            "italian"
        ],
        "title": "Napoletana"
    },
    {
        "country_whitelist": [
            "MY",
            "SG"
        ],
        "alias": "nasilemak",
        "parents": [
            "food"
        ],
        "title": "Nasi Lemak"
    },
    {
        "alias": "naturopathic",
        "parents": [
            "physicians"
        ],
        "title": "Naturopathic/Holistic"
    },
    {
        "alias": "nephrologists",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Nephrologists"
    },
    {
        "alias": "neurologist",
        "parents": [
            "physicians"
        ],
        "title": "Neurologist"
    },
    {
        "alias": "neuropathologists",
        "parents": [
            "physicians"
        ],
        "title": "Neuropathologists"
    },
    {
        "alias": "neurotologists",
        "country_blacklist": [
            "JP"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Neurotologists"
    },
    {
        "country_whitelist": [
            "DK",
            "SE",
            "NO",
            "IE",
            "US",
            "GB"
        ],
        "alias": "newamerican",
        "parents": [
            "restaurants"
        ],
        "title": "American (New)"
    },
    {
        "country_whitelist": [
            "CA"
        ],
        "alias": "newcanadian",
        "parents": [
            "restaurants"
        ],
        "title": "Canadian (New)"
    },
    {
        "country_whitelist": [
            "NZ"
        ],
        "alias": "newzealand",
        "parents": [
            "restaurants"
        ],
        "title": "New Zealand"
    },
    {
        "alias": "nicaraguan",
        "country_blacklist": [
            "AR",
            "CL"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Nicaraguan"
    },
    {
        "country_whitelist": [
            "FR"
        ],
        "alias": "nicois",
        "parents": [
            "french"
        ],
        "title": "Nicoise"
    },
    {
        "country_whitelist": [
            "NO",
            "TR",
            "DK",
            "SE",
            "PL"
        ],
        "alias": "nightfood",
        "parents": [
            "restaurants"
        ],
        "title": "Night Food"
    },
    {
        "alias": "nightlife",
        "parents": [],
        "title": "Nightlife"
    },
    {
        "country_whitelist": [
            "AR",
            "BR",
            "ES",
            "CL"
        ],
        "alias": "nikkei",
        "parents": [
            "restaurants"
        ],
        "title": "Nikkei"
    },
    {
        "alias": "nonprofit",
        "parents": [
            "localservices"
        ],
        "title": "Community Service/Non-Profit"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "norcinerie",
        "parents": [
            "restaurants"
        ],
        "title": "Norcinerie"
    },
    {
        "country_whitelist": [
            "BR"
        ],
        "alias": "northeasternbrazilian",
        "parents": [
            "brazilian"
        ],
        "title": "Northeastern Brazilian"
    },
    {
        "country_whitelist": [
            "BR"
        ],
        "alias": "northernbrazilian",
        "parents": [
            "brazilian"
        ],
        "title": "Northern Brazilian"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "northerngerman",
        "parents": [
            "german"
        ],
        "title": "Northern German"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "northernmexican",
        "parents": [
            "mexican"
        ],
        "title": "Northern Mexican"
    },
    {
        "country_whitelist": [
            "FR",
            "NO"
        ],
        "alias": "norwegian",
        "parents": [
            "restaurants"
        ],
        "title": "Traditional Norwegian"
    },
    {
        "alias": "notaries",
        "country_blacklist": [
            "NO"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Notaries"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "PT",
            "NO",
            "CA",
            "DE",
            "US",
            "CZ",
            "BR",
            "FI",
            "SE"
        ],
        "alias": "nudist",
        "parents": [
            "active"
        ],
        "title": "Nudist"
    },
    {
        "alias": "nursepractitioner",
        "parents": [
            "health"
        ],
        "title": "Nurse Practitioner"
    },
    {
        "alias": "nursingschools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Nursing Schools"
    },
    {
        "alias": "nutritionists",
        "parents": [
            "health"
        ],
        "title": "Nutritionists"
    },
    {
        "country_whitelist": [
            "AU",
            "MY"
        ],
        "alias": "nyonya",
        "parents": [
            "malaysian"
        ],
        "title": "Nyonya"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "oaxacan",
        "parents": [
            "mexican"
        ],
        "title": "Oaxacan"
    },
    {
        "alias": "obgyn",
        "parents": [
            "physicians"
        ],
        "title": "Obstetricians & Gynecologists"
    },
    {
        "alias": "observatories",
        "parents": [
            "arts"
        ],
        "title": "Observatories"
    },
    {
        "country_whitelist": [
            "AU",
            "GB",
            "PT",
            "CA",
            "DE",
            "IE",
            "US"
        ],
        "alias": "occupationaltherapy",
        "parents": [
            "health"
        ],
        "title": "Occupational Therapy"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "oden",
        "parents": [
            "japanese"
        ],
        "title": "Oden"
    },
    {
        "alias": "officecleaning",
        "parents": [
            "professional"
        ],
        "title": "Office Cleaning"
    },
    {
        "alias": "officeequipment",
        "parents": [
            "shopping"
        ],
        "title": "Office Equipment"
    },
    {
        "alias": "officiants",
        "parents": [
            "eventservices"
        ],
        "title": "Officiants"
    },
    {
        "alias": "oilchange",
        "country_blacklist": [
            "CZ",
            "CH",
            "AT",
            "BR",
            "NO",
            "DE",
            "SE"
        ],
        "parents": [
            "auto"
        ],
        "title": "Oil Change Stations"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "okinawan",
        "parents": [
            "japanese"
        ],
        "title": "Okinawan"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "okonomiyaki",
        "parents": [
            "japanese"
        ],
        "title": "Okonomiyaki"
    },
    {
        "alias": "oncologist",
        "parents": [
            "physicians"
        ],
        "title": "Oncologist"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "onigiri",
        "parents": [
            "japanese"
        ],
        "title": "Onigiri"
    },
    {
        "country_whitelist": [
            "TR",
            "DK",
            "SE",
            "NO"
        ],
        "alias": "opensandwiches",
        "parents": [
            "restaurants"
        ],
        "title": "Open Sandwiches"
    },
    {
        "alias": "opera",
        "parents": [
            "arts"
        ],
        "title": "Opera & Ballet"
    },
    {
        "alias": "opthamalogists",
        "parents": [
            "physicians"
        ],
        "title": "Ophthalmologists"
    },
    {
        "alias": "opticians",
        "parents": [
            "shopping"
        ],
        "title": "Eyewear & Opticians"
    },
    {
        "alias": "optometrists",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "health"
        ],
        "title": "Optometrists"
    },
    {
        "alias": "oralsurgeons",
        "parents": [
            "dentists"
        ],
        "title": "Oral Surgeons"
    },
    {
        "alias": "organic_stores",
        "parents": [
            "food"
        ],
        "title": "Organic Stores"
    },
    {
        "country_whitelist": [
            "FR",
            "CH",
            "DE",
            "AT",
            "PT"
        ],
        "alias": "oriental",
        "parents": [
            "restaurants"
        ],
        "title": "Oriental"
    },
    {
        "alias": "orthodontists",
        "parents": [
            "dentists"
        ],
        "title": "Orthodontists"
    },
    {
        "alias": "orthopedists",
        "parents": [
            "physicians"
        ],
        "title": "Orthopedists"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "NO",
            "IE",
            "IT",
            "US",
            "CZ",
            "NZ",
            "AU",
            "GB",
            "BR",
            "FI",
            "SG",
            "ES"
        ],
        "alias": "orthotics",
        "parents": [
            "health"
        ],
        "title": "Orthotics"
    },
    {
        "alias": "osteopathicphysicians",
        "parents": [
            "physicians"
        ],
        "title": "Osteopathic Physicians"
    },
    {
        "country_whitelist": [
            "AU"
        ],
        "alias": "osteopaths",
        "parents": [
            "medcenters"
        ],
        "title": "Osteopaths"
    },
    {
        "alias": "othersalons",
        "parents": [
            "beautysvc"
        ],
        "title": "Nail Salons"
    },
    {
        "alias": "otologists",
        "parents": [
            "physicians"
        ],
        "title": "Otologists"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "ottomancuisine",
        "parents": [
            "turkish"
        ],
        "title": "Ottoman Cuisine"
    },
    {
        "alias": "outdoorfurniture",
        "parents": [
            "homeandgarden"
        ],
        "title": "Outdoor Furniture Stores"
    },
    {
        "alias": "outdoorgear",
        "parents": [
            "sportgoods"
        ],
        "title": "Outdoor Gear"
    },
    {
        "alias": "outdoormovies",
        "country_blacklist": [
            "PL"
        ],
        "parents": [
            "movietheaters"
        ],
        "title": "Outdoor Movies"
    },
    {
        "alias": "outlet_stores",
        "parents": [
            "shopping"
        ],
        "title": "Outlet Stores"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "oxygenbars",
        "parents": [
            "health"
        ],
        "title": "Oxygen Bars"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "oyakodon",
        "parents": [
            "donburi"
        ],
        "title": "Oyakodon"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "pachinko",
        "parents": [
            "arts"
        ],
        "title": "Pachinko"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "PT",
            "NO",
            "IE",
            "US",
            "NZ",
            "AU",
            "FI",
            "SG",
            "ES"
        ],
        "alias": "paddleboarding",
        "parents": [
            "active"
        ],
        "title": "Paddleboarding"
    },
    {
        "alias": "painmanagement",
        "parents": [
            "physicians"
        ],
        "title": "Pain Management"
    },
    {
        "country_whitelist": [
            "HK",
            "US"
        ],
        "alias": "paintandsip",
        "parents": [
            "arts"
        ],
        "title": "Paint & Sip"
    },
    {
        "alias": "paintball",
        "country_blacklist": [
            "SG"
        ],
        "parents": [
            "active"
        ],
        "title": "Paintball"
    },
    {
        "alias": "painters",
        "parents": [
            "homeservices"
        ],
        "title": "Painters"
    },
    {
        "alias": "paintstores",
        "country_blacklist": [
            "PT",
            "IE",
            "SG",
            "CA",
            "TR",
            "HK",
            "GB",
            "TW",
            "FI",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "homeandgarden"
        ],
        "title": "Paint Stores"
    },
    {
        "alias": "pakistani",
        "parents": [
            "restaurants"
        ],
        "title": "Pakistani"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "palatine",
        "parents": [
            "german"
        ],
        "title": "Palatine"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "panzerotti",
        "parents": [
            "food"
        ],
        "title": "Panzerotti"
    },
    {
        "alias": "parentingclasses",
        "parents": [
            "specialtyschools"
        ],
        "title": "Parenting Classes"
    },
    {
        "alias": "parking",
        "parents": [
            "auto"
        ],
        "title": "Parking"
    },
    {
        "alias": "parks",
        "parents": [
            "active"
        ],
        "title": "Parks"
    },
    {
        "country_whitelist": [
            "AU"
        ],
        "alias": "parma",
        "parents": [
            "restaurants"
        ],
        "title": "Parma"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "ES",
            "DE",
            "IE",
            "US"
        ],
        "alias": "partybikerentals",
        "parents": [
            "eventservices"
        ],
        "title": "Party Bike Rentals"
    },
    {
        "alias": "partybusrentals",
        "country_blacklist": [
            "FR",
            "PT",
            "CZ",
            "IE",
            "TW",
            "CA",
            "JP",
            "IT",
            "HK",
            "ES",
            "PH",
            "MY",
            "MX",
            "PL"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Party Bus Rentals"
    },
    {
        "alias": "partycharacters",
        "parents": [
            "eventservices"
        ],
        "title": "Party Characters"
    },
    {
        "alias": "partyequipmentrentals",
        "country_blacklist": [
            "CH",
            "CZ",
            "TW",
            "CA",
            "DE",
            "JP",
            "HK",
            "NZ",
            "AT",
            "FI"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Party Equipment Rentals"
    },
    {
        "alias": "partysupplies",
        "parents": [
            "eventservices"
        ],
        "title": "Party Supplies"
    },
    {
        "alias": "passportvisaservices",
        "parents": [
            "travelservices"
        ],
        "title": "Passport & Visa Services"
    },
    {
        "country_whitelist": [
            "CZ",
            "AR",
            "IT",
            "US",
            "CL"
        ],
        "alias": "pastashops",
        "parents": [
            "gourmet"
        ],
        "title": "Pasta Shops"
    },
    {
        "alias": "patentlaw",
        "parents": [
            "professional"
        ],
        "title": "Patent Law"
    },
    {
        "alias": "pathologists",
        "parents": [
            "physicians"
        ],
        "title": "Pathologists"
    },
    {
        "country_whitelist": [
            "BR",
            "IT",
            "US"
        ],
        "alias": "patiocoverings",
        "parents": [
            "homeservices"
        ],
        "title": "Patio Coverings"
    },
    {
        "alias": "pawn",
        "country_blacklist": [
            "TR",
            "BR"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Pawn Shops"
    },
    {
        "alias": "paydayloans",
        "country_blacklist": [
            "CH",
            "DK",
            "DE",
            "IT",
            "CZ",
            "NZ",
            "AT",
            "ES"
        ],
        "parents": [
            "financialservices"
        ],
        "title": "Check Cashing/Pay-day Loans"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "TR",
            "US",
            "CZ",
            "NZ",
            "AU",
            "SG"
        ],
        "alias": "payroll",
        "parents": [
            "professional"
        ],
        "title": "Payroll Services"
    },
    {
        "alias": "pediatric_dentists",
        "parents": [
            "dentists"
        ],
        "title": "Pediatric Dentists"
    },
    {
        "alias": "pediatricians",
        "parents": [
            "physicians"
        ],
        "title": "Pediatricians"
    },
    {
        "country_whitelist": [
            "CH",
            "DK",
            "NO",
            "DE",
            "US",
            "AT",
            "PH",
            "MY",
            "SE"
        ],
        "alias": "pedicabs",
        "parents": [
            "transport"
        ],
        "title": "Pedicabs"
    },
    {
        "country_whitelist": [
            "HK",
            "FR",
            "TW",
            "JP",
            "SG",
            "MY",
            "IT"
        ],
        "alias": "pekinese",
        "parents": [
            "chinese"
        ],
        "title": "Pekinese"
    },
    {
        "country_whitelist": [
            "ES",
            "DK",
            "NO",
            "DE",
            "JP",
            "CZ",
            "AT",
            "BR",
            "SE"
        ],
        "alias": "pensions",
        "parents": [
            "hotels"
        ],
        "title": "Pensions"
    },
    {
        "alias": "perfume",
        "country_blacklist": [
            "NL",
            "CA",
            "TR",
            "US",
            "BR",
            "FI",
            "SG",
            "PL"
        ],
        "parents": [
            "shopping",
            "beautysvc"
        ],
        "title": "Perfume"
    },
    {
        "alias": "periodontists",
        "parents": [
            "dentists"
        ],
        "title": "Periodontists"
    },
    {
        "alias": "permanentmakeup",
        "country_blacklist": [
            "DK",
            "NO",
            "IE",
            "CA",
            "NZ",
            "PL",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "parents": [
            "beautysvc"
        ],
        "title": "Permanent Makeup"
    },
    {
        "alias": "persian",
        "parents": [
            "restaurants"
        ],
        "title": "Persian/Iranian"
    },
    {
        "alias": "personal_injury",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "lawyers"
        ],
        "title": "Personal Injury Law"
    },
    {
        "alias": "personal_shopping",
        "country_blacklist": [
            "CZ",
            "BR"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Personal Shopping"
    },
    {
        "country_whitelist": [
            "CZ",
            "PT",
            "US"
        ],
        "alias": "personalassistants",
        "parents": [
            "professional"
        ],
        "title": "Personal Assistants"
    },
    {
        "country_whitelist": [
            "FR",
            "AU",
            "BR",
            "US"
        ],
        "alias": "personalcare",
        "parents": [
            "health"
        ],
        "title": "Personal Care Services"
    },
    {
        "alias": "personalchefs",
        "parents": [
            "eventservices"
        ],
        "title": "Personal Chefs"
    },
    {
        "alias": "peruvian",
        "country_blacklist": [
            "SG",
            "TR",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Peruvian"
    },
    {
        "alias": "pest_control",
        "parents": [
            "localservices"
        ],
        "title": "Pest Control"
    },
    {
        "alias": "pet_sitting",
        "parents": [
            "petservices"
        ],
        "title": "Pet Boarding/Pet Sitting"
    },
    {
        "alias": "pet_training",
        "parents": [
            "petservices"
        ],
        "title": "Pet Training"
    },
    {
        "alias": "petadoption",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "pets"
        ],
        "title": "Pet Adoption"
    },
    {
        "alias": "petbreeders",
        "country_blacklist": [
            "PT",
            "CL",
            "IE",
            "SG",
            "TR",
            "CZ",
            "NZ",
            "AR",
            "BR",
            "TW",
            "HK",
            "FI",
            "PH",
            "MY",
            "MX"
        ],
        "parents": [
            "petservices"
        ],
        "title": "Pet Breeders"
    },
    {
        "alias": "pets",
        "parents": [],
        "title": "Pets"
    },
    {
        "alias": "petservices",
        "parents": [
            "pets"
        ],
        "title": "Pet Services"
    },
    {
        "alias": "petstore",
        "parents": [
            "pets"
        ],
        "title": "Pet Stores"
    },
    {
        "country_whitelist": [
            "SE",
            "US"
        ],
        "alias": "pettransport",
        "parents": [
            "petservices"
        ],
        "title": "Pet Transportation"
    },
    {
        "country_whitelist": [
            "BR"
        ],
        "alias": "pfcomercial",
        "parents": [
            "restaurants"
        ],
        "title": "PF/Comercial"
    },
    {
        "alias": "pharmacy",
        "country_blacklist": [
            "FI",
            "US"
        ],
        "parents": [
            "health"
        ],
        "title": "Pharmacy"
    },
    {
        "alias": "phlebologists",
        "parents": [
            "physicians"
        ],
        "title": "Phlebologists"
    },
    {
        "alias": "photoboothrentals",
        "country_blacklist": [
            "HK",
            "AR",
            "CL",
            "FI",
            "JP",
            "MX"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Photo Booth Rentals"
    },
    {
        "alias": "photographers",
        "parents": [
            "eventservices"
        ],
        "title": "Photographers"
    },
    {
        "alias": "photographystores",
        "parents": [
            "shopping"
        ],
        "title": "Photography Stores & Services"
    },
    {
        "alias": "physicaltherapy",
        "parents": [
            "health"
        ],
        "title": "Physical Therapy"
    },
    {
        "alias": "physicians",
        "parents": [
            "health"
        ],
        "title": "Doctors"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "piadina",
        "parents": [
            "food"
        ],
        "title": "Piadina"
    },
    {
        "alias": "pianobars",
        "country_blacklist": [
            "ES",
            "CH",
            "IE",
            "CZ",
            "NZ",
            "AU",
            "AT",
            "BR",
            "FI",
            "SG",
            "PL"
        ],
        "parents": [
            "nightlife"
        ],
        "title": "Piano Bars"
    },
    {
        "alias": "pianoservices",
        "parents": [
            "musicinstrumentservices"
        ],
        "title": "Piano Services"
    },
    {
        "alias": "pianostores",
        "parents": [
            "musicinstrumentservices"
        ],
        "title": "Piano Stores"
    },
    {
        "country_whitelist": [
            "CH",
            "JP",
            "AT",
            "US",
            "DE"
        ],
        "alias": "pickyourown",
        "parents": [
            "farms"
        ],
        "title": "Pick Your Own Farms"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "piemonte",
        "parents": [
            "italian"
        ],
        "title": "Piemonte"
    },
    {
        "alias": "piercing",
        "parents": [
            "beautysvc"
        ],
        "title": "Piercing"
    },
    {
        "country_whitelist": [
            "PL"
        ],
        "alias": "pierogis",
        "parents": [
            "polish"
        ],
        "title": "Pierogis"
    },
    {
        "alias": "pilates",
        "parents": [
            "fitness"
        ],
        "title": "Pilates"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "pita",
        "parents": [
            "restaurants"
        ],
        "title": "Pita"
    },
    {
        "alias": "pizza",
        "parents": [
            "restaurants"
        ],
        "title": "Pizza"
    },
    {
        "alias": "placentaencapsulation",
        "country_blacklist": [
            "CZ",
            "FR",
            "CH",
            "AT",
            "DE",
            "TR",
            "PL"
        ],
        "parents": [
            "health"
        ],
        "title": "Placenta Encapsulations"
    },
    {
        "alias": "planetarium",
        "parents": [
            "arts"
        ],
        "title": "Planetarium"
    },
    {
        "alias": "playgrounds",
        "parents": [
            "active"
        ],
        "title": "Playgrounds"
    },
    {
        "alias": "plumbing",
        "parents": [
            "homeservices"
        ],
        "title": "Plumbing"
    },
    {
        "alias": "plus_size_fashion",
        "country_blacklist": [
            "CH",
            "CL",
            "IE",
            "JP",
            "CA",
            "TR",
            "HK",
            "AR",
            "AT",
            "SG",
            "MX",
            "PL",
            "GB"
        ],
        "parents": [
            "fashion"
        ],
        "title": "Plus Size Fashion"
    },
    {
        "alias": "podiatrists",
        "country_blacklist": [
            "FR"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Podiatrists"
    },
    {
        "alias": "poledancingclasses",
        "country_blacklist": [
            "ES",
            "BE",
            "CH",
            "PT",
            "CL",
            "CA",
            "TR",
            "AR",
            "AT",
            "IE",
            "MX",
            "PL",
            "GB"
        ],
        "parents": [
            "specialtyschools"
        ],
        "title": "Pole Dancing Classes"
    },
    {
        "alias": "policedepartments",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Police Departments"
    },
    {
        "alias": "polish",
        "country_blacklist": [
            "FI",
            "SG",
            "DK",
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Polish"
    },
    {
        "alias": "poolbilliards",
        "country_blacklist": [
            "ES",
            "CH",
            "NO",
            "DE",
            "CZ",
            "AT",
            "SE",
            "FI",
            "PL"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Pool & Billiards"
    },
    {
        "alias": "poolcleaners",
        "country_blacklist": [
            "DK",
            "NO"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Pool Cleaners"
    },
    {
        "alias": "poolhalls",
        "parents": [
            "nightlife"
        ],
        "title": "Pool Halls"
    },
    {
        "alias": "poolservice",
        "parents": [
            "homeservices"
        ],
        "title": "Pool & Hot Tub Service"
    },
    {
        "country_whitelist": [
            "JP",
            "GB",
            "US"
        ],
        "alias": "popcorn",
        "parents": [
            "gourmet"
        ],
        "title": "Popcorn Shops"
    },
    {
        "alias": "popupshops",
        "country_blacklist": [
            "PT"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Pop-up Shops"
    },
    {
        "alias": "portuguese",
        "country_blacklist": [
            "FI"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Portuguese"
    },
    {
        "alias": "postoffices",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Post Offices"
    },
    {
        "country_whitelist": [
            "CH",
            "AU",
            "AT",
            "DE"
        ],
        "alias": "potatoes",
        "parents": [
            "restaurants"
        ],
        "title": "Potatoes"
    },
    {
        "country_whitelist": [
            "CA",
            "US"
        ],
        "alias": "poutineries",
        "parents": [
            "restaurants"
        ],
        "title": "Poutineries"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "powdercoating",
        "parents": [
            "localservices"
        ],
        "title": "Powder Coating"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "NO",
            "IT",
            "US",
            "CZ",
            "NZ",
            "AU",
            "ES",
            "BR",
            "SE"
        ],
        "alias": "prenatal",
        "parents": [
            "health"
        ],
        "title": "Prenatal/Perinatal Care"
    },
    {
        "alias": "preschools",
        "country_blacklist": [
            "DK"
        ],
        "parents": [
            "education"
        ],
        "title": "Preschools"
    },
    {
        "alias": "pressurewashers",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Pressure Washers"
    },
    {
        "country_whitelist": [
            "DE",
            "PT",
            "US"
        ],
        "alias": "pretzels",
        "parents": [
            "food"
        ],
        "title": "Pretzels"
    },
    {
        "alias": "preventivemedicine",
        "parents": [
            "physicians"
        ],
        "title": "Preventive Medicine"
    },
    {
        "alias": "printmedia",
        "parents": [
            "massmedia"
        ],
        "title": "Print Media"
    },
    {
        "alias": "privateinvestigation",
        "parents": [
            "professional"
        ],
        "title": "Private Investigation"
    },
    {
        "alias": "privatejetcharter",
        "parents": [
            "transport"
        ],
        "title": "Private Jet Charter"
    },
    {
        "country_whitelist": [
            "PT",
            "NO",
            "CZ",
            "NZ",
            "AU",
            "BR",
            "MX",
            "SE"
        ],
        "alias": "privateschools",
        "parents": [
            "education"
        ],
        "title": "Private Schools"
    },
    {
        "alias": "privatetutors",
        "parents": [
            "education"
        ],
        "title": "Private Tutors"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "processservers",
        "parents": [
            "legalservices"
        ],
        "title": "Process Servers"
    },
    {
        "alias": "proctologist",
        "parents": [
            "physicians"
        ],
        "title": "Proctologists"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "US"
        ],
        "alias": "productdesign",
        "parents": [
            "professional"
        ],
        "title": "Product Design"
    },
    {
        "alias": "professional",
        "parents": [],
        "title": "Professional Services"
    },
    {
        "alias": "propane",
        "country_blacklist": [
            "CZ",
            "NZ",
            "AR",
            "MX"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Propane"
    },
    {
        "alias": "propertymgmt",
        "parents": [
            "realestate"
        ],
        "title": "Property Management"
    },
    {
        "country_whitelist": [
            "ES",
            "AU",
            "IT",
            "US"
        ],
        "alias": "prosthetics",
        "parents": [
            "health"
        ],
        "title": "Prosthetics"
    },
    {
        "country_whitelist": [
            "ES",
            "IT",
            "US"
        ],
        "alias": "prosthodontists",
        "parents": [
            "health"
        ],
        "title": "Prosthodontists"
    },
    {
        "country_whitelist": [
            "FR"
        ],
        "alias": "provencal",
        "parents": [
            "french"
        ],
        "title": "Provencal"
    },
    {
        "alias": "psychiatrists",
        "parents": [
            "physicians"
        ],
        "title": "Psychiatrists"
    },
    {
        "alias": "psychic_astrology",
        "parents": [
            "arts"
        ],
        "title": "Psychics & Astrologers"
    },
    {
        "country_whitelist": [
            "CZ",
            "FR"
        ],
        "alias": "psychoanalysts",
        "parents": [
            "c_and_mh"
        ],
        "title": "Psychoanalysts"
    },
    {
        "alias": "psychologists",
        "country_blacklist": [
            "HK",
            "GB",
            "PT",
            "IE",
            "JP",
            "SG",
            "PL"
        ],
        "parents": [
            "c_and_mh"
        ],
        "title": "Psychologists"
    },
    {
        "country_whitelist": [
            "FR",
            "CH",
            "DK",
            "NO",
            "DE",
            "CZ",
            "AT",
            "BR",
            "FI",
            "SG"
        ],
        "alias": "psychotherapists",
        "parents": [
            "c_and_mh"
        ],
        "title": "Psychotherapists"
    },
    {
        "country_whitelist": [
            "AU"
        ],
        "alias": "pubfood",
        "parents": [
            "restaurants"
        ],
        "title": "Pub Food"
    },
    {
        "alias": "publicplazas",
        "country_blacklist": [
            "BE",
            "NL",
            "CA",
            "US",
            "NZ",
            "AU",
            "GB",
            "BR",
            "IE"
        ],
        "parents": [
            "active"
        ],
        "title": "Public Plazas"
    },
    {
        "alias": "publicrelations",
        "parents": [
            "professional"
        ],
        "title": "Public Relations"
    },
    {
        "alias": "publicservicesgovt",
        "parents": [],
        "title": "Public Services & Government"
    },
    {
        "alias": "publictransport",
        "parents": [
            "transport"
        ],
        "title": "Public Transportation"
    },
    {
        "alias": "pubs",
        "parents": [
            "bars"
        ],
        "title": "Pubs"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "pueblan",
        "parents": [
            "mexican"
        ],
        "title": "Pueblan"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "puertorican",
        "parents": [
            "caribbean"
        ],
        "title": "Puerto Rican"
    },
    {
        "alias": "pulmonologist",
        "parents": [
            "physicians"
        ],
        "title": "Pulmonologist"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "pulquerias",
        "parents": [
            "bars"
        ],
        "title": "Pulquerias"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "pumpkinpatches",
        "parents": [
            "homeandgarden"
        ],
        "title": "Pumpkin Patches"
    },
    {
        "alias": "qigong",
        "parents": [
            "fitness"
        ],
        "title": "Qi Gong"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "NO",
            "US",
            "NZ",
            "AU",
            "BR",
            "SG",
            "SE"
        ],
        "alias": "races",
        "parents": [
            "active"
        ],
        "title": "Races & Competitions"
    },
    {
        "alias": "racetracks",
        "country_blacklist": [
            "CH",
            "AT",
            "BR",
            "IE",
            "CA",
            "DE",
            "SG"
        ],
        "parents": [
            "arts"
        ],
        "title": "Race Tracks"
    },
    {
        "alias": "radiologists",
        "parents": [
            "physicians"
        ],
        "title": "Radiologists"
    },
    {
        "alias": "radiostations",
        "parents": [
            "massmedia"
        ],
        "title": "Radio Stations"
    },
    {
        "alias": "rafting",
        "parents": [
            "active"
        ],
        "title": "Rafting/Kayaking"
    },
    {
        "alias": "ramen",
        "parents": [
            "japanese"
        ],
        "title": "Ramen"
    },
    {
        "country_whitelist": [
            "ES",
            "AR",
            "MX",
            "US",
            "CL"
        ],
        "alias": "ranches",
        "parents": [
            "farms"
        ],
        "title": "Ranches"
    },
    {
        "alias": "raw_food",
        "parents": [
            "restaurants"
        ],
        "title": "Live/Raw Food"
    },
    {
        "alias": "realestate",
        "parents": [
            "homeservices"
        ],
        "title": "Real Estate"
    },
    {
        "alias": "realestateagents",
        "parents": [
            "realestate"
        ],
        "title": "Real Estate Agents"
    },
    {
        "alias": "realestatelawyers",
        "parents": [
            "lawyers"
        ],
        "title": "Real Estate Law"
    },
    {
        "alias": "realestatesvcs",
        "country_blacklist": [
            "CZ",
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "realestate"
        ],
        "title": "Real Estate Services"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT",
            "PT"
        ],
        "alias": "record_labels",
        "parents": [
            "localservices"
        ],
        "title": "Record Labels"
    },
    {
        "alias": "recording_studios",
        "parents": [
            "localservices"
        ],
        "title": "Recording & Rehearsal Studios"
    },
    {
        "alias": "recreation",
        "parents": [
            "active"
        ],
        "title": "Recreation Centers"
    },
    {
        "alias": "recyclingcenter",
        "parents": [
            "localservices"
        ],
        "title": "Recycling Center"
    },
    {
        "alias": "refinishing",
        "parents": [
            "homeservices"
        ],
        "title": "Refinishing Services"
    },
    {
        "alias": "reflexology",
        "country_blacklist": [
            "DK",
            "SE",
            "NO",
            "FI",
            "TR",
            "ES",
            "PL"
        ],
        "parents": [
            "health"
        ],
        "title": "Reflexology"
    },
    {
        "country_whitelist": [
            "BR",
            "IT",
            "US",
            "PT"
        ],
        "alias": "registrationservices",
        "parents": [
            "auto"
        ],
        "title": "Registration Services"
    },
    {
        "country_whitelist": [
            "CH",
            "DK",
            "PT",
            "DE",
            "IT",
            "CZ",
            "AT",
            "FI"
        ],
        "alias": "registry_office",
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Registry Office"
    },
    {
        "country_whitelist": [
            "DE",
            "DK",
            "PT",
            "CL",
            "NO",
            "JP",
            "IT",
            "US",
            "CZ",
            "AR",
            "ES",
            "BR",
            "FI",
            "MX",
            "SE"
        ],
        "alias": "rehabilitation_center",
        "parents": [
            "health"
        ],
        "title": "Rehabilitation Center"
    },
    {
        "alias": "reiki",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "health"
        ],
        "title": "Reiki"
    },
    {
        "alias": "religiousorgs",
        "parents": [],
        "title": "Religious Organizations"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "CL",
            "NO",
            "US",
            "CZ",
            "NZ",
            "AR",
            "AU",
            "BR",
            "PH",
            "MY",
            "MX",
            "ES"
        ],
        "alias": "religiousschools",
        "parents": [
            "education"
        ],
        "title": "Religious Schools"
    },
    {
        "country_whitelist": [
            "AU",
            "JP",
            "US"
        ],
        "alias": "rentfurniture",
        "parents": [
            "localservices"
        ],
        "title": "Furniture Rental"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "DK",
            "NO",
            "DE",
            "JP",
            "IT",
            "US",
            "ES",
            "SE"
        ],
        "alias": "reptileshops",
        "parents": [
            "petstore"
        ],
        "title": "Reptile Shops"
    },
    {
        "country_whitelist": [
            "SG",
            "IT",
            "ES"
        ],
        "alias": "residences",
        "parents": [
            "hotels"
        ],
        "title": "Residences"
    },
    {
        "alias": "resorts",
        "parents": [
            "hotelstravel"
        ],
        "title": "Resorts"
    },
    {
        "alias": "restaurants",
        "parents": [],
        "title": "Restaurants"
    },
    {
        "alias": "reststops",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "hotels"
        ],
        "title": "Rest Stops"
    },
    {
        "alias": "retirement_homes",
        "parents": [
            "health"
        ],
        "title": "Retirement Homes"
    },
    {
        "alias": "reupholstery",
        "parents": [
            "localservices"
        ],
        "title": "Furniture Reupholstery"
    },
    {
        "alias": "rhematologists",
        "country_blacklist": [
            "BE",
            "NL",
            "PT",
            "IE",
            "JP",
            "CA",
            "TR",
            "HK",
            "NZ",
            "AU",
            "GB",
            "TW",
            "FI",
            "SG",
            "PL"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Rheumatologists"
    },
    {
        "country_whitelist": [
            "DE"
        ],
        "alias": "rhinelandian",
        "parents": [
            "german"
        ],
        "title": "Rhinelandian"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "ribatejo",
        "parents": [
            "portuguese"
        ],
        "title": "Ribatejo"
    },
    {
        "country_whitelist": [
            "JP",
            "TR"
        ],
        "alias": "riceshop",
        "parents": [
            "restaurants"
        ],
        "title": "Rice"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "CL",
            "CA",
            "JP",
            "IT",
            "US",
            "AR",
            "AU",
            "MX",
            "ES"
        ],
        "alias": "roadsideassist",
        "parents": [
            "auto"
        ],
        "title": "Roadside Assistance"
    },
    {
        "country_whitelist": [
            "HK",
            "JP",
            "TW"
        ],
        "alias": "robatayaki",
        "parents": [
            "japanese"
        ],
        "title": "Robatayaki"
    },
    {
        "alias": "rock_climbing",
        "country_blacklist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "IE",
            "TW",
            "CA",
            "TR",
            "IT",
            "HK",
            "GB",
            "SG",
            "PH",
            "MY"
        ],
        "parents": [
            "active"
        ],
        "title": "Rock Climbing"
    },
    {
        "country_whitelist": [
            "AR",
            "BR",
            "PT"
        ],
        "alias": "rodizios",
        "parents": [
            "brazilian"
        ],
        "title": "Rodizios"
    },
    {
        "country_whitelist": [
            "CA",
            "PT",
            "US"
        ],
        "alias": "rolfing",
        "parents": [
            "beautysvc"
        ],
        "title": "Rolfing"
    },
    {
        "country_whitelist": [
            "JP",
            "IT"
        ],
        "alias": "roman",
        "parents": [
            "italian"
        ],
        "title": "Roman"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CZ"
        ],
        "alias": "romanian",
        "parents": [
            "restaurants"
        ],
        "title": "Romanian"
    },
    {
        "alias": "roofing",
        "parents": [
            "homeservices"
        ],
        "title": "Roofing"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "roofinspectors",
        "parents": [
            "homeservices"
        ],
        "title": "Roof Inspectors"
    },
    {
        "country_whitelist": [
            "FR",
            "CL",
            "IT",
            "NZ",
            "AR",
            "AU",
            "BR",
            "MX",
            "ES"
        ],
        "alias": "rotisserie_chicken",
        "parents": [
            "restaurants"
        ],
        "title": "Rotisserie Chicken"
    },
    {
        "alias": "rugs",
        "country_blacklist": [
            "CH",
            "CZ",
            "CA",
            "DE",
            "JP",
            "HK",
            "AT",
            "IE",
            "PL"
        ],
        "parents": [
            "homeandgarden"
        ],
        "title": "Rugs"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT"
        ],
        "alias": "rumanian",
        "parents": [
            "restaurants"
        ],
        "title": "Rumanian"
    },
    {
        "alias": "russian",
        "parents": [
            "restaurants"
        ],
        "title": "Russian"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "NO",
            "CA",
            "IT",
            "US",
            "ES",
            "BR",
            "FI",
            "SE"
        ],
        "alias": "rv_dealers",
        "parents": [
            "auto"
        ],
        "title": "RV Dealers"
    },
    {
        "country_whitelist": [
            "ES",
            "FR",
            "NO",
            "DE",
            "TR",
            "IT",
            "US",
            "CZ",
            "SE",
            "FI",
            "PL"
        ],
        "alias": "rvparks",
        "parents": [
            "hotelstravel"
        ],
        "title": "RV Parks"
    },
    {
        "alias": "rvrental",
        "country_blacklist": [
            "SG",
            "DK",
            "BR"
        ],
        "parents": [
            "hotelstravel"
        ],
        "title": "RV Rental"
    },
    {
        "country_whitelist": [
            "CA",
            "US"
        ],
        "alias": "rvrepair",
        "parents": [
            "auto"
        ],
        "title": "RV Repair"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "ryokan",
        "parents": [
            "hotels"
        ],
        "title": "Ryokan"
    },
    {
        "alias": "sailing",
        "country_blacklist": [
            "TR",
            "PL",
            "US"
        ],
        "parents": [
            "active"
        ],
        "title": "Sailing"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "sakebars",
        "parents": [
            "bars"
        ],
        "title": "Sake Bars"
    },
    {
        "alias": "salad",
        "parents": [
            "restaurants"
        ],
        "title": "Salad"
    },
    {
        "country_whitelist": [
            "AR",
            "PT",
            "CL",
            "IT",
            "ES",
            "MX"
        ],
        "alias": "salumerie",
        "parents": [
            "food"
        ],
        "title": "Salumerie"
    },
    {
        "country_whitelist": [
            "CA",
            "US"
        ],
        "alias": "salvadoran",
        "parents": [
            "latin"
        ],
        "title": "Salvadoran"
    },
    {
        "country_whitelist": [
            "FI",
            "IT",
            "BR",
            "SE"
        ],
        "alias": "sambaschools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Samba Schools"
    },
    {
        "country_whitelist": [
            "BE",
            "CH",
            "NL",
            "DE",
            "IT",
            "US",
            "AT",
            "BR",
            "ES"
        ],
        "alias": "sandblasting",
        "parents": [
            "localservices"
        ],
        "title": "Sandblasting"
    },
    {
        "alias": "sandwiches",
        "parents": [
            "restaurants"
        ],
        "title": "Sandwiches"
    },
    {
        "country_whitelist": [
            "IT",
            "US"
        ],
        "alias": "sardinian",
        "parents": [
            "italian"
        ],
        "title": "Sardinian"
    },
    {
        "alias": "saunas",
        "country_blacklist": [
            "NL",
            "MY",
            "CA",
            "NZ",
            "AU",
            "ES",
            "BR",
            "PH",
            "SG",
            "PL"
        ],
        "parents": [
            "health"
        ],
        "title": "Saunas"
    },
    {
        "alias": "scandinavian",
        "country_blacklist": [
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Scandinavian"
    },
    {
        "country_whitelist": [
            "FI",
            "DK",
            "SE",
            "NO"
        ],
        "alias": "scandinaviandesign",
        "parents": [
            "shopping"
        ],
        "title": "Scandinavian Design"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "scavengerhunts",
        "parents": [
            "active"
        ],
        "title": "Scavenger Hunts"
    },
    {
        "country_whitelist": [
            "CH",
            "AT",
            "CA",
            "DE",
            "IE",
            "US",
            "GB"
        ],
        "alias": "scottish",
        "parents": [
            "restaurants"
        ],
        "title": "Scottish"
    },
    {
        "alias": "screen_printing_tshirt_printing",
        "country_blacklist": [
            "HK",
            "IE",
            "TW",
            "CA",
            "TR",
            "IT",
            "CZ",
            "NZ",
            "GB",
            "FI",
            "SG",
            "PL"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Screen Printing/T-Shirt Printing"
    },
    {
        "alias": "screenprinting",
        "parents": [
            "localservices"
        ],
        "title": "Screen Printing"
    },
    {
        "alias": "scuba",
        "parents": [
            "diving"
        ],
        "title": "Scuba Diving"
    },
    {
        "alias": "seafood",
        "parents": [
            "restaurants"
        ],
        "title": "Seafood"
    },
    {
        "alias": "seafoodmarkets",
        "parents": [
            "gourmet"
        ],
        "title": "Seafood Markets"
    },
    {
        "alias": "seasonaldecorservices",
        "country_blacklist": [
            "BE",
            "FR",
            "CH",
            "NL",
            "DK",
            "NO",
            "JP",
            "DE",
            "TR",
            "IT",
            "AT"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Holiday Decorating Services"
    },
    {
        "alias": "security",
        "country_blacklist": [
            "BE",
            "CA",
            "NZ",
            "BR"
        ],
        "parents": [
            "professional"
        ],
        "title": "Security Services"
    },
    {
        "alias": "securitysystems",
        "parents": [
            "homeservices"
        ],
        "title": "Security Systems"
    },
    {
        "alias": "selfstorage",
        "parents": [
            "localservices"
        ],
        "title": "Self Storage"
    },
    {
        "country_whitelist": [
            "BE",
            "CA",
            "FR",
            "US",
            "IT"
        ],
        "alias": "senegalese",
        "parents": [
            "african"
        ],
        "title": "Senegalese"
    },
    {
        "country_whitelist": [
            "CA",
            "US"
        ],
        "alias": "septicservices",
        "parents": [
            "localservices"
        ],
        "title": "Septic Services"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "CL",
            "DE",
            "IT",
            "PL",
            "CZ",
            "AR",
            "AT",
            "SE"
        ],
        "alias": "serbocroatian",
        "parents": [
            "restaurants"
        ],
        "title": "Serbo Croatian"
    },
    {
        "alias": "servicestations",
        "parents": [
            "auto"
        ],
        "title": "Gas & Service Stations"
    },
    {
        "alias": "sessionphotography",
        "parents": [
            "photographers"
        ],
        "title": "Session Photography"
    },
    {
        "alias": "sewingalterations",
        "parents": [
            "localservices"
        ],
        "title": "Sewing & Alterations"
    },
    {
        "alias": "sextherapists",
        "parents": [
            "c_and_mh"
        ],
        "title": "Sex Therapists"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "TW",
            "JP",
            "IT",
            "US",
            "HK",
            "AU",
            "MY",
            "SG",
            "SE"
        ],
        "alias": "shanghainese",
        "parents": [
            "chinese"
        ],
        "title": "Shanghainese"
    },
    {
        "alias": "sharedofficespaces",
        "parents": [
            "realestate"
        ],
        "title": "Shared Office Spaces"
    },
    {
        "country_whitelist": [
            "DK",
            "BR",
            "NO",
            "PH",
            "TR",
            "SE"
        ],
        "alias": "sharedtaxis",
        "parents": [
            "transport"
        ],
        "title": "Shared Taxis"
    },
    {
        "country_whitelist": [
            "CL",
            "TW",
            "JP",
            "IT",
            "US",
            "CZ",
            "AR",
            "SG",
            "MX"
        ],
        "alias": "shavedice",
        "parents": [
            "food"
        ],
        "title": "Shaved Ice"
    },
    {
        "alias": "shipping_centers",
        "country_blacklist": [
            "SE",
            "NO"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Shipping Centers"
    },
    {
        "alias": "shoerepair",
        "parents": [
            "localservices"
        ],
        "title": "Shoe Repair"
    },
    {
        "alias": "shoes",
        "parents": [
            "fashion"
        ],
        "title": "Shoe Stores"
    },
    {
        "alias": "shoeshine",
        "country_blacklist": [
            "BE",
            "NL"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Shoe Shine"
    },
    {
        "alias": "shopping",
        "parents": [],
        "title": "Shopping"
    },
    {
        "alias": "shoppingcenters",
        "parents": [
            "shopping"
        ],
        "title": "Shopping Centers"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "shredding",
        "parents": [
            "professional"
        ],
        "title": "Shredding Services"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "shrines",
        "parents": [
            "religiousorgs"
        ],
        "title": "Shrines"
    },
    {
        "alias": "shutters",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Shutters"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "sicilian",
        "parents": [
            "italian"
        ],
        "title": "Sicilian"
    },
    {
        "country_whitelist": [
            "DK",
            "PT",
            "NO",
            "CL",
            "AR",
            "ES",
            "MX",
            "SE"
        ],
        "alias": "signature_cuisine",
        "parents": [
            "restaurants"
        ],
        "title": "Signature Cuisine"
    },
    {
        "alias": "signmaking",
        "country_blacklist": [
            "CH",
            "NL",
            "PT",
            "CZ",
            "JP",
            "CA",
            "DE",
            "TR",
            "HK",
            "AU",
            "AT",
            "TW",
            "IE",
            "GB"
        ],
        "parents": [
            "professional"
        ],
        "title": "Signmaking"
    },
    {
        "alias": "silentdisco",
        "country_blacklist": [
            "JP"
        ],
        "parents": [
            "eventservices"
        ],
        "title": "Silent Disco"
    },
    {
        "alias": "singaporean",
        "country_blacklist": [
            "CZ",
            "DK",
            "PT",
            "FI",
            "TR",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Singaporean"
    },
    {
        "alias": "skate_parks",
        "parents": [
            "parks"
        ],
        "title": "Skate Parks"
    },
    {
        "alias": "skateshops",
        "parents": [
            "sportgoods"
        ],
        "title": "Skate Shops"
    },
    {
        "alias": "skatingrinks",
        "parents": [
            "active"
        ],
        "title": "Skating Rinks"
    },
    {
        "country_whitelist": [
            "ES",
            "CH",
            "DK",
            "PT",
            "CL",
            "CA",
            "DE",
            "JP",
            "CZ",
            "NZ",
            "AR",
            "AT",
            "FI",
            "NO",
            "SE"
        ],
        "alias": "skiing",
        "parents": [
            "active"
        ],
        "title": "Skiing"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "skillednursing",
        "parents": [
            "health"
        ],
        "title": "Skilled Nursing"
    },
    {
        "alias": "skincare",
        "parents": [
            "beautysvc"
        ],
        "title": "Skin Care"
    },
    {
        "alias": "skiresorts",
        "country_blacklist": [
            "SG",
            "DK",
            "BR",
            "MX"
        ],
        "parents": [
            "hotelstravel"
        ],
        "title": "Ski Resorts"
    },
    {
        "alias": "skischools",
        "parents": [
            "specialtyschools"
        ],
        "title": "Ski Schools"
    },
    {
        "alias": "skishops",
        "country_blacklist": [
            "DK",
            "PT",
            "TW",
            "TR",
            "HK",
            "MY",
            "BR",
            "PH",
            "SG",
            "MX"
        ],
        "parents": [
            "sportgoods"
        ],
        "title": "Ski & Snowboard Shops"
    },
    {
        "alias": "skydiving",
        "parents": [
            "active"
        ],
        "title": "Skydiving"
    },
    {
        "country_whitelist": [
            "CH",
            "PT",
            "NO",
            "CA",
            "DE",
            "TR",
            "IT",
            "US",
            "CZ",
            "NZ",
            "AT",
            "FI"
        ],
        "alias": "sledding",
        "parents": [
            "active"
        ],
        "title": "Sledding"
    },
    {
        "alias": "sleepspecialists",
        "parents": [
            "health"
        ],
        "title": "Sleep Specialists"
    },
    {
        "country_whitelist": [
            "AU",
            "PT"
        ],
        "alias": "sleepwear",
        "parents": [
            "fashion"
        ],
        "title": "Sleepwear"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CA",
            "IT",
            "US",
            "CZ",
            "AU",
            "GB",
            "IE",
            "PL"
        ],
        "alias": "slovakian",
        "parents": [
            "restaurants"
        ],
        "title": "Slovakian"
    },
    {
        "alias": "smog_check_stations",
        "country_blacklist": [
            "FI",
            "DK",
            "SE",
            "NO"
        ],
        "parents": [
            "auto"
        ],
        "title": "Smog Check Stations"
    },
    {
        "alias": "snorkeling",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "active"
        ],
        "title": "Snorkeling"
    },
    {
        "alias": "snowremoval",
        "country_blacklist": [
            "HK",
            "NZ",
            "MX",
            "BR"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Snow Removal"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "soba",
        "parents": [
            "japanese"
        ],
        "title": "Soba"
    },
    {
        "alias": "social_clubs",
        "parents": [
            "arts"
        ],
        "title": "Social Clubs"
    },
    {
        "alias": "softwaredevelopment",
        "parents": [
            "professional"
        ],
        "title": "Software Development"
    },
    {
        "alias": "solarinstallation",
        "parents": [
            "homeservices"
        ],
        "title": "Solar Installation"
    },
    {
        "country_whitelist": [
            "ES",
            "NL",
            "NO",
            "CA",
            "US",
            "GB",
            "SE",
            "IE",
            "PL"
        ],
        "alias": "soulfood",
        "parents": [
            "restaurants"
        ],
        "title": "Soul Food"
    },
    {
        "alias": "soup",
        "parents": [
            "restaurants"
        ],
        "title": "Soup"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "AU",
            "CA",
            "IT",
            "US"
        ],
        "alias": "southafrican",
        "parents": [
            "african"
        ],
        "title": "South African"
    },
    {
        "country_whitelist": [
            "NL",
            "CA",
            "TR",
            "US",
            "PL",
            "NZ",
            "GB",
            "IE",
            "SE"
        ],
        "alias": "southern",
        "parents": [
            "restaurants"
        ],
        "title": "Southern"
    },
    {
        "alias": "souvenirs",
        "country_blacklist": [
            "CA",
            "SG"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Souvenir Shops"
    },
    {
        "alias": "spanish",
        "parents": [
            "restaurants"
        ],
        "title": "Spanish"
    },
    {
        "alias": "spas",
        "parents": [
            "beautysvc"
        ],
        "title": "Day Spas"
    },
    {
        "country_whitelist": [
            "DK",
            "PT"
        ],
        "alias": "specialbikes",
        "parents": [
            "bicycles"
        ],
        "title": "Special Bikes"
    },
    {
        "alias": "specialed",
        "country_blacklist": [
            "FI"
        ],
        "parents": [
            "education"
        ],
        "title": "Special Education"
    },
    {
        "alias": "specialtyschools",
        "parents": [
            "education"
        ],
        "title": "Specialty Schools"
    },
    {
        "alias": "speech_therapists",
        "parents": [
            "health"
        ],
        "title": "Speech Therapists"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "NL",
            "DK",
            "NO",
            "DE",
            "IT",
            "US",
            "ES"
        ],
        "alias": "spermclinic",
        "parents": [
            "health"
        ],
        "title": "Sperm Clinic"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "spinesurgeons",
        "parents": [
            "physicians"
        ],
        "title": "Spine Surgeons"
    },
    {
        "country_whitelist": [
            "BR"
        ],
        "alias": "spiritism",
        "parents": [
            "religiousorgs"
        ],
        "title": "Spiritism"
    },
    {
        "alias": "spiritual_shop",
        "parents": [
            "shopping"
        ],
        "title": "Spiritual Shop"
    },
    {
        "country_whitelist": [
            "CZ",
            "AU",
            "PT",
            "NO"
        ],
        "alias": "sport_equipment_hire",
        "parents": [
            "active"
        ],
        "title": "Sport Equipment Hire"
    },
    {
        "alias": "sportgoods",
        "parents": [
            "shopping"
        ],
        "title": "Sporting Goods"
    },
    {
        "alias": "sports_clubs",
        "parents": [
            "active"
        ],
        "title": "Sports Clubs"
    },
    {
        "alias": "sportsbars",
        "country_blacklist": [
            "CH",
            "AT"
        ],
        "parents": [
            "bars"
        ],
        "title": "Sports Bars"
    },
    {
        "alias": "sportsmed",
        "parents": [
            "physicians"
        ],
        "title": "Sports Medicine"
    },
    {
        "country_whitelist": [
            "NZ",
            "SG",
            "IT",
            "US"
        ],
        "alias": "sportspsychologists",
        "parents": [
            "c_and_mh"
        ],
        "title": "Sports Psychologists"
    },
    {
        "alias": "sportsteams",
        "parents": [
            "arts"
        ],
        "title": "Professional Sports Teams"
    },
    {
        "alias": "sportswear",
        "parents": [
            "sportgoods",
            "fashion"
        ],
        "title": "Sports Wear"
    },
    {
        "alias": "spraytanning",
        "country_blacklist": [
            "CA",
            "IE",
            "BR",
            "PL",
            "SE"
        ],
        "parents": [
            "tanning"
        ],
        "title": "Spray Tanning"
    },
    {
        "alias": "squash",
        "country_blacklist": [
            "NZ",
            "SG",
            "BR",
            "PT"
        ],
        "parents": [
            "active"
        ],
        "title": "Squash"
    },
    {
        "alias": "srilankan",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Sri Lankan"
    },
    {
        "alias": "stadiumsarenas",
        "parents": [
            "arts"
        ],
        "title": "Stadiums & Arenas"
    },
    {
        "alias": "stationery",
        "parents": [
            "artsandcrafts",
            "flowers",
            "eventservices"
        ],
        "title": "Cards & Stationery"
    },
    {
        "alias": "steak",
        "parents": [
            "restaurants"
        ],
        "title": "Steakhouses"
    },
    {
        "alias": "stereo_installation",
        "country_blacklist": [
            "CH",
            "AT",
            "DK"
        ],
        "parents": [
            "auto"
        ],
        "title": "Car Stereo Installation"
    },
    {
        "country_whitelist": [
            "CZ",
            "PT"
        ],
        "alias": "stockings",
        "parents": [
            "fashion"
        ],
        "title": "Stockings"
    },
    {
        "alias": "streetart",
        "country_blacklist": [
            "BE",
            "FR",
            "CH",
            "NL",
            "IE",
            "SG",
            "CA",
            "TR",
            "US",
            "AT",
            "FI",
            "MY",
            "GB"
        ],
        "parents": [
            "arts"
        ],
        "title": "Street Art"
    },
    {
        "alias": "streetvendors",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "food"
        ],
        "title": "Street Vendors"
    },
    {
        "alias": "structuralengineers",
        "parents": [
            "homeservices"
        ],
        "title": "Structural Engineers"
    },
    {
        "alias": "stucco",
        "parents": [
            "homeservices"
        ],
        "title": "Stucco Services"
    },
    {
        "country_whitelist": [
            "BE",
            "NL",
            "US"
        ],
        "alias": "studiotaping",
        "parents": [
            "arts"
        ],
        "title": "Studio Taping"
    },
    {
        "country_whitelist": [
            "BE",
            "FR"
        ],
        "alias": "sud_ouest",
        "parents": [
            "restaurants"
        ],
        "title": "French Southwest"
    },
    {
        "country_whitelist": [
            "CH",
            "DK",
            "NO",
            "DE",
            "US",
            "CZ",
            "AT",
            "FI"
        ],
        "alias": "sugaring",
        "parents": [
            "hairremoval"
        ],
        "title": "Sugaring"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "sukiyaki",
        "parents": [
            "japanese"
        ],
        "title": "Sukiyaki"
    },
    {
        "alias": "summer_camps",
        "parents": [
            "active"
        ],
        "title": "Summer Camps"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "supperclubs",
        "parents": [
            "restaurants"
        ],
        "title": "Supper Clubs"
    },
    {
        "country_whitelist": [
            "FR",
            "NL",
            "DK",
            "PT",
            "CL",
            "DE",
            "JP",
            "IT",
            "US",
            "NZ",
            "ES",
            "BR",
            "MX",
            "SE"
        ],
        "alias": "surfing",
        "parents": [
            "active"
        ],
        "title": "Surfing"
    },
    {
        "country_whitelist": [
            "NZ",
            "AU",
            "BR",
            "PT"
        ],
        "alias": "surflifesaving",
        "parents": [
            "active"
        ],
        "title": "Surf Lifesaving"
    },
    {
        "alias": "surfshop",
        "country_blacklist": [
            "BE",
            "FR",
            "NL",
            "NO",
            "IE",
            "CA",
            "CZ",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "parents": [
            "fashion"
        ],
        "title": "Surf Shop"
    },
    {
        "alias": "surgeons",
        "country_blacklist": [
            "FR",
            "IE",
            "JP",
            "CA",
            "TR",
            "HK",
            "NZ",
            "AU",
            "GB",
            "TW",
            "FI",
            "SG"
        ],
        "parents": [
            "physicians"
        ],
        "title": "Surgeons"
    },
    {
        "alias": "sushi",
        "parents": [
            "restaurants"
        ],
        "title": "Sushi Bars"
    },
    {
        "country_whitelist": [
            "CH",
            "DE",
            "AT"
        ],
        "alias": "swabian",
        "parents": [
            "restaurants"
        ],
        "title": "Swabian"
    },
    {
        "country_whitelist": [
            "SE"
        ],
        "alias": "swedish",
        "parents": [
            "restaurants"
        ],
        "title": "Swedish"
    },
    {
        "alias": "swimminglessons",
        "parents": [
            "specialtyschools",
            "fitness"
        ],
        "title": "Swimming Lessons/Schools"
    },
    {
        "alias": "swimmingpools",
        "parents": [
            "active"
        ],
        "title": "Swimming Pools"
    },
    {
        "alias": "swimwear",
        "parents": [
            "fashion"
        ],
        "title": "Swimwear"
    },
    {
        "country_whitelist": [
            "CZ",
            "CH",
            "ES",
            "CL",
            "DE",
            "MX",
            "AR"
        ],
        "alias": "swissfood",
        "parents": [
            "restaurants"
        ],
        "title": "Swiss Food"
    },
    {
        "alias": "synagogues",
        "parents": [
            "religiousorgs"
        ],
        "title": "Synagogues"
    },
    {
        "alias": "syrian",
        "parents": [
            "restaurants"
        ],
        "title": "Syrian"
    },
    {
        "country_whitelist": [
            "FR",
            "IE",
            "TW",
            "JP",
            "US",
            "HK",
            "NZ",
            "AU",
            "GB",
            "SG",
            "MY"
        ],
        "alias": "szechuan",
        "parents": [
            "chinese"
        ],
        "title": "Szechuan"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "IT",
            "ES",
            "CZ"
        ],
        "alias": "tabac",
        "parents": [
            "bars"
        ],
        "title": "Tabac"
    },
    {
        "country_whitelist": [
            "TR",
            "ES",
            "PT"
        ],
        "alias": "tabernas",
        "parents": [
            "restaurants"
        ],
        "title": "Tabernas"
    },
    {
        "country_whitelist": [
            "ES",
            "AR",
            "MX",
            "PT",
            "CL"
        ],
        "alias": "tablaoflamenco",
        "parents": [
            "arts"
        ],
        "title": "Tablao Flamenco"
    },
    {
        "alias": "tabletopgames",
        "parents": [
            "shopping"
        ],
        "title": "Tabletop Games"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "PT",
            "DE",
            "CZ",
            "AT",
            "BR"
        ],
        "alias": "tableware",
        "parents": [
            "homeandgarden"
        ],
        "title": "Tableware"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "tacos",
        "parents": [
            "mexican"
        ],
        "title": "Tacos"
    },
    {
        "alias": "taichi",
        "parents": [
            "fitness"
        ],
        "title": "Tai Chi"
    },
    {
        "alias": "taiwanese",
        "country_blacklist": [
            "CZ",
            "TR",
            "ES",
            "PT",
            "FI"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Taiwanese"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "taiyaki",
        "parents": [
            "jpsweets"
        ],
        "title": "Taiyaki"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "takoyaki",
        "parents": [
            "japanese"
        ],
        "title": "Takoyaki"
    },
    {
        "alias": "talentagencies",
        "country_blacklist": [
            "ES",
            "CH",
            "CL",
            "IE",
            "CA",
            "TR",
            "CZ",
            "NZ",
            "AU",
            "AT",
            "HK",
            "SG",
            "PL",
            "GB"
        ],
        "parents": [
            "professional"
        ],
        "title": "Talent Agencies"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "tamales",
        "parents": [
            "mexican"
        ],
        "title": "Tamales"
    },
    {
        "alias": "tanning",
        "parents": [
            "beautysvc"
        ],
        "title": "Tanning"
    },
    {
        "alias": "tanningbeds",
        "country_blacklist": [
            "FI",
            "BR",
            "PL",
            "SE"
        ],
        "parents": [
            "tanning"
        ],
        "title": "Tanning Beds"
    },
    {
        "country_whitelist": [
            "TW"
        ],
        "alias": "taoisttemples",
        "parents": [
            "religiousorgs"
        ],
        "title": "Taoist Temples"
    },
    {
        "alias": "tapas",
        "country_blacklist": [
            "CZ",
            "AU",
            "SG",
            "FI"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Tapas Bars"
    },
    {
        "alias": "tapasmallplates",
        "parents": [
            "restaurants"
        ],
        "title": "Tapas/Small Plates"
    },
    {
        "alias": "tastingclasses",
        "parents": [
            "education"
        ],
        "title": "Tasting Classes"
    },
    {
        "alias": "tattoo",
        "parents": [
            "beautysvc"
        ],
        "title": "Tattoo"
    },
    {
        "alias": "tattooremoval",
        "parents": [
            "physicians"
        ],
        "title": "Tattoo Removal"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "tavolacalda",
        "parents": [
            "restaurants"
        ],
        "title": "Tavola Calda"
    },
    {
        "alias": "taxidermy",
        "country_blacklist": [
            "NL",
            "DK",
            "NO",
            "IE",
            "CA",
            "CZ",
            "NZ",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "parents": [
            "professional"
        ],
        "title": "Taxidermy"
    },
    {
        "alias": "taxis",
        "parents": [
            "transport"
        ],
        "title": "Taxis"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "DE",
            "US",
            "CZ",
            "AU",
            "BR",
            "SG"
        ],
        "alias": "taxlaw",
        "parents": [
            "lawyers"
        ],
        "title": "Tax Law"
    },
    {
        "alias": "taxoffice",
        "country_blacklist": [
            "ES",
            "CA",
            "SG",
            "PL",
            "US"
        ],
        "parents": [
            "publicservicesgovt"
        ],
        "title": "Tax Office"
    },
    {
        "alias": "taxservices",
        "parents": [
            "financialservices"
        ],
        "title": "Tax Services"
    },
    {
        "alias": "tcm",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "health"
        ],
        "title": "Traditional Chinese Medicine"
    },
    {
        "alias": "tea",
        "parents": [
            "food"
        ],
        "title": "Tea Rooms"
    },
    {
        "alias": "teethwhitening",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "beautysvc"
        ],
        "title": "Teeth Whitening"
    },
    {
        "alias": "telecommunications",
        "country_blacklist": [
            "HK",
            "AR",
            "JP",
            "MX",
            "CL"
        ],
        "parents": [
            "itservices"
        ],
        "title": "Telecommunications"
    },
    {
        "alias": "televisionserviceproviders",
        "parents": [
            "homeservices"
        ],
        "title": "Television Service Providers"
    },
    {
        "alias": "televisionstations",
        "parents": [
            "massmedia"
        ],
        "title": "Television Stations"
    },
    {
        "country_whitelist": [
            "JP",
            "SG",
            "TW"
        ],
        "alias": "tempura",
        "parents": [
            "japanese"
        ],
        "title": "Tempura"
    },
    {
        "alias": "tenantlaw",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "professional"
        ],
        "title": "Tenant and Eviction Law"
    },
    {
        "alias": "tennis",
        "parents": [
            "active"
        ],
        "title": "Tennis"
    },
    {
        "country_whitelist": [
            "HK",
            "SG",
            "MY",
            "TW"
        ],
        "alias": "teochew",
        "parents": [
            "chinese"
        ],
        "title": "Teochew"
    },
    {
        "country_whitelist": [
            "TW",
            "JP",
            "US",
            "HK",
            "NZ",
            "AU",
            "SG",
            "MX"
        ],
        "alias": "teppanyaki",
        "parents": [
            "japanese"
        ],
        "title": "Teppanyaki"
    },
    {
        "alias": "testprep",
        "parents": [
            "education"
        ],
        "title": "Test Preparation"
    },
    {
        "alias": "tex-mex",
        "country_blacklist": [
            "AU",
            "DK",
            "ES",
            "PT"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Tex-Mex"
    },
    {
        "alias": "thai",
        "parents": [
            "restaurants"
        ],
        "title": "Thai"
    },
    {
        "alias": "theater",
        "parents": [
            "arts"
        ],
        "title": "Performing Arts"
    },
    {
        "alias": "threadingservices",
        "parents": [
            "hairremoval"
        ],
        "title": "Threading Services"
    },
    {
        "alias": "thrift_stores",
        "country_blacklist": [
            "FI"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Thrift Stores"
    },
    {
        "country_whitelist": [
            "SE",
            "PT",
            "NO",
            "FI",
            "CL",
            "PL"
        ],
        "alias": "tickets",
        "parents": [
            "shopping"
        ],
        "title": "Tickets"
    },
    {
        "alias": "ticketsales",
        "country_blacklist": [
            "ES",
            "NL",
            "IE",
            "TR",
            "NZ",
            "PL",
            "BR",
            "FI",
            "SG",
            "SE",
            "GB"
        ],
        "parents": [
            "arts"
        ],
        "title": "Ticket Sales"
    },
    {
        "alias": "tiling",
        "country_blacklist": [
            "BE",
            "NL",
            "PT",
            "IE",
            "JP",
            "CA",
            "TR",
            "HK",
            "GB",
            "BR",
            "TW",
            "FI",
            "PH",
            "MY",
            "PL"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Tiling"
    },
    {
        "alias": "tires",
        "parents": [
            "auto"
        ],
        "title": "Tires"
    },
    {
        "country_whitelist": [
            "CA",
            "US"
        ],
        "alias": "titleloans",
        "parents": [
            "financialservices"
        ],
        "title": "Title Loans"
    },
    {
        "alias": "tobaccoshops",
        "parents": [
            "shopping"
        ],
        "title": "Tobacco Shops"
    },
    {
        "country_whitelist": [
            "JP"
        ],
        "alias": "tofu",
        "parents": [
            "gourmet"
        ],
        "title": "Tofu Shops"
    },
    {
        "country_whitelist": [
            "JP",
            "SG",
            "TW"
        ],
        "alias": "tonkatsu",
        "parents": [
            "japanese"
        ],
        "title": "Tonkatsu"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "torshi",
        "parents": [
            "food"
        ],
        "title": "Torshi"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "tortillas",
        "parents": [
            "food"
        ],
        "title": "Tortillas"
    },
    {
        "alias": "tours",
        "parents": [
            "hotelstravel"
        ],
        "title": "Tours"
    },
    {
        "alias": "towing",
        "parents": [
            "auto"
        ],
        "title": "Towing"
    },
    {
        "alias": "toxicologists",
        "parents": [
            "physicians"
        ],
        "title": "Toxicologists"
    },
    {
        "alias": "toys",
        "parents": [
            "shopping"
        ],
        "title": "Toy Stores"
    },
    {
        "alias": "tradamerican",
        "parents": [
            "restaurants"
        ],
        "title": "American (Traditional)"
    },
    {
        "country_whitelist": [
            "CH",
            "NL",
            "PT",
            "NO",
            "JP",
            "DE",
            "TR",
            "IT",
            "CZ",
            "NZ",
            "AT",
            "FI",
            "MX"
        ],
        "alias": "tradefairs",
        "parents": [
            "festivals"
        ],
        "title": "Trade Fairs"
    },
    {
        "country_whitelist": [
            "SE"
        ],
        "alias": "traditional_swedish",
        "parents": [
            "restaurants"
        ],
        "title": "Traditional Swedish"
    },
    {
        "country_whitelist": [
            "AU",
            "US"
        ],
        "alias": "trailerdealers",
        "parents": [
            "auto"
        ],
        "title": "Trailer Dealers"
    },
    {
        "country_whitelist": [
            "AU",
            "US"
        ],
        "alias": "trailerrepair",
        "parents": [
            "auto"
        ],
        "title": "Trailer Repair"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "DK",
            "NO",
            "DE",
            "US",
            "CZ",
            "AU",
            "BR",
            "SE"
        ],
        "alias": "trains",
        "parents": [
            "transport"
        ],
        "title": "Trains"
    },
    {
        "alias": "trainstations",
        "parents": [
            "hotelstravel"
        ],
        "title": "Train Stations"
    },
    {
        "country_whitelist": [
            "DK",
            "CA",
            "TR",
            "IT",
            "US",
            "CZ",
            "AU",
            "PL"
        ],
        "alias": "trampoline",
        "parents": [
            "active"
        ],
        "title": "Trampoline Parks"
    },
    {
        "alias": "translationservices",
        "country_blacklist": [
            "SE"
        ],
        "parents": [
            "professional"
        ],
        "title": "Translation Services"
    },
    {
        "alias": "transmissionrepair",
        "country_blacklist": [
            "CH",
            "AT",
            "PH",
            "DE",
            "MY",
            "IT"
        ],
        "parents": [
            "auto"
        ],
        "title": "Transmission Repair"
    },
    {
        "alias": "transport",
        "parents": [
            "hotelstravel"
        ],
        "title": "Transportation"
    },
    {
        "country_whitelist": [
            "PT"
        ],
        "alias": "tras_os_montes",
        "parents": [
            "portuguese"
        ],
        "title": "Tras-os-Montes"
    },
    {
        "country_whitelist": [
            "FR",
            "AR",
            "IT",
            "CL"
        ],
        "alias": "trattorie",
        "parents": [
            "restaurants"
        ],
        "title": "Trattorie"
    },
    {
        "alias": "travelagents",
        "country_blacklist": [
            "IT"
        ],
        "parents": [
            "travelservices"
        ],
        "title": "Travel Agents"
    },
    {
        "alias": "travelservices",
        "parents": [
            "hotelstravel"
        ],
        "title": "Travel Services"
    },
    {
        "alias": "treeservices",
        "parents": [
            "homeservices"
        ],
        "title": "Tree Services"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "trinidadian",
        "parents": [
            "caribbean"
        ],
        "title": "Trinidadian"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "triviahosts",
        "parents": [
            "eventservices"
        ],
        "title": "Trivia Hosts"
    },
    {
        "alias": "trophyshops",
        "country_blacklist": [
            "DK",
            "NO",
            "CA",
            "TR",
            "CZ",
            "NZ",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Trophy Shops"
    },
    {
        "alias": "truck_rental",
        "country_blacklist": [
            "BE",
            "CH",
            "NL",
            "CZ",
            "IE",
            "JP",
            "TR",
            "HK",
            "NZ",
            "AT",
            "TW",
            "FI",
            "SG",
            "SE",
            "GB"
        ],
        "parents": [
            "auto"
        ],
        "title": "Truck Rental"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "DK",
            "CL",
            "DE",
            "IT",
            "US",
            "NO",
            "AR",
            "AT",
            "BR",
            "MX",
            "ES"
        ],
        "alias": "truckdealers",
        "parents": [
            "auto"
        ],
        "title": "Commercial Truck Dealers"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "CH",
            "CL",
            "DE",
            "IT",
            "US",
            "AR",
            "AT",
            "BR",
            "MX",
            "ES"
        ],
        "alias": "truckrepair",
        "parents": [
            "auto"
        ],
        "title": "Commercial Truck Repair"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "tubing",
        "parents": [
            "active"
        ],
        "title": "Tubing"
    },
    {
        "alias": "tuina",
        "parents": [
            "tcm"
        ],
        "title": "Tui Na"
    },
    {
        "alias": "turkish",
        "country_blacklist": [
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Turkish"
    },
    {
        "country_whitelist": [
            "TR"
        ],
        "alias": "turkishravioli",
        "parents": [
            "turkish"
        ],
        "title": "Turkish Ravioli"
    },
    {
        "country_whitelist": [
            "FR",
            "IT",
            "US"
        ],
        "alias": "tuscan",
        "parents": [
            "italian"
        ],
        "title": "Tuscan"
    },
    {
        "alias": "tutoring",
        "parents": [
            "education"
        ],
        "title": "Tutoring Centers"
    },
    {
        "alias": "tvmounting",
        "country_blacklist": [
            "BE",
            "FR",
            "JP",
            "IT",
            "NL"
        ],
        "parents": [
            "localservices"
        ],
        "title": "TV Mounting"
    },
    {
        "country_whitelist": [
            "HK",
            "FI",
            "DK",
            "NO",
            "TW",
            "JP",
            "SE"
        ],
        "alias": "udon",
        "parents": [
            "japanese"
        ],
        "title": "Udon"
    },
    {
        "alias": "ukrainian",
        "country_blacklist": [
            "TR",
            "DK",
            "ES"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Ukrainian"
    },
    {
        "country_whitelist": [
            "TW",
            "JP"
        ],
        "alias": "unagi",
        "parents": [
            "japanese"
        ],
        "title": "Unagi"
    },
    {
        "alias": "underseamedicine",
        "parents": [
            "physicians"
        ],
        "title": "Undersea/Hyperbaric Medicine"
    },
    {
        "alias": "uniforms",
        "country_blacklist": [
            "CH",
            "NL",
            "JP",
            "TR",
            "CZ",
            "AT",
            "IE",
            "SE"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Uniforms"
    },
    {
        "alias": "university_housing",
        "parents": [
            "realestate"
        ],
        "title": "University Housing"
    },
    {
        "alias": "unofficialyelpevents",
        "parents": [
            "localflavor"
        ],
        "title": "Unofficial Yelp Events"
    },
    {
        "alias": "urgent_care",
        "parents": [
            "health"
        ],
        "title": "Urgent Care"
    },
    {
        "alias": "urologists",
        "parents": [
            "physicians"
        ],
        "title": "Urologists"
    },
    {
        "alias": "usedbooks",
        "country_blacklist": [
            "BE",
            "NL",
            "CL",
            "JP",
            "CA",
            "TR",
            "AR",
            "AU"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Used Bookstore"
    },
    {
        "country_whitelist": [
            "AU",
            "GB",
            "PT",
            "SG",
            "IT",
            "US"
        ],
        "alias": "utilities",
        "parents": [
            "homeservices"
        ],
        "title": "Utilities"
    },
    {
        "country_whitelist": [
            "CZ",
            "US"
        ],
        "alias": "uzbek",
        "parents": [
            "restaurants"
        ],
        "title": "Uzbek"
    },
    {
        "alias": "vacation_rentals",
        "country_blacklist": [
            "SG",
            "AT"
        ],
        "parents": [
            "hotelstravel"
        ],
        "title": "Vacation Rentals"
    },
    {
        "alias": "vacationrentalagents",
        "country_blacklist": [
            "SG",
            "ES"
        ],
        "parents": [
            "hotelstravel"
        ],
        "title": "Vacation Rental Agents"
    },
    {
        "country_whitelist": [
            "TR",
            "BR",
            "US"
        ],
        "alias": "valetservices",
        "parents": [
            "eventservices"
        ],
        "title": "Valet Services"
    },
    {
        "alias": "vapeshops",
        "country_blacklist": [
            "SG"
        ],
        "parents": [
            "shopping"
        ],
        "title": "Vape Shops"
    },
    {
        "alias": "vascularmedicine",
        "parents": [
            "physicians"
        ],
        "title": "Vascular Medicine"
    },
    {
        "alias": "vegan",
        "parents": [
            "restaurants"
        ],
        "title": "Vegan"
    },
    {
        "alias": "vegetarian",
        "parents": [
            "restaurants"
        ],
        "title": "Vegetarian"
    },
    {
        "alias": "vehicleshipping",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "auto"
        ],
        "title": "Vehicle Shipping"
    },
    {
        "alias": "vehiclewraps",
        "country_blacklist": [
            "BE",
            "FR",
            "TR"
        ],
        "parents": [
            "auto"
        ],
        "title": "Vehicle Wraps"
    },
    {
        "country_whitelist": [
            "IT"
        ],
        "alias": "venetian",
        "parents": [
            "italian"
        ],
        "title": "Venetian"
    },
    {
        "country_whitelist": [
            "CA",
            "AR",
            "FR",
            "US",
            "CL"
        ],
        "alias": "venezuelan",
        "parents": [
            "latin"
        ],
        "title": "Venezuelan"
    },
    {
        "country_whitelist": [
            "IT",
            "PL"
        ],
        "alias": "venison",
        "parents": [
            "restaurants"
        ],
        "title": "Venison"
    },
    {
        "alias": "venues",
        "parents": [
            "eventservices"
        ],
        "title": "Venues & Event Spaces"
    },
    {
        "alias": "vet",
        "parents": [
            "pets"
        ],
        "title": "Veterinarians"
    },
    {
        "alias": "videoandgames",
        "parents": [
            "media"
        ],
        "title": "Videos & Video Game Rental"
    },
    {
        "alias": "videofilmproductions",
        "parents": [
            "professional"
        ],
        "title": "Video/Film Production"
    },
    {
        "alias": "videogamestores",
        "parents": [
            "media"
        ],
        "title": "Video Game Stores"
    },
    {
        "alias": "videographers",
        "parents": [
            "eventservices"
        ],
        "title": "Videographers"
    },
    {
        "alias": "vietnamese",
        "parents": [
            "restaurants"
        ],
        "title": "Vietnamese"
    },
    {
        "alias": "vintage",
        "parents": [
            "fashion"
        ],
        "title": "Used, Vintage & Consignment"
    },
    {
        "alias": "vinyl_records",
        "parents": [
            "media"
        ],
        "title": "Vinyl Records"
    },
    {
        "country_whitelist": [
            "SE",
            "US"
        ],
        "alias": "vinylsiding",
        "parents": [
            "homeservices"
        ],
        "title": "Vinyl Siding"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "NO",
            "JP",
            "DE",
            "TR",
            "IT",
            "US",
            "NZ",
            "ES",
            "BR",
            "SE"
        ],
        "alias": "vitaminssupplements",
        "parents": [
            "shopping"
        ],
        "title": "Vitamins & Supplements"
    },
    {
        "alias": "vocation",
        "parents": [
            "specialtyschools"
        ],
        "title": "Vocational & Technical School"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "NO",
            "DE",
            "JP",
            "CZ",
            "NZ",
            "AU",
            "AT",
            "BR",
            "FI",
            "SG",
            "SE"
        ],
        "alias": "volleyball",
        "parents": [
            "active"
        ],
        "title": "Volleyball"
    },
    {
        "alias": "waffles",
        "parents": [
            "restaurants"
        ],
        "title": "Waffles"
    },
    {
        "alias": "walkinclinics",
        "country_blacklist": [
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "medcenters"
        ],
        "title": "Walk-in Clinics"
    },
    {
        "alias": "walkingtours",
        "parents": [
            "tours"
        ],
        "title": "Walking Tours"
    },
    {
        "alias": "watch_repair",
        "parents": [
            "localservices"
        ],
        "title": "Watch Repair"
    },
    {
        "alias": "watches",
        "parents": [
            "shopping"
        ],
        "title": "Watches"
    },
    {
        "country_whitelist": [
            "HK",
            "PH",
            "MY",
            "BR",
            "US"
        ],
        "alias": "waterdelivery",
        "parents": [
            "localservices"
        ],
        "title": "Water Delivery"
    },
    {
        "alias": "waterheaterinstallrepair",
        "parents": [
            "homeservices"
        ],
        "title": "Water Heater Installation/Repair"
    },
    {
        "alias": "waterparks",
        "country_blacklist": [
            "BE",
            "CH",
            "CL",
            "CA",
            "DE",
            "HK",
            "AR",
            "AU",
            "AT",
            "FI",
            "IE",
            "NL",
            "PT",
            "NZ",
            "MY",
            "GB"
        ],
        "parents": [
            "active"
        ],
        "title": "Water Parks"
    },
    {
        "alias": "waterproofing",
        "parents": [
            "homeservices"
        ],
        "title": "Waterproofing"
    },
    {
        "alias": "waterpurification",
        "country_blacklist": [
            "CZ"
        ],
        "parents": [
            "homeservices"
        ],
        "title": "Water Purification Services"
    },
    {
        "country_whitelist": [
            "NZ",
            "AU"
        ],
        "alias": "watertaxis",
        "parents": [
            "transport"
        ],
        "title": "Water Taxis"
    },
    {
        "alias": "waxing",
        "parents": [
            "hairremoval"
        ],
        "title": "Waxing"
    },
    {
        "alias": "web_design",
        "parents": [
            "professional"
        ],
        "title": "Web Design"
    },
    {
        "alias": "wedding_planning",
        "parents": [
            "eventservices"
        ],
        "title": "Wedding Planning"
    },
    {
        "country_whitelist": [
            "AU",
            "JP",
            "US"
        ],
        "alias": "weddingchappels",
        "parents": [
            "eventservices"
        ],
        "title": "Wedding Chapels"
    },
    {
        "alias": "weightlosscenters",
        "parents": [
            "health"
        ],
        "title": "Weight Loss Centers"
    },
    {
        "country_whitelist": [
            "DK",
            "CL",
            "NO",
            "IT",
            "US",
            "AR",
            "ES",
            "BR",
            "MX",
            "PL"
        ],
        "alias": "welldrilling",
        "parents": [
            "localservices"
        ],
        "title": "Well Drilling"
    },
    {
        "country_whitelist": [
            "JP",
            "SG",
            "TW"
        ],
        "alias": "westernjapanese",
        "parents": [
            "japanese"
        ],
        "title": "Western Style Japanese Food"
    },
    {
        "country_whitelist": [
            "IT",
            "US",
            "PT"
        ],
        "alias": "wheelrimrepair",
        "parents": [
            "auto"
        ],
        "title": "Wheel & Rim Repair"
    },
    {
        "alias": "whiskeybars",
        "country_blacklist": [
            "IT"
        ],
        "parents": [
            "bars"
        ],
        "title": "Whiskey Bars"
    },
    {
        "alias": "wholesale_stores",
        "parents": [
            "shopping"
        ],
        "title": "Wholesale Stores"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "PT",
            "NO",
            "CA",
            "DE",
            "IT",
            "US",
            "CZ",
            "AU",
            "FI",
            "MX",
            "ES"
        ],
        "alias": "wigs",
        "parents": [
            "shopping"
        ],
        "title": "Wigs"
    },
    {
        "alias": "wildlifecontrol",
        "country_blacklist": [
            "JP"
        ],
        "parents": [
            "localservices"
        ],
        "title": "Wildlife Control"
    },
    {
        "country_whitelist": [
            "US"
        ],
        "alias": "wildlifehunting",
        "parents": [
            "active"
        ],
        "title": "Wildlife Hunting Ranges"
    },
    {
        "country_whitelist": [
            "SG",
            "AU",
            "NL",
            "IT",
            "US"
        ],
        "alias": "willstrustsprobates",
        "parents": [
            "estateplanning"
        ],
        "title": "Wills, Trusts, & Probates"
    },
    {
        "alias": "windowsinstallation",
        "parents": [
            "homeservices"
        ],
        "title": "Windows Installation"
    },
    {
        "alias": "windowwashing",
        "parents": [
            "homeservices"
        ],
        "title": "Window Washing"
    },
    {
        "alias": "windshieldinstallrepair",
        "country_blacklist": [
            "CZ",
            "CH",
            "DE",
            "AT"
        ],
        "parents": [
            "auto"
        ],
        "title": "Windshield Installation & Repair"
    },
    {
        "alias": "wine_bars",
        "parents": [
            "bars"
        ],
        "title": "Wine Bars"
    },
    {
        "alias": "wineries",
        "country_blacklist": [
            "FI"
        ],
        "parents": [
            "food",
            "arts"
        ],
        "title": "Wineries"
    },
    {
        "alias": "winetasteclasses",
        "parents": [
            "tastingclasses"
        ],
        "title": "Wine Tasting Classes"
    },
    {
        "alias": "winetastingroom",
        "parents": [
            "wineries"
        ],
        "title": "Wine Tasting Room"
    },
    {
        "alias": "winetours",
        "parents": [
            "tours"
        ],
        "title": "Wine Tours"
    },
    {
        "alias": "wok",
        "country_blacklist": [
            "IE",
            "JP",
            "CA",
            "TR",
            "IT",
            "US",
            "HK",
            "NZ",
            "AR",
            "AU",
            "GB",
            "BR",
            "TW",
            "SG",
            "PL"
        ],
        "parents": [
            "restaurants"
        ],
        "title": "Wok"
    },
    {
        "alias": "womenscloth",
        "parents": [
            "fashion"
        ],
        "title": "Women's Clothing"
    },
    {
        "country_whitelist": [
            "CZ",
            "DK",
            "PT",
            "NO",
            "TR",
            "SE"
        ],
        "alias": "wraps",
        "parents": [
            "restaurants"
        ],
        "title": "Wraps"
    },
    {
        "alias": "xmasmarkets",
        "country_blacklist": [
            "NZ",
            "BR",
            "TR",
            "CA",
            "SG",
            "IE",
            "US"
        ],
        "parents": [
            "festivals"
        ],
        "title": "Christmas Markets"
    },
    {
        "country_whitelist": [
            "JP",
            "SG",
            "TW"
        ],
        "alias": "yakiniku",
        "parents": [
            "japanese"
        ],
        "title": "Yakiniku"
    },
    {
        "country_whitelist": [
            "JP",
            "SG",
            "TW"
        ],
        "alias": "yakitori",
        "parents": [
            "japanese"
        ],
        "title": "Yakitori"
    },
    {
        "alias": "yelpevents",
        "parents": [
            "localflavor"
        ],
        "title": "Yelp Events"
    },
    {
        "alias": "yoga",
        "parents": [
            "fitness"
        ],
        "title": "Yoga"
    },
    {
        "country_whitelist": [
            "FR",
            "DK",
            "PT",
            "NO",
            "FI",
            "IT",
            "SE"
        ],
        "alias": "youth_club",
        "parents": [
            "localservices"
        ],
        "title": "Youth Club"
    },
    {
        "country_whitelist": [
            "MX"
        ],
        "alias": "yucatan",
        "parents": [
            "mexican"
        ],
        "title": "Yucatan"
    },
    {
        "country_whitelist": [
            "BE",
            "FR",
            "AU",
            "PT",
            "IT",
            "SE"
        ],
        "alias": "yugoslav",
        "parents": [
            "restaurants"
        ],
        "title": "Yugoslav"
    },
    {
        "country_whitelist": [
            "PL"
        ],
        "alias": "zapiekanka",
        "parents": [
            "food"
        ],
        "title": "Zapiekanka"
    },
    {
        "alias": "zipline",
        "parents": [
            "active"
        ],
        "title": "Ziplining"
    },
    {
        "alias": "zoos",
        "parents": [
            "active"
        ],
        "title": "Zoos"
    },
    {
        "country_whitelist": [
            "CZ",
            "NZ",
            "PT"
        ],
        "alias": "zorbing",
        "parents": [
            "active"
        ],
        "title": "Zorbing"
    }
]