# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:47:58 2017

@author: eloy
"""

import json

dir(json)

# load - load JSON data from file
# loads - load JSON data from a string
# dump - write JSON object to file
# dumps - output JSON object as string

json_file = open("movie_1.txt", "r", encoding = "utf-8")

movie = json.load(json_file)

json_file.close()

movie
type(movie)

print(movie["title"])
print(movie["actors"])
print(movie["release_year"])


# loads (string)
value = """
{"title": "Tron: Legacy",
"composer": "Daft Punk",
"release_year" : 2010,
"budget": 170000000,
"actors": null,
"won_oscar": false
}"""

tron = json.loads(value)

print(tron)

json.dumps(movie)
# Note that unicode character for l with slash has been escaped
# To avoid this use ensure_ascii = False
json.dumps(movie,ensure_ascii=False)

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell",
 "Samantha Morton","Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinemotographer"] = "Janusz Kami\u0144ski"

file2 = open("./movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)
file2.close()





