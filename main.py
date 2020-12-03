from random import randint

import pandas as pd
import telebot

import config
import dbworker

bot = telebot.TeleBot('1413386374:AAHDlVvaHph1NRT6PXvYluxkjyuor9Y2Cjs')

Classic_Doctors = {'Doctors_name': ['FirstDoctor', 'SecondDoctor', 'ThirdDoctor', 'FourthDoctor', 'FifthDoctor', 'SixthDoctor', 'SeventhDoctor', 'EighthDoctor'], 'About': ['William Hartnell (1963–1966). The First Doctor appeared to be a frail old man but don\'t be fooled. He played deadly games with the Celestial Toymaker, he fooled Roman emperors and French revolutionaries and foiled everything the evil Daleks could throw at him.',
'Patrick Troughton (1966–1969). The Second Doctor was very different to his predecessor. A more playful attitude disguised dark undercurrents and a sharp mind. He was famous for freezing the emotionless Cybermen into their ancient tombs but he was forced into exile after being tried for interference by the The Time Lords.',
'Jon Pertwee (1970–1974). The Third Doctor began his exile on earth with a new face. He was confident, bold and brash, but with a soft fatherly side. He helped the extraterrestrial taskforce Unit combat living plastic Autons, Sea Devils and polluted giant green maggots, as well as fellow renegade Time Lord, The Master.',
'Tom Baker (1974–1981). From witnessing the genesis of the Daleks to preventing the death of the universe at Logopolis, the Fourth Doctor was an adventurer on an epic scale. It was this incarnation of the Doctor that found and reassembled the Key to Time, and was invested as Lord President of the High Council of Time Lords. Tom Baker is currently the longest-serving Doctor.',
'Peter Davison (1981–1984). Clever, considered and kind, the Fifth Doctor\'s world was one of fascination and science. And it was in this fifth body that the Doctor was reunited with his past selves to fight in the Death Zone on Gallifrey.',
'Colin Baker (1984–1986). The Sixth Doctor was an explosion of colours, words and emotions. Passionate and sometimes quick to anger, this was a Doctor you did not want to make enemies with. He tangled with the corporate greed of the slimy Sil, and defeated the amoral Gallifreyan scientist known only as the Rani.',
'Seventh Doctor: Sylvester McCoy (1987–1989, 1996) The seventh incarnation of the Doctor was both a spoon-playing clown and a master of deep dark secrets. He toppled empires in a single night, entertained in the circus of the Gods of Ragnarok and played chess with the ancient and evil Fenric.',
'Paul McGann (1996, 2013). The Doctor regenerated into his Eighth form in a hospital morgue, on December 31, 1999 and teamed up with Grace Holloway to save the world from being pulled inside-out by the Master’s hijacking of the Tardis. Paul McGann only played the Doctor once, in a 1996 Doctor Who film, before reappearing in a special clip for the 2013 anniversary.']}

Classic_Docs = ['FirstDoctor','SecondDoctor','ThirdDoctor', 'FourthDoctor', 'FifthDoctor', 'SixthDoctor', 'SeventhDoctor', 'EighthDoctor']
Classic_Docs_About = [['William Hartnell (1963–1966). The First Doctor appeared to be a frail old man but don\'t be fooled. He played deadly games with the Celestial Toymaker, he fooled Roman emperors and French revolutionaries and foiled everything the evil Daleks could throw at him.'],
['Patrick Troughton (1966–1969). The Second Doctor was very different to his predecessor. A more playful attitude disguised dark undercurrents and a sharp mind. He was famous for freezing the emotionless Cybermen into their ancient tombs but he was forced into exile after being tried for interference by the The Time Lords.'],
['Jon Pertwee (1970–1974). The Third Doctor began his exile on earth with a new face. He was confident, bold and brash, but with a soft fatherly side. He helped the extraterrestrial taskforce Unit combat living plastic Autons, Sea Devils and polluted giant green maggots, as well as fellow renegade Time Lord, The Master.'],
['Tom Baker (1974–1981). From witnessing the genesis of the Daleks to preventing the death of the universe at Logopolis, the Fourth Doctor was an adventurer on an epic scale. It was this incarnation of the Doctor that found and reassembled the Key to Time, and was invested as Lord President of the High Council of Time Lords. Tom Baker is currently the longest-serving Doctor.'],
['Peter Davison (1981–1984). Clever, considered and kind, the Fifth Doctor\'s world was one of fascination and science. And it was in this fifth body that the Doctor was reunited with his past selves to fight in the Death Zone on Gallifrey.'],
['Colin Baker (1984–1986). The Sixth Doctor was an explosion of colours, words and emotions. Passionate and sometimes quick to anger, this was a Doctor you did not want to make enemies with. He tangled with the corporate greed of the slimy Sil, and defeated the amoral Gallifreyan scientist known only as the Rani.'],
['Seventh Doctor: Sylvester McCoy (1987–1989, 1996) The seventh incarnation of the Doctor was both a spoon-playing clown and a master of deep dark secrets. He toppled empires in a single night, entertained in the circus of the Gods of Ragnarok and played chess with the ancient and evil Fenric.'],
['Paul McGann (1996, 2013). The Doctor regenerated into his Eighth form in a hospital morgue, on December 31, 1999 and teamed up with Grace Holloway to save the world from being pulled inside-out by the Master’s hijacking of the Tardis. Paul McGann only played the Doctor once, in a 1996 Doctor Who film, before reappearing in a special clip for the 2013 anniversary.']]
Classic_Doctors_About = dict(zip(Classic_Docs, Classic_Docs_About))

New_Docs = ['TheWarDoctor', 'NinthDoctor', 'TenthDoctor', 'EleventhDoctor', 'TwelfthDoctor', 'ThirteenthDoctor']
New_Docs_About = [['John Hurt (50th anniversary episode) Although not technically classed as an official Doctor, The War Doctor\'s origin is explained in the mini-episode "The Night of the Doctor" whereby the eighth Doctor wishes to regenerate as a Warrior, instead of a Doctor. This is confirmed when he regenerates as John Hurt, whose first words are "Doctor no more." He then joins the tenth and eleventh Doctors in an attempt to stop the war on their home planet of Gallifrey.'], ['Christopher Eccleston (2005). The sole survivor of the Last Great Time War, scarred by the terrible things he\’d seen and done, the Ninth Doctor was an intense and emotional incarnation. He took Rose Tyler to see the end of the world, inspired Charles Dickens and showed that for once, everybody could live.'], ['David Tennant (2005–2010). Waking on Christmas Day in his new form, the tenth Doctor fought the Sycorax high above London. Travelling with Rose and Mickey he battled Cybermen, werewolves and possibly even the Devil itself. David was voted the nation\'s favourite Doctor.'], ['Matt Smith (2010–2013). Born, “still cooking”, into a crashing TARDIS, the Eleventh Doctor hurtled into the life of Amy Pond. The Doctor and Amy battled new paradigm Daleks in World War Two, Weeping Angels by the thousand and the depression in Vincent van Gogh\’s mind.'], ['Peter Capaldi (2013-2017). Peter first appeared as the Doctor briefly in the 50th anniversary special episode, but played minor characters in previous series. Peter\'s Doctor fought Daleks and Davros, Cybermen, Zygons, the Veil and the Time Lords.'], ['Jodie Whittaker (2017-present). We\'re yet to see what Jodie will be like as the Doctor. She\'s the first female to play the role and the first words she said when she realised she\'d regenerated as a woman were \'Aw, Brilliant!\' We agree!']]
New_Doctors_About = dict(zip(New_Docs, New_Docs_About))

New_Doctors = {'New_Doctors_name': ['TheWarDoctor', 'NinthDoctor', 'TenthDoctor', 'EleventhDoctor', 'TwelfthDoctor', 'ThirteenthDoctor'],
                             'About':[['John Hurt (50th anniversary episode) Although not technically classed as an official Doctor, The War Doctor\'s origin is explained in the mini-episode "The Night of the Doctor" whereby the eighth Doctor wishes to regenerate as a Warrior, instead of a Doctor. This is confirmed when he regenerates as John Hurt, whose first words are "Doctor no more." He then joins the tenth and eleventh Doctors in an attempt to stop the war on their home planet of Gallifrey.'],
                                      ['Christopher Eccleston (2005). The sole survivor of the Last Great Time War, scarred by the terrible things he\’d seen and done, the Ninth Doctor was an intense and emotional incarnation. He took Rose Tyler to see the end of the world, inspired Charles Dickens and showed that for once, everybody could live.'],
                                      ['David Tennant (2005–2010). Waking on Christmas Day in his new form, the tenth Doctor fought the Sycorax high above London. Travelling with Rose and Mickey he battled Cybermen, werewolves and possibly even the Devil itself. David was voted the nation\'s favourite Doctor.'], ['Matt Smith (2010–2013). Born, “still cooking”, into a crashing TARDIS, the Eleventh Doctor hurtled into the life of Amy Pond. The Doctor and Amy battled new paradigm Daleks in World War Two, Weeping Angels by the thousand and the depression in Vincent van Gogh\’s mind.'],
                                      ['Peter Capaldi (2013-2017). Peter first appeared as the Doctor briefly in the 50th anniversary special episode, but played minor characters in previous series. Peter\'s Doctor fought Daleks and Davros, Cybermen, Zygons, the Veil and the Time Lords.'],
                                      ['Jodie Whittaker (2017-present). We\'re yet to see what Jodie will be like as the Doctor. She\'s the first female to play the role and the first words she said when she realised she\'d regenerated as a woman were \'Aw, Brilliant!\' We agree!']]}

def infoDW(tag=0):
    df1 = pd.DataFrame(Classic_Doctors)
    return df1
df1 = pd.DataFrame(Classic_Doctors)

def infoNDW(tag=0):
    df2 = pd.DataFrame(New_Doctors)
    return df2

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Unofficial Doctor Who information bot. \n"
                 "I could provide you some information about \'Doctor Who\': TV show and main character. \n"
                 "First you could select the /intro_docto_who to know \'What is Doctor Who?\' \n"
                 "Then it's time to specify if you are interested in 'oldschool' stories or in 'new era' series from 2005.\n"
                 "You gotta type either /oldschool or /newera.\n"
                 "Type /reset to start again.")
    bot.send_message(message.chat.id, "There's a number of commands you can use here. \n"
                                      "Type /commands to get the list of available functions.\n"
                                      "Type /reset to start anew.")

@bot.message_handler(commands=["list_doctors"])
def cmd_list_doctors(message):
    x = infoDW()['Doctors_name']
    bot.send_message(message.chat.id, ', '.join(i for i in list(x)))
    bot.send_message(message.chat.id,'What\'s next? Copy one of the Doctor name to the Chat and press "Enter" ')

@bot.message_handler(commands=["list_new_doctors"])
def cmd_list_new_doctors(message):
    x = infoNDW()['New_Doctors_name']
    bot.send_message(message.chat.id, ', '.join(i for i in list(x)))
    bot.send_message(message.chat.id, 'What\'s next? Copy one of the Doctor name to the Chat and press "Enter" ')

@bot.message_handler(commands=["intro_docto_who"])
def cmd_commands(message):
    bot.send_message(message.chat.id, 'What is Doctor Who? \n'
                                      '\n'
'Doctor Who is a TV show. It has aired on the BBC \n'
'(British Broadcasting Corporation), in the United Kingdom, since November 1963 (although not continuously). \n'
'Because it\'s about time travel, Doctor Who is usually considered to be a science-fiction series. \n'
'However, individual stories run the gamut from action-adventure to gothic horror to dark comedy.\n')
    bot.send_message(message.chat.id, 'What is Doctor Who all about? \n'
                                      '\n'
'Doctor Who is about an alien time traveller known as the Doctor \n'
'“Doctor Who” is very rarely used as the name of the character -typically only in the end credits). \n'
'The Doctor is a member of a race of beings called the Time Lords, from the planet Gallifrey. \n '
'Most Time Lords obey a strict policy of non-interference in the events of the universe, \n '
'but the Doctor is a renegade, willfully intervening in history in order to fight evil and aid the oppressed.')


@bot.message_handler(commands=["start"])
def cmd_start(message):
    dbworker.set_state(message.chat.id, config.States.S_START.value)
    state = dbworker.get_current_state(message.chat.id)
    # Под "остальным" понимаем состояние "0" - начало диалога
    bot.send_message(message.chat.id, "Hi! I'm the Unofficial Doctor Who information bot :) \n"
                                      "You gotta specify which Doctor you want to get: /oldschool or /newera.\n"
                                      "Type /info to know what I am and what I can do for you.\n"
                                      "Type /commands to list the available commands.\n"
                                      "Type /reset to discard previous selections and start anew.")
    bot.send_photo(message.chat.id, pict[randint(0, 7)])
    dbworker.set_state(message.chat.id, config.States.S_INTRODUCTION.value)

@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Let's start anew.\n"
                                      "Use /info or /commands to rewind what I am and what can I do.")
    bot.send_photo(message.chat.id, pict[randint(0, 8)])
    dbworker.set_state(message.chat.id, config.States.S_INTRODUCTION.value)
    #TODO:
    # Удалить состояние пользователя

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_INTRODUCTION.value
                     and message.text.strip().lower() not in ('/reset', '/info', '/start', '/commands'))

@bot.message_handler(commands=["oldschool","newera"])
def oldscool_or_newera(message):
    dbworker.del_state(str(message.chat.id))
    if message.text.lower().strip() == '/oldschool':
        bot.send_message(message.chat.id, "Ok, you want to know more about Classic Doctor Who seasons from 1963 till 1989. \n"
                         "Enter the Doctor's \"reincarnation\" name.\n"
                         "Type /list_doctors to get the list of available fields.\n"
                         "You could also type /info to recollect what we are doing now.\n"
                         "Type /reset to start anew.")
        dbworker.set_state(str(message.chat.id), 'oldschool')  # запишем день в базу
        dbworker.set_state(message.chat.id, config.States.S_NEWERA_OR_OLDSCHOOL.value)
    elif message.text.lower().strip() == '/newera':
        bot.send_message(message.chat.id, "Ok, you want to know more about Modern Doctor Who seasons, which srats since 2005. \n"
                         "Enter the Doctor's \"new_reincarnation\" name.\n"
                         "Type /list_new_doctors to get the list of available fields.\n"
                         "You could also type /info to recollect what we are doing now.\n"
                         "Type /reset to start anew.")
        dbworker.set_state(str(message.chat.id), 'newera')  # запишем день в базу
        dbworker.set_state(message.chat.id, config.States.S_NEWERA_OR_OLDSCHOOL.value)
    else:
        bot.send_message(message.chat.id, "Something has gone wrong! Type either /oldschool or /newera.\n"
                                          "Type /info to recollect what we are doing now.\n"
                                          "Type /reset to start anew.")
# dbworker

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_NEWERA_OR_OLDSCHOOL.value
                     and message.text.strip() not in ('/reset', '/info', '/start', '/commands'))

# функция, которая будет печатать нужный текст про Доктора на основании ввода пользователя
@bot.message_handler(commands=['FirstDoctor','SecondDoctor','ThirdDoctor', 'FourthDoctor', 'FifthDoctor', 'SixthDoctor', 'SeventhDoctor', 'EighthDoctor',
                               'TheWarDoctor', 'NinthDoctor', 'TenthDoctor', 'EleventhDoctor', 'TwelfthDoctor', 'ThirteenthDoctor'])
def about_doctor(message):
    n = message.text.strip()
    dbworker.del_state(str(message.chat.id))
    if n in Classic_Docs:
        bot.send_message(message.chat.id, Classic_Doctors_About[n])
        index = Classic_Docs.index(n)
        if index == 0:
            bot.send_photo(message.chat.id, pict1[randint(0, 6)])
        elif index == 1:
            bot.send_photo(message.chat.id, pict2[randint(0, 3)])
        elif index == 2:
            bot.send_photo(message.chat.id, pict3[randint(0, 4)])
        elif index == 3:
            bot.send_photo(message.chat.id, pict4[randint(0, 3)])
        elif index == 4:
            bot.send_photo(message.chat.id, pict5[randint(0, 7)])
        elif index == 5:
            bot.send_photo(message.chat.id, pict6[randint(0, 4)])
        elif index == 6:
            bot.send_photo(message.chat.id, pict7[randint(0, 3)])
        elif index == 7:
            bot.send_photo(message.chat.id, pict8[randint(0, 3)])
        dbworker.set_state(str(message.chat.id), n)
        dbworker.set_state(message.chat.id, config.States.S_ENTER_WHICH_DOCTOR.value)
    elif n in New_Docs:
        bot.send_message(message.chat.id, New_Doctors_About[n])
        index = New_Docs.index(n)
        if index == 0:
            bot.send_photo(message.chat.id, pictNo[randint(0, 3)])
        elif index == 1:
            bot.send_photo(message.chat.id, pict9[randint(0, 3)])
        elif index == 2:
            bot.send_photo(message.chat.id, pict10[randint(0, 4)])
        elif index == 3:
            bot.send_photo(message.chat.id, pict11[randint(0, 4)])
        elif index == 4:
            bot.send_photo(message.chat.id, pict12[randint(0, 6)])
        elif index == 5:
            bot.send_photo(message.chat.id, pict13[randint(0, 6)])
        dbworker.set_state(str(message.chat.id), n)
        dbworker.set_state(message.chat.id, config.States.S_ENTER_WHICH_DOCTOR.value)
    else:
        bot.send_message(message.chat.id, "Something has gone wrong! Type name from /list_new_doctors or /list_doctors.\n"
                                          "Type /info to recollect what we are doing now.\n"
                                          "Type /reset to start anew.")


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_WHICH_DOCTOR.value
                     and message.text.strip() not in ('/reset', '/info', '/start', '/commands'))

# пришлось продублировать функцию ещё раз, чтобы программа корректно отвечала на запрос после первого вызова по имени доктора.
# без состояний, она корректно работала на основании первой функции, после внесения состояний вызывала функцию 1 раз и всё, потому что потом в базе перезаписывалось состояние
@bot.message_handler(commands=['FirstDoctor','SecondDoctor','ThirdDoctor', 'FourthDoctor', 'FifthDoctor', 'SixthDoctor', 'SeventhDoctor', 'EighthDoctor',
                               'TheWarDoctor', 'NinthDoctor', 'TenthDoctor', 'EleventhDoctor', 'TwelfthDoctor', 'ThirteenthDoctor'])
def about_doctor(message):
    n = message.text.strip()
    dbworker.del_state(str(message.chat.id))
    if n in Classic_Docs:
        bot.send_message(message.chat.id, Classic_Doctors_About[n])
        index = Classic_Docs.index(n)
        if index == 0:
            bot.send_photo(message.chat.id, pict1[randint(0, 5)])
        elif index == 1:
            bot.send_photo(message.chat.id, pict2[randint(0, 2)])
        elif index == 2:
            bot.send_photo(message.chat.id, pict3[randint(0, 3)])
        elif index == 3:
            bot.send_photo(message.chat.id, pict4[randint(0, 2)])
        elif index == 4:
            bot.send_photo(message.chat.id, pict5[randint(0, 7)])
        elif index == 5:
            bot.send_photo(message.chat.id, pict6[randint(0, 4)])
        elif index == 6:
            bot.send_photo(message.chat.id, pict7[randint(0, 3)])
        elif index == 7:
            bot.send_photo(message.chat.id, pict8[randint(0, 2)])
        dbworker.set_state(str(message.chat.id), n)
        dbworker.set_state(message.chat.id, config.States.S_ENTER_WHICH_DOCTOR.value)
    elif n in New_Docs:
        bot.send_message(message.chat.id, New_Doctors_About[n])
        index = New_Docs.index(n)
        if index == 0:
            bot.send_photo(message.chat.id, pictNo[randint(0, 2)])
        elif index == 1:
            bot.send_photo(message.chat.id, pict9[randint(0, 3)])
        elif index == 2:
            bot.send_photo(message.chat.id, pict10[randint(0, 3)])
        elif index == 3:
            bot.send_photo(message.chat.id, pict11[randint(0, 3)])
        elif index == 4:
            bot.send_photo(message.chat.id, pict12[randint(0, 6)])
        elif index == 5:
            bot.send_photo(message.chat.id, pict13[randint(0, 4)])
        dbworker.set_state(str(message.chat.id), n)
        dbworker.set_state(message.chat.id, config.States.S_ENTER_WHICH_DOCTOR.value)
    else:
        bot.send_message(message.chat.id, "Something has gone wrong! Type name from /list_new_doctors or /list_doctors.\n"
                                          "Type /info to recollect what we are doing now.\n"
                                          "Type /reset to start anew.")



@bot.message_handler(commands=["commands"])
def cmd_commands(message):
    bot.send_message(message.chat.id, "/reset - is used to discard previous selections and start anew.\n"
                                      "/start - is used to start a new dialogue from the very beginning.\n"
                                      "/info - is used to know what i can do for you (there's a tree of commands)\n"
                                      "/oldschool or /newera - for lists of Doctor's names \n"
                                      "/intro_docto_who - is used to list find basic info about.\n")

pict1 = ['https://media.archonia.com/images/samples/30/80/283080_s0.jpg',
         'https://v1.popcornnews.ru/upload/editor/William-Hartness-Doctor-Who(1).jpg',
         'https://svopi.ru/uploads/posts/2018-05/1525517099_doktor-kto.jpg',
         'https://i.pinimg.com/736x/d0/cb/c0/d0cbc08614fbc4f1302f8c318971898a--lost-episodes-first-doctor.jpg',
         'https://i.pinimg.com/originals/2e/05/cb/2e05cbcbf270c9b0d5de066f72581aa3.jpg',
         'http://img0.safereactor.cc/pics/post/full/Doctor-Who-%D1%84%D1%8D%D0%BD%D0%B4%D0%BE%D0%BC%D1%8B-DW-Art-1-%D0%94%D0%BE%D0%BA%D1%82%D0%BE%D1%80-1525656.jpeg']
pict2 = ['https://m.media-amazon.com/images/M/MV5BMTc2ODc4MTExMF5BMl5BanBnXkFtZTgwNzM5OTAzMTI@._V1_SY300_CR116',
         'https://images-cdn.9gag.com/photo/aN1gpoG_700b.jpg', 'https://fantazya.org/wp-content/uploads/2016/12/1.jpg',
         'https://kto-chto-gde.ru/wp-content/uploads/2018/03/luchshie-serii-klassicheskogo-doktora-kto-3.jpg']
pict3 = ['https://i.pinimg.com/736x/8e/72/36/8e7236a5177f94a587bc5599ad030a91.jpg',
         'https://whobackwhen.com/wp-content/uploads/jon-pertwee-third-doctor-who-back-when-retrospective.jpg',
         'https://i.pinimg.com/236x/8a/9f/aa/8a9faabb0fc2556c56839d09a229e99f.jpg',
         'https://ichef.bbci.co.uk/images/ic/1008xn/p00v94z7.jpg']
pict4 = ['https://cdn.oboi7.com/600794671da590b579de2ac69fd493e510cfe80a/kino-lyudi-chetvertyj-doktor-tom-bejker-aktery-doktor-kto.jpg',
         'https://i.pinimg.com/736x/fd/48/35/fd4835d90ada85ddd58fb6e3be1b7d5c.jpg',
         'https://i.pinimg.com/736x/b6/07/87/b6078700b86fc643d70bb1d3646c9e49.jpg']
pict5 = ['https://i1.wp.com/s.pikabu.ru/post_img/big/2013/06/07/10/1370622772_1625186235.jpg',
            'https://s14.stc.all.kpcdn.net/putevoditel/serialy/wp-content/uploads/2019/11/aNggtrwgPGVavEZmcjMPAVeRSFg.jpg',
            'http://static2.wikia.nocookie.net/__cb20100730233355/doctor-who-collectors/images/4/4f/Peter_davison_signed_postcard.jpg',
            'https://pm1.narvii.com/6730/2fa2201f7c5d5e23fbed03996f87d26959b6458dv2_hq.jpg',
            'https://www.syl.ru/misc/i/ni/1/1/7/4/6/0/i/117460_700x525.jpg',
            'http://www.tv-wallpapers.ru/posters/doctor_who_2005_6053_wallpaper.jpg',
            'http://www.tv-wallpapers.ru/posters/doctor_who_2005_6054_wallpaper.jpg',
            'http://baskino.me/uploads/images/2016/303/nyqv998.jpg']
pict6 = ['https://aif-s3.aif.ru/images/015/653/48009b0ab04eacb7fa56ed12bfde0653.jpg',
         'https://i.pinimg.com/originals/71/11/fd/7111fdff0afab97c0d62324bccae5dae.jpg',
         'https://kto-chto-gde.ru/wp-content/uploads/2018/03/luchshie-serii-klassicheskogo-doktora-kto-7.jpg',
         'https://4.bp.blogspot.com/-mTycsZRNJjI/WWvvcU-NweI/AAAAAAAABDM/9ngBmSEFnS4FnzZjac-8GNd0mvCmquoYgCLcBGAs/s1600/Doctor%2BWho%2BMagazine%2BSpecial%2B03%2B-%2BComplete%2B6th%2BDoctor%2B%25282002%2529_page62_image8.jpg',
         'https://fashionandphotographers.files.wordpress.com/2016/02/img_8596.jpg?w=793&h=1150']
pict7 = ['http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/11/remembrance-11.21.2013.jpg',
         'https://fb.ru/misc/i/gallery/71663/3143560.jpg',
         'https://image.invaluable.com/housePhotos/Chaucer/85/637985/H4586-L161178568.jpg',
         'https://unaffiliatedcritic.com/wp-content/uploads/2017/04/The-Seventh-Doctor-Sylvester-McCoy-and-Ace-Sophie-Aldred.jpg']
pict8 = ['https://www.soyuz.ru/public/uploads/files/6/7395782/20191113234252ee5d0a6930.jpg',
         'https://pbs.twimg.com/media/EOTWhhjXkAAPVWh.jpg',
         'https://cdn1.thr.com/sites/default/files/2013/11/doctor_who_8th_doctor.jpg']
pictNo = ['https://3.bp.blogspot.com/-IFlKVxa8zqU/WI-Wi6dHfqI/AAAAAAAAA0I/eZiFzHMHpOYamOt44Op-yugY6uUY9a4sACLcB/w1200-h630-p-k-no-nu/maxresdefault.jpg',
          'https://www.mirf.ru/wp-content/uploads/2020/10/2fbj91uo0wv1000.jpg',
          'https://2.bp.blogspot.com/-8CQaOq0240w/UolFDwEG0nI/AAAAAAAACi0/wxgMLAH4cWs/s1600/DOCTOR-WHO-50TH-ANNIVERSARY_THE-DAY-OF-THE-DOCTOR_69.jpg']
pict9 = ['https://wallup.net/wp-content/uploads/2018/10/05/907485-doctor-who-bbc-sci-fi-futuristic-series-comedy-adventure-drama-1dwho-tardis.jpg',
         'https://i.pinimg.com/originals/45/d4/d6/45d4d6968524c7e28424f4ba72b98e84.jpg',
         'https://cdn.quotesgram.com/img/34/42/1078952056-No_-62-The-9th-Doctor.jpg',
         'https://i.dailymail.co.uk/i/newpix/2019/07/17/16/025129600000044D-7256875-image-a-80_1563377041268.jpg']
pict10 = ['https://i.pinimg.com/originals/75/f8/c5/75f8c57aaaea4fb5aeefbe746e595ba5.png',
          'https://dvdbash.files.wordpress.com/2014/09/doctor-who-190-the-fires-of-pompeii-s4e02-dvdbash-14.jpg',
          'https://www.tokkoro.com/picsup/2907204-tardis-doctor-who-david-tennant-tenth-doctor___movie-wallpapers.jpg',
          'https://wallpaperscave.ru/images/original/18/06-14/tv-series-doctor-who-57715.jpg']
pict11 = ['https://i.pinimg.com/736x/e4/c7/e7/e4c7e7b764b91ffdbc19c6de4c25b22e.jpg',
          'https://wallpapertag.com/wallpaper/full/0/2/7/592105-download-matt-smith-doctor-who-wallpaper-2069x3000-for-lockscreen.jpg',
          'https://img2.pngio.com/13th-doctor-doctor-who-tardis-script-female-doctor-11th-doctor-who-11th-doctor-png-820_1019.png',
          'https://s3-eu-west-1.amazonaws.com/files.surfory.com/uploads/2015/5/3/554667c71f395da11b8b45bc/1280x/55466afb1f395d6a2d8b4576.jpg']
pict12 = ['https://img5tv.cdnvideo.ru/webp/shared/files/201704/1_478521.jpg',
          'https://cdn2-www.comingsoon.net/assets/uploads/gallery/doctor-who-series-10/s10_ep-1_24.jpg',
          'https://i.pinimg.com/originals/13/30/24/133024430d2231f24f29d73ecd9a806c.jpg',
          'https://i.pinimg.com/736x/e2/db/64/e2db6458a1b778c47e228dbafbb26ac6--doctor-who-peter-capaldi-doctor-who-.jpg',
          'https://i.pinimg.com/originals/48/0e/21/480e21767db3cb2373ad78202b8d8272.jpg',
          'https://i.pinimg.com/originals/e0/47/1d/e0471d7631cbc03b1bdacfd2f2f5fff2.jpg',
          'https://wallpaperscave.ru/images/original/18/01-27/tv-series-doctor-who-15834.jpg']
pict13 = ['https://krot.info/uploads/posts/2020-02/thumbs/1580749366_8-p-kadri-iz-filma-doktor-kto-reshenie-9.jpg',
          'https://image.tmdb.org/t/p/original/fMfL4vtoZO3Aa3fFq198otSsg0d.jpg',
          'https://u.kanobu.ru/editor/images/91/797a6a54-61b1-44f9-8943-abfb4b9fbc51.jpg',
          'https://brod.kz/media/news/wmul39/1510247967mgc15.jpg','https://pbs.twimg.com/media/DuZC8zrWkAAN-Ll.jpg',
          'https://i.imgur.com/p7cZsTd.jpg']



pict = ['https://pbs.twimg.com/media/EL5jdfqUwAE6qoY.jpg',
        'https://wallpaperscave.ru/images/original/18/06-20/tv-series-doctor-who-59671.jpg',
        'https://www.thesun.co.uk/wp-content/uploads/2019/03/NINTCHDBPICT000266505239.jpg',
        'https://wallpapertag.com/wallpaper/full/6/1/f/592080-matt-smith-doctor-who-wallpaper-1920x1080-download-free.jpg',
        'https://i.pinimg.com/736x/d0/10/7f/d0107f218198e8ebb493aaa1e4bcf4ac--david-tennant-doctor-who-david-tennant-funny.jpg',
        'https://ic.pics.livejournal.com/debora_debora/25070693/49001/49001_original.jpg',
        'http://doctor-kto.com/uploads/images/2018/789/pmut781.jpg',
        'https://r4.wallpaperflare.com/wallpaper/716/422/495/doctor-who-season-11-2018-4k-wallpaper-c826ad78e0c06cd8704cb10e988294da.jpg']


bot.polling()
