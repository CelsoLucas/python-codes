import urllib.parse
import urllib.request

url = 'https://www.nike.com/w?q=jordan&vst=jordan'
parsed_url = urllib.parse.urlparse(url)
print("Componentes da URL:")
print("Esquema:", parsed_url.scheme) 
print("Domínio:", parsed_url.netloc)  
print("Caminho:", parsed_url.path)    
print("Consulta:", parsed_url.query)  