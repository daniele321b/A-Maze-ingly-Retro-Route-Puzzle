#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 11:16:26 2021

@author: danielecioffi
"""

import json


class Room:
    def __init__(self, id, name, neigh_list, objs):
        self.id = id
        self.name = name
        self.neigh = neigh_list
        self.objs = objs

# function to open json file in object


def read_from_json(name):
    with open(name) as f:
        data = json.load(f)
    return data

# function to return id of rooms


def return_id(data, i):
    return data["rooms"][i]["id"]

# function to return name od rooms


def return_name_room(data, i):
    return data["rooms"][i]["name"]

# function to create a list of objects in each room


def return_objects(data, i):
    list_obj = data["rooms"][i]["objects"]
    list = []
    if len(list_obj) > 0:
        for j in range(len(list_obj)):
            x = list_obj[j]["name"]
            list.append(x)
    # print(list)
    return list

# function to create a list of neighbords in each room


def return_list_neigh(data, i):
    list = []
    try:
        # print(data["rooms"][i]["north"])
        list.append(data["rooms"][i]["north"])
    except:
        list.append(0)
    try:
        # print(data["rooms"][i]["south"])
        list.append(data["rooms"][i]["south"])
    except:
        list.append(0)
    try:
        # print(data["rooms"][i]["west"])
        list.append(data["rooms"][i]["west"])
    except:
        list.append(0)
    try:
        # print(data["rooms"][i]["east"])
        list.append(data["rooms"][i]["east"])
    except:
        list.append(0)
    return list

# function to return the next room to move in order by north, south, west, east


def get_id(neig):
    if neig[0] > 0:
        x = neig[0]
        neig[0] = 0
        return x
    elif neig[1] > 0:
        x = neig[1]
        neig[1] = 0
        return x
    elif neig[2] > 0:
        x = neig[2]
        neig[2] = 0
        return x
    elif neig[3] > 0:
        x = neig[3]
        neig[3] = 0
        return x
    else:
        return -1


# START
name_file = input("Insert name json file: ")
search = []
rooms = []
collection = []
insert = ""
while insert != "exit":
    insert = input("insert object name to search (exit to exit): ")
    if insert != "exit":
        search.append(insert)

#print("Inserimenti", search)
# search = ["Knife", "Potted Plant", "Pillow"]
# print(data["rooms"][2]["objects"][0]["name"])
data = read_from_json(name_file)
id_input = int(input("Insert id initial room: "))
#print("input", id)
for i in range(len(data["rooms"])):
    id = return_id(data, i)
    name = return_name_room(data, i)
    list = return_list_neigh(data, i)
    objs = return_objects(data, i)
    #print(i, id, name, list, objs)
    room = Room(id, name, list, objs)
    rooms.append(room)

terminated = False


while(terminated == False):
    r = rooms[id_input-1]
    x = []
    for c in r.objs:
        if (c in search):
            collection.append(c)
            x.append(c)
    if len(x) > 0:
        print(id_input, "-  Room: ", r.name, x)
    else:
        print(id_input, "-  Room: ", r.name, "  None")
    if len(collection) == len(search):
        terminated = True
    # print("<-------->")

    id_input = get_id(r.neigh)
    # print(id_input)
    if(id_input == -1):
        terminated = True


print("Collected:", collection)
