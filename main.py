import telebot 
from telebot import types
from cred import TOKEN

bot = telebot.TeleBot(TOKEN)
tb = telebot.TeleBot(TOKEN)
usuarios = list()

for linea in open('/Ingrese/ubicacion/De/Carpeta/usu.txt','r'):

    chatid = int(linea)
    
    usuarios.append(chatid)
    
@bot.message_handler(commands=['start'])
def send_welcome(m):
    cid = m.chat.id

    if cid not in usuarios:


        nombre = m.from_user.first_name

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        boa = types.KeyboardButton('馃彞Covid-19')
        bob = types.KeyboardButton('馃樂Prevenci贸n')
        boc = types.KeyboardButton('馃殤S铆ntomas')
        bod = types.KeyboardButton('馃懌馃懌Propagaci贸n')
        boe = types.KeyboardButton('馃摪Noticias')
        bof = types.KeyboardButton('馃搳Casos')
        bog = types.KeyboardButton('馃搶Bulos')
        boh = types.KeyboardButton('馃搼Acerca de este Bot')
        markup.row(boa, bob)
        markup.row(boc, bod)
        markup.row(boe, bof)
        markup.row(bog, boh)
        bot.send_message(cid, "隆Hola <i>" + nombre + "</i>!" + ", mucho gusto me llamo CovidBarinasBot. Soy un Bot de telegram y te proporcionare informaci贸n acerca del Covid-19, que te pueda interesar en el estado Barinas.", parse_mode="HTML",reply_markup=markup)


        usuarios.append(cid)
        with open('/Ingrese/ubicacion/De/Carpeta/usuarios.txt','a') as f:
            f.write(str(cid)+'\n')

    else:
    
    
        nombre = m.from_user.first_name

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        boa = types.KeyboardButton('馃彞Covid-19')
        bob = types.KeyboardButton('馃樂Prevenci贸n')
        boc = types.KeyboardButton('馃殤S铆ntomas')
        bod = types.KeyboardButton('馃懌馃懌Propagaci贸n')
        boe = types.KeyboardButton('馃摪Noticias')
        bof = types.KeyboardButton('馃搳Casos')
        bog = types.KeyboardButton('馃搶Bulos')
        boh = types.KeyboardButton('馃搼Acerca de este Bot')
        markup.row(boa, bob)
        markup.row(boc, bod)
        markup.row(boe, bof)
        markup.row(bog, boh)
        bot.send_message(cid, "隆Hola <i>" + nombre + "</i>!" + ", mucho gusto me llamo CovidBarinasBot. Soy un Bot de telegram y te proporcionare informaci贸n acerca del Covid-19, que te pueda interesar en el estado Barinas.(R)", parse_mode="HTML",reply_markup=markup)

@bot.message_handler(regexp="Covid-19")
def send_welcome(message):
    chatid = message.chat.id
    cov = "La COVID-19 es la enfermedad infecciosa causada por el coronavirus que se ha descubierto m谩s recientemente. Tanto el nuevo virus como la enfermedad eran desconocidos antes de que estallara el brote en Wuhan (China) en diciembre de 2019.\n \n驴Qu茅 es un coronavirus?\n \nLos coronavirus son una extensa familia de virus que pueden causar enfermedades tanto en animales como en humanos. En los humanos, se sabe que varios coronavirus causan infecciones respiratorias que pueden ir desde el resfriado com煤n hasta enfermedades m谩s graves como el s铆ndrome respiratorio de Oriente Medio (MERS) y el s铆ndrome respiratorio agudo severo (SRAS). El coronavirus que se ha descubierto m谩s recientemente causa la enfermedad por coronavirus COVID-19."
    photo = open('/Ingrese/ubicacion/De/Carpeta/cov.jpg' , 'rb')
    bot.send_message(chatid, cov)
    tb.send_photo(chatid, photo)

@bot.message_handler(regexp="S铆ntomas")
def handle_message(message):
    chatid = message.chat.id
    sint = "La COVID-19 afecta a las personas de distintas maneras. La mayor铆a de las personas infectadas desarrollan s铆ntomas de leves a moderados.\n \nS铆ntomas comunes:\n \n   -Fiebre\n \n   -Cansancio\n \n   -Tos seca\n \nAlgunas personas tambi茅n pueden experimentar:\n \n   -Dolores y molestias\n \n   -Congesti贸n nasal\n \n   -Abundante secreci贸n nasal\n \n   -Dolor de garganta\n \n   -Diarrea\n \nCuando una persona se infecta con el virus, los s铆ntomas tardan en aparecer en t茅rmino medio de 5 a 6 d铆as, pero pueden tardar hasta 14 d铆as.\n \nLas personas con s铆ntomas leves que, por lo dem谩s, est茅n sanas deber铆an aislarse. Solicite atenci贸n m茅dica si tiene fiebre, tos y dificultad para respirar. Llame con antelaci贸n."
    bot.send_message(chatid, sint)

@bot.message_handler(regexp="Propagaci贸n")
def handle_message(message):
	chatid = message.chat.id
	prop = "Una persona puede contraer la COVID-19 por contacto con otra que est茅 infectada por el virus. La enfermedad puede propagarse de persona a persona a trav茅s de las got铆culas procedentes de la nariz o la boca que salen despedidas cuando una persona infectada tose o exhala. Estas got铆culas caen sobre los objetos y superficies que rodean a la persona, de modo que otras personas pueden contraer la COVID-19 si tocan estos objetos o superficies y luego se tocan los ojos, la nariz o la boca. Tambi茅n pueden contagiarse si inhalan las got铆culas que haya esparcido una persona con COVID-19 al toser o exhalar. Por eso es importante mantenerse a m谩s de 1 metro (3 pies) de distancia de una persona que se encuentre enferma.\n \nLa OMS est谩 estudiando las investigaciones en curso sobre las formas de propagaci贸n de la COVID-19 y seguir谩 informando sobre los resultados actualizados."
	bot.send_message(chatid, prop)

@bot.message_handler(regexp="Prevenci贸n")
def handle_message(message):
	chatid = message.chat.id
	preve = "1-L谩vese las manos a fondo y con frecuencia usando un desinfectante a base de alcohol o con agua y jab贸n.\n \n2-Mantenga una distancia m铆nima de 1 metro (3 pies) entre usted y cualquier persona que tosa o estornude.\n \n3-Evite tocarse los ojos, la nariz y la boca\n \n4-Tanto usted como las personas que les rodean deben asegurarse de mantener una buena higiene de las v铆as respiratorias. Eso significa cubrirse la boca y la nariz con el codo doblado o con un pa帽uelo de papel al toser o estornudar. El pa帽uelo usado debe desecharse de inmediato.\n \n5Permanezca en casa si no se encuentra bien. Si tiene fiebre, tos y dificultad para respirar, busque atenci贸n m茅dica y llame con antelaci贸n. Siga las instrucciones de las autoridades sanitarias locales.\n \n6-Mant茅ngase informado sobre las 煤ltimas novedades en relaci贸n con la COVID-19. Siga los consejos de su dispensador de atenci贸n de salud, de las autoridades sanitarias pertinentes a nivel nacional y local o de su empleador sobre la forma de protegerse a s铆 mismo y a los dem谩s ante la COVID-19.\n \n7-Consulte las noticias m谩s recientes sobre las zonas de mayor peligro (es decir, las ciudades y lugares donde la enfermedad se est谩 propagando m谩s extensamente). Si le es posible, evite desplazarse a estas zonas, sobre todo si su edad es avanzada o tiene usted diabetes, cardiopat铆as o neumopat铆as."
	bot.send_message(chatid, preve)

@bot.message_handler(regexp="Noticias")
def handle_message(message):
    chatid = message.chat.id
    bot.send_message(chatid, "https://elpais.com/sociedad/2020-06-11/la-expansion-del-virus-por-america-preocupa-a-los-expertos.html")
    bot.send_message(chatid, "http://ultimasnoticias.com.ve/noticias/mundo/asciende-a-7-487-704-los-casos-positivos-por-covid-19-a-escala-global/")
    bot.send_message(chatid, "http://www.ultimasnoticias.com.ve/noticias/pulso/cierran-10-establecimientos-por-incumplir-cuarentena-en-barinas/")

#@bot.message_handler(regexp="Noticias")
#def handle_message(message):
#	chatid = message.chat.id
#	notic = "驴Sobre cual lugar deseas ver las noticas acerca del Covid-19?"
#	markup = types.ReplyKeyboardMarkup()
#	boa = types.KeyboardButton('Noticias en el Mundo')
#	bob = types.KeyboardButton('Noti Venezuela')
#	boc = types.KeyboardButton('Noticias en Barinas')
#	markup.row(boa)
#	markup.row(bob)
#	markup.row(boc)
#	bot.send_message(chatid, notic, reply_markup=markup)

#@bot.message_handler(regexp="Casos")
#def handle_message(message):
#	chatid = message.chat.id
#	cac = "Por favor, elige una de estas opciones para ver los casos."
#	markup = types.ReplyKeyboardMarkup()
#	boa = types.KeyboardButton('Casos en el Mundo')
#	bob = types.KeyboardButton('/Casos')
#	boc = types.KeyboardButton('Casos en Barinas')
#	markup.row(boa)
#	markup.row(bob)
#	markup.row(boc)
#	bot.send_message(chatid, cac, reply_markup=markup)

@bot.message_handler(regexp="Casos")
def handle_message(message):
    chatid = message.chat.id
    photo = open(/Ingrese/ubicacion/De/Carpeta/mapcov.png' , 'rb')
    bot.send_message(chatid, "https://news.google.com/covid19/map?hl=es-419&gl=VE&ceid=VE%3Aes-419&mid=%2Fm%2F07ylj")
    tb.send_photo(chatid, photo)

@bot.message_handler(regexp="Bulos")
def handle_message(message):
	chatid = message.chat.id
	bul = "Noticias falsas\n \n1- La orina infantil: La orina no mata los virus ni las bacterias, m谩s bien al contrario, ya que puede contener peque帽as cantidades de material v铆rico o bacteriano.\n \nPor ello, lavarse las manos o limpiar superficies con orina infantil no protege frente a la COVID-19. Lo recomendable es usar un desinfectante a base de alcohol o agua y jab贸n.\n \n2- La vitamina C: Las supuestas bondades de la vitamina C frente al coronavirus se han prodigado de muchas formas. Entre ellas, v铆deos de una doctora que aseguraba haber curado a enfermos con un tratamiento basado en esta vitamina o audios de una presunta estudiante china de Ciencias M茅dicas que la recomendaba para 鈥減revenir la COVID-19鈥?.\n \nNo es as铆: la OMS dice que ning煤n alimento protege frente al nuevo coronavirus.\n \n3- T茅 caliente de lim贸n y bicarbonato: Beber agua caliente no evitar谩 que contraigamos la COVID-19, as铆 como tampoco su mezcla con lim贸n y bicarbonato, un 鈥渕ejunje casi divino鈥? cuyo origen se atribuye a Israel.\n \nLa 鈥渁lcalinizaci贸n del sistema inmunol贸gico鈥? que supuestamente se consigue por consumir una mezcla de lim贸n y bicarbonato no es real y, del mismo modo, tampoco refuerza las defensas inmunol贸gicas.\n \n鈥淓n personas sanas, la dieta no afecta de forma significativa al pH de la sangre, aunque pueda modificar el de la orina鈥?, precisa el experto en Nutrici贸n Joe Leech.\n \n4- Comer ajo: El ajo es un alimento saludable que puede tener algunas propiedades antimicrobianas, pero no se ha demostrado que comerlo proteja contra el virus que causa el brote actual.\n \n5- Beber mucha agua: Otros consejos difundidos por 鈥渦nos m茅dicos japoneses鈥? hablaban de beber 鈥渁gua cada 15 minutos y que la garganta nunca est茅 seca鈥? para evitar el contagio.\n \nLa OMS y otros especialistas no creen que esto impida el avance de la enfermedad: 鈥淥tra tonter铆a que no est谩 recomendada por ning煤n organismo o instituci贸n sanitaria鈥?, apunta Jaime Barrio, del Consejo Cient铆fico del Colegio de M茅dicos de Madrid.\n \n6- El clorito de sodio: Las supuestas bondades del clorito de sodio han sido difundidas sobre todo a trav茅s de v铆deos, en los que se llega a asegurar que es posible superar el coronavirus si lo tomamos a diario, rebajado con agua.\n \n7- El vino: Una noticia positiva apareci贸 en medio del drama por la propagaci贸n del virus a escala mundial: 鈥淟a supervivencia del coronavirus en el vino es imposible鈥? y 鈥渦n consumo moderado puede ser beneficioso frente a la enfermedad鈥?.\n \n8- La coca铆na: Es simplemente una droga estimulante y adictiva, cuyo consumo provoca graves efectos secundarios y es perjudicial para la salud de las personas. No funciona contra el nuevo coronavirus, recuerda la OMS.\n \n9- Vacunas contra la neumon铆a: La neumoc贸cica y la vacuna contra la Haemophilus influenzae de tipo B (Hib) no protegen tampoco contra el nuevo coronavirus.\n \nEl virus que provoca la COVID-19 es tan nuevo y diferente que es necesario desarrollar una vacuna espec铆fica, en la que ya se est谩 trabajando con el apoyo de la OMS.\n \n10- Antibi贸ticos: Estos medicamentos tampoco evitan el contagio ni curan al enfermo de la COVID-19. Los antibi贸ticos son eficaces contra las bacterias, pero no contra los virus, como el que provoca esta enfermedad."
	bot.send_message(chatid, bul)


@bot.message_handler(regexp="Acerca de este Bot")
def handle_message(message):
    chatid = message.chat.id
    ace = "驴Qui茅n creo este Bot?\n \nSu creador es Luis Ruiz (@LuisRuiz1998), estudiante de Telecomunicaciones en la E.T.I.E.Z.\n \nOrigen de este Bot\n \n El origen del bot radica en que fue hecho como un proyecto tecnol贸gico.\n \n驴Con qu茅 fin se cre贸 este BOT?\n \nEste Bot fue creado con el fin de proporcionar informaci贸n veraz y actualizada acerca de la enfermedad Covid-19."
    photo = open('/Ingrese/ubicacion/De/Carpeta/log.png' , 'rb')
    bot.send_message(chatid, ace)
    tb.send_photo(chatid, photo)

@bot.message_handler(regexp="barinas")
def handle_message(message):
    chatid = message.chat.id
    photo = open('/Ingrese/ubicacion/De/Carpeta/mapbab.png' , 'rb')
    bot.send_message(chatid, "https://news.google.com/covid19/map?hl=es-419&gl=VE&ceid=VE%3Aes-419&mid=%2Fm%2F02pp3d")
    tb.send_photo(chatid, photo)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	chatid = message.chat.id
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	boa = types.KeyboardButton('馃彞Covid-19')
	bob = types.KeyboardButton('馃樂Prevenci贸n')
	boc = types.KeyboardButton('馃殤S铆ntomas')
	bod = types.KeyboardButton('馃懌馃懌Propagaci贸n')
	boe = types.KeyboardButton('馃摪Noticias')
	bof = types.KeyboardButton('馃搳Casos')
	bog = types.KeyboardButton('馃搶Bulos')
	boh = types.KeyboardButton('馃搼Acerca de este Bot')
	markup.row(boa, bob)
	markup.row(boc, bod)
	markup.row(boe, bof)
	markup.row(bog, boh)
	tb.send_message(chatid, "Disculpa, pero no tengo respuesta para eso. Prueba a preguntar otra cosa o a presionar uno de estos botones. :)", reply_markup=markup)
#	bot.send_message(chatid, "Disculpa, pero no tengo respuesta para eso")

print ("CovidBarinasBot se a iniciado.")
bot.polling()
