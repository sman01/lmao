from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
from itertools import zip_longest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
# Converting datetime object to string
iz=0
def err(url,no):
    if no<5:
        try:
            time.sleep(100)
            result = requests.get(url,headers=headers)
            print(result.status_code)
            print('why')
            return result.status_code
        except:
            print("error")
            time.sleep(150)
            return 2
            
    else:
        return 3
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}

reve=0

#models and manufacturers


acura=['ilx', 'mdx', 'nsx', 'rdx', 'rlx', 'tlx', 'cl', 'ilx-hybrid', 'integra', 'legend', 'rl', 'rsx', 'slx', 'tl', 'tsx', 'tsx-sport-wagon', 'vigor', 'zdx']
alfa=[ '4c', 'giulia', 'stelvio']
aston=['db11', 'dbs-superleggera', 'dbx', 'rapide-amr', 'vantage', 'db7', 'db9', 'db9-gt', 'dbs', 'rapide', 'rapide-s', 'v12-vanquish', 'v12-vantage', 'v12-vantage-s', 'v8-vantage', 'vanquish', 'vanquish-s', 'virage']
audi=['a3', 'a4', 'a4-allroad', 'a5', 'a6', 'a6-allroad', 'a7', 'a8', 'e-tron', 'e-tron-sportback', 'q3', 'q5', 'q7', 'q8', 'r8', 'rs-3', 'rs-5', 's3', 's4', 's5', 's6', 's7', 's8', 'sq5', 'sq7', 'sq8', 'tt', 'tt-rs', 'tts', '100', '200', '80', '90', 'a3-sportback-e-tron', 'allroad', 'allroad-quattro', 'cabriolet', 'coupe', 'rs-4', 'rs-6', 'rs-7', 'v8']
bentley=['bentayga', 'continental', 'flying-spur', 'mulsanne', 'arnage', 'azure', 'azure-t', 'brooklands', 'continental-flying-spur', 'continental-flying-spur-speed', 'continental-gt', 'continental-gt-speed', 'continental-gt-speed-convertible', 'continental-gt3-r', 'continental-gtc', 'continental-gtc-speed', 'continental-supersports', 'continental-supersports-convertible', 'supersports-convertible-isr']
bmw=['2-series', '2-series-gran-coupe', '3-series', '3-series-gran-turismo', '4-series', '4-series-gran-coupe', '5-series', '6-series-gran-coupe', '6-series-gran-turismo', '7-series', '8-series', '8-series-gran-coupe', 'alpina-b6-gran-coupe', 'alpina-b7', 'i3', 'i8', 'm2', 'm4', 'm4-cs', 'm5', 'm6-gran-coupe', 'm8', 'm8-gran-coupe', 'x1', 'x2', 'x3', 'x3-m', 'x4', 'x4-m', 'x5', 'x5-m', 'x6', 'x6-m', 'x7', 'z4', '1-series', '1-series-m', '3-series-edrive', '5-series-gran-turismo', '6-series', 'activehybrid-5', 'activehybrid-7', 'activehybrid-x6', 'alpina', 'm', 'm3', 'm3-cs', 'm4-gts', 'm6', 'x5-edrive', 'z3', 'z4-m', 'z8']
buick=['cascada', 'enclave', 'encore', 'encore-gx', 'envision', 'lacrosse', 'regal-sportback', 'regal-tourx', 'century', 'electra', 'estate-wagon', 'lesabre', 'lucerne', 'park-avenue', 'rainier', 'reatta', 'regal', 'rendezvous', 'riviera', 'roadmaster', 'skylark', 'terraza', 'verano']
cadillac=['ats-coupe', 'ats-v', 'ct4', 'ct5', 'ct6', 'ct6-v', 'cts', 'cts-v', 'escalade', 'escalade-esv', 'xt4', 'xt5', 'xt6', 'xts', 'allante', 'ats', 'brougham', 'catera', 'cts-coupe', 'cts-wagon', 'cts-v-coupe', 'cts-v-wagon', 'deville', 'dts', 'eldorado', 'elr', 'escalade-ext', 'escalade-hybrid', 'fleetwood', 'seville', 'sixty-special', 'srx', 'sts', 'sts-v', 'xlr', 'xlr-v']
chevrolet=['blazer', 'bolt-ev', 'camaro', 'colorado', 'corvette', 'cruze', 'equinox', 'express', 'express-cargo', 'impala', 'malibu', 'silverado-1500', 'silverado-1500-ld', 'silverado-2500hd', 'silverado-3500hd', 'sonic', 'spark', 'suburban', 'tahoe', 'trailblazer', 'traverse', 'trax', 'volt', 'astro', 'astro-cargo', 'avalanche', 'aveo', 'beretta', 'black-diamond-avalanche', 'c/k-1500-series', 'c/k-2500-series', 'c/k-3500-series', 'caprice', 'captiva-sport', 'cavalier', 'celebrity', 'chevy-van', 'chevy-van-classic', 'city-express', 'classic', 'cobalt', 'corsica', 'corvette-stingray', 'cruze-limited', 'hhr', 'impala-limited', 'lumina', 'lumina-minivan', 'malibu-classic', 'malibu-hybrid', 'malibu-limited', 'malibu-maxx', 'metro', 'monte-carlo', 'prizm', 'r/v-3500-series', 's-10', 's-10-blazer', 'silverado-1500-classic', 'silverado-1500-hybrid', 'silverado-1500hd', 'silverado-1500hd-classic', 'silverado-2500', 'silverado-2500hd-classic', 'silverado-3500', 'silverado-3500-classic', 'spark-ev', 'sportvan', 'ss', 'ssr', 'tahoe-hybrid', 'tahoe-limited/z71', 'tracker', 'trailblazer-ext', 'uplander', 'venture']
chrysler=['300', 'pacifica', 'pacifica-hybrid', 'voyager', '200', '300m', 'aspen', 'cirrus', 'concorde', 'crossfire', 'grand-voyager', 'imperial', 'le-baron', 'lhs', 'new-yorker', 'prowler', 'pt-cruiser', 'sebring', 'tc', 'town-and-country']
dodge=['challenger', 'charger', 'durango', 'grand-caravan', 'journey', 'avenger', 'caliber', 'caravan', 'colt', 'dakota', 'dart', 'daytona', 'dynasty', 'intrepid', 'magnum', 'monaco', 'neon', 'nitro', 'omni', 'ram-150', 'ram-250', 'ram-350', 'ram-50-pickup', 'ram-cargo', 'ram-pickup-1500', 'ram-pickup-2500', 'ram-pickup-3500', 'ram-van', 'ram-wagon', 'ramcharger', 'shadow', 'spirit', 'sprinter', 'sprinter-cargo', 'srt-viper', 'stealth', 'stratus', 'viper']
ferrari=['488-gtb', '488-spider', 'portofino', '360', '430-scuderia', '456m', '458-italia', '550', '575m', '599', '612-scaglietti', '812-superfast', 'california', 'california-t', 'enzo', 'f12-berlinetta', 'f430', 'ff', 'gtc4lusso', 'superamerica']
ford=['bronco-sport', 'ecosport', 'edge', 'escape', 'escape-plug-in-hybrid', 'expedition', 'explorer', 'f-150', 'f-250-super-duty', 'f-350-super-duty', 'f-450-super-duty', 'fiesta', 'flex', 'fusion', 'fusion-energi', 'fusion-hybrid', 'fusion-plug-in-hybrid', 'mustang', 'mustang-mach-e', 'ranger', 'shelby-gt350', 'shelby-gt500', 'taurus', 'transit-cargo-van', 'transit-connect', 'transit-crew-van', 'transit-passenger-van', 'transit-van', 'transit-wagon', 'aerostar', 'aspire', 'bronco', 'bronco-ii', 'c-max-energi', 'c-max-hybrid', 'contour', 'contour-svt', 'crown-victoria', 'e-150', 'e-250', 'e-350', 'e-series-van', 'e-series-wagon', 'econoline-cargo', 'econoline-wagon', 'escape-hybrid', 'escort', 'excursion', 'expedition-el', 'explorer-sport', 'explorer-sport-trac', 'f-150-heritage', 'f-150-svt-lightning', 'f-250', 'f-350', 'festiva', 'five-hundred', 'focus', 'focus-rs', 'focus-st', 'freestar', 'freestyle', 'gt', 'ltd-crown-victoria', 'mustang-svt-cobra', 'probe', 'taurus-x', 'tempo', 'thunderbird', 'windstar', 'windstar-cargo']
honda=['accord', 'accord-hybrid', 'civic', 'clarity', 'cr-v', 'cr-v-hybrid', 'fit', 'hr-v', 'insight', 'odyssey', 'passport', 'pilot', 'ridgeline', 'accord-crosstour', 'accord-plug-in-hybrid', 'civic-crx', 'civic-del-sol', 'cr-z', 'crosstour', 'element', 'fit-ev', 'prelude', 's2000']
hyundai=['accent', 'azera', 'elantra', 'elantra-gt', 'ioniq-electric', 'ioniq-hybrid', 'ioniq-plug-in-hybrid', 'kona', 'kona-electric', 'nexo', 'palisade', 'santa-fe', 'santa-fe-sport', 'santa-fe-xl', 'sonata', 'sonata-hybrid', 'sonata-plug-in-hybrid', 'tucson', 'veloster', 'venue', 'elantra-coupe', 'elantra-touring', 'entourage', 'equus', 'excel', 'genesis', 'genesis-coupe', 'scoupe', 'tiburon', 'veracruz', 'xg300', 'xg350']
infiniti=['q50', 'q60', 'q70', 'qx30', 'qx50', 'qx60', 'qx80', 'ex', 'ex35', 'fx', 'fx35', 'fx45', 'fx50', 'g-convertible', 'g-coupe', 'g-sedan', 'g20', 'g35', 'g37', 'g37-convertible', 'g37-coupe', 'g37-sedan', 'i30', 'i35', 'j30', 'jx', 'm', 'm30', 'm35', 'm37', 'm45', 'm56', 'q40', 'q45', 'q60-convertible', 'q60-coupe', 'qx', 'qx4', 'qx56', 'qx70']
jaguar=['e-pace', 'f-pace', 'f-type', 'i-pace', 'xe', 'xf', 'xj', 's-type', 'x-type', 'xj-series', 'xjr', 'xk', 'xk-series', 'xkr']
jeep=['cherokee', 'compass', 'gladiator', 'grand-cherokee', 'renegade', 'wrangler', 'comanche', 'commander', 'grand-cherokee-srt', 'grand-wagoneer', 'liberty', 'patriot', 'wagoneer', 'wrangler-jk']
kia=['cadenza', 'forte', 'k900', 'niro', 'niro-ev', 'niro-plug-in-hybrid', 'optima', 'optima-hybrid', 'optima-plug-in-hybrid', 'rio', 'sedona', 'seltos', 'sorento', 'soul', 'soul-ev', 'sportage', 'stinger', 'telluride', 'amanti', 'borrego', 'rondo', 'sephia', 'spectra']      
land=['defender', 'discovery', 'discovery-sport', 'range-rover', 'range-rover-evoque', 'range-rover-sport', 'range-rover-velar', 'discovery-series-ii', 'freelander', 'lr2', 'lr3', 'lr4']
lexus=['es-250', 'es-300h', 'es-350', 'gs-300', 'gs-350', 'gs-450h', 'gs-f', 'gx-460', 'is-300', 'is-350', 'lc-500', 'lc-500h', 'ls-500', 'ls-500h', 'lx-570', 'nx-300', 'nx-300h', 'rc-300', 'rc-350', 'rc-f', 'rx-350', 'rx-350l', 'rx-450h', 'rx-450hl', 'ux-200', 'ux-250h', 'ct-200h', 'es-300', 'es-330', 'gs-200t', 'gs-400', 'gs-430', 'gs-460', 'gx-470', 'hs-250h', 'is-200t', 'is-250', 'is-250-c', 'is-350-c', 'is-f', 'lfa', 'ls-400', 'ls-430', 'ls-460', 'ls-600h-l', 'lx-450', 'lx-470', 'nx-200t', 'rc-200t', 'rx-300', 'rx-330', 'rx-400h', 'sc-300', 'sc-400', 'sc-430']
lincoln=['aviator', 'continental', 'corsair', 'mkc', 'mkt', 'mkz', 'nautilus', 'navigator', 'blackwood', 'ls', 'mark-lt', 'mark-vii', 'mark-viii', 'mks', 'mkx', 'mkz-hybrid', 'navigator-l', 'town-car', 'zephyr']
lotus=['evora-gt', 'elise', 'esprit', 'evora', 'evora-400', 'exige']
maserati=['ghibli', 'granturismo-convertible', 'levante', 'quattroporte', 'coupe', 'gransport', 'granturismo', 'spyder']
mazda=['3', '6', 'cx-3', 'cx-30', 'cx-5', 'cx-9', 'mx-5-miata', 'mx-5-miata-rf', '2', '323', '5', '626', '929', 'b-series', 'b-series-pickup', 'b-series-truck', 'cx-7', 'mazdaspeed-3', 'mazdaspeed-6', 'mazdaspeed-mx-5-miata', 'mazdaspeed-protege', 'millenia', 'mpv', 'mx-3', 'mx-6', 'navajo', 'protege', 'protege5', 'rx-7', 'rx-8', 'tribute', 'tribute-hybrid', 'truck']
mercedes=['a-class', 'amg-gt', 'c-class', 'cla-class', 'cls-class', 'e-class', 'g-class', 'gla-class', 'glb-class', 'glc-class', 'glc-class-coupe', 'gle-class', 'gle-class-coupe', 'gls-class', 'maybach', 'metris', 's-class', 'sl-class', 'slc-class', 'sprinter', 'sprinter-worker', '190-class', '300-class', '350-class', '400-class', '420-class', '500-class', '560-class', '600-class', 'b-class-electric-drive', 'c36-amg', 'c43-amg', 'cl-class', 'clk-class', 'e55-amg', 'gl-class', 'glk-class', 'm-class', 'ml55-amg', 'r-class', 'slk-class', 'slr-mclaren', 'sls-amg', 'sls-amg-gt', 'sls-amg-gt-final-edition']
mini=['clubman', 'convertible', 'countryman', 'hardtop-2-door', 'hardtop-4-door', 'cooper', 'cooper-clubman', 'cooper-countryman', 'cooper-coupe', 'cooper-paceman', 'cooper-roadster']
mitsubishi=['eclipse-cross', 'mirage', 'mirage-g4', 'outlander', 'outlander-phev', 'outlander-sport', '3000gt', 'diamante', 'eclipse', 'eclipse-spyder', 'endeavor', 'expo', 'galant', 'i-miev', 'lancer', 'lancer-evolution', 'lancer-sportback', 'mighty-max-pickup', 'montero', 'montero-sport', 'precis', 'raider', 'sigma', 'vanwagon']
nissan=['370z', 'altima', 'armada', 'frontier', 'gt-r', 'kicks', 'leaf', 'maxima', 'murano', 'nv-cargo', 'nv-passenger', 'nv200', 'pathfinder', 'rogue', 'rogue-sport', 'sentra', 'titan', 'titan-xd', 'versa', 'versa-note', '200sx', '240sx', '300zx', '350z', 'altima-hybrid', 'axxess', 'cube', 'juke', 'murano-crosscabriolet', 'nv', 'nx', 'pulsar', 'quest', 'rogue-select', 'stanza', 'truck', 'van', 'xterra']
porsche=['718-boxster', '718-cayman', '911', 'cayenne', 'cayenne-coupe', 'macan', 'panamera', 'taycan', '918-spyder', '928', '944', '968', 'boxster', 'carrera-gt', 'cayman', 'cayman-s']
subaru=['b9-tribeca', 'baja', 'impreza-wrx', 'justy', 'loyale', 'svx', 'tribeca', 'xt', 'xv-crosstrek']
suzuki=[ 'aerio', 'equator', 'esteem', 'forenza', 'grand-vitara', 'kizashi', 'reno', 'samurai', 'sidekick', 'swift', 'sx4', 'verona', 'vitara', 'x-90', 'xl-7', 'xl7']
tesla=['model-3', 'model-s', 'model-x', 'model-y', 'roadster']	
toyota=['4runner', '86', 'avalon', 'avalon-hybrid', 'c-hr', 'camry', 'camry-hybrid', 'corolla', 'corolla-hatchback', 'corolla-hybrid', 'gr-supra', 'highlander', 'highlander-hybrid', 'land-cruiser', 'mirai', 'prius', 'prius-c', 'prius-prime', 'rav4', 'rav4-hybrid', 'rav4-prime', 'sequoia', 'sienna', 'tacoma', 'tundra', 'venza', 'yaris', 'yaris-hatchback', 'camry-solara', 'celica', 'corolla-im', 'cressida', 'echo', 'fj-cruiser', 'matrix', 'mr2', 'mr2-spyder', 'paseo', 'pickup', 'previa', 'prius-plug-in', 'prius-v', 'rav4-ev', 'supra', 't100', 'tercel', 'yaris-ia']
volkswagen=['arteon', 'atlas', 'atlas-cross-sport', 'beetle', 'beetle-convertible', 'e-golf', 'golf', 'golf-alltrack', 'golf-gti', 'golf-r', 'golf-sportwagen', 'jetta', 'jetta-gli', 'passat', 'tiguan', 'cabrio', 'cabriolet', 'cc', 'corrado', 'eos', 'eurovan', 'fox', 'gli', 'gti', 'jetta-hybrid', 'jetta-sportwagen', 'new-beetle', 'phaeton', 'r32', 'rabbit', 'routan', 'tiguan-limited', 'touareg', 'touareg-2', 'vanagon']
volvo=['s60', 's60-cross-country', 's90', 'v60', 'v60-cross-country', 'v90', 'v90-cross-country', 'xc40', 'xc60', 'xc90', '240', '740', '760', '780', '850', '940', '960', 'c30', 'c70', 'coupe', 's40', 's70', 's80', 'v40', 'v50', 'v70', 'xc', 'xc70']
saab=[ '9-2x', '9-3', '9-3-griffin', '9-4x', '9-5', '9-7x', '900', '9000']
fiat=[ '124-spider', '500', '500e', '500l', '500x']
oldsmobile=[ 'achieva', 'alero', 'aurora', 'bravada', 'ciera', 'custom-cruiser', 'cutlass', 'cutlass-calais', 'cutlass-ciera', 'cutlass-supreme', 'eighty-eight', 'eighty-eight-royale', 'intrigue', 'lss', 'ninety-eight', 'regency', 'silhouette', 'toronado']
plymouth=[ 'acclaim', 'breeze', 'colt', 'grand-voyager', 'horizon', 'laser', 'neon', 'prowler', 'sundance', 'voyager']
pontiac=[ '6000', 'aztek', 'bonneville', 'firebird', 'g3', 'g5', 'g6', 'g8', 'grand-am', 'grand-prix', 'gto', 'le-mans', 'montana', 'montana-sv6', 'solstice', 'sunbird', 'sunfire', 'torrent', 'trans-sport', 'vibe']
mercury=[ 'capri', 'cougar', 'grand-marquis', 'marauder', 'mariner', 'mariner-hybrid', 'milan', 'milan-hybrid', 'montego', 'monterey', 'mountaineer', 'mystique', 'sable', 'topaz', 'tracer', 'villager']
rolls=['cullinan', 'dawn', 'ghost-series-ii', 'phantom', 'wraith', 'corniche', 'ghost', 'park-ward', 'phantom-coupe', 'phantom-drophead-coupe', 'silver-seraph']
ram=['1500', '1500-classic', '2500', '3500', 'promaster-cargo-van', 'promaster-city', 'promaster-window-van', 'c/v-cargo-van', 'c/v-tradesman', 'dakota']
isuzu=[ 'amigo', 'ascender', 'axiom', 'hombre', 'i-series', 'impulse', 'oasis', 'pickup', 'rodeo', 'rodeo-sport', 'stylus', 'trooper', 'vehicross']
gmc=['acadia-limited', 'envoy', 'envoy-xl', 'envoy-xuv', 'jimmy', 'r/v-3500-series', 'rally-wagon', 's-15', 's-15-jimmy', 'safari', 'safari-cargo', 'sierra-1500-classic', 'sierra-1500-hybrid', 'sierra-1500hd', 'sierra-1500hd-classic', 'sierra-2500', 'sierra-2500hd-classic', 'sierra-3500', 'sierra-3500-classic', 'sierra-c3', 'sierra-classic-1500', 'sierra-classic-2500', 'sierra-classic-3500', 'sonoma', 'suburban', 'syclone', 'typhoon', 'vandura', 'yukon-denali', 'yukon-hybrid']


"""
 'alfa-romeo', 'aston-martin', 'acura', 'audi', 'bentley','bmw', 'buick', 'cadillac', 'chevrolet', 'chrysler','dodge', 'ferrari', 
 'ford', 'honda',  'hyundai', 'infiniti', 'jaguar', 'jeep', 'kia',  'land-rover',
 'lexus', 'lincoln', 'lotus',  'maserati', 'mazda',  'mercedes-benz',  'mini', 'mitsubishi',
   'nissan',  'porsche', 'subaru','suzuki', 'tesla',
 """
companies=[  
   'toyota', 'volkswagen', 'saab', 'volvo', 'fiat','gmc','isuzu','mercury','oldsmobile', 'plymouth',
   'pontiac',
  'ram',  'rolls-royce']
        




#'coupe','wagon','sedan','hatchback','suv','type-s','32-type-s','hybrid','type-r'}
car_year=[
       '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
       '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'
       ]
options = Options()
 # Last I checked this was necessary.

driver = webdriver.Firefox()
comps=[]
sum=0
ifi=0
dateTimeObj = datetime.now()
timestampStr_start = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
for comp in companies:
       models=[]
       years=[]
       page_count=0
       review=[]
       heading=[]
       rating=[]
       reviewer=[]
       date=[]
       coms=[]
       if comp=="aston-martin":
           car_model=aston
       elif comp=="land-rover":
           car_model=land
       elif comp=="mercedes-benz":
           car_model=mercedes
       elif comp=="rolls-royce":
           car_model=rolls
       elif comp=="alfa-romeo":
           car_model=alfa
       else:
           car_model=eval(comp)

       for model in car_model:
        sum+=1
        print("**************************************"+str(sum)+"*****************************************")
        for year in car_year:
            for i in range(1,5):
                
              url= "https://www.edmunds.com/"+comp+"/"+model+"/"+year+"/consumer-reviews/?pagenum="+str(i)+"&pagesize=50"
              print(page_count)
              page_count+=1
              print(url)
              try:
                 result = requests.get(url,headers=headers)
                 print(result.status_code)
                 ifi=0
              except:
                 print("error")
                 b=err(url,ifi)
                 if b==2:
                     ifi+=1
                     print("try again")
                     b=err(url,ifi)
                 elif b==200:
                     result.status_code=b
                     print("found after sleep")
                 elif b==3:
                     print("skip this, not found")
                     break
              if result.status_code==200:
                driver.set_page_load_timeout(180)  
                driver.get(url)
                time.sleep(10)
                revdate=driver.find_elements_by_xpath("/html/body/div/div/main/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div[1]")
                if revdate==[]:
                      # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$=============next year=============$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                       break
       
                for it in range (1,60):
                        hed=driver.find_elements_by_xpath("/html/body/div/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/h3")
                        revdate=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[1]/div[1]")
                        rev=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[4]")
                        srev=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[4]/div[2]")
                        rat=driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/span")

                        if srev==[]:
                               srev=driver.find_elements_by_xpath("/html/body/div/div/main/div/div[3]/div[1]/div[5]/div/div["+str(it)+"]/div[4]/div")
                               
                        if revdate==None:
                               iz+=1
                               if iz==5:
                                     # print("This page has been scraped, moving to the next page")
                                      break
                        else:
                            iz=0

                            if len(revdate)!=0:
                                   for redtape in revdate:
                                          if len(redtape.text)!=0:
                                                 if srev==[]:
                                                        #print("how stupid can you be?????????????????????????????????????????????????????????")
                                                        review.append(" ")
                        
                               
                            for hedr in hed:
                                   hedre=hedr.text
                                   heading.append(hedre)
                            for snance in revdate:
                                redat=snance.text
                                reed=redat.split(',')
                                if reed==['']:
                                    print(".")
                                else:
                                    #print("acceptable")
                                    reviewer.append(reed[0])
                                    date.append(reed[1])
                                    coms.append(comp)
                                    models.append(model)
                                    years.append(year)
                                    
                                    
                                           
                            for (jheff,jeff) in zip(srev,rev):
                                revi=jeff.text
                                srevi=jheff.text
                                if revi!=srevi:
                                       rev1 = revi.replace(srevi, '')
                                else:
                                       rev1=revi
                                review.append(rev1)
                            for nyess in rat:
                                boss=nyess.get_attribute('aria-label')
                                rating.append(boss[0])
                                


                print("------------------------sleep----------------------------")
                time.sleep(10)
              else:
                    # print("__________________________________________go to next year____________________________________")
                     break
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            print('Current Timestamp : ', timestampStr)
       d = [coms,models,years,reviewer,date,heading,rating,review]
       export_data = zip_longest(*d, fillvalue = '')
       with open('reviews/'+comp+'.csv', 'w',encoding="utf-8",  newline='') as myfile:
             wr = csv.writer(myfile)
             print("writing")
             wr.writerow(("Company","Model", "Year","Reviewer","Date","Title","Rating","Review"))
             time.sleep(2)
             wr.writerows(export_data)
       myfile.close()
       dateTimeObj = datetime.now()
       timestampStr_end = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    
       print(len(models))
       print(len(coms))
       print(len(years))
       print(len(reviewer))
       print(len(date))
       print(len(rating))
       print(len(review))
       print(len(heading))
       reve+=len(review)
       print("Started at: ",timestampStr_start)
       print("Right now at: ",timestampStr_end)
       print("Reviews till now: ",reve)
       time.sleep(30)
       print("Done with rest, moving on")

driver.quit()
print("done")
print("Started at: ",timestampStr_start)
print("Ended at: ",timestampStr_end)
print("Total number of reviews scraped:", reve)

