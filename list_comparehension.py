list = [0,1,2,3,4]
eq_list = [(x+1) for x in range(5)]

mul_list = [x*3 for x in range(5)]
print([n for n in range(10) if n % 2 == 0])

ppl_u_know = ["Rolf", "john", "Anna", "GREG"]
normalised_ppl = [person.strip().lower() for person in ppl_u_know]
print(normalised_ppl)
