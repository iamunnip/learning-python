acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
print(acronyms[0])
print(acronyms[1])
print(acronyms[2])
print(acronyms[3])
print(acronyms)

acronyms.append('BFN')
acronyms.append('IMHO')
print(acronyms)

acronyms.remove('BFN')
print(acronyms)

del acronyms[4]
print(acronyms)

word = 'LOL'
if word in acronyms:
  print(word + " found in acronyms")
else:
  print(word + " not found in acronyms")
  
for acronym in acronyms:
  print(acronym)
