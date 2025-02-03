time = int (input("Enter Length of Time in Seconds "))

secsperyear = 60*60*24*365
years = time // secsperyear
time = time - (secsperyear * years)

secsperday = 60 * 60 * 24
days = time // secsperday
time = time - (secsperday * days)

secsperhour = 60 * 60
hours = time // secsperhour
time = time - (secsperhour * hours)

secpermin = 60
minutes = time // secpermin
time = time - (secpermin * minutes)

print("Years:", years)
print("Days:", days)
print("Hours", hours)
print("Minutes:", minutes)
print("Second:", time)