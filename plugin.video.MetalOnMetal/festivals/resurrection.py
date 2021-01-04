import plugintools
from logos import logos_festivals

_2020 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy09SDil5kqb_dO1PKmSV7Tu/"
_2019 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy2z9Ny1X0R2tZMHE4F6rL11/"
_2018 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy0f_obllTKr_CpivVyTarKm/"
_2017 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy13ZyWSou-cMJA3eEn3JkpW/"
_2016 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy2E3NblQ5m-FI83b653Jkb_/"
_2015 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy0UqBGj1-ZxNaxOPDKrtmu3/"
_2014 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy1ioBPyUAJKuQjQEbtCndC9/"
EXODUS = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy3vlXGVhkfMgIx982OaLU9N/"
BIOHAZARD = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy0JEkOgqFyVT0g6-aEi-_Oj/"
LAMBOFGOD = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy2ZLHLy4fBxgIN23yU93uHl/"
TRIVIUM = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy1iCs4pYl2Wf6FWSqcQQ9kr/"
_2012 = "plugin://plugin.video.youtube/playlist/PLS7iEf0zVCy0cOjy_R27hltRkiBS1cr-I/"

def resurrection1(params):
    logo=logos_festivals.resurrection(params)
     
    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2020 - Stay at home",
        url=_2020,
        thumbnail=logo, folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2019",
        url=_2019,
        thumbnail=logo, folder=True ) 
 
    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2018",
        url=_2018,
        thumbnail=logo, folder=True ) 
       
    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2017",
        url=_2017,
        thumbnail=logo, folder=True ) 
 
    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2016",
        url=_2016,
        thumbnail=logo, folder=True ) 
        
    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2015",
        url=_2015,
        thumbnail=logo, folder=True ) 
 
    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2014",
        url=_2014,
        thumbnail=logo, folder=True ) 
        
        
    plugintools.add_item( 
        #action="", 
        title="Exodus - Resurrection Fest 2013",
        url=EXODUS,
        thumbnail=logo, folder=True ) 
 
    plugintools.add_item( 
        #action="", 
        title="Biohazard - Resurrection Fest 2013",
        url=BIOHAZARD,
        thumbnail=logo, folder=True ) 
        
    plugintools.add_item( 
        #action="", 
        title="Lamb of God - Resurrection Fest 2013",
        url=LAMBOFGOD,
        thumbnail=logo, folder=True ) 
 
    plugintools.add_item( 
        #action="", 
        title="Trivium - Resurrection Fest 2013",
        url=TRIVIUM,
        thumbnail=logo, folder=True ) 
 
    plugintools.add_item( 
        #action="", 
        title="Resurrection Fest 2012",
        url=_2012,
        thumbnail=logo, folder=True ) 
        
