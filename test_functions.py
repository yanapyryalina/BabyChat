import string
import random
from my_module.functions import *

# test for callability of most important methods
assert callable(remove_punctuation)
assert callable(prepare_text)
assert callable(selector)
assert callable(end_chat)
assert callable(talk_to_baby)
assert callable(talk_to_toddler)

# test for the proper results of most important methods
assert remove_punctuation("Hi! My name is Yana!") == "Hi My name is Yana"
assert isinstance(self.prepare_text("Hi!!! There?!!"), list)


# test for types of acceptable inputs
assert isinstance(self.greetings_in, list)
assert isinstance(self.food_in, list)
assert isinstance(self.mom_in, list)
assert isinstance(self.sleep_in, list)
assert isinstance(self.tickle_in, list)
assert isinstance(self.point_in, list)
assert isinstance(self.dog_in, list)


