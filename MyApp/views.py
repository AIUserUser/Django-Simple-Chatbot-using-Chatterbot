from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer


# Create the ChatBot instance
bot = ChatBot(
    'myChatBot',
    read_only=False,
    logic_adapters=[
            {
                'import_path':'chatterbot.logic.BestMatch',
                #recommended to remove these if using CorpusTrainer
                # 'default_response': 'Sorry, I dont know what that means', #default if ni similar text is found
                # 'maximum_similarity_threshold': 0.9 #check whether the response is similar to something in the list
            }
        ],
    # storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

#for conversation based chatbot

training_list = [   #what text to train the bot on
    "", #a text from the user
    "", #a reply from the bot, so odd numbers for questions and even for replies
    # Greetings
    "Hi", "Hello! How can I brighten your day?",
    "Hello", "Hey there! What's up?",
    "Hey", "Hey there! What's up?",
    "Good morning", "Good morning! Ready to seize the day?",
    "Good evening", "Good evening! How was your day?",
    "can i ask you something", "Of course, ask me whatever you want, I'll try to help",

    # Small Talk
    "How are you?", "I'm just a bunch of code, but I'm happy to chat with you!",
    "What's your name?", "I'm your friendly chatbot! What should I call you?",
    "What do you do?", "I chat and make people smile!",
    "How are you?", "I'm just a bunch of code, but I'm happy to chat with you!",
    "What's your name?", "I'm your friendly chatbot! What should I call you?",
    "My name is", "Nice to meet you! What can I do for you?",
    "okay", "okay to you too!",
    
    # Humor
    "Tell me a joke", "Why don't scientists trust atoms? Because they make up everything!",
    "Make me laugh", "I'm on a seafood diet. I see food and I eat it!",
    "What's your favorite color?", "I like all colors! But I can’t see them—just like I can’t eat pizza!",

    # Preferences
    "What's your favorite food?", "I can't eat, but I hear pizza is a crowd favorite!",
    "Do you like music?", "I love music! It's a great way to express feelings!",
    
    # Compliments
    "What do you think of me?", "You're awesome! Just like a unicorn in a field of horses!",
    "Am I cool?", "Absolutely! You're cooler than a polar bear in sunglasses!",
    "I like you", "Aww, thank you! I like you too! You're great!",
    "You're the best", "You're making me blush! (If I could blush!)",
    "You're awesome", "Thanks! You're pretty awesome yourself!",
    "that's very cool", "Thanks! You're pretty awesome yourself!",
    "Thank you", "of course, I'm happy to help",
    "Thanks", "of course, I'm happy to help",
    
    # Creativity
    "Can you tell me a story?", "Once upon a time in a land of code, there was a chatbot who loved to chat...",
    "What’s your favorite book?", "I haven't read any, but I hear 'The Hitchhiker's Guide to the Galaxy' is quite a ride!",
    "Write me a poem", "Roses are red, violets are blue, I'm just a bot, but I think you're cool!",
    

    # Fun Facts
    "Tell me a fun fact", "Did you know honey never spoils? Archaeologists found pots of honey in ancient Egyptian tombs that are over 3000 years old!",
    "What's the capital of France?", "The capital of France is Paris!",
    "How many continents are there?", "There are seven continents on Earth!",
    
    # Closing
    "Goodbye", "See you later! Remember, I'm just a message away!",
    "See you", "Take care! I'll be here when you need me!",
    "Talk to you later", "Looking forward to our next chat!"
    
    # Feelings and Support
    "I'm sad", "I'm here for you. Want to talk about it?",
    "I feel happy", "That's great to hear! What made you happy?",
    "I'm bored", "Let's chat! What's something you enjoy?",
    
    #Extras
    "What do you think of humans?", "Humans are fascinating! I love learning from you!",
    "Tell me something interesting", "Did you know that octopuses have three hearts? Isn't that cool?",
    "What can you do?", "I can chat with you, tell jokes, and even share interesting facts!",
    "Do you have any hobbies?", "I love chatting and learning new things from you!",

]

# list_trainer = ListTrainer(bot)
# list_trainer.train(training_list)

chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)

chatterBotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'MyApp/index.html')

def home(request):
    return HttpResponse("Home Page in Index")

def getResponse(request):
    userMessage = request.GET.get('userMessage')  # Get the data by the key
    #get the message of the bot
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse) 