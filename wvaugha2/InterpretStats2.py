# Ty Vaughan
# CS 545 - Fall 2017
# Final Project

import random


if __name__ == '__main__':

    '''
    # Get coordinates to place on map.
    f = open('allUserGpsLocations.txt', 'r')
    fout = open('gpsCoordinates.txt', 'w')
    for line in f.readlines():
        elements = line.strip().split(';')
        e1 = float(elements[7]) + random.uniform(-1.0, 1.0)
        e2 = float(elements[6]) + random.uniform(-1.0, 1.0)
        fout.write('{},{}\n'.format(e1, e2))
    '''


    # Store all countries and their continents
    Continents = {
        'North America': {
            'barbados': 'bb',
            'cuba': 'cu',
            'guatemala': 'gt',
            'haiti': 'ht',
            'jamaica': 'jm',
            'nicaragua': 'ni',
            'panama': 'pa',
            'saint kitts and nevis': 'kn',
            'saint vincent and the grenadines': 'vc',
            'belize': 'bz',
            'trinidad and tobago': 'tt',
            'antigua and barbuda': 'ag',
            'dominican republic': 'do',
            'el salvador': 'sv',
            'united states': 'us',
            'canada': 'ca',
            'greenland': 'gl',
            'mexico': 'mx',
            'bahamas': 'bs',
            'costa rica': 'cr',
            'curacao': 'cw',
            'dominica': 'dm',
            'grenada': 'gd',
            'honduras': 'hn',
            'puerto rico': 'pr',
            'saint lucia': 'lc',
            'turks and caicos islands': 'tc',
            'united states minor outlying islands': 'um',
            'cayman islands': 'ky',
            'saint barthlemy': 'bl',
            'montserrat': 'ms',
            'sint maarten (dutch part)': 'sx',
            'bonaire, sint eustatius and saba': 'bq',
            'saint pierre and miquelon': 'pm',
            'anguilla': 'ai',
            'martinique': 'mq',
            'virgin islands, british': 'vg',
            'virgin islands, u.s.': 'vi',
            'guadeloupe': 'gp',
            'saint martin (french part)': 'mf',
            'bermuda': 'bm'
        },
        'South America': {
            'french guiana': 'gf',
            'argentina': 'ar',
            'brazil': 'br',
            'paraguay': 'py',
            'colombia': 'co',
            'bolivia, plurinational state of': 'bo',
            'chile': 'cl',
            'ecuador': 'ec',
            'guyana': 'gy',
            'peru': 'pe',
            'suriname': 'sr',
            'uruguay': 'uy',
            'venezuela, bolivarian republic of': 've',
            'aruba': 'aw',
            'falkland islands (malvinas)': 'fk'
        },
        'Europe': {
            'malta': 'mt',
            'hungary': 'hu',
            'cyprus': 'cy',
            'macedonia, republic of': 'mk',
            'lithuania': 'lt',
            'andorra': 'ad',
            'norway': 'no',
            'serbia': 'rs',
            'belarus': 'by',
            'montenegro': 'me',
            'belgium': 'be',
            'netherlands': 'nl',
            'denmark': 'dk',
            'latvia': 'lv',
            'croatia': 'hr',
            'bosnia and herzegovina': 'ba',
            'switzerland': 'ch',
            'bulgaria': 'bg',
            'albania': 'al',
            'greece': 'gr',
            'luxembourg': 'lu',
            'finland': 'fi',
            'united kingdom': 'gb',
            'romania': 'ro',
            'austria': 'at',
            'czechia': 'cz',
            'estonia': 'ee',
            'france': 'fr',
            'germany': 'de',
            'iceland': 'is',
            'ireland': 'ie',
            'italy': 'it',
            'liechtenstein': 'li',
            'moldova, republic of': 'md',
            'monaco': 'mc',
            'poland': 'pl',
            'portugal': 'pt',
            'san marino': 'sm',
            'slovakia': 'sk',
            'slovenia': 'si',
            'spain': 'es',
            'sweden': 'se',
            'ukraine': 'ua',
            'holy see (vatican city state)': 'va',
            'isle of man': 'im',
            'land islands': 'ax',
            'jersey': 'je',
            'gibraltar': 'gi',
            'svalbard and jan mayen': 'sj',
            'faroe islands': 'fo',
            'guernsey': 'gg'
        },
        'Africa': {
            'djibouti': 'dj',
            'tunisia': 'tn',
            'rwanda': 'rw',
            'liberia': 'lr',
            'sierra leone': 'sl',
            'somalia': 'so',
            'zambia': 'zm',
            'burkina faso': 'bf',
            'senegal': 'sn',
            'chad': 'td',
            'angola': 'ao',
            'mozambique': 'mz',
            'tanzania, united republic of': 'tz',
            'equatorial guinea': 'gq',
            'guinea': 'gn',
            'central african republic': 'cf',
            'cte d\'ivoire': 'ci',
            'swaziland': 'sz',
            'namibia': 'na',
            'mali': 'ml',
            'libya': 'ly',
            'gambia': 'gm',
            'mauritius': 'mu',
            'seychelles': 'sc',
            'egypt': 'eg',
            'congo': 'cg',
            'algeria': 'dz',
            'benin': 'bj',
            'botswana': 'bw',
            'burundi': 'bi',
            'cameroon': 'cm',
            'congo, the democratic republic of the': 'cd',
            'eritrea': 'er',
            'ethiopia': 'et',
            'gabon': 'ga',
            'ghana': 'gh',
            'guinea-bissau': 'gw',
            'kenya': 'ke',
            'lesotho': 'ls',
            'madagascar': 'mg',
            'malawi': 'mw',
            'mauritania': 'mr',
            'morocco': 'ma',
            'niger': 'ne',
            'nigeria': 'ng',
            'sao tome and principe': 'st',
            'south africa': 'za',
            'south sudan': 'ss',
            'sudan': 'sd',
            'togo': 'tg',
            'uganda': 'ug',
            'western sahara': 'eh',
            'zimbabwe': 'zw',
            'french southern territories': 'tf',
            'saint helena, ascension and tristan da cunha': 'sh',
            'runion': 're',
            'mayotte': 'yt',
            'cabo verde': 'cv',
            'comoros': 'km',
            'bouvet island': 'bv'
        },
        'Antarctica': {
            'antarctica': 'aq'
        },
        'Oceanic-Australasian': {
            'micronesia, federated states of': 'fm',
            'new zealand': 'nz',
            'palau': 'pw',
            'solomon islands': 'sb',
            'tuvalu': 'tv',
            'nauru': 'nr',
            'kiribati': 'ki',
            'australia': 'au',
            'fiji': 'fj',
            'vanuatu': 'vu',
            'marshall islands': 'mh',
            'tonga': 'to',
            'timor-leste': 'tl',
            'samoa': 'ws',
            'tokelau': 'tk',
            'french polynesia': 'pf',
            'american samoa': 'as',
            'christmas island': 'cx',
            'pitcairn': 'pn',
            'cook islands': 'ck',
            'northern mariana islands': 'mp',
            'niue': 'nu',
            'guam': 'gu',
            'heard island and mcdonald islands': 'hm',
            'new caledonia': 'nc',
            'cocos (keeling) islands': 'cc',
            'wallis and futuna': 'wf',
            'norfolk island': 'nf'
        },
        'Asia': {
            'japan': 'jp',
            'iran, islamic republic of': 'ir',
            'azerbaijan': 'az',
            'uzbekistan': 'uz',
            'bhutan': 'bt',
            'mongolia': 'mn',
            'bahrain': 'bh',
            'kazakhstan': 'kz',
            'kyrgyzstan': 'kg',
            'kuwait': 'kw',
            'philippines': 'ph',
            'lebanon': 'lb',
            'malaysia': 'my',
            'afghanistan': 'af',
            'qatar': 'qa',
            'turkmenistan': 'tm',
            'nepal': 'np',
            'united arab emirates': 'ae',
            'sri lanka': 'lk',
            'china': 'cn',
            'armenia': 'am',
            'palestine, state of': 'ps',
            'korea, republic of': 'kr',
            'pakistan': 'pk',
            'myanmar': 'mm',
            'papua new guinea': 'pg',
            'bangladesh': 'bd',
            'brunei darussalam': 'bn',
            'cambodia': 'kh',
            'taiwan, province of china': 'tw',
            'south georgia and the south sandwich islands': 'gs',
            'british indian ocean territory': 'io',
            'india': 'in',
            'indonesia': 'id',
            'iraq': 'iq',
            'israel': 'il',
            'jordan': 'jo',
            'maldives': 'mv',
            'korea, democratic people\'s republic of': 'kp',
            'oman': 'om',
            'russian federation': 'ru',
            'saudi arabia': 'sa',
            'singapore': 'sg',
            'syrian arab republic': 'sy',
            'tajikistan': 'tj',
            'thailand': 'th',
            'turkey': 'tr',
            'viet nam': 'vn',
            'yemen': 'ye',
            'hong kong': 'hk',
            'georgia': 'ge',
            'macao': 'mo',
            'lao people\'s democratic republic': 'la'
        }
    }

    # Store the time cutoffs for the last five years.
    dates = [
        1508111137,
        1476489600,
        1444867200,
        1413331200,
        1381795200,
        1350259200
    ]

    # Load user information
    Users = []
    f = open('allUserGpsLocations2.txt','r')
    for line in f.readlines():
        try:
            elements = line.strip().split(';')
            userId = elements[0]
            country = elements[3]
            city = elements[4]
            state = elements[5]
            Users.append((userId, country, city, state))
        except:
            print('Unable to process user: {}'.format(userId))
    f.close()

    ContCounts = {
        'North America': 0,
        'South America': 0,
        'Europe': 0,
        'Africa': 0,
        'Antarctica': 0,
        'Oceanic-Australasian': 0,
        'Asia': 0
    }

    ContCountryCounts = {
        'North America': {},
        'South America': {},
        'Europe': {},
        'Africa': {},
        'Antarctica': {},
        'Oceanic-Australasian': {},
        'Asia': {}
    } 

    # Go through users in the current time and increase counts.
    for user in Users:
            
        # Identify the continent
        found = False
        for continent, countries in Continents.items():
            for country, code in countries.items():
                if code == user[1]:
                    ContCounts[continent] += 1

                    if(code in ContCountryCounts[continent].keys()):
                        # ContCountryCounts[continent][code] += 1

                        if user[3] != '':
                            if(user[3] in ContCountryCounts[continent][code].keys()):
                                ContCountryCounts[continent][code][user[3]] += 1
                            else:
                                ContCountryCounts[continent][code][user[3]] = 1 
                    else:
                        #ContCountryCounts[continent][code] = 1

                        if user[3] != '':
                            ContCountryCounts[continent][code] = { user[3]: 1 }


                    found = True
                    break
            if found:
                break

    for continent, countries in ContCountryCounts.items():
        print('{}: {}'.format(continent, ContCounts[continent]))
        for country, cities in countries.items():
            for city, count in cities.items():
                print('    {:20} -- {:20}: {}'.format(country, city, count))
        print('')

    '''
    # Print the results to an output file.
    f = open('LocationsOverTime.csv', 'w')
    output0 = ''
    output1 = 'North America'
    output2 = 'South America'
    output3 = 'Europe'
    output4 = 'Africa'
    output5 = 'Antarctica'
    output6 = 'Oceanic-Australasian'
    output7 = 'Asia'
    for year in LocationsOverTime:
        output0 += ',' + year[0]
        output1 += ',' + str(year[3]['North America'])
        output2 += ',' + str(year[3]['South America'])
        output3 += ',' + str(year[3]['Europe'])
        output4 += ',' + str(year[3]['Africa'])
        output5 += ',' + str(year[3]['Antarctica'])
        output6 += ',' + str(year[3]['Oceanic-Australasian'])
        output7 += ',' + str(year[3]['Asia'])
    f.write(output0 + '\n')
    f.write(output1 + '\n')
    f.write(output2 + '\n')
    f.write(output3 + '\n')
    f.write(output4 + '\n')
    f.write(output5 + '\n')
    f.write(output6 + '\n')
    f.write(output7 + '\n')
    '''
