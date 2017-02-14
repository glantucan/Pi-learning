#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pygame

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        self.name = name # public attribute
        self.__mood = mood # private attribute
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")
    def __privateMethod(self):
        print("Private method") 
    # Get and set methods
    def get_mood(self):
        return self.__mood
    def set_mood(self, mood):
        self.__mood = mood

    # properties
    #mood = property(get_mood, set_mood)
    #mood = property(None, set_mood)
    mood = property(lambda self: self.__mood,  self.__mood = mood)

crit = Critter(name = "Dan", mood = "happy")
crit.talk()
print(crit._Critter__mood)
crit._Critter__privateMethod()
print("\n\n\n")
# crit.__privateMethod() # Does not work
print(crit.mood)
##crit.mood = "sad"
crit.talk()
print(crit.mood)