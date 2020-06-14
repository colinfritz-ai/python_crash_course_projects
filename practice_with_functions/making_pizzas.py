import pizza as p 
import printing_models as pm 
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

unprinted_designs= ['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]

print("")
print("")
print("")
print("")

pm.print_models(unprinted_designs, completed_models)
print(unprinted_designs)
print(completed_models)




