import plugintools
#from logos import logos_bands

from logos import logos_labels


ALL  = "plugin://plugin.video.youtube/playlist/PL8B6C0DAB78462F56/"
CLASSIC  = "plugin://plugin.video.youtube/playlist/PLFA2085CCB025E3B7/"
A30_ANNIVERSARY = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnmR8YRo70uua6CMoer9ghaY/"

DEATH_GRIND = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnmZiRsVdD4XNhPzCISdEF8j/"
SWEDISH = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnmud_DzzmWhOWXGgDEvExDZ/"
HALLOWEEN = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnlrCJ_o5SP-TmebZWrzXwwv/"
ROCK  = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnluyAbeGkEYE_8bR2m0xYfO/" 
GOTHIC  = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnngg8FvzuP7M0azkhFcYeVa/"
SIRENS  = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnkoDdLRXmJlpjWUPB895WA6/" 
EXTREME  = "plugin://plugin.video.youtube/playlist/PLB1357DD0B2462645/"

LYRICS  = "plugin://plugin.video.youtube/playlist/PL61FB67864E036E68/"
Playthroughs  = "plugin://plugin.video.youtube/playlist/PL84FEBB669200C262/"
  
UNBOXING = "plugin://plugin.video.youtube/playlist/PLVWT5waYZYnk7dVMGVkvO7xOa2CpxeoI6/"

def century1(params):
    #logo=logos_bands.amorphis(params)
    logo=logos_labels.century(params)

    plugintools.add_item( 
        title="All Century Media Records Music Videos",
        url=ALL,
        thumbnail=logo, folder=True )  
       
    plugintools.add_item( 
        title="Classic Century Media Videos",
        url=CLASSIC,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="We Are Century Media - 30 Years Anniversary",
        url=A30_ANNIVERSARY,
        thumbnail=logo, folder=True )  
        

        
    plugintools.add_item( 
        title="Death Metal/Grind (Century Media Bands)",
        url=DEATH_GRIND,
        thumbnail=logo, folder=True )  
        
        
    plugintools.add_item( 
        title="Metal For The Masses - SWEDISH INVASION!",
        url=SWEDISH,
        thumbnail=logo, folder=True )  


    plugintools.add_item( 
        title="Ultimate Halloween Playlist ",
        url=HALLOWEEN,
        thumbnail=logo, folder=True ) 
        
    plugintools.add_item( 
        title="Century Media Rock",
        url=ROCK,
        thumbnail=logo, folder=True ) 
        
        
    plugintools.add_item( 
        title="Gothic Metal",
        url=GOTHIC,
        thumbnail=logo, folder=True ) 

        
    plugintools.add_item( 
        title="Sirens That Slay",
        url=SIRENS,
        thumbnail=logo, folder=True ) 



    plugintools.add_item( 
        title="Leaders of the Extreme!",
        url=EXTREME,
        thumbnail=logo, folder=True )  
        


    plugintools.add_item( 
        title="Century Media Records Lyric Videos",
        url=LYRICS,
        thumbnail=logo, folder=True )
        
        
    plugintools.add_item( 
        title="Tutorials/Playthroughs from Century Media Records' Artists",
        url=Playthroughs,
        thumbnail=logo, folder=True )  
                

    plugintools.add_item( 
        title="Unboxing",
        url=UNBOXING,
        thumbnail=logo, folder=True )  
        

 
 
