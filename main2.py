
import requests 
import bs4 

print('''    \033[92m

██╗      █████╗     ███╗   ███╗███████╗████████╗███████╗ ██████╗ 
██║     ██╔══██╗    ████╗ ████║██╔════╝╚══██╔══╝██╔════╝██╔═══██╗
██║     ███████║    ██╔████╔██║█████╗     ██║   █████╗  ██║   ██║
██║     ██╔══██║    ██║╚██╔╝██║██╔══╝     ██║   ██╔══╝  ██║   ██║
███████╗██║  ██║    ██║ ╚═╝ ██║███████╗   ██║   ███████╗╚██████╔╝
╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ 
                                                                  by badr sifaoui !!

     
''')


while True:



    
        


 
# Taking thecity name as an input from the user 
   city = input('  Enter your city name : ')
  
# Generating the url   
   url = "https://google.com/search?q=weather+in+" + city 
  
# Sending HTTP request  
   request_result = requests.get( url ) 
  
   soup = bs4.BeautifulSoup( request_result.text  
                         , "html.parser" ) 
  
# Finding temperature in Celsius. 
# The temperature is stored inside the class "BNeawe".  
   temp = soup.find( "div" , class_='BNeawe' ).text  

   print('--------------')    
   print( temp )  
   print('--------------')





































