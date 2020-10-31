# Bayesian stats continued

The posterior distribution that you arrived at in the previous exercise was:

![](https://render.githubusercontent.com/render/math?math=P(p=\theta|T_1=1)=3\theta^2\qquad\0<\theta<1)

If this is compared with the prior (![](https://render.githubusercontent.com/render/math?math=2\theta)) you will notice that the probability of getting large values for the parameter is increased, while the probabilities of low values for the parameter is lowered.  This result makes total sense as the first test (![](https://render.githubusercontent.com/render/math?math=T_1)) was positive, which suggests that positive test results are more likely than negative results.

The essence of Bayesian statistics is to repeat the process that you have performed for a single outcome for each of the tests that you have performed.  Every time that you do a new experiment, however, you use the posterior that was output from a previous experiment as the prior.  In other words, when you are considering the result from the second experiment the prior will be ![](https://render.githubusercontent.com/render/math?math=3\theta^2) as this is what we now believe about the distribution given our prior and the outcome of the first experiment.

Your task in this exercise is thus to determine the posterior probability density for p after 10 experiments.  The results that have been obtained in these 10 experiment are contained in the Python list called results.  You will notice that I have written a loop over the ten elements in this list.  As in the last exercise, `denom` should be calculated using `sy.integrate`.  You can then set `posterior` equal to the posterior probability density function.   Notice that the the precise integrals that should be calculated will depend on the result of the experiment `r`.  Furthermore, you should use the variable `prior` as the prior distribution as this is updated after each pass through the loop.

When the exercise completes the final function that gives the probability is output and a graph of the predicted probability density function for p is generated.
