import plugintools


from logos import logos_guitar


_100  = "plugin://plugin.video.youtube/playlist/PLhQCJTkrHOwSX8LUnIMgaTq3chP1tiTut/"
CLASSIC  = "plugin://plugin.video.youtube/playlist/PLzXCQ595AwdmXPh-SKnYUX0WHd519Glue/"
METAL = "plugin://plugin.video.youtube/playlist/PLWUXmX2htJ7Nx2_luG8WAVEnShOW-lGal/"

SPOTIFY = "plugin://plugin.video.youtube/playlist/PLhwykgk4XwFkeKjyFQYEmH-MHwPRKPGA5/"
_2021 = "plugin://plugin.video.youtube/playlist/PL3oW2tjiIxvQO6yqJEkrP47yYG_pJ7XJU/"
MELODIC = "plugin://plugin.video.youtube/playlist/PLyNluqYn9ZuiK_HyJeUa1hSOT0t4oIbC0/"
COVER  = "plugin://plugin.video.youtube/playlist/PLjtWZjV2yK5TX0aJ0O47Qe_wN0Tpa57HW/" 





def best1(params):
    logo=logos_guitar.logo_04(params)
    plugintools.add_item( 
        title="100 Best Metal Songs of all time",
        url=_100,
        thumbnail=logo, folder=True )  
       
    plugintools.add_item( 
        title="Best Heavy Metal Classics Playlist Ever Made",
        url=CLASSIC,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Best Metal Songs of All Time - Top Heavy Metal Music Playlist",
        url=METAL,
        thumbnail=logo, folder=True )  
        

        
    plugintools.add_item( 
        title="Spotify's Metal Essentials Playlist",
        url=SPOTIFY,
        thumbnail=logo, folder=True )  
        
        
    plugintools.add_item( 
        title="Top Metal 2021  Ultimate Hard Rock & Heavy Metal Playlist 2021",
        url=_2021,
        thumbnail=logo, folder=True )  


    plugintools.add_item( 
        title="Melodic Metal Movement",
        url=MELODIC,
        thumbnail=logo, folder=True ) 
        
    plugintools.add_item( 
        title="100 Best Metal Covers",
        url=COVER,
        thumbnail=logo, folder=True ) 
        
   
