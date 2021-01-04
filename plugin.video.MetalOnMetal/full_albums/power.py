import plugintools


from logos import logos_guitar



P01  = "plugin://plugin.video.youtube/playlist/PL5JVKTZDw2DIpIorxoGMbn3m1SZc47_5v/"
P02  = "plugin://plugin.video.youtube/playlist/PLon80IwDVRqAuTxGeYqE3uKTAx8Xz8TAV/"
P03  = "plugin://plugin.video.youtube/playlist/PL5JVKTZDw2DKmZBG42LB2yezLIvx1bRKF/"
P04  = "plugin://plugin.video.youtube/playlist/PLRf2J11NUd0JGcFH__AhdRjH312H5ZNZm/"



def power1(params):
    logo=logos_guitar.logo_08(params)
    
    plugintools.add_item( 
        title="Power Metal Full Albums (I)",
        url=P01,
        thumbnail=logo, folder=True )
        

    
    plugintools.add_item( 
        title="Power Metal Full Albums (II)",
        url=P02,
        thumbnail=logo, folder=True )
        
    
    plugintools.add_item( 
        title="Power Metal Full Albums (III)",
        url=P03,
        thumbnail=logo, folder=True )
        
    
    plugintools.add_item( 
        title="Power Metal Full Albums (IV)",
        url=P04,
        thumbnail=logo, folder=True )
        
  
