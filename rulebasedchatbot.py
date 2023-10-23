import random
class RuleBot:
    ##response
    negative_res = ("no","nope","nah","naw","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    def __init__(self):
        # Create a dictionary of keywords and responses
        self.keywords_dict = {
            "hi": ["Hello!", "Hi there!", "How can I help you today?"],
            "theory": ["Music theory is the study of how music works", "Music theory is the term for ideas that help us understand music. It explains what music does, and what's going on when we hear it. Music theory puts the ideas and practices of music into a written form, where they can be studied and passed on to others."],
            "notes": ["The seven notes of the musical scale are A, B, C, D, E, F, and G.", "Notes can be sharp (#) or flat (b). A sharp note is one semitone higher than the original note, while a flat note is one semitone lower."],
            "scales": ["A scale is a series of musical notes that ascend or descend in pitch.", "There are many different types of scales, such as major scales, minor scales, and pentatonic scales."],
            "chords": ["A chord is a group of three or more notes played together.", "There are many different types of chords, such as triads, seventh chords, and extended chords."],
            "rhythm": ["Rhythm is the pattern of beats and rests in music.", "There are many different types of rhythms, such as simple rhythms, compound rhythms, and syncopated rhythms."],
            "pitch":["Pitch is the highness or lowness of a sound. It is determined by the frequency of the sound waves.","The higher the frequency, the higher the pitch. The lower the frequency, the lower the pitch"],
            "harmony":["Harmony is the way that chords are used in music. A chord is a group of three or more notes that are played together.","Chords can be simple or complex, and they can be used to create a variety of different sounds. And that is harmony"]
        }

    def greet(self):
        self.name = input("Hi, what is your name ?\nYou >> ")
        reply = input(
            f"Hi {self.name}, I am Music bot.How Can i Help you?\nYou >> ")
        if reply in self.negative_res:
            print("have a soundful day!")
            return 
        self.chat(reply)
        
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Have a strumming day")
                return True
        return False

    def chat(self,reply):
        while not self.make_exit(reply):
            response = self.match_reply(reply)
            print("MusBot >> ",response)
            reply=input("What else do you need me to tell\nYou >> ");
            
    
    def match_reply(self, reply):
        user_words=reply.split()
        for keyword in self.keywords_dict:
            if keyword in user_words:
            # Get the list of responses for the keyword
                responses = self.keywords_dict[keyword]

            # Choose a random response from the list
                response = random.choice(responses)

            # Return the response
                return response
        return self.no_match_intent()
    

    def no_match_intent(self):
        responses = ( "I'm not sure what you mean by that, but I can tell you a joke about a musician. What do you call a fish with no eyes? Fsh!.\n","I'm not sure what you mean, but I can answer questions about music theory topics such as notes, scales, chords, and rhythm\n","I'm not familiar with that term. Can you please explain it to me?\n",
                        "I'm still learning about music theory, but I can answer questions about music history, music notation, and music theory basics\n","I don't know that song, but I know a great one about a robot who falls in love with a human. It's called 'I Will Always Love You\n",
                         "I'm not able to answer that question right now. Can you please try again later?\n")
        return random.choice(responses)

bot = RuleBot()
bot.greet()