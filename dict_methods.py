d={} # empty dictionary
marks = {
    "Rhythm":95,
    "Prashant":95,
    "Ranjeet":94,
    "Karan":99,
    1:"Palkin"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Rhythm":94,"Nandini":95})
# print(marks)
print(marks.get("Palkin")) # prints None
print(marks["Palkin"]) # returns an error