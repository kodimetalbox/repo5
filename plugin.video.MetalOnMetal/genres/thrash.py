# -*- coding: utf-8 -*-
#------------------------------------------------------------
import plugintools
from logos import logos_guitar

NUCLEARBLAST = "plugin://plugin.video.youtube/playlist/PLB4brr7vf-P4ocoTLNNB-tQEao4T5doxp/"
RELAPSE = "plugin://plugin.video.youtube/playlist/PLq6NULtuhFunARjAXTLeb5i_pErL84gnP/"
PLAYLIST = "plugin://plugin.video.youtube/playlist/PL5fRL6A4m-DFl8TkofBGy8uxbZrBbmwhE/"

BEST  = "plugin://plugin.video.youtube/playlist/PLHQpsO1FrfZ1fAG_Jj2tHRUPZsx2Xae9E/"

TMV1  = "plugin://plugin.video.youtube/playlist/PLVQYYTxTxpYdNHHetjaMaZkCVmYK6ZfCL/"
TMV2  = "plugin://plugin.video.youtube/playlist/PLUuCtr3VjoK2VCuqD4WQmd7BZteKLhPAm/"
TMV3  = "plugin://plugin.video.youtube/playlist/PLkdSC3c33L8mradkKNUxDqQl4DM48wMCH/"
TMV4 = "plugin://plugin.video.youtube/playlist/PL9BD30D6B37987485/"
TMV5  = "plugin://plugin.video.youtube/playlist/PLcNmBW5DYbVY1bZSowzo6w-TbIs-79jj7/"
TMV6  = "plugin://plugin.video.youtube/playlist/PLvDtqwUzmWY3A6fcLyuW_IBxCWrfQdF3y/"
TMV7 = "plugin://plugin.video.youtube/playlist/PLE00DBD3756C9D3EA/"
TMV8 = "plugin://plugin.video.youtube/playlist/PLANWERo6LlcWRjS9HXabX-n86UdqRxLth/"

TMV9  = "plugin://plugin.video.youtube/playlist/PL49044935EDF00826/"
TMV10  = "plugin://plugin.video.youtube/playlist/PL3A86604E8F246357/"
OLDSCHOOL2 = "plugin://plugin.video.youtube/playlist/PL-5fe781eQt8dPDdbJ9fV3sxYk5tL5TuM/"
MODERN = "plugin://plugin.video.youtube/playlist/PL4n8hcWsobePvu90zGWt8Q4roHO3a4kzR/"

DEATH  = "plugin://plugin.video.youtube/playlist/PLi-xhtW1nwLo1BhZwIpPrfu0rbUodFzXG/"


NEWWAVE  = "plugin://plugin.video.youtube/playlist/PL_JE4b6_wstVQCUaM50K8IG7BYAw8kMzW/"
OLDSCHOOL3  = "plugin://plugin.video.youtube/playlist/PLvkFzI_b6HNV_pf6ICj4t0dvikjFgXd-J/"


_2019  = "plugin://plugin.video.youtube/playlist/PLXg-lxs-OztPr_GmXX7qdcr3liV-8y-NZ/"
_2019_  = "plugin://plugin.video.youtube/playlist/PLXg-lxs-OztP7Mlzos_cuWFTWLIWdCVfl/"
_2018  = "plugin://plugin.video.youtube/playlist/PLXg-lxs-OztNWd2Rnr5zS5O2j8FXm_1ar/"



NV  = "plugin://plugin.video.youtube/playlist/PLXg-lxs-OztOf7ch6dr3MCTQV4x0-t8WP/"
LIVE  = "plugin://plugin.video.youtube/playlist/PLXg-lxs-OztPDS0b3HRV1iM2X-THuy2jo/"
CARTOONS  = "plugin://plugin.video.youtube/playlist/PLhHaGCkTYWKhMCIjrOU0J9WBO-SQxfFQc/"
LIVE2  = "plugin://plugin.video.youtube/playlist/PLXg-lxs-OztOlYbAybFMGN6T-hVGEG0_u/"

def thrash1(params):
    logo=logos_guitar.logo_07(params)

    plugintools.add_item( 
        title="Thrashing Cartoons [Caricaturas thrashers]",
        url=CARTOONS,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Thrash Death Old School New Videos",
        url=NV,
        thumbnail=logo, folder=True )

    plugintools.add_item( 
        title="Thrash Metal / Speed Metal - Nuclear Blast Records",
        url=NUCLEARBLAST,
        thumbnail=logo, folder=True )  
 
    plugintools.add_item( 
        title="THRASH METAL - Relapse Records",
        url=RELAPSE,
        thumbnail=logo, folder=True )


    plugintools.add_item( 
        title="Modern Thrash Videos",
        url=MODERN,
        thumbnail=logo, folder=True )  
      



   
    plugintools.add_item( 
        title="New Wave of Thrash Metal",
        url=NEWWAVE,
        thumbnail=logo, folder=True )  


    plugintools.add_item( 
        title="Thrash Metal New School 2018",
        url=_2018,
        thumbnail=logo, folder=True )
        
 
        

    plugintools.add_item( 
        title="Thrash Metal New School 2019 (I)",
        url=_2019,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Thrash Metal New School 2019 (II)",
        url=_2019_,
        thumbnail=logo, folder=True )
        


    plugintools.add_item( 
        title="Thrash Death Metal New School Live",
        url=LIVE,
        thumbnail=logo, folder=True )
        

        
        
    plugintools.add_item( 
        title="Old School Metal Live Videos",
        url=LIVE2,
        thumbnail=logo, folder=True )
                

     
    plugintools.add_item( 
        title="The Best Thrash Metal videos of all time +800 Videos",
        url=BEST,
        thumbnail=logo, folder=True )


    plugintools.add_item( 
        title="Thrash / Death",
        url=DEATH,
        thumbnail=logo, folder=True )  
       



    plugintools.add_item( 
        title="Old School Thrash Metal (I)",
        url=PLAYLIST,
        thumbnail=logo, folder=True )  


  
    plugintools.add_item( 
        title="Old School Thrash Metal (II)",
        url=OLDSCHOOL2,
        thumbnail=logo, folder=True )  
      

    plugintools.add_item( 
        title="Old School Thrash Metal (III)",
        url=OLDSCHOOL3,
        thumbnail=logo, folder=True )



        
    plugintools.add_item( 
        title="Thrash Metal Videos 1",
        url=TMV1,
        thumbnail=logo, folder=True )
        
   
    plugintools.add_item( 
        title="Thrash Metal Videos 2",
        url=TMV2,
        thumbnail=logo, folder=True )
   
    plugintools.add_item( 
        title="Thrash Metal Videos 3",
        url=TMV3,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Thrash Metal Videos 4",
        url=TMV4,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Thrash Metal Videos 5",
        url=TMV5,
        thumbnail=logo, folder=True )  
  
    plugintools.add_item( 
        title="Thrash Metal Videos 6",
        url=TMV6,
        thumbnail=logo, folder=True )  
      
    plugintools.add_item( 
        title="Thrash Metal Videos 7",
        url=TMV7,
        thumbnail=logo, folder=True )  
      
    plugintools.add_item( 
        title="Thrash Metal Videos 8",
        url=TMV8,
        thumbnail=logo, folder=True )  

    plugintools.add_item( 
        title="Thrash Metal Videos 9",
        url=TMV9,
        thumbnail=logo, folder=True )  

    plugintools.add_item( 
        title="Thrash Metal Videos 10",
        url=TMV10,
        thumbnail=logo, folder=True )  

   
   
