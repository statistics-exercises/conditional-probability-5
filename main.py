from os import system
system('pip install sympy')
import sympy as sy

results = [1,1,1,0,1,0,1,1,1,0]

# I have defined the symbol t for you to use in the SymPy expressions you will write below
t = sy.Symbol("t")

# I have setup the initial prior 
prior = sy.simplify("2*t")
for r in results : 
  if r==1 : 
    denom = 
    posterior = 
  else : 
    denom = 
    posterior = 
  prior = posterior 
  
# You shouldn't need to adjust anything from here 
print("The posterior probability density function for the parameter given the first ten results is")
print( posterior )
graph = sy.plot( posterior, xlim=[0,1], ylim=[0,6], xlabel="t", ylabel="Posterior probability")
graph.save("mybayes.png")
