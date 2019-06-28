import string
import random

class SmallPerson():
    def __init__(self):
        self.greetings_in = ['hello', 'hi', 'hii', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
        self.food_in = ['food', 'cream', 'pizza', 'eat', 'eating', 'juice', 'broccoli']
        self.mom_in = ['mom', 'mommy', 'mother', 'mama', 'moms', 'daddy', 'dad', 'dads']
        self.sleep_in = ['sleep']
        self.tickle_in = ['tickle', '-tickle-']
        self.toy_in = ['toy', 'car', 'play']
        self.point_in = ['point']
        self.dog_in = ['dog', 'doggy', 'doggie', 'dogs', 'doggies', 'doggys']

        
    def remove_punctuation(self, input_string):
        """ 
        Strips punctuation from input string
        
        Parameters
        -----------
        input_string: String
            The user input sentence
        
        Returns the input string with punctuation removed
        """
        out_string = ''
        for item in input_string:
            if ((item in string.punctuation) == False):
                out_string = out_string + item
        return out_string
    
    def prepare_text(self, input_string):
        """ 
        Prepares the input text: makes everything lowercase, removes punctuation, splits into separate words 
        
        Parameters
        -----------
        input_string: String
            The user input sentence
        
        Returns the input string made into a list of words
        """
        out_list = []
        temp_string = input_string.lower()
        #print(temp_string)
        temp_string = self.remove_punctuation(temp_string)
        #print(temp_string)
        out_list = temp_string.split(); # split at the space
        return out_list
    
    def selector(self, input_list, check_list, return_list):
        """ 
        Selects the output for the chatbot based on the given input 
        
        Parameters
        -----------
        input_string: Input list, list of words to check from, list of outputs
            
        
        Returns the string output of the child
        """
        output = None
        #print(check_list)
        for item in input_list:
            #print(item)
            if (item in check_list):
                #print("if statement reached")
                output = random.choice(return_list)
                break
        #print(output)
        return output
    
    def end_chat(self, input_list):
        """ 
        Returns a boolean value based on whether the user typed in 'quit' 
        
        input_string: String
            The user input sentence
        
        """
        for item in input_list:
            if(item == 'quit'):
                output = True
            else:
                output = False
        return output
  

class Baby(SmallPerson):
    
    def __init__(self):
        super().__init__()
        self.age = 1
        
        # Create vocabulary
        self.greetings_out = ['ba!', 'ma!', '*smiles*', '*is looking at you*', '*is looking at you* *drooles*', '*giggles*']
        self.unknown = ['aaa? *tears up* *starts crying* aaaaaaaaaaAAAAAAAAAAAAAAAAAAA *probably because it didnt understand you*',
                       'aaaa? *tears up* *talk to him before he starts crying!!!* *p.s. he likes talking about food*',
                       'aaaa? *tears up* *talk to him before he cries again!* *p.s. maybe ask him about his mom*',
                       'aaaa? *tears up* *talk to him before he starts crying!* *p.s. he likes hearing about sleep*',
                       'aaaaaa? *tears up* *starts crying* *life is hard when youre a baby and dont understand anything*',
                       'aa? aaaa? *tears up* *type tickle to make him laugh!*',
                       'tatata??', 'tata?', 'ta??', 'tata tata?']
        self.food_out = ['*excited* yaaaa! *he likes food*', 'bababa! *he understood you!*', 
                         'aaaaa! *drooles on you* *he REALLY likes food*']
        self.mom_out = ['*smiles* mama!', '*happy* maaa!', '*smiles* mamama? mamamama!']
        self.sleep_out = ['aaaa... *closes his eyes* *it is not time for the nap though!!!*',
                          'vaaa... *starts closing his eyes* *probably sleepy*']
        self.tickle_out = ['*gets happy* AAAaaa! *starts giggling a lot*']
        
        self.tata_in = ['ta', 'tata', 'tatata', 'tatatata', 'tata tata', 'tatatatata','tatatatatata']
        self.tata_out = ['taaa?', 'tata?', 'tatata?', 'tata tata??', 'tatata ta?', 'ta tatata??', 'tatatatata!', 'tatatatatata!!!!']
                      
            
    def selector(self, input_list, check_list, return_list):
        return super().selector(input_list, check_list, return_list)

    def end_chat(self, input_list):
        return super().end_chat(input_list)
    
    def remove_punctuation(self, input_string):
        return super().remove_punctuation(input_string)
    
    def prepare_text(self, input_string):
        return super().prepare_text(input_string)
    
    def talk_to_baby(self):
        
        chat = True
        while (chat):
            
            msg = input('INPUT :\t')
            out_msg = None
            
            # Prepare the input message
            msg = self.prepare_text(msg)
            
            # Check for an end msg 
            if self.end_chat(msg):
                out_msg = '*falls asleep* *thanks for talking to him! I think he really liked you!*'
                chat = False

            if not out_msg:
               # Initialize to collect a list of possible outputs
                outs = []

                # Check if the input looks like a greeting, add a greeting output if so
                outs.append(self.selector(msg, self.greetings_in, self.greetings_out))
                
                # Check if the input looks like a message about food, add a response output if so
                outs.append(self.selector(msg, self.food_in, self.food_out))
                
                # Check if the input looks like a message about mom, add a response output if so
                outs.append(self.selector(msg, self.mom_in, self.mom_out))
                
                # Check if the input looks like a message about sleep, add a response output if so
                outs.append(self.selector(msg, self.sleep_in, self.sleep_out))
                
                # Check if the input looks like a message about tickling, add a response output if so
                outs.append(self.selector(msg, self.tickle_in, self.tickle_out))
                
                # Check if the input looks like a message in baby's secret language, add a response output if so
                outs.append(self.selector(msg, self.tata_in, self.tata_out))
                
                #   Randomly select an output from the set of outputs that are not None
                options = list(filter(None, outs))
                if options:
                    out_msg = random.choice(options)
                    
                else:
                    out_msg = random.choice(self.unknown)
           
            print('OUTPUT:', out_msg)
            

class Toddler(SmallPerson):
    
    def __init__(self):
        super().__init__()
        self.age = 3
        
        self.greetings_out = ['haii!', 'mama!', 'lady!', 'daddy!', 'boy!', 'girl!']
        self.unknown = ['*looks at you* *gets sad* *probably because it doesnt understand you* *tears up* *oh no he is about to cry*',
                        'mmmm? *tears up* *oh no here we go again* aaaaa aaaaaaaaaaAAAAAAAAAAAAAAA *he cries when he doesnt understand*',
                        '*gets distracted* *starts looking around* *get his attention! he always liked talking about food!*',
                  'aaaaaaaa? *oops* *he may cry* *gets red* *tears up* *oh no! talk to him before he cries! he likes hearing about mom!*',
                        '*tears up* ghe-ghe *oh no* *i swear if he cries, it will be loud* *maybe... type toy to give him a toy!*',
                        '*tears up* mommyyyyyyyy *mommy cant come now, she is busy outside* *but you can point at mommy by typing point!*',
                        'eeeeeeeee *gets red* *tears up* daddddyyyyy *daddy is working* *but you can talk to him about his dog!*',
                        '*stares at you* *gets grumpy* .... *gets sad and rolls his lip out* *gets red* aaaa aaaaaaaaa *oh no what a crybaby*']
        
        self.food_out = ['food! love food!', 'food! *points at the fridge* sweet!! *oh yeah he loves sweet things* ice cream! *pssttsss dont give him ice cream, he will start running around like crazy under his sugar high!!!*', 
                        '*eyes get super wide* *opens mouth* *oh no, mouth open for too long, drool everywhere* gibe!!! food!!! *oh no you better call his mom sometime soon to feed him*',
                        '*gets grumpy* bbfbfbffff *shakes his head* *points at broccoli on the counter* *he hates broccoli* *and guess what his mom fed him today* *yes, broccoli puree*',
                        '*eyes get really wide* *gets happy* aaaa! *did he eat sugar recently?* JUUUUUUUCEEEEE!!! *oh well he did* *he wont stop remembering that juice he got this morning*']
        self.mom_out = ['maammi! *points outside* mammi! ausai! *i think he means that she is outside* ausai! go! *gets very excited* goooo!!!! *ppptttssst dont take him outside! his mom is just trying to finish watering plants*',
                       'mommy.. *gets sad* miss mommy... ausai? *outside? nonono, we cant go outside just yet*',
                       'mama! love mama! *aww he really likes his mom* *gets really happy*',
                       'mama and daddy! pretty mama daddy! *reaches for your hair* *touches hair* *i guess your hair reminds him of his parents hair* *ahhhhh nonono dont let him pull on your hair! damn his grip is strong!* *such a tiny hand, and so strong already...*',
                       '*mommy! want mommy! mmmmmm... no want mommy. *gets grumpy* *sulks* *i think he remembered he is grumpy at his mom about something*']
        self.toy_out = ['yayyyy! toy! play! *takes toy* ehe! *gets really happy* ehehehehehehehe!',
                       '*eyes get big* aaaaa? plaaay taiim! *takes toy* *starts riding it around the couch* vruuuuuummmm... vrummmm...',
                       'ehe! *gets happy* *yay he doesnt cry anymore!*',
                       '*looks at the toy veeeery carefully* *suspicious* *takes toy* *starts putting it in his mouth* *oh no dont do it! oh no he is gonna swallow the whole thing!* *ewww and there is drool on it everywhere now!* *take it! take it!*',
                       '*looks grumpy* m? *takes toy* ...... .......... *throws it at you! dammit!* *i guess he doesnt want to play*']
        self.point_out = ['ausai! play ausai! ausai! *nope, mommy is busy outside in the garden* *the last time he went outside without his mom knowing about it was when he tried eating about every plant there* *didnt go well*',
                         'mommy. come back?', 'mommy? *points at you* *points outside* *now again at you* mommy? *oh no, is he thinking youre the mommy now?* *smiles* ehe ehe mommyyyyyy!']
        self.dog_out = ['doggie! charlie a big doggie! *spreads his arms wide* biiiiiiggg doooggie!', 
                        'ehe! me doggie too! *starts crawling around you, laughing histerically*',
                       'charlie! chaaaaliiiieee! *charlie the old dog comes by and sits down* *of course what does our toddler do?* *pulls on the poor dogs tail!* -dog: ........- *charlie leaves, disappointed* doggy? dogggyyyyyy.... doggy left.']   
        
    def selector(self, input_list, check_list, return_list):
        return super().selector(input_list, check_list, return_list)

    def end_chat(self, input_list):
        return super().end_chat(input_list)
    
    def remove_punctuation(self, input_string):
        return super().remove_punctuation(input_string)
    
    def prepare_text(self, input_string):
        return super().prepare_text(input_string)
    
    
    def talk_to_toddler(self):
        
        chat = True
        while (chat):
            
            msg = input('INPUT :\t')
            out_msg = None
            
            # Prepare the input message
            msg = self.prepare_text(msg)
            
            # Check for an end msg 
            if self.end_chat(msg):
                out_msg = '*gets distracted* *starts getting sleepy* *starts falling asleep sitting down* *hits head on the table* *he is too tired to cry though* *thanks for talking to him! I know he is a crybaby, but he said later that he liked you!*'
                chat = False

            if not out_msg:
               # Initialize to collect a list of possible outputs
                outs = []

                # Check if the input looks like a greeting, add a greeting output if so
                outs.append(self.selector(msg, self.greetings_in, self.greetings_out))
                
                # Check if the input looks like a message about food, add a response output if so
                outs.append(self.selector(msg, self.food_in, self.food_out))
                
                # Check if the input looks like a message about mom, add a response output if so
                outs.append(self.selector(msg, self.mom_in, self.mom_out))
                
                # Check if the input looks like a message about toy, add a response output if so
                outs.append(self.selector(msg, self.toy_in, self.toy_out))
                
                # Check if the input looks like a message about point, add a response output if so
                outs.append(self.selector(msg, self.point_in, self.point_out))
                
                # Check if the input looks like a message about dog, add a response output if so
                outs.append(self.selector(msg, self.dog_in, self.dog_out))
    
                #   Randomly select an output from the set of outputs that are not None
                options = list(filter(None, outs))
                if options:
                    out_msg = random.choice(options)
                    
                else:
                    out_msg = random.choice(self.unknown)
                    
            print('OUTPUT:', out_msg)
                       
class Preschooler(SmallPerson):
    
    def __init__(self):
        super().__init__()
        self.age = 5
        
        self.greetings_out = ['*quietly* hi.', '*looks up* *keeps playing with his car* *still doesnt look at you* *eventually says* hi.']