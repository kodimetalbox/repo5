import plugintools


from logos import logos_guitar


_280 = "plugin://plugin.video.youtube/playlist/PLlIXsXPSwnwkGGLTcot2_HU1lOz_2GFOZ/"
HP  = "plugin://plugin.video.youtube/playlist/PLXg-lxs-OztOJV0O_rSSHPCT6f8pYjccs/"
_2020 = "plugin://plugin.video.youtube/playlist/PLEOX-VnEHlPRu7U2yp8bII4UPjHaturg3/"
_1920  = "plugin://plugin.video.youtube/playlist/PLDtEhCmtpLd-4MrgWLx2LYHjuB3o6Zw6h/"

CPM1 = "plugin://plugin.video.youtube/playlist/PLUyML3-RrWa-SE52WN6YcuEbJdj1F49ut/"
CPM2  = "plugin://plugin.video.youtube/playlist/PLO0-HZEy-V3C22bVtU-9WkVVCB4qcRXCW/"
BC = "plugin://plugin.video.youtube/playlist/PLvRs1UwA0RZ3cWsRh7leuhpSSOibNwmFn/"
_1000  = "plugin://plugin.video.youtube/playlist/PLqYXv_L7NiEyWdU0CBKh8FlqRc2EY4lqs/"
TOP100  = "plugin://plugin.video.youtube/playlist/PLwnBXVpo3GDB0wziaiaW3IqkWgLS_AcN7/"


def power1(params):
    logo=logos_guitar.logo_07(params)
    
    plugintools.add_item( 
        title="Heavy Power Metal Videos",
        url=HP,
        thumbnail=logo, folder=True )
        

    plugintools.add_item( 
        title="Best Power Metal Songs of All Time EVER! 280 Bands on 1 Playlist",
        url=_280,
        thumbnail=logo, folder=True )  
       

   
    plugintools.add_item( 
        title="Best 2020s Power Metal Songs!",
        url=_2020,
        thumbnail=logo, folder=True )  
       
    plugintools.add_item( 
        title="Power metal 2019-2020",
        url=_1920,
        thumbnail=logo, folder=True )
   
   
        

    plugintools.add_item( 
        title="Classic Power Metal Vol. 1",
        url=CPM1,
        thumbnail=logo, folder=True )  
       
    plugintools.add_item( 
        title="Classic Power Metal Vol. 2",
        url=CPM2,
        thumbnail=logo, folder=True )
        
   
    plugintools.add_item( 
        title="Best Power Metal Classics",
        url=BC,
        thumbnail=logo, folder=True )  

    plugintools.add_item( 
        title="Power Metal Music Education: 1000 of the Greatest Songs",
        url=_1000,
        thumbnail=logo, folder=True )
       
    plugintools.add_item( 
        title="Top 100: Power Metal",
        url=TOP100,
        thumbnail=logo, folder=True )

