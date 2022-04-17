#file that creates the board and players.

def country_setup():
    countries = {

    #North American Territories
        'Alaska': ['Kamchatka', 'Alberta', 'NW Territory'],
        'NW Territory': ['Alaska', 'Alberta', 'Ontario', 'Greenland'],
        'Alberta' : ['Alaska', 'NW Territory', 'Ontario', 'Western US'],
        'Ontario': ['Alberta', 'Greenland', 'Quebec','Western US', 'Eastern US', 'NW Territory'],
        'Quebec': ['Ontario', 'Eastern US', 'Greenland'],
        'Western US': ['Alberta', 'Ontario', 'Eastern US'],
        'Central America': ['Western US', 'Eastern US'],
        'Eastern US': ['Western US', 'Quebec', 'Ontario', 'Central America'],
        'Greenland': ['NW Territory', 'Ontario', 'Quebec', 'Iceland',],

    #South American Territories
        'Venezuela': ['Peru', 'Brazil'],
        'Peru': ['Brazil', 'Venezuela', 'Argentina'],
        'Brazil': ['Venezuela', 'Argentina', 'Peru', 'Northern Africa'],
        'Argentina': ['Peru', 'Brazil'],

    #Africa
        'Northern Africa': ['Egypt', 'Brazil', 'Congo', 'Eastern Africa', 'Western Europe', 'Southern Europe'],
        'Egypt': ['Eastern Africa', 'Middle East', 'Southern Europe', 'Northern Africa'],
        'Eastern Africa': ['Egypt', 'Congo', 'Southern Africa', 'Madagascar'],
        'Congo': ['Southern Africa', 'Eastern Africa', 'Northern Africa'],
        'Southern Africa': ['Madagascar', 'Congo', 'Eastern Africa'],
        'Madagascar': ['Southern Africa', 'Eastern Africa'],

    #Oceania
        'Western Australia': ['Indonesia', 'New Guinea', 'Eastern Australia'],
        'Eastern Australia': ['New Guinea', 'Western Australia'],
        'New Guinea': ['Indonesia', 'Western Australia', 'Eastern Australia'],
        'Indonesia': ['New Guinea', 'Western Australia', 'Siam'],

    #Europe
        'Western Europe': ['Great Britain', 'Northern Africa', 'Southern Europe', 'Northern Europe'],
        'Great Britain': ['Iceland', 'Scandinavia', 'Northern Europe', 'Western Europe'],
        'Northern Europe': ['Great Britain', 'Scandinavia', 'Ukraine', 'Southern Europe', 'Western Europe'],
        'Iceland': ['Great Britain', 'Scandinavia', 'Greenland',],
        'Scandinavia': ['Ukraine', 'Iceland', 'Great Britain', 'Northern Europe'],
        'Southern Europe': ['Western Europe', 'Middle East', 'Northern Africa', 'Egypt', 'Northern Europe', 'Ukraine'],
        'Ukraine': ['Scandinavia', 'Northern Europe', 'Southern Europe', 'Middle East', 'Afghanistan', 'Ural'],

    #Asia
        'Middle East': ['Egypt', 'Ukraine', 'Southern Europe', 'Afghanistan', 'India'],
        'India': ['Middle East', 'Afghanistan', 'China', 'Siam'],
        'Siam': ['Indonesia', 'China', ],
        'China': ['Siam', 'India', 'Afghanistan', 'Ural', 'Siberia', 'Mongolia'],
        'Afghanistan': ['Ukraine', 'China', 'Ural', 'Middle East', 'India', ],
        'Ural': ['Ukraine', 'Siberia', 'China', 'Afghanistan', ],
        'Siberia': ['Ural', 'China', 'Mongolia' , 'Irkutsk', 'Yakutsk'],
        'Yakutsk': ['Siberia', 'Irkutsk', 'Kamchatka'],
        'Kamchatka': ['Alaska', 'Japan', 'Mongolia', 'Irkutsk', 'Yakutsk'],
        'Irkutsk': ['Mongolia', 'Siberia', 'Yakutsk', 'Kamchatka'],
        'Japan': ['Mongolia', 'Kamchatka'],
        'Mongolia': ['Siberia', 'China', 'Irkutsk', 'Japan']
    }

    return(countries)