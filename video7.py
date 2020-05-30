''' Topic : Dictionary comprehension with example '''

# Basic syntax : {key : value for (key, value) in iterable if key, value satisfies a condition}

males = ['swapnomoy', 'sagnik', 'reshav']
females = ['manjistha', 'sampanna', 'sukanya']

# rel = {'swapnomoy' : 'manjistha', }

rel = {male : female for (male, female) in zip(males, females) if len(male) == len(female)}

print(rel)