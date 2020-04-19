class Object:

    def __repr__(self):

        return '<%s>' % getattr(self, '__name__', self.__class__.__name__)



    def is_alive(self):
        return hasattr(self, 'alive') and self.alive



    def display(self, canvas, x, y, width, height):

        """Display an image of this Object on the canvas."""

        pass


class Agent():

    def __init__(self):

        def program(percept):

            return input('Percept=%s; action? ' % percept)

        self.program = program

        self.alive = True

class TableDrivenAgent(Agent):

    def __init__(self, table):
        Agent.__init__(self)

        percepts = []

        def program(percept):

            percepts.append(percept)

            action = table.get(tuple(percepts))

            return action

        self.program = program

class ReflexVacuumAgent(Agent):
    def __init__(self):

        Agent.__init__(self)

        def program(A):
           
            if A == 'hi':
                
                return 'Hello, I\'m Chatbot. How may I help you?'

            elif A =='how are you?':
                return 'i am doing good what about you?'

            elif A =='I am Great' :
                return 'nice to hear'

            elif A =='cancel my reservation' :
                return 'sure cancelling your reservation'

            elif A =='search my reservation' :
                return 'sure searching your reservation'

            elif A =='book my reservation' :
                return 'sure booking your reservation, where and when?'

        self.program = program

def TableDrivenVacuumAgent():
    table = {((A, 'hi'),): 'Hello, I\'m Chatbot. How may I help you?',

             ((A, 'how are you?'),): 'i am doing good\ what about you?',

             ((A, 'cancel'),(A, 'my reservation'),): 'sure cancelling your reservation',
             ((A, 'cancel booking'),(A, 'for'),): 'sure cancelling your reservation',
             ((A, 'I am'),(A, 'Great'),): 'nice to hear',

             ((A, 'book'),(A, 'my reservation'),): 'sure booking your reservation, where and when?',
             ((A, 'booking'),(A, 'for'),): 'sure booking your reservation',

             ((A, 'search'),(A, 'my reservation'),): 'sure searching your reservation',
             ((A, 'booking'),(A, 'for'),): 'sure searching your reservation',

             ((A, 'thank you'),): 'its my pleasure..',

             ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck',

             }

    return TableDrivenAgent(table)

class Environment():
    def __init__(self,):

        self.objects = []; self.agents = []



    object_classes = [] ## List of classes that can go into environment



    def percept(self, agent):
        action=input('you:')
        return self.execute_action(agent,action)


    def execute_action(self, agent, action):
        print('me:',agent.program(action))
#A=input('you:')
e=Environment()
r=ReflexVacuumAgent()
e.percept(r)
#e.execute_action()
