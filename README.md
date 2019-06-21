# BabyChat
The following repository holds my python chatbot project - BabyChat. The two chatbots simulate children of different ages, and are created based on my knowledge of child language developement. 

# Concept
The concept for this project first came from taking cognitive science classes, in particular Cognition in the Wild, where we looked at what makes humans.. human - for example, what makes human conversations realistic, how humans came to inherit gestures from our ape ancestors as earliest sign of language and culture, and why children's behavior changes the way it does over time. As a student specializing in Machine Learning and wishing to go into AI, I am particularly interested in creating the most human-like experiences with a computer program. To get a start on this endeavor, I chose to create two chatbots - a baby and a toddler - that would provide the user with most human experiences possible, using real research of child development and conversation.

# Approach
The approach I took when coding this project is a mix of modular and linear. 
In terms of modular, I created a general Small Person class, from which Baby and a Toddler classes would inherit general methods and possible inputs. The Baby and Toddler classes are child classes of Small Person, and each have their personalized output messages, conversation topics, and smaller methods. 
In terms of linear, I decided to incorporate more script-like method calls in this notebook to make it more fun for the user to see the process of creation of Baby and Toddler, as well as to ensure that in extreme cases most important imports and calls get executed. The semi-linear approach also helps guide the user through two chatbots. 
