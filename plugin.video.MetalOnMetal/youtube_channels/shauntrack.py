import plugintools


from logos import logos_youtube_channels


METAL = "plugin://plugin.video.youtube/playlist/PLgyUYejNPEs2N30vrCZHF6sgae6teIUjs/"
ROCKPOP  = "plugin://plugin.video.youtube/playlist/PLgyUYejNPEs2pL_5qiAEe1V5hIw7rlUjy/"

def shauntrack1(params):
    logo=logos_youtube_channels.shauntrack(params)

    plugintools.add_item( 
        title="Metal",
        url=METAL,
        thumbnail=logo, folder=True )  
       
    plugintools.add_item( 
        title="Rock/Pop",
        url=ROCKPOP,
        thumbnail=logo, folder=True )
        

        
   
