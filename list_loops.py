#we created a list called songs
songs = ["ROCKSTAR", "Do It", "For The Night"]
#now we will get the first and last song of the list
print(songs[0])
print(songs[2])
#using range we print out do it and for the night
print(songs[1:3])
#no we will change the last song to a new one 
songs[2] = "Patek"
print(songs)
#we will now add more songs to the list and remove one 
songs.extend(["6 Kiss", "20 Mins"])
songs.append("Man of The Year")
songs.remove("Do It")
print(songs)
for i in (songs):
    print(i)

animals = ["cat", "dog", "fish"]
print(animals)
animals.append("lizard")
print(animals)
print (animals[2])
animals.remove("cat")
for animal in (animals):
    print(animal)