# -*- coding: utf-8 -*-
#------------------------------------------------------------

import plugintools

from logos import logos_guitar

XXI  = "plugin://plugin.video.youtube/playlist/PL48A141CBC5965002/"
ACERO  = "plugin://plugin.video.youtube/playlist/PL3EAC9C1D4E97AFF2/"
HME = "plugin://plugin.video.youtube/playlist/PLglLEhldqRTMAKfTxkF7trIOp_GdLugdE/"
_80_90 = "plugin://plugin.video.youtube/playlist/PLZj2HROfo5c8PPhF-18ffJHOu2AfvDSZf/"
TOP20 = "plugin://plugin.video.youtube/playlist/PLF4mb3b-Y6burdjz_YAq9S7aJ9JQkNKcS/"
HEAVY = "plugin://plugin.video.youtube/playlist/PL4A0jrfkoDjAQB3z_ab1vnPpun9A76X-m/" 
_80  = "plugin://plugin.video.youtube/playlist/PLd-iUXSuOEbrEv_1PHJ1gUTjh4Yo2nsfI/" 
_70_80  = "plugin://plugin.video.youtube/playlist/PLrnl_9jiwB9UrWElBue1G-h5OcFb1v_JB/" 




def spanish1(params):
    logo=logos_guitar.logo_04(params)

    plugintools.add_item( 
        title="Spanish Metal XXI",
        url=XXI,
        thumbnail=logo, folder=True )  
       

    plugintools.add_item( 
        title="Cuerdas de Acero",
        url=ACERO,
        thumbnail=logo, folder=True )
        
    plugintools.add_item( 
        title="Heavy Metal Español ",
        url=HME,
        thumbnail=logo, folder=True )       
  
      
    plugintools.add_item( 
        title="Grupos de heavy y rock en España de los 80 a los 90",
        url=_80_90,
        thumbnail=logo, folder=True )  
        
        
    plugintools.add_item( 
        title="TOP 20 Bandas de Heavy Metal en español de España",
        url=TOP20,
        thumbnail=logo, folder=True )  


    plugintools.add_item( 
        title="Rock/ Hard Rock/ Heavy Metal Español",
        url=HEAVY,
        thumbnail=logo, folder=True ) 

        
    plugintools.add_item( 
        title="Lo mejor del Heavy Metal español de los 80",
        url=_80,
        thumbnail=logo, folder=True )         

       
    plugintools.add_item( 
        title="Arte: Rock & Heavy 70s 80s en Español",
        url=_70_80,
        thumbnail=logo, folder=True )         
   
