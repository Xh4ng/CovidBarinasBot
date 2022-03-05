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
        boa = types.KeyboardButton('🏥Covid-19')
        bob = types.KeyboardButton('😷Prevención')
        boc = types.KeyboardButton('🚑Síntomas')
        bod = types.KeyboardButton('👫👫Propagación')
        boe = types.KeyboardButton('📰Noticias')
        bof = types.KeyboardButton('📊Casos')
        bog = types.KeyboardButton('📌Bulos')
        boh = types.KeyboardButton('📑Acerca de este Bot')
        markup.row(boa, bob)
        markup.row(boc, bod)
        markup.row(boe, bof)
        markup.row(bog, boh)
        bot.send_message(cid, "¡Hola <i>" + nombre + "</i>!" + ", mucho gusto me llamo CovidBarinasBot. Soy un Bot de telegram y te proporcionare información acerca del Covid-19, que te pueda interesar en el estado Barinas.", parse_mode="HTML",reply_markup=markup)


        usuarios.append(cid)
        with open('/Ingrese/ubicacion/De/Carpeta/usuarios.txt','a') as f:
            f.write(str(cid)+'\n')

    else:
    
    
        nombre = m.from_user.first_name

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        boa = types.KeyboardButton('🏥Covid-19')
        bob = types.KeyboardButton('😷Prevención')
        boc = types.KeyboardButton('🚑Síntomas')
        bod = types.KeyboardButton('👫👫Propagación')
        boe = types.KeyboardButton('📰Noticias')
        bof = types.KeyboardButton('📊Casos')
        bog = types.KeyboardButton('📌Bulos')
        boh = types.KeyboardButton('📑Acerca de este Bot')
        markup.row(boa, bob)
        markup.row(boc, bod)
        markup.row(boe, bof)
        markup.row(bog, boh)
        bot.send_message(cid, "¡Hola <i>" + nombre + "</i>!" + ", mucho gusto me llamo CovidBarinasBot. Soy un Bot de telegram y te proporcionare información acerca del Covid-19, que te pueda interesar en el estado Barinas.(R)", parse_mode="HTML",reply_markup=markup)

@bot.message_handler(regexp="Covid-19")
def send_welcome(message):
    chatid = message.chat.id
    cov = "La COVID-19 es la enfermedad infecciosa causada por el coronavirus que se ha descubierto más recientemente. Tanto el nuevo virus como la enfermedad eran desconocidos antes de que estallara el brote en Wuhan (China) en diciembre de 2019.\n \n¿Qué es un coronavirus?\n \nLos coronavirus son una extensa familia de virus que pueden causar enfermedades tanto en animales como en humanos. En los humanos, se sabe que varios coronavirus causan infecciones respiratorias que pueden ir desde el resfriado común hasta enfermedades más graves como el síndrome respiratorio de Oriente Medio (MERS) y el síndrome respiratorio agudo severo (SRAS). El coronavirus que se ha descubierto más recientemente causa la enfermedad por coronavirus COVID-19."
    photo = open('/Ingrese/ubicacion/De/Carpeta/cov.jpg' , 'rb')
    bot.send_message(chatid, cov)
    tb.send_photo(chatid, photo)

@bot.message_handler(regexp="Síntomas")
def handle_message(message):
    chatid = message.chat.id
    sint = "La COVID-19 afecta a las personas de distintas maneras. La mayoría de las personas infectadas desarrollan síntomas de leves a moderados.\n \nSíntomas comunes:\n \n   -Fiebre\n \n   -Cansancio\n \n   -Tos seca\n \nAlgunas personas también pueden experimentar:\n \n   -Dolores y molestias\n \n   -Congestión nasal\n \n   -Abundante secreción nasal\n \n   -Dolor de garganta\n \n   -Diarrea\n \nCuando una persona se infecta con el virus, los síntomas tardan en aparecer en término medio de 5 a 6 días, pero pueden tardar hasta 14 días.\n \nLas personas con síntomas leves que, por lo demás, estén sanas deberían aislarse. Solicite atención médica si tiene fiebre, tos y dificultad para respirar. Llame con antelación."
    bot.send_message(chatid, sint)

@bot.message_handler(regexp="Propagación")
def handle_message(message):
	chatid = message.chat.id
	prop = "Una persona puede contraer la COVID-19 por contacto con otra que esté infectada por el virus. La enfermedad puede propagarse de persona a persona a través de las gotículas procedentes de la nariz o la boca que salen despedidas cuando una persona infectada tose o exhala. Estas gotículas caen sobre los objetos y superficies que rodean a la persona, de modo que otras personas pueden contraer la COVID-19 si tocan estos objetos o superficies y luego se tocan los ojos, la nariz o la boca. También pueden contagiarse si inhalan las gotículas que haya esparcido una persona con COVID-19 al toser o exhalar. Por eso es importante mantenerse a más de 1 metro (3 pies) de distancia de una persona que se encuentre enferma.\n \nLa OMS está estudiando las investigaciones en curso sobre las formas de propagación de la COVID-19 y seguirá informando sobre los resultados actualizados."
	bot.send_message(chatid, prop)

@bot.message_handler(regexp="Prevención")
def handle_message(message):
	chatid = message.chat.id
	preve = "1-Lávese las manos a fondo y con frecuencia usando un desinfectante a base de alcohol o con agua y jabón.\n \n2-Mantenga una distancia mínima de 1 metro (3 pies) entre usted y cualquier persona que tosa o estornude.\n \n3-Evite tocarse los ojos, la nariz y la boca\n \n4-Tanto usted como las personas que les rodean deben asegurarse de mantener una buena higiene de las vías respiratorias. Eso significa cubrirse la boca y la nariz con el codo doblado o con un pañuelo de papel al toser o estornudar. El pañuelo usado debe desecharse de inmediato.\n \n5Permanezca en casa si no se encuentra bien. Si tiene fiebre, tos y dificultad para respirar, busque atención médica y llame con antelación. Siga las instrucciones de las autoridades sanitarias locales.\n \n6-Manténgase informado sobre las últimas novedades en relación con la COVID-19. Siga los consejos de su dispensador de atención de salud, de las autoridades sanitarias pertinentes a nivel nacional y local o de su empleador sobre la forma de protegerse a sí mismo y a los demás ante la COVID-19.\n \n7-Consulte las noticias más recientes sobre las zonas de mayor peligro (es decir, las ciudades y lugares donde la enfermedad se está propagando más extensamente). Si le es posible, evite desplazarse a estas zonas, sobre todo si su edad es avanzada o tiene usted diabetes, cardiopatías o neumopatías."
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
#	notic = "¿Sobre cual lugar deseas ver las noticas acerca del Covid-19?"
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
	bul = "Noticias falsas\n \n1- La orina infantil: La orina no mata los virus ni las bacterias, más bien al contrario, ya que puede contener pequeñas cantidades de material vírico o bacteriano.\n \nPor ello, lavarse las manos o limpiar superficies con orina infantil no protege frente a la COVID-19. Lo recomendable es usar un desinfectante a base de alcohol o agua y jabón.\n \n2- La vitamina C: Las supuestas bondades de la vitamina C frente al coronavirus se han prodigado de muchas formas. Entre ellas, vídeos de una doctora que aseguraba haber curado a enfermos con un tratamiento basado en esta vitamina o audios de una presunta estudiante china de Ciencias Médicas que la recomendaba para “prevenir la COVID-19”.\n \nNo es así: la OMS dice que ningún alimento protege frente al nuevo coronavirus.\n \n3- Té caliente de limón y bicarbonato: Beber agua caliente no evitará que contraigamos la COVID-19, así como tampoco su mezcla con limón y bicarbonato, un “mejunje casi divino” cuyo origen se atribuye a Israel.\n \nLa “alcalinización del sistema inmunológico” que supuestamente se consigue por consumir una mezcla de limón y bicarbonato no es real y, del mismo modo, tampoco refuerza las defensas inmunológicas.\n \n“En personas sanas, la dieta no afecta de forma significativa al pH de la sangre, aunque pueda modificar el de la orina”, precisa el experto en Nutrición Joe Leech.\n \n4- Comer ajo: El ajo es un alimento saludable que puede tener algunas propiedades antimicrobianas, pero no se ha demostrado que comerlo proteja contra el virus que causa el brote actual.\n \n5- Beber mucha agua: Otros consejos difundidos por “unos médicos japoneses” hablaban de beber “agua cada 15 minutos y que la garganta nunca esté seca” para evitar el contagio.\n \nLa OMS y otros especialistas no creen que esto impida el avance de la enfermedad: “Otra tontería que no está recomendada por ningún organismo o institución sanitaria”, apunta Jaime Barrio, del Consejo Científico del Colegio de Médicos de Madrid.\n \n6- El clorito de sodio: Las supuestas bondades del clorito de sodio han sido difundidas sobre todo a través de vídeos, en los que se llega a asegurar que es posible superar el coronavirus si lo tomamos a diario, rebajado con agua.\n \n7- El vino: Una noticia positiva apareció en medio del drama por la propagación del virus a escala mundial: “La supervivencia del coronavirus en el vino es imposible” y “un consumo moderado puede ser beneficioso frente a la enfermedad”.\n \n8- La cocaína: Es simplemente una droga estimulante y adictiva, cuyo consumo provoca graves efectos secundarios y es perjudicial para la salud de las personas. No funciona contra el nuevo coronavirus, recuerda la OMS.\n \n9- Vacunas contra la neumonía: La neumocócica y la vacuna contra la Haemophilus influenzae de tipo B (Hib) no protegen tampoco contra el nuevo coronavirus.\n \nEl virus que provoca la COVID-19 es tan nuevo y diferente que es necesario desarrollar una vacuna específica, en la que ya se está trabajando con el apoyo de la OMS.\n \n10- Antibióticos: Estos medicamentos tampoco evitan el contagio ni curan al enfermo de la COVID-19. Los antibióticos son eficaces contra las bacterias, pero no contra los virus, como el que provoca esta enfermedad."
	bot.send_message(chatid, bul)


@bot.message_handler(regexp="Acerca de este Bot")
def handle_message(message):
    chatid = message.chat.id
    ace = "¿Quién creo este Bot?\n \nSu creador es Luis Ruiz (@LuisRuiz1998), estudiante de Telecomunicaciones en la E.T.I.E.Z.\n \nOrigen de este Bot\n \n El origen del bot radica en que fue hecho como un proyecto tecnológico.\n \n¿Con qué fin se creó este BOT?\n \nEste Bot fue creado con el fin de proporcionar información veraz y actualizada acerca de la enfermedad Covid-19."
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
	boa = types.KeyboardButton('🏥Covid-19')
	bob = types.KeyboardButton('😷Prevención')
	boc = types.KeyboardButton('🚑Síntomas')
	bod = types.KeyboardButton('👫👫Propagación')
	boe = types.KeyboardButton('📰Noticias')
	bof = types.KeyboardButton('📊Casos')
	bog = types.KeyboardButton('📌Bulos')
	boh = types.KeyboardButton('📑Acerca de este Bot')
	markup.row(boa, bob)
	markup.row(boc, bod)
	markup.row(boe, bof)
	markup.row(bog, boh)
	tb.send_message(chatid, "Disculpa, pero no tengo respuesta para eso. Prueba a preguntar otra cosa o a presionar uno de estos botones. :)", reply_markup=markup)
#	bot.send_message(chatid, "Disculpa, pero no tengo respuesta para eso")

print ("CovidBarinasBot se a iniciado.")
bot.polling()
