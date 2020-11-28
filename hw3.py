#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:01:21 2019

@author: Juan Carbajal
@content: PIC 16 Homework 3
"""
#%%
"""LINKED LIST IMPLEMENTATION
Composed of a Node class and a LinkedList class which will contain instances of Nodes
Defined operations: add, get, set, len, str, repr
"""
class Node:
    # Node Initializer. Sets first node to carry data and sets pointer to next node
    def __init__(self,data):
        self.data = data
        self.next = None
    # allows the printing of individual nodes    
    def __str__(self):
        return str(self.data)
    # defines repr() for Nodes
    def __repr__(self):
        return repr(self.data)
    # redefines how equality is understood amongst nodes
    def __eq__(self,item):
        return self.data == item

class LinkedList:
    def __init__(self,data):
        # Create a new node, root, to store that data
        self.root = Node(data)
        # set two instance variables of the LinkedList 
        # first and last to that node.
        self.first = self.root
        self.last = self.root
        # A third instance variable n should track the number of elements.
        self.n = 1
    # returns total # of nodes in int
    def __len__(self):
        if self.first is None:
            return 0
        else:
            return self.n
    # allows the list to be printed in its entirety
    def __str__(self):
        temp = '['
        if self.first is None:
            print "empty list"
            return
        else:
            x = self.first
            while x is not None:
                temp = temp + str(x.data) + "->"
                x = x.next
            #raise StopIteration
        return temp+"]"

    # defines repr() for LinkedList objects
    def __repr__(self):
        return repr(self.__str__())
            
    #accepts one argument: the data to be stored in a new node at the end of the list.
    def append(self, data):
        # Store that data in a new node
        newNode = Node(data)
        # update the next field of the current last node of the Linked List,
        # and update the last node. 
        self.last.next = newNode 
        self.last = self.last.next 
        #Remember to increment n.
        self.n += 1
    # List iterator that will allows the traversal of the class object
    def __iter__(self):
        self.root = self.first
        return self
    # Generator to pair with LinkedList iterator
    def next(self):
        if self.first is None:
            print "empty list"
            return
        else:
            if self.root is not None:
                tmp = self.root
                self.root = self.root.next
                return tmp
                
            else:
                raise StopIteration
    # LinkedList setter that grants assignment access to individual nodes
    def __setitem__(self, key, item):
        assert key < self.n, "wrong index"
        
        count = 0
        newNode = self.first
        while count < self.n:
            if count == key:
                newNode.data = item
                return
            count+=1
            newNode = newNode.next
        return self
    # LinkedList getter that grants access to individual nodes
    def __getitem__(self,key):
        if key >= self.n:
            raise IndexError, "list index out of range"
        count = 0
        newNode = self.first
        while count < self.n:
            if count == key:
                return newNode.data
            count+=1
            newNode = newNode.next
    # addition for LinkedList so that added values are appended 
    # rather than calculating a sum or something of that manner
    def __add__(self,key):
        newList = LinkedList(self.first.data)
        self.root = self.first.next
        for i in range(self.n-1):
            newList.append(self.root.data)
            self.root = self.root.next
        newList.append(key)
        return newList
              
