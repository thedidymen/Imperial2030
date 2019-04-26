areas = {'Canada': ['Alaska', 'Quebec', 'San Francisco', 'Chicago', 'New York', 'North Pacific', 'North Atlantic'], 'Manaus': ['Colombia', 'Peru', 'Brasillia', 'Fortaleza', 'Caribbean Sea'], 'Gulf of Guinea': ['Guinea', 'Nigeria', 'Congo', 'South-Africa', 'Indian Ocean', 'South Atlantic', 'Caribbean Sea', 'North Atlantic'], 'Paris': ['London', 'Berlin', 'Rome', 'Mediterranean Sea', 'North Atlantic'], 'Guinea': ['Gulf of Guinea', 'Nigeria', 'North-Africa', 'North Atlantic'], 'Rio de Janeiro': ['Argentina', 'South Atlantic', 'Brasillia', 'Fortaleza'], 'Fortaleza': ['Manaus', 'Brasillia', 'Caribbean Sea', 'Rio de Janeiro'], 'San Francisco': ['Canada', 'Mexico', 'North Pacific', 'Chicago', 'New Orleans'], 'Argentina': ['Peru', 'South Pacific', 'South Atlantic', 'Rio de Janeiro', 'Brasillia'], 'Australia': ['Tasman Sea'], 'Iran': ['Moscow', 'Indian Ocean', 'Near East', 'Turkey', 'Afghanistan', 'Mumbai'], 'North-Africa': ['Guinea', 'Mediterranean Sea', 'Near East', 'East-Africa', 'Nigeria', 'North Atlantic', 'Indian Ocean'], 'Chicago': ['Canada', 'San Francisco', 'New York', 'New Orleans'], 'East-Africa': ['Indian Ocean', 'Congo', 'South-Africa', 'Near East', 'North-Africa', 'Nigeria'], 'Caribbean Sea': ['Mexico', 'Gulf of Guinea', 'Manaus', 'South Atlantic', 'Fortaleza', 'New Orleans', 'Colombia', 'Manaus', 'North Atlantic', 'North Pacific'], 'Near East': ['Indian Ocean', 'Iran', 'Turkey', 'Mediterranean Sea', 'North-Africa', 'East-Africa'], 'New Delhi': ['Afghanistan', 'Urumqi', 'Kolkata', 'Mumbai'], 'Alaska': ['North Pacific', 'Canada'], 'Rome': ['Paris', 'Berlin', 'Ukraine', 'Turkey', 'Mediterranean Sea'], 'Tasman Sea': ['Australia', 'New-Zeeland', 'Indonesia', 'South Pacific', 'Indian Ocean', 'China Sea'], 'Beijing': ['China Sea', 'Mongolia', 'Urumqi', 'Chongging', 'Shanghai', 'Vladivostok', 'Korea'], 'South-Africa': ['Gulf of Guinea', 'Indian Ocean', 'Congo', 'East-Africa'], 'Mexico': ['North Pacific', 'San Francisco', 'New Orleans', 'Caribbean Sea', 'Colombia'], 'Mediterranean Sea': ['Indian Ocean', 'Paris', 'North-Africa', 'Near East', 'Rome', 'Turkey', 'North Atlantic'], 'New Orleans': ['Mexico', 'San Francisco', 'Caribbean Sea', 'Chicago', 'New York'], 'London': ['Paris', 'North Atlantic'], 'Colombia': ['Mexico', 'Manaus', 'North Pacific', 'Caribbean Sea', 'Peru'], 'Brasillia': ['Argentina', 'Manaus', 'Rio de Janeiro', 'Fortaleza', 'Peru'], 'Turkey': ['Moscow', 'Iran', 'Near East', 'Rome', 'Mediterranean Sea'], 'Afghanistan': ['Iran', 'New Delhi', 'Kazakhstan', 'Urumqi', 'Mumbai'], 'Indochina': ['Kolkata', 'Chongging', 'Shanghai', 'China Sea', 'Indian Ocean'], 'Vladivostok': ['Beijing', 'Novasibirsk', 'Sea of Japan', 'Korea', 'Mongolia'], 'North Atlantic': ['Canada', 'Quebec', 'Gulf of Guinea', 'Paris', 'Guinea', 'North-Africa', 'Caribbean Sea', 'Mediterranean Sea', 'London', 'Berlin', 'Paris', 'New York', 'Murmansk'], 'Mumbai': ['Indian Ocean', 'Iran', 'New Delhi', 'Afghanistan', 'Chennai', 'Kolkata'], 'Shanghai': ['Indochina', 'China Sea', 'Beijing', 'Chongging'], 'Mongolia': ['Beijing', 'Novasibirsk', 'Vladivostok', 'Urumqi', 'Kazakhstan'], 'Philppines': ['China Sea'], 'Peru': ['Argentina', 'Manaus', 'Brasillia', 'South Pacific', 'Colombia'], 'China Sea': ['Sea of Japan', 'North Pacific', 'South Pacific', 'Philppines', 'Indonesia', 'Korea', 'Beijing', 'Shanghai', 'Indochina', 'Indian Ocean', 'Tasman Sea'], 'Kolkata': ['Indochina', 'Indian Ocean', 'New Delhi', 'Chongging', 'Urumqi', 'Mumbai', 'Chennai'], 'Nigeria': ['Gulf of Guinea', 'Congo', 'Guinea', 'North-Africa', 'East-Africa'], 'Korea': ['China Sea', 'Beijing', 'Vladivostok', 'Sea of Japan'], 'South Pacific': ['Argentina', 'China Sea', 'Tasman Sea', 'South Atlantic', 'North Pacific', 'Peru'], 'Moscow': ['Murmansk', 'Novasibirsk', 'Kazakhstan', 'Iran', 'Turkey', 'Ukraine'], 'Berlin': ['Paris', 'Rome', 'North Atlantic', 'Ukraine', 'Murmansk'], 'New York': ['Canada', 'Quebec', 'Chicago', 'New Orleans', 'North Atlantic'], 'Kazakhstan': ['Moscow', 'Novasibirsk', 'Afghanistan', 'Mongolia', 'Urumqi'], 'Chongging': ['Indochina', 'Beijing', 'Shanghai', 'Kolkata', 'Urumqi'], 'Ukraine': ['Moscow', 'Rome', 'Berlin', 'Murmansk'], 'Murmansk': ['Moscow', 'Novasibirsk', 'Berlin', 'Ukraine', 'North Atlantic'], 'Indonesia': ['China Sea', 'Tasman Sea', 'Indian Ocean'], 'Urumqi': ['Beijing', 'New Delhi', 'Afghanistan', 'Mongolia', 'Kolkata', 'Kazakhstan', 'Chongging'], 'Chennai': ['Indian Ocean', 'Mumbai', 'Kolkata'], 'Sea of Japan': ['China Sea', 'North Pacific', 'Japan', 'Vladivostok', 'Korea'], 'North Pacific': ['Canada', 'Alaska', 'Mexico', 'China Sea', 'Sea of Japan', 'Colombia', 'San Francisco', 'South Pacific', 'Caribbean Sea'], 'New-Zeeland': ['Tasman Sea'], 'South Atlantic': ['Gulf of Guinea', 'Argentina', 'Caribbean Sea', 'Rio de Janeiro', 'Indian Ocean', 'South Pacific'], 'Indian Ocean': ['South Atlantic', 'Gulf of Guinea', 'Indochina', 'Mumbai', 'Chennai', 'Kolkata', 'Indonesia', 'Tasman Sea', 'South-Africa', 'East-Africa', 'North-Africa', 'Near East', 'Iran', 'Mediterranean Sea', 'China Sea'], 'Novasibirsk': ['Moscow', 'Murmansk', 'Vladivostok', 'Mongolia', 'Kazakhstan'], 'Congo': ['Gulf of Guinea', 'Nigeria', 'East-Africa', 'South-Africa'], 'Quebec': ['Canada', 'North Atlantic', 'New York'], 'Japan': ['Sea of Japan']}
land = []
sea = []
for area in areas.keys():
	print area
	ans = raw_input("land (1), sea (2)")
	if ans == "1":
		land.append(area)
	elif ans == "2":
		sea.append(area)


print land
print sea

landdict = {area:areas[area] for area in land}
seadict = {area:areas[area] for area in sea}

a = {}
a['Land'] = landdict
a['Sea'] = seadict

print a

land = ['Canada', 'Manaus', 'Paris', 'Guinea', 'Rio de Janeiro', 'Fortaleza', 'San Francisco', 'Argentina', 'Australia', 'Iran', 'North-Africa', 'Mumbai', 'East-Africa', 'Near East', 'New-Zeeland', 'Alaska', 'Rome', 'Beijing', 'South-Africa', 'New Orleans', 'London', 'Colombia', 'Brasillia', 'Turkey', 'Afghanistan', 'Indochina', 'Vladivostok', 'Chicago', 'Shanghai', 'Mongolia', 'Philppines', 'Peru', 'Kolkata', 'Nigeria', 'Korea', 'Moscow', 'Berlin', 'New York', 'Kazakhstan', 'Quebec', 'Ukraine', 'Murmansk', 'Indonesia', 'Urumqi', 'Chennai', 'New Delhi', 'Mexico', 'Novasibirsk', 'Congo', 'Chongging', 'Japan']
sea = ['Gulf of Guinea', 'Caribbean Sea', 'Tasman Sea', 'South Atlantic', 'Mediterranean Sea', 'North Atlantic', 'China Sea', 'South Pacific', 'Sea of Japan', 'North Pacific', 'Indian Ocean']
areas = {'Land': {'Canada': ['Alaska', 'Quebec', 'San Francisco', 'Chicago', 'New York', 'North Pacific', 'North Atlantic'], 'Turkey': ['Moscow', 'Iran', 'Near East', 'Rome', 'Mediterranean Sea'], 'Indochina': ['Kolkata', 'Chongging', 'Shanghai', 'China Sea', 'Indian Ocean'], 'Vladivostok': ['Beijing', 'Novasibirsk', 'Sea of Japan', 'Korea', 'Mongolia'], 'Mumbai': ['Indian Ocean', 'Iran', 'New Delhi', 'Afghanistan', 'Chennai', 'Kolkata'], 'Paris': ['London', 'Berlin', 'Rome', 'Mediterranean Sea', 'North Atlantic'], 'Guinea': ['Gulf of Guinea', 'Nigeria', 'North-Africa', 'North Atlantic'], 'Shanghai': ['Indochina', 'China Sea', 'Beijing', 'Chongging'], 'Chennai': ['Indian Ocean', 'Mumbai', 'Kolkata'], 'Rio de Janeiro': ['Argentina', 'South Atlantic', 'Brasillia', 'Fortaleza'], 'Mongolia': ['Beijing', 'Novasibirsk', 'Vladivostok', 'Urumqi', 'Kazakhstan'], 'Kolkata': ['Indochina', 'Indian Ocean', 'New Delhi', 'Chongging', 'Urumqi', 'Mumbai', 'Chennai'], 'Fortaleza': ['Manaus', 'Brasillia', 'Caribbean Sea', 'Rio de Janeiro'], 'Peru': ['Argentina', 'Manaus', 'Brasillia', 'South Pacific', 'Colombia'], 'Philppines': ['China Sea'], 'San Francisco': ['Canada', 'Mexico', 'North Pacific', 'Chicago', 'New Orleans'], 'Argentina': ['Peru', 'South Pacific', 'South Atlantic', 'Rio de Janeiro', 'Brasillia'], 'New Delhi': ['Afghanistan', 'Urumqi', 'Kolkata', 'Mumbai'], 'Nigeria': ['Gulf of Guinea', 'Congo', 'Guinea', 'North-Africa', 'East-Africa'], 'Australia': ['Tasman Sea'], 'Iran': ['Moscow', 'Indian Ocean', 'Near East', 'Turkey', 'Afghanistan', 'Mumbai'], 'Korea': ['China Sea', 'Beijing', 'Vladivostok', 'Sea of Japan'], 'North-Africa': ['Guinea', 'Mediterranean Sea', 'Near East', 'East-Africa', 'Nigeria', 'North Atlantic', 'Indian Ocean'], 'Moscow': ['Murmansk', 'Novasibirsk', 'Kazakhstan', 'Iran', 'Turkey', 'Ukraine'], 'Manaus': ['Colombia', 'Peru', 'Brasillia', 'Fortaleza', 'Caribbean Sea'], 'Congo': ['Gulf of Guinea', 'Nigeria', 'East-Africa', 'South-Africa'], 'East-Africa': ['Indian Ocean', 'Congo', 'South-Africa', 'Near East', 'North-Africa', 'Nigeria'], 'Berlin': ['Paris', 'Rome', 'North Atlantic', 'Ukraine', 'Murmansk'], 'New York': ['Canada', 'Quebec', 'Chicago', 'New Orleans', 'North Atlantic'], 'Near East': ['Indian Ocean', 'Iran', 'Turkey', 'Mediterranean Sea', 'North-Africa', 'East-Africa'], 'Chongging': ['Indochina', 'Beijing', 'Shanghai', 'Kolkata', 'Urumqi'], 'Ukraine': ['Moscow', 'Rome', 'Berlin', 'Murmansk'], 'Murmansk': ['Moscow', 'Novasibirsk', 'Berlin', 'Ukraine', 'North Atlantic'], 'Chicago': ['Canada', 'San Francisco', 'New York', 'New Orleans'], 'Beijing': ['China Sea', 'Mongolia', 'Urumqi', 'Chongging', 'Shanghai', 'Vladivostok', 'Korea'], 'Indonesia': ['China Sea', 'Tasman Sea', 'Indian Ocean'], 'Alaska': ['North Pacific', 'Canada'], 'Urumqi': ['Beijing', 'New Delhi', 'Afghanistan', 'Mongolia', 'Kolkata', 'Kazakhstan', 'Chongging'], 'Afghanistan': ['Iran', 'New Delhi', 'Kazakhstan', 'Urumqi', 'Mumbai'], 'Rome': ['Paris', 'Berlin', 'Ukraine', 'Turkey', 'Mediterranean Sea'], 'New-Zeeland': ['Tasman Sea'], 'South-Africa': ['Gulf of Guinea', 'Indian Ocean', 'Congo', 'East-Africa'], 'Mexico': ['North Pacific', 'San Francisco', 'New Orleans', 'Caribbean Sea', 'Colombia'], 'Kazakhstan': ['Moscow', 'Novasibirsk', 'Afghanistan', 'Mongolia', 'Urumqi'], 'Novasibirsk': ['Moscow', 'Murmansk', 'Vladivostok', 'Mongolia', 'Kazakhstan'], 'New Orleans': ['Mexico', 'San Francisco', 'Caribbean Sea', 'Chicago', 'New York'], 'London': ['Paris', 'North Atlantic'], 'Quebec': ['Canada', 'North Atlantic', 'New York'], 'Colombia': ['Mexico', 'Manaus', 'North Pacific', 'Caribbean Sea', 'Peru'], 'Japan': ['Sea of Japan'], 'Brasillia': ['Argentina', 'Manaus', 'Rio de Janeiro', 'Fortaleza', 'Peru']}, 'Sea': {'Sea of Japan': ['China Sea', 'North Pacific', 'Japan', 'Vladivostok', 'Korea'], 'North Atlantic': ['Canada', 'Quebec', 'Gulf of Guinea', 'Paris', 'Guinea', 'North-Africa', 'Caribbean Sea', 'Mediterranean Sea', 'London', 'Berlin', 'Paris', 'New York', 'Murmansk'], 'Gulf of Guinea': ['Guinea', 'Nigeria', 'Congo', 'South-Africa', 'Indian Ocean', 'South Atlantic', 'Caribbean Sea', 'North Atlantic'], 'South Atlantic': ['Gulf of Guinea', 'Argentina', 'Caribbean Sea', 'Rio de Janeiro', 'Indian Ocean', 'South Pacific'], 'Caribbean Sea': ['Mexico', 'Gulf of Guinea', 'Manaus', 'South Atlantic', 'Fortaleza', 'New Orleans', 'Colombia', 'Manaus', 'North Atlantic', 'North Pacific'], 'North Pacific': ['Canada', 'Alaska', 'Mexico', 'China Sea', 'Sea of Japan', 'Colombia', 'San Francisco', 'South Pacific', 'Caribbean Sea'], 'South Pacific': ['Argentina', 'China Sea', 'Tasman Sea', 'South Atlantic', 'North Pacific', 'Peru'], 'Indian Ocean': ['South Atlantic', 'Gulf of Guinea', 'Indochina', 'Mumbai', 'Chennai', 'Kolkata', 'Indonesia', 'Tasman Sea', 'South-Africa', 'East-Africa', 'North-Africa', 'Near East', 'Iran', 'Mediterranean Sea', 'China Sea'], 'Mediterranean Sea': ['Indian Ocean', 'Paris', 'North-Africa', 'Near East', 'Rome', 'Turkey', 'North Atlantic'], 'Tasman Sea': ['Australia', 'New-Zeeland', 'Indonesia', 'South Pacific', 'Indian Ocean', 'China Sea'], 'China Sea': ['Sea of Japan', 'North Pacific', 'South Pacific', 'Philppines', 'Indonesia', 'Korea', 'Beijing', 'Shanghai', 'Indochina', 'Indian Ocean', 'Tasman Sea']}}
