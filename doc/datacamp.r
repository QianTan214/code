Datacamp Code


*************************************************************************************
Assessment 1.1: Parameters and Estimates
*************************************************************************************


Exercise 5. se versus p
# ===================================================================================

# `N` represents the number of people polled
N <- 25

# Create a variable `p` that contains 100 proportions ranging from 0 to 1 using seq function
p = seq(0, 1, length.out = 100)

# Create a variable `se` that contains the standard error of each sample average
se = sqrt(p*(1-p)/N)

# Plot `p` on the x-axis and `se` on the y-axis
plot(p,se)



Exercise 6. Multiple plots of se versus p
# ===================================================================================

# The vector `p` contains 100 proportions of Democrats ranging from 0 to 1 using seq function
p <- seq(0, 1, length = 100)

# The vector `sample_sizes` contains the three sample sizes
sample_sizes <- c(25, 100, 1000)

# Write a for-loop that calculates the standard error `se` for every value of `p` for each of the three samples sizes `N` in the vector `sample_sizes`. Plot the three graphs, using the `ylim` argument to standardize the y-axis across all three plots.

for (N in sample_sizes){
    se = sqrt(p*(1-p)/N)
    plot(p,se,ylim = c(0,0.1) )
}


Exercise 9. Standard error of the spread
# ===================================================================================

N <- 25
p <- 0.45

# Calculate the standard error of the spread. Print this value to the console.
se = 2*sqrt(p*(1-p)/N)
print(se)


Exercise 10. Sample size
# ===================================================================================

This sample size is too small because the standard error is larger than the spread.








*************************************************************************************
Assessment 2.1: Introduction to Inference
*************************************************************************************


Exercise 1. Sample average
# ===================================================================================

# Write a function called `take_sample` that takes `p` and `N` as arguements and returns the average value of a randomly sampled population.

take_sample = function(p,N){
    x = sample(c(1,0),size=N,replace=TRUE,prob=c(p,1-p))
    mean(x)
}

set.seed(1)
p <- 0.45
N <- 100
print(take_sample(p,N))




Exercise 2. Distribution of errors - 1
# ===================================================================================

p <- 0.45
N <- 100

# The variable `B` specifies the number of times we want the sample to be replicated
B <- 10000

set.seed(1)

# Create an objected called `errors` that replicates subtracting the result of the `take_sample` function from `p` for `B` replications
errors = replicate(B,{
    p - take_sample(p,N)
})

# Calculate the mean of the errors. Print this value to the console.
mean(errors)
hist(errors)



Exercise 4. Average size of error
# ===================================================================================

p <- 0.45
N <- 100
B <- 10000
set.seed(1)

# We generated `errors` by subtracting the estimate from the actual proportion of Democratic voters
errors <- replicate(B, p - take_sample(p, N))

# Calculate the mean of the absolute value of each simulated error. Print this value to the console.
mean(abs(errors))



Exercise 5. Standard deviation of the spread
# ===================================================================================

p <- 0.45
N <- 100
B <- 10000
set.seed(1)
errors <- replicate(B, p - take_sample(p, N))

# Calculate the standard deviation of `errors`
mean(errors^2)
sqrt(mean(errors^2))



Exercise 6. Estimating the standard error
# ===================================================================================

p <- 0.45
N <- 100

# Calculate the standard error
sqrt(p*(1-p)/N)



Exercise 7. Standard error of the estimate
# ===================================================================================

p <- 0.45
N <- 100
set.seed(1)

# Define `X` as a random sample of `N` voters with a probability of picking a Democrat ('1') equal to `p`
X = sample(c(1,0),N, replace= TRUE, prob=c(p,1-p))

# Define `X_bar` as the average sampled proportion
X_bar = mean(X)

# Calculate the standard error of the estimate. Print the result to the console.
sqrt(X_bar*(1-X_bar)/N)




Exercise 8. Plotting the standard error
# ===================================================================================

2500


Exercise 9. Distribution of X-hat
# ===================================================================================

B


Exercise 10. Distribution of the errors
# ===================================================================================

B



Exercise 11. Plotting the errors
# ===================================================================================

p <- 0.45
N <- 100
B <- 10000
set.seed(1)
errors <- replicate(B, p - take_sample(p, N))

# Generate a qq-plot of `errors` with a qq-line showing a normal distribution
qqnorm(errors)
qqline(errors)



Exercise 12. Estimating the probability of a specific value of X-bar
# ===================================================================================

p <- 0.45
N <- 100

# Calculate the probability that the estimated proportion of Democrats in the population is greater than 0.5. Print this value to the console.
se = sqrt(0.45*(1-0.45)/100)
1-pnorm(0.05/se)



Exercise 13. Estimating the probability of a specific error size
# ===================================================================================

N <-100
X_hat <- 0.51

# Define `se_hat` as the standard error of the sample average
se_hat = sqrt(X_hat*(1-X_hat)/N)

# Calculate the probability that the error is 0.01 or larger
1 - (pnorm(0.01/se_hat) - pnorm(-0.01/se_hat))


