# -*-coding: utf-8 -*-  

import fileinput
import re
import sys

filename = sys.argv[1]

outfile = open(filename+".orth", "w")

for line in fileinput.input():


#PREP + Possesive Pronoun

#DE
    line = re.sub(' de a ', ' dá ', line.rstrip())
    line = re.sub(' de ár ', ' dár ', line.rstrip())

#DO
    line = re.sub(' do a ', ' dá ', line.rstrip())
    line = re.sub(' do ár ', ' dár ', line.rstrip())
    
#LE
    line = re.sub(' le a ', ' lena ', line.rstrip())
    line = re.sub(' le ár ', ' lenár ', line.rstrip())
    
#FAOI
    line = re.sub(' faoi a ', ' faoina ', line.rstrip())
    line = re.sub(' faoi ár ', ' faoinár ', line.rstrip()) 
    
#I
    line = re.sub(' i a ', ' ina ', line.rstrip())
    line = re.sub(' i ár ', ' inár ', line.rstrip())
    line = re.sub(' in a ', ' ina ', line.rstrip())
    line = re.sub(' in ár ', ' inár ', line.rstrip())
    line = re.sub(' i i ', ' i ', line.rstrip())
    
#Ó
    line = re.sub(' ó a ', ' óna ', line.rstrip())
    line = re.sub(' ó ár ', ' ónár ', line.rstrip())
    
#TRÍ
    line = re.sub(' trí a ', ' trína ', line.rstrip())
    line = re.sub(' trí ár ', ' trínár ', line.rstrip())

#PREP + PRONOUN


#AG
    line = re.sub(' ag mé ', ' agam ', line.rstrip())
    line = re.sub(' ag tú ', ' agat ', line.rstrip())
    line = re.sub(' ag é ', ' aige ', line.rstrip())
    line = re.sub(' ag í ',' aici ', line.rstrip())
    line = re.sub(' ag muid ', ' againn ', line.rstrip())
    line = re.sub(' ag sinn ', ' againn ', line.rstrip())
    line = re.sub(' ag sibh ', ' agaibh ', line.rstrip())
    line = re.sub(' ag iad ', ' acu ', line.rstrip())

#AR                                                                                                                                                                                 
    line = re.sub(' ar mé ', ' orm ', line.rstrip())
    line = re.sub(' ar tú ','  ort ', line.rstrip())
    line = re.sub(' ar é ', ' air ', line.rstrip())
    line = re.sub(' ar í ', ' uirthi ', line.rstrip())
    line = re.sub(' ar muid ', ' orainn ', line.rstrip())
    line = re.sub(' ar sinn ', ' orainn ', line.rstrip())
    line = re.sub(' ar sibh ', '  oraibh ', line.rstrip())
    line = re.sub(' ar iad ', '  orthu ', line.rstrip())

#AS                                                                                                                                                                                 
    line = re.sub(' as mé ', '  asam ', line.rstrip())
    line = re.sub(' as tú ', ' asat ', line.rstrip())
    line = re.sub(' as é ', ' as ', line.rstrip())
    line = re.sub(' as í ', ' aisti ', line.rstrip())
    line = re.sub(' as muid ', ' asainn ', line.rstrip())
    line = re.sub(' as sinn ', ' asainn ', line.rstrip())
    line = re.sub(' as sibh ', ' asaibh ', line.rstrip())
    line = re.sub(' as iad ', ' astu ', line.rstrip())

#CHUIG                                                                 
    line = re.sub(' chuig mé ', ' chugam ', line.rstrip())
    line = re.sub(' chuig tú ', ' chugat ', line.rstrip())
    line = re.sub(' chuig é ', ' chuige ', line.rstrip())
    line = re.sub(' chuig í ', ' chuici ', line.rstrip())
    line = re.sub(' chuig muid ', ' chugainn ', line.rstrip())
    line = re.sub(' chuig sinn ', ' chugainn ', line.rstrip())
    line = re.sub(' chuig sibh ', ' chugaibh ', line.rstrip())
    line = re.sub(' chuig iad ', ' chucu ', line.rstrip())
    
#DE
    line = re.sub(' de mé ',' díom ', line.rstrip())
    line = re.sub(' de tú ', ' díot ', line.rstrip())
    line = re.sub(' de é ', ' de ', line.rstrip())
    line = re.sub(' de í ', ' di ', line.rstrip())
    line = re.sub(' de muid ', ' dínn ', line.rstrip())
    line = re.sub(' de sinn ', ' dínn ', line.rstrip())
    line = re.sub(' de sibh ', ' díbh ', line.rstrip())
    line = re.sub(' de iad ', ' díobh ', line.rstrip())
#DO                                                                                                                                                       
    line = re.sub(' do mé ', ' dom ', line.rstrip())
    line = re.sub(' do tú ', ' duit ', line.rstrip())
    line = re.sub(' do é ', ' dó ', line.rstrip())
    line = re.sub(' do í ', ' di ', line.rstrip())
    line = re.sub(' do muid ', ' dúinn ', line.rstrip())
    line = re.sub(' do sinn ', ' dúinn ', line.rstrip())
    line = re.sub(' do sibh ', ' daoibh ', line.rstrip())
    line = re.sub(' do iad ', ' dóibh ', line.rstrip())

#FAOI                                                                                                                                                                               
    line = re.sub(' faoi mé ', ' fúm ', line.rstrip())
    line = re.sub(' faoi tú ', ' fút ', line.rstrip())
    line = re.sub(' faoi é ', ' faoi ', line.rstrip())
    line = re.sub(' faoi í ', ' fúithi ', line.rstrip())
    line = re.sub(' faoi muid ', ' fúinn ', line.rstrip())
    line = re.sub(' faoi sinn ', ' fúinn ', line.rstrip())
    line = re.sub(' faoi sibh ', ' fúibh ', line.rstrip())
    line = re.sub(' faoi iad ', ' fúthu ', line.rstrip())
    
#I                                                                                                                                                                               
    line = re.sub(' i mé ', ' ionam ', line.rstrip())
    line = re.sub(' i tú ', ' ionat ', line.rstrip())
    line = re.sub(' i é ', ' ann ', line.rstrip())
    line = re.sub(' i í ', ' inti ', line.rstrip())
    line = re.sub(' i muid ', ' ionainn ', line.rstrip())
    line = re.sub(' i sinn ', ' ionainn ', line.rstrip())
    line = re.sub(' i sibh ', ' ionaibh ', line.rstrip())
    line = re.sub(' i iad ', ' iontu ', line.rstrip())
    
#IDIR                                                                                                                                                                               
    line = re.sub(' idir muid ','  eadrainn ', line.rstrip())
    line = re.sub(' idir sinn ', ' eadrainn ', line.rstrip())
    line = re.sub(' idir sibh ', ' eadraibh ', line.rstrip())
    line = re.sub(' idir iad ',' eatarthu ', line.rstrip())
    
#LE
    line = re.sub(' le mé ', ' liom ', line.rstrip())
    line = re.sub(' le tú ', ' leat ', line.rstrip())
    line = re.sub(' le é ', ' leis ', line.rstrip())
    line = re.sub(' le í ', ' leí ', line.rstrip())
    line = re.sub(' le muid ', ' linn ', line.rstrip())
    line = re.sub(' le sinn ', ' linn ', line.rstrip())
    line = re.sub(' le sibh ', ' libh ', line.rstrip())
    line = re.sub(' le iad ', ' leo ', line.rstrip())
    
#Ó
    line = re.sub(' ó mé ', ' uaim ', line.rstrip())
    line = re.sub(' ó tú ', ' uait ', line.rstrip())
    line = re.sub(' ó é ', ' uaidh ', line.rstrip())
    line = re.sub(' ó í ', ' uathi ', line.rstrip())
    line = re.sub(' ó muid ', ' uainn ', line.rstrip())
    line = re.sub(' ó sinn ', ' uainn ', line.rstrip())
    line = re.sub(' ó sibh ', ' uaibh ', line.rstrip())
    line = re.sub(' ó iad ', ' uathu ', line.rstrip())
    
#ROIMH                                                                                                                                                                              
    line = re.sub(' roimh mé ',' romham ', line.rstrip())
    line = re.sub(' roimh tú ',' romhat ', line.rstrip())
    line = re.sub(' roimh é',' roimhe ', line.rstrip())
    line = re.sub(' roimh í ',' roimpi ', line.rstrip())
    line = re.sub(' roimh muid ','  romhainn ', line.rstrip())
    line = re.sub(' roimh sinn ', ' romhainn ', line.rstrip())
    line = re.sub(' roimh sibh ', ' romhaibh ', line.rstrip())
    line = re.sub(' roimh iad ',' rompu ', line.rstrip())

#THAR                                                                                                                                                                               
    line = re.sub(' thar mé ',' tharam ', line.rstrip())
    line = re.sub(' thar tú ',' tharat ', line.rstrip())
    line = re.sub(' thar é',' thairis ', line.rstrip())
    line = re.sub(' thar í ',' thairsti ', line.rstrip())
    line = re.sub(' thar muid ','  tharainn ', line.rstrip())
    line = re.sub(' thar sinn ', ' tharainn ', line.rstrip())
    line = re.sub(' thar sibh ', ' tharaibh ', line.rstrip())
    line = re.sub(' thar iad ',' tharstu ', line.rstrip())

#TRÍ                                                                                                                                                                                
    line = re.sub(' trí mé ',' tríom ', line.rstrip())
    line = re.sub(' trí tú ',' tríot ', line.rstrip())
    line = re.sub(' trí é ',' tríd ', line.rstrip())
    line = re.sub(' trí í ',' tríthi ', line.rstrip())
    line = re.sub(' trí muid ','  trínn ', line.rstrip())
    line = re.sub(' trí sinn ', ' trínn ', line.rstrip())
    line = re.sub(' trí sibh ', ' tríibh ', line.rstrip())
    line = re.sub(' trí iad ',' tríothu ', line.rstrip())
    
#UM                                                                                                                                                                              
    line = re.sub(' um mé ',' umam ', line.rstrip())
    line = re.sub(' um tú ',' umat ', line.rstrip())
    line = re.sub(' um é ',' uime ', line.rstrip())
    line = re.sub(' um í ',' uimpi ', line.rstrip())
    line = re.sub(' um muid ','  uamainn ', line.rstrip())
    line = re.sub(' um sinn ', ' uamainn ', line.rstrip())
    line = re.sub(' um sibh ', ' uamaibh ', line.rstrip())
    line = re.sub(' um iad ',' umpu ', line.rstrip())

#PREP + DEF ARTICLE

#DE
    line = re.sub(' de an ',' den ', line.rstrip())
    line = re.sub(' de An ',' den ', line.rstrip())

#DO
    line = re.sub(' do an ',' don ', line.rstrip())
    line = re.sub(' do An ',' don ', line.rstrip())

#FAOI
    line = re.sub(' faoi an ',' faoin ', line.rstrip())
    line = re.sub(' faoi An ',' faoin ', line.rstrip())

#I
    line = re.sub(' i an ',' sa ', line.rstrip()) 
    line = re.sub(' i na ',' sna ', line.rstrip())
    line = re.sub(' i An ',' sa ', line.rstrip()) 
    line = re.sub(' i Na ',' sna ', line.rstrip())
    
    line = re.sub(' sa f',' san fh', line.rstrip())
    line = re.sub(' san fhh',' san fh', line.rstrip())
    
    #+article
    line = re.sub(' sa a',' san a', line.rstrip())
    line = re.sub(' sa e',' san e', line.rstrip())
    line = re.sub(' sa i',' san i', line.rstrip())
    line = re.sub(' sa o',' san o', line.rstrip())
    line = re.sub(' sa u',' san u', line.rstrip())

    line = re.sub(' sa á',' san á', line.rstrip())
    line = re.sub(' sa é',' san é', line.rstrip())
    line = re.sub(' sa í',' san í', line.rstrip())
    line = re.sub(' sa ó',' san ó', line.rstrip())
    line = re.sub(' sa ú',' san ú', line.rstrip())
    
    
     #captials
    line = re.sub(' sa A', ' san A', line.rstrip())
    line = re.sub(' sa E', ' san E', line.rstrip())
    line = re.sub(' sa I', ' san I', line.rstrip())
    line = re.sub(' sa O', ' san O', line.rstrip())
    line = re.sub(' sa U', ' san U', line.rstrip())

    line = re.sub(' sa Á', ' san Á', line.rstrip())
    line = re.sub(' sa É', ' san É', line.rstrip())
    line = re.sub(' sa Í', ' san Í', line.rstrip())
    line = re.sub(' sa Ó', ' san Ó', line.rstrip())
    line = re.sub(' sa Ú', ' san Ú', line.rstrip())
    

#LE                                                                                                                                                                                 
    line = re.sub(' le an ',' leis an ', line.rstrip())
    line = re.sub(' le An ',' leis An ', line.rstrip())
    
    #exceptions
    line = re.sub(' leis An Post ',' le An Post ', line.rstrip())


     #+vowel
    line = re.sub(' le a',' le ha', line.rstrip())
    line = re.sub(' le e',' le he', line.rstrip())
    line = re.sub(' le i',' le hi', line.rstrip())
    line = re.sub(' le o',' le ho', line.rstrip())
    line = re.sub(' le u',' le hu', line.rstrip())

    line = re.sub(' le á',' le há', line.rstrip())
    line = re.sub(' le é',' le hé', line.rstrip())
    line = re.sub(' le í',' le hí', line.rstrip())
    line = re.sub(' le ó',' le hó', line.rstrip())
    line = re.sub(' le ú',' le hú', line.rstrip())
    
    
     #captials
    line = re.sub(' le A', ' le hA', line.rstrip())
    line = re.sub(' le E', ' le hE', line.rstrip())
    line = re.sub(' le I', ' le hI', line.rstrip())
    line = re.sub(' le O', ' le hO', line.rstrip())
    line = re.sub(' le U', ' le hU', line.rstrip())

    line = re.sub(' le Á', ' le hÁ', line.rstrip())
    line = re.sub(' le É', ' le hÉ', line.rstrip())
    line = re.sub(' le Í', ' le hÍ', line.rstrip())
    line = re.sub(' le Ó', ' le hÓ', line.rstrip())
    line = re.sub(' le Ú', ' le hÚ', line.rstrip())

    #exceptions
    line = re.sub(' le hos ', ' le os ', line.rstrip())
    line = re.sub(' le hi ', ' le i ', line.rstrip())
    line = re.sub(' le há ', ' le á ', line.rstrip())
    line = re.sub(' le hag ', ' le ag ', line.rstrip())
    line = re.sub(' le hAn Post ', ' le An Post ', line.rstrip())

#Ó                                                                                                                                                                                  
    line = re.sub(' ó an ',' ón ', line.rstrip())
    line = re.sub(' ó An ',' ón ', line.rstrip())

    #exceptions
    line = re.sub(' ón Post ', ' ó An Post ', line.rstrip())

#TRÍ                                                                                                                                                                                
    line = re.sub(' trí an ', ' tríd an ', line.rstrip())
    line = re.sub(' trí An ', ' tríd An ', line.rstrip())
    
    #I +vowels
    line = re.sub(' i t-', ' in ', line.rstrip())
    
    line = re.sub(' i a', ' in a', line.rstrip())
    line = re.sub(' i e', ' in e', line.rstrip())
    line = re.sub(' i i', ' in i', line.rstrip())
    line = re.sub(' i o', ' in o', line.rstrip())
    line = re.sub(' i u', ' in u', line.rstrip())
    
    line = re.sub(' i á', ' in á', line.rstrip())
    line = re.sub(' i é', ' in é', line.rstrip())
    line = re.sub(' i í', ' in í', line.rstrip())
    line = re.sub(' i ó', ' in ó', line.rstrip())
    line = re.sub(' i ú', ' in ú', line.rstrip())
    
    #capitals
    line = re.sub(' i A', ' in A', line.rstrip())
    line = re.sub(' i E', ' in E', line.rstrip())
    line = re.sub(' i I', ' in I', line.rstrip())
    line = re.sub(' i O', ' in O', line.rstrip())
    line = re.sub(' i U', ' in U', line.rstrip())

    line = re.sub(' i Á', ' in Á', line.rstrip())
    line = re.sub(' i É', ' in É', line.rstrip())
    line = re.sub(' i Í', ' in Í', line.rstrip())
    line = re.sub(' i Ó', ' in Ó', line.rstrip())
    line = re.sub(' i Ú', ' in Ú', line.rstrip())

#ARTICLE PL

    #NA +vowels 
    line = re.sub(' na a', ' na ha', line.rstrip())
    line = re.sub(' na e', ' na he', line.rstrip())
    line = re.sub(' na i', ' na hi', line.rstrip())
    line = re.sub(' na o', ' na ho', line.rstrip())
    line = re.sub(' na u', ' na hu', line.rstrip())
    
    line = re.sub(' na á', ' na há', line.rstrip())
    line = re.sub(' na é', ' na hé', line.rstrip())
    line = re.sub(' na í', ' na hí', line.rstrip())
    line = re.sub(' na ó', ' na hó', line.rstrip())
    line = re.sub(' na ú', ' na hú', line.rstrip())
    
    #capitals
    line = re.sub(' na A', ' na hA', line.rstrip())
    line = re.sub(' na E', ' na hE', line.rstrip())
    line = re.sub(' na I', ' na hI', line.rstrip())
    line = re.sub(' na O', ' na hO', line.rstrip())
    line = re.sub(' na U', ' na hU', line.rstrip())

    line = re.sub(' na Á', ' na hÁ', line.rstrip())
    line = re.sub(' na É', ' na hÉ', line.rstrip())
    line = re.sub(' na Í', ' na hÍ', line.rstrip())
    line = re.sub(' na Ó', ' na hÓ', line.rstrip())
    line = re.sub(' na Ú', ' na hÚ', line.rstrip())
    
    #miscellaneous
    line = re.sub(' le seo ', ' leis seo ', line.rstrip())


    
    outfile.write(line+"\n")

