import BeautifulSoup
import re

tetLookedUp = "Caprock Academy"
columns = soup.findAll('h3', text = re.compile(tetLookedUp), attrs = {'class' : 'LC20lb DKV0Md'})

