import vk_api
import requests
from vk_api.utils import get_random_id
#import datetime
from vk_api import VkUpload 
from main import startParse, conn, cur

###Session Creation
session = requests.Session()
login, password = '+79166463387', '3004990q'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
    print("Success")
except vk_api.AuthError as error_msg:
    print(error_msg)

work_list = ["Хей, бот", "Оладьи", "Салам"]


###Longpool Creation
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print(event.text)
        if event.text in work_list: #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Введи запрос для анализа hh.ru (быстрее, пока я не передумал)'
		        )
            elif event.from_chat:
                    vk.messages.send( #Отправляем сообщение
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message='Введи запрос для анализа hh.ru (быстрее, пока я не передумал)'
		        )
            for eventNew in longpoll.listen():
                if eventNew.type == VkEventType.MESSAGE_NEW and eventNew.to_me and eventNew.text:
                    if eventNew.from_user:
                        print(eventNew.text)
                        eventor = eventNew.text.split()
                        startParse(eventor)
                        upload = VkUpload(vk_session)
                        for i in eventor:
                                photo = upload.photo_messages(photos="%s_plot.png"%i)[0]
                                
                                vk.messages.send(
                                    user_id=eventNew.user_id,
                                    random_id=get_random_id(),
                                    attachment='photo{}_{}'.format(photo['owner_id'], photo['id']),
                                    message='%s Salary info'%i
                                )

                                vk.messages.send( #Отправляем сообщение
                                user_id=eventNew.user_id,
                                random_id=get_random_id(),
                                message='Бывай'
                                )
                            
                                break


                    elif eventNew.from_chat:
                        print(eventNew.text)
                        eventor = eventNew.text.split()
                        startParse(eventor)
                        upload = VkUpload(vk_session)
                        for i in eventor:
                                photo = upload.photo_messages(photos="%s_plot.png"%i)[0]
                                
                                vk.messages.send(
                                    chat_id=eventNew.chat_id,
                                    random_id=get_random_id(),
                                    attachment='photo{}_{}'.format(photo['owner_id'], photo['id']),
                                    message='%s Salay info'%i
                                )
                        vk.messages.send( #Отправляем сообщение
                            chat_id=eventNew.chat_id,
                            random_id=get_random_id(),
                            message='Бывай'
                        )
                        break

