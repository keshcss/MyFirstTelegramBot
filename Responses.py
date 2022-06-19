from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "hey"):
        return "Hey! How is it going"

    if user_message in ("who are you", "who are you?"):
        return "I am Kesh! Well not really Kesh, but here to entertain you while the real kesh is stuck in camp oopsie."

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Well the guy who created me have not drummed up a response for that HAHAHA"