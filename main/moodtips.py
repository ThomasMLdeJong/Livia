import random

y = 'tekst' '\n' 'tekst '
mood_dict_nl = {   
        'boos': {
            1: ['EFT relatietherapie bij boosheid op je partner', 'Iedereen is wel eens boos op zijn partner. Soms omdat de ander iets doet wat je niet leuk vindt, je boosheid heeft dan de functie om jou en jullie veiligheid te waarborgen. Soms ervaar je bij je boosheid een enorm gevoel van machteloosheid. Bij Emotionally Focussed Couple Therapy (EFT) is er all ruimte om je boosheid te voelen, onderzoeken en veiligte leren uiten. Misschien roept het gdrag van je partner naast boosheid nog iets anders op, bijvoorbeeld angst om in de steek gelaten te worden of een gevoel van niet belangrijk zijn of je niet gezien of gehoord te voelen. Als dit vaak genoeg gebeurt en je vindt bijvoorbeeld van jezelf dat je niet moet zeuren of de ander niet wil belasten met je behoeften dan kan deze meer kwetsbare emotie er uit komen als frustratie of machteloze woede. Bij EFT maken we op een veilige manier ruimte voor zowel de gevoelens van boosheid en frustratie als voor de angst en het verdriet die er soms onder schuil gaan. Zodat er meer inzicht en begrip ontstaat tussen jullie en je het samen weer veilig kan maken op kwetsbare momenten. Hester'],
            2: ['Stoplicht-methode inzetten bij boosheid', " Als je last hebt van boosheid of woedeaanvallen kan het handig zijn om het stoplicht in te zetten. Het groen van het stoplicht staat voor wanneer alles lekker loopt. Het rood staat voor het moment dat je ontploft! Dat moment lijkt vaak uit het niets te komen. Maar dat is niet zo. Er is altijd een moment tussen de groene en rode fase. Dat moment is het oranje moment. Als je je niet prettig voelt, dan geef je aan dat je oranje bent. Je hoeft niet uit te leggen wat er is, soms is dat ook niet meteen duidelijk voor jezelf. Het is aan de ander om te vragen wat diegene kan doen om het groen te krijgen of in ieder geval te zorgen dat het geen rood wordt. Of je geeft zelf aan wat je nodig hebt. De ander heeft dat tot op zekere hoogte te accepteren. Maar na een verloop van tijd mag er wel op terug gekomen worden: wat was er nu aan de hand? Is diegene daar nog niet aan toe, dan afspreken wanneer dan wel. Veel succes! Germien Brouwer - Therapie Oss >> Lid van Therapiepsycholoog "],
            3: ['Wat jij ervaart is niet automatisch "waar"', "Boosheid verwijst meestal naar een situatie waarvan je vindt dat er iets anders zou moeten zijn dan er in werkelijkheid is. Ja, de meeste mensen vinden eigenlijk dat, wat zij vinden dat er zou moeten zijn, volstrekt 'normaal' is. Of het nu kinderen zijn die stil moeten zijn, collega's die wat meer inzet zouden moeten tonen, automobilisten die wat langzamer of harder zouden moeten rijden. Mijn norm is eigenlijk DE norm. Wanneer je boosheid ervaart, stroomt het bloed naar je spieren en wil je direct in actie komen om de boel recht te zetten en de ander duidelijk maken wat h/zij eigenlijk zou moeten doen. We reageren emotioneel, gaan schreeuwen, gebaren, ingrijpen. En soms is dit ook precies wat nodig is. In de meeste gevallen is het echter niet helpend en dat krijg je ook vaak als reactie terug uit je omgeving. Kinderen worden eerder bang of opstandig wanneer je hen boos of kwaad benadert. Collega's gaan je vermijden, negeren of terugfluiten. Andere weggebruikers reageren boos terug of nemen je niet serieus. Ervaar je boosheid of woede? En wil je er constructief mee om leren gaan? Zonder je af en onderzoek eerst bij jezelf wat het is dat je zo boos maakt. Wat leeft er in je: wat denk je, wat gaat er door je heen. Schrijf het op, herhaal het hardop in de spiegel voor jezelf . Dat werkt vertragend, brengt je weer wat bij je positieven. Dit is wat ik denk en waardoor ik boosheid ervaar. Zeg tegen jezelf: ik ervaar boosheid omdat ik denk dat .... Onderzoek of dat wat je denkt dat er zou moeten zijn inderdaad te maken heeft met jouw norm, jouw ervaring van de realiteit. Realiseer je dat de wereld is zoals hij is en niet altijd functioneert naar jouw norm. Weten wat jij normaal vindt is belangrijk. Maar normen en overtuigingen kleuren ook jouw ervaringen. En andere mensen ervaren op hun beurt de situatie vanuit hun eigen perspectief. Realiseer je dus dat wat jij ervaart, niet automatisch 'waar' hoeft te zijn. Je neemt maar een gedeelte van de werkelijkheid en waarheid waar. Sla de brug naar de ander door je enerzijds bewust te worden wat jezelf ervaart, voelt en denkt. En anderzijds te beseffen dat de ander ook een eigen ervaringswereld heeft die je niet kent. Je gevoelens uiten is iets anders dan emotioneel reageren.Maak duidelijk wat je ervaart (voelt en denkt) door te zeggen: 'Ik voel me nu boos worden omdat ik denk......' of 'ik ervaar nu ....... en ik zou wensen dat .....'. Vraag vervolgens de ander wat er in hem of haar leeft waardoor h/zij zo reageert. Stel je open voor het feit dat dit wel eens iets anders kan zijn dan jij denkt. Veel succes! " ],
            4: ['Accepteer en onderzoek je boosheid', "Accepteer en onderzoek je boosheid. Je bent niet zomaar boos, toch? Vaak zijn we ergens in geraakt, waardoor we niet anders kunnen dan boos worden: erken dat en onderzoek hoe het komt dat je zo boos bent. Marjo Adan - Therapie Eindhoven >> Lid van Therapiepsycholoog "],
            5: ['Vertel waarom het zo moeilijk voor je is', "Als je boos bent op een ander is het vaak heel moeilijk hoé je dit de ander kunt zeggen, zonder de relatie te verslechteren. Denk daarom eerst goed na waar je precies boos over bent. Met welk gedrag van de ander heb je moeite, waarom en wat doet het jou? Maak vervolgens contact met de ander en zeg dat je hem/haar iets wilt vertellen wat je dwars zit. Vertel óók dat je het bijvoorbeeld heel moeilijk/ niet leuk vindt om dit te vertellen maar dat je dit móet omdat je jullie relatie te belangrijk vindt om dit NIET te vertellen. Vertel hem/ haar daarna je persoonlijke boodschap. Stel je kwetsbaar op door vooral te vertellen wat het gedrag van de ander jou deed of nog steeds doet, en waarom dat zo moeilijk voor je is. Dan hou je het bij jezelf, en heb je ook de meeste kans dat de ander kan blijven openstaan voor wat je zegt. Pieternel Geurts - Therapie Wageningen >> Lid van Therapiepsycholoog "],
            6: ['Zie boosheid als signaalfunctie voor grenzen stellen', "Boosheid en irritatie hebben een belangrijke signaalfunctie als het gaat om grenzen stellen. Als deze gevoelens bij je opkomen, betekent het vaak dat een grens wordt overschreden. Voel je je boos of geïrriteerd, vraag je dan af welke grens dit voor jou is, zo leer je beter om je bewust te worden van waar jij grenzen wilt trekken. Pascale van der Wiel - Therapie Amsterdam >> Lid van Therapiepsycholoog  "],
            7: ['Spreek je behoefte uit', "Als je je woede uit tegen iemand met je wie je graag een goed contact hebt, probeer dat dan eens op de volgende manier: “Als ik je …. hoor zeggen, dan voel ik me boos, want ik heb behoefte heb aan … .” Dus bijvoorbeeld: “Als ik je dit hoor zeggen, voel ik me boos, want ik heb behoefte aan respect”. Als je dat probeert, valt je vast iets op: zodra je je behoefte uitspreekt, zakt de boosheid onmiddellijk. Je boosheid zal niet zakken als je zegt: “Ik ben boos, omdat je dit zegt”. Als je namelijk naar de ander wijst als oorzaak van je boosheid en een oordeel over de ander velt, wordt boosheid steeds erger. Als je daarentegen contact maakt met jezelf, met je behoefte en die uitspreekt, verdwijnt de boosheid en krijg je ruimte om te kijken hoe je jouw behoefte graag vervuld wilt zien. Jacqueline Medendorp - Psycholoog Nijmegen >> Lid van Therapiepsycholoog "],
            8: ['Richt je aandacht op jezelf', 'Aandacht hebben voor je boosheid is als licht in de duisternis. Je gaat zien wat er werkelijk speelt. In plaats van je aandacht te richten op de persoon of situatie die je zo boos maakt, richt je je aandacht op jezelf. Wat in jou zorgt ervoor dat je boos bent? Als je hier de vinger op weet te leggen en er echt naar kijkt zul je merken dat de boosheid verdwijnt. Sandra - Therapie Purmerend >> Lid van Therapiepsycholoog '],
            9: ['Lichaamsgerichte therapie bij boosheid', " Boosheid is de minst geaccepteerde emotie; 'je moet je gevoelens onder controle houden, anders heb je geen zelfbeheersing'. Meestal loopt de boosheid dan alleen maar op en word je of heel boos op iemand die dicht bij je staat of op jezelf, waarna je je weer afsluit of jezelf veroordeeld. Lichaams-gerichte therapie is een prachtige manier om de boosheid in je lijf te gaan herkennen en te leren wat deze jou te vertellen heeft. Misschien is er ergens in je leven iemand over een grens gegaan of ga je zelf regelmatig over je grenzen? We oefenen om de boosheid op een veilige en constructieve manier te uiten zodat je bereikt wat je wil en waar je boosheid in de eerste plaats voor opgekomen is. Hester" ],
            10: ['Je boosheid niet onderdrukken', ' Boosheid is niet alleen maar negatief. Boosheid is ook energiegevende en beschermende energie. Het wordt pas een probleem als deze emotie wordt onderdrukt. Dan kan het gaan etteren en klachten veroorzaken. Debby - Therapie De Meern >> Lid van Therapiepsycholoog '],
            11: ['Onderzoek je gedachten die je boos maken', 'Wordt je eerder boos om je eigen of juist om andermans gedrag? Of maakt niets je zo boos als haperende apparaten? Dat inzien is stap één. Stap twee is onderzoeken wat je op die momenten concreet denk. Enkele bekende "boosmakers zijn": catastroferen - tegenvallers enorm opblazen; lage frustratietolerantie - situaties zien als onoverkomelijk én je zelfredzaamheid onderschatten; en veeleisendheid - je regels willen opleggen aan iedereen om je heen. Besef dat het die gedachten zijn die je boos maken, niet de gebeurtenissen op zich. Rita Rogge - Therapie Amstelveen >> Lid van Therapiepsycholoog ']
            },
        'gefrustreerd': {
            1: ["Vraag jezelf af: is dit mijn boosheid en frustratie waard?', 'Sommige mensen kunnen heel goed omgaan met kleine tegenslagen. Er zijn mensen die kunnen denken 'Ja dat ging even allemaal niet zo lekker, maar het is niet het einde van de wereld.' Ik was daar altijd wel een beetje jaloers op. Die mensen leken er eigenlijk weinig last van te hebben. En ze hebben gelijk. Het is ook niet het einde van de wereld. En juist als je je er op gaat focussen groeit het en zullen er nog veel meer dingen fout gaan. Ik heb op gegeven moment mijzelf steeds de vraag gesteld: 'Is dit mijn boosheid en frustratie waard?'. In eerste instantie denk ik dan JA! Maar als ik dan wat langer nadenk, kom ik tot de conclusie dat het het eigenlijk niet waard is. Door zoveel boosheid en frustratie te voelen bepaal ik eigenlijk zelf al hoe mijn dag verloopt. Op zo'n moment probeer ik dan te relativeren en te bedenken dat het niet het einde van de wereld is en dat er dingen zijn die zoveel belangrijker zijn. Laura - redactrice Proud2Bme "],
            2: ['Wees je er bewust van en kies een weg', 'Eigenlijk kies je op dat punt een kant. Ga ik mee in mijn frustratie en blijf ik mij hier rot over voelen of kies ik er voor om te accepteren dat het even allemaal niet zo lekker gaat en probeer ik wat van mijn dag te maken? Dat is zoveel meer waard. Hierbij helpt het mij vaak om te bedenken dat iedereen weleens zulke dingen meemaakt en dat ik hierin echt niet de enige ben. Daarnaast probeer ik te denken aan dat er nog een hele dag is die wel goed kan verlopen in plaats van een hele dag waarop nog vanalles mis kan gaan. Laura - redactrice Proud2Bme'],
            3: ['Tel tot 10', 'Dit is een klassieke tip als het gaat om woedebeheersing. Het werkt ook echt en ik merk ook dat veel mensen dit toepassen. Wanneer je boos bent of iets of iemand, is het goed om heel even te wachten voordat je in woede uitbarst. Dit kun je doen door tot 10 te tellen. Hierdoor reageer je niet direct vanuit je eerste emotie, maar geef je jezelf de kans om even tot rust te komen. Hierdoor kun je vaak rationeler reageren en heb je hier vaak zelf (en de ander ook) meer aan. Soms is dit best moeilijk, maar je kunt het jezelf wel aanleren. Laura - redactrice Proud2Bme'],
            4: ['Denk aan rust', 'Klinkt misschien gek, maar rust visualiseren of denken aan rust, kan je kalmeren. Juist op die kritieke momenten van boosheid en frustratie is het goed om even een moment je ogen dicht te doen en aan rust te denken. Dit is misschien best lastig, maar desnoods denk je aan dat woord. Of stel je je een rustig natuurgebied voor. Bijvoorbeeld een weiland waar alleen wat dieren staan te grazen. Neem hier in ieder geval heel even de tijd voor. Laura - redactrice Proud2Bme'],
            5: ['Neem afstand', 'Afstand nemen van de situatie waar je op dat moment in zit kan ook goed helpen. Misschien heb je net ruzie gehad met je vriend en word je er wanhopig van. Je weet niet meer wat je moet zeggen om jouw standpunt duidelijk te maken en het frustreert je dat hij niet (genoeg) naar je luistert. Loop even weg en denk bijvoorbeeld aan je lievelingskleur of een dier wat je heel leuk vindt. Het kan ook een mooie vakantie zijn of je lievelingsliedje. Door even afstand te nemen en later weer terug te komen in die frustrerende situatie kun je het vaak op een andere, meer rationele manier bekijken.Laura - redactrice Proud2Bme'],
            6: ['Verander van omgeving', 'Als je bijvoorbeeld op je werk zit en iets lukt niet waardoor je gefrustreerd raakt, is het verstandig om even je werkplek te verlaten en bijvoorbeeld een rondje te lopen. Ga koffie halen of maak even een praatje met een collega. Dit geldt natuurlijk ook in andere situaties waarin je boos of gefrustreerd bent. Misschien heeft iemand je een whatsapp berichtje gestuurd met een opmerking die je niet leuk vindt en waar je boos van wordt. Neem even afstand, leg je telefoon weg en ga iets anders doen. Als je weer teruggaat naar die situatie, ziet het er vaak weer anders uit. Laura - redactrice Proud2Bme'],
            7: ["Stel je iemand voor die je inspirerend vindt", 'Soms kan het helpen om te denken aan iemand die je inspirerend vindt. Hoe zou hij of zij reageren in deze situatie? Hoe zou hij of zij de woede kunnen beheersen? Laura - redactrice Proud2Bme'],
            8: ['Uit het op iets onschuldigs', 'Woede moet soms ook gewoon echt geuit worden. Soms wil je gewoon heel hard gillen, even van je af slaan, iets kapot maken, etc. Dat kan natuurlijk! Maar kies dan iets onschuldigs en dan bedoel ik geen mensen of dieren. Kies voor bijvoorbeeld een kussen waar je even in kan schreeuwen of slaan. Of pak een tijdschrift en scheur het in duizend stukjes. Laura - redactrice Proud2Bme'],
            9: ['Schrijf van je af', 'We kennen deze tip allemaal wel maar toch laten we het vaak links liggen. Kost zoveel moeite en tijd. Wel kan het je heel veel opleveren. Schrijf je frustraties en boosheid van je af. Hierdoor verplaats je het vanuit je hoofd op papier. Het maakt je hoofd wat leger en tegelijkertijd kun je meer inzicht krijgen in waarom je nou boos of gefrustreerd bent. Het kan je ook helpen te reflecteren. Laura - redactrice Proud2Bme'],
            10: ['Reflecteer', 'Reflecteren op je eigen gevoelens en gedrag is eigenlijk altijd belangrijk. Dit doe je achteraf en je kunt dan vaak met wat meer afstand naar de situatie kijken. Hierdoor kun je er achter komen wat er in jouw hoofd omging en waarom je je op een bepaalde manier gedroeg. Je kunt dan ook inzien of dit bij jou paste, of dit het gedrag was wat jij wilde en wat jou heeft geholpen. Naar aanleiding van deze dingen kun je beslissen wat je de volgende keer hetzelfde of anders wil doen Laura - redactrice Proud2Bme'] 
            },
        'verdrietig': {
            1: ["Laat je tranen gaan", "Hoewel we vaak het gevoel hebben dat we sterk moeten zijn, blijkt uit verschillende studies dat het loont om tranen de vrije loop te laten. Door te huilen komt namelijk het ‘geluksstofje’ endorfine vrij, waardoor je jezelf beter voelt."],
            2: ["Zet je gevoelens op papier","Wanneer je verdrietig bent, denk je vaak aan niets anders. Door je gevoelens en gedachten op papier te zetten, kan je met afstand naar de situatie kijken en makkelijker je verdriet verwerken." ],
            3: ["Zoek het op", "Het is verleidelijk om zo min mogelijk bij je verdriet stil te staan. Toch is het aan te raden om dagelijks een (vast) moment te kiezen waarop je bewust met je verdriet bezig bent. Zo voorkom je dat jij je gevoelens opkropt."],
            4: ["Blijf lachen", "Uit onderzoek blijkt dat je gemoedstoestand verbetert wanneer je glimlacht; zelfs als het een niet gemeende glimlach is. Probeer dus om regelmatig een lach op je gezicht te toveren."],
            5: ["Zorg voor afleiding", "Het is niet goed om je verdriet weg te stoppen, maar dat betekent niet dat je er de hele dag mee bezig hoeft te zijn. Door leuke dingen te doen, kan jij je zinnen verzetten en zal je merken dat er nog genoeg is waar je plezier uit haalt."],
            6: ["Doe ontspanningsoefeningen", "Mindfulness, yoga en meditatie helpen bij verdriet verwerken omdat het accepteren van gedachten, ervaringen en gevoelens hierbij centraal staat. Het is dus zeker de moeite waard om je elke dag even terug te trekken."],
            7: ["Schaam je niet", "Voel jij je al weken ellendig omdat je kat is overleden? Ben je nog steeds verdrietig omdat die blind date op niets is uitgelopen? Ook al lijkt de reden van je verdriet voor anderen klein; je gevoelens mogen er zijn."],
            8: ["Zoek steun", "Verdriet verwerken gaat vaak makkelijker als jij je gevoelens deelt met vrienden of familie. Je staat er dan niet alleen voor en je kan je ei kwijt. In sommige situaties kan het fijn zijn om steun te zoeken bij iemand die wat verder van je af staat."],
            9: ["Geef jezelf de tijd", "Vooral bij ingrijpende gebeurtenissen als het overlijden van een dierbare kan het lang duren voordat jij je beter voelt. Wees geduldig en geef jezelf de tijd om het verdriet te verwerken."],
            10:["Zoek professionele hulp", "Merk je dat je steeds veder wegzakt in het verdriet? Voel jij je neerslachtig of depressief? Blijf dan niet in je eentje worstelen met je gevoelens en zoek professionele hulp!" ],
            11:["Sport regelmatig", "Sporten is niet alleen goed voor het lichaam, maar ook voor de geest. Wie dagelijks zo'n dertig minuten in beweging is, zal zich dan ook beter voelen."]
            }
        }

def getTip(mood):
    """
    Neemt als parameter 'mood' zoals Verdrietig of Boos.
    Vervolgens pakt deze functie een random tip uit de bovenstaande dictionary met de juiste mood en stuurt deze terug.
    """
    length_tips = len(mood_dict[mood])
    tip = mood_dict[mood][random.choice(range(1, length_tips))]
    
    return tip
