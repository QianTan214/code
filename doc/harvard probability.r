



*************************************************************************************
Introduction to Discrete Probability
*************************************************************************************


Exercise 1. Probability of cyan - generalized
# ===================================================================================

p = cyan/(cyan+magenta+yellow)
p


Exercise 2. Probability of not cyan - generalized
# ===================================================================================

1-p


Exercise 3. Sampling without replacement - generalized
# ===================================================================================

p_2 = (magenta + yellow)/(cyan + magenta + yellow-1)
p_1 * p_2


Exercise 4. Sampling with replacement - generalized
# ===================================================================================
p_2 <- (magenta + yellow) / (cyan + magenta + yellow)
p_1 * p_2






*************************************************************************************
Independence and Multiplication Rule
*************************************************************************************


Exercise 1. Independence
# ===================================================================================

B



Exercise 2. Sampling with replacement
# ===================================================================================
p_yellow = 7/15
p_yellow



Exercise 3. Rolling a die
# ===================================================================================

p_no6 = 5 / 6 
(5 / 6)^6


Exercise 4. Probability the Celtics win a game
# ===================================================================================

p_cavs_win4 = 0.6^4
1-0.6^4


Exercise 5. Monte Carlo simulation for Celtics winning a game
# ===================================================================================

celtic_wins = replicate(B,{
    simulated_games =  sample(c("lose","win"), 4, replace = TRUE, prob = c(0.6, 0.4))
    any(simulated_games == "win")
})

mean(celtic_wins)






*************************************************************************************
The Addition Rule
*************************************************************************************


Exercise 1. The Cavs and the Warriors
# ===================================================================================

# Assign a variable 'n' as the number of remaining games.

n = 6
# Assign a variable `outcomes` as a vector of possible game outcomes, where 0 indicates a loss and 1 indicates a win for the Cavs.
outcomes = c(0,1)

# Assign a variable `l` to a list of all possible outcomes in all remaining games. Use the `rep` function on `list(outcomes)` to create list of length `n`.

l = rep(list(outcomes),times=n)
l

# Create a data frame named 'possibilities' that contains all combinations of possible outcomes for the remaining games.
possibilities = expand.grid(l)
possibilities

# Create a vector named 'results' that indicates whether each row in the data frame 'possibilities' contains enough wins for the Cavs to win the series.
results = rowSums(possibilities)>=4

# Calculate the proportion of 'results' in which the Cavs win the series. Print the outcome to the console.
mean(results)


note: rowSums函数，每行的和
possibilities有64种组合结果(2^6)




Exercise 2. The Cavs and the Warriors - Monte Carlo
# ===================================================================================

# The variable `B` specifies the number of times we want the simulation to run. Let's run the Monte Carlo simulation 10,000 times.
B <- 10000

# Use the `set.seed` function to make sure your answer matches the expected result after random sampling.
set.seed(1)

# Create an object called `results` that replicates for `B` iterations a simulated series and determines whether that series contains at least four wins for the Cavs.

results = replicate(B,{
    x = sample(c(0,1),6,replace=TRUE) # 根据题意，后面不要加prob=c(...)
    sum(x)>=4
})


# Calculate the frequency out of `B` iterations that the Cavs won at least four games in the remainder of the series. Print your answer to the console.
mean(results)





Exercise 3. A and B play a series - part 1
# ===================================================================================


# Let's assign the variable 'p' as the vector of probabilities that team A will win.
p <- seq(0.5, 0.95, 0.025)

# Given a value 'p', the probability of winning the series for the underdog team B can be computed with the following function based on a Monte Carlo simulation:
prob_win <- function(p){
  B <- 10000
  result <- replicate(B, {
    b_win <- sample(c(1,0), 7, replace = TRUE, prob = c(1-p, p))
    sum(b_win)>=4
    })
  mean(result)
}

# Apply the 'prob_win' function across the vector of probabilities that team A will win to determine the probability that team B will win. Call this object 'Pr'.
Pr = sapply(p,prob_win)

# Plot the probability 'p' on the x-axis and 'Pr' on the y-axis.
plot(p,Pr)




Exercise 4. A and B play a series - part 2
# ===================================================================================

# Given a value 'p', the probability of winning the series for the underdog team B can be computed with the following function based on a Monte Carlo simulation:
prob_win <- function(N, p=0.75){
      B <- 10000
      result <- replicate(B, {
        b_win <- sample(c(1,0), N, replace = TRUE, prob = c(1-p, p))
        sum(b_win)>=(N+1)/2
        })
      mean(result)
    }

# Assign the variable 'N' as the vector of series lengths. Use only odd numbers ranging from 1 to 25 games.
N = seq(1,25,2)

# Apply the 'prob_win' function across the vector of series lengths to determine the probability that team B will win. Call this object `Pr`.
Pr = sapply(N,prob_win)

# Plot the number of games in the series 'N' on the x-axis and 'Pr' on the y-axis.
plot(N,Pr)








*************************************************************************************
Continuous Probability
*************************************************************************************

Exercise 1. Distribution of female heights - 1
# ===================================================================================

pnorm(60,64,3)



Exercise 2. Distribution of female heights - 2
# ===================================================================================

1-pnorm(72,64,3)



Exercise 3. Distribution of female heights - 3
# ===================================================================================

pnorm(67,64,3)-pnorm(61,64,3)



Exercise 4. Distribution of female heights - 4
# ===================================================================================

pnorm(67*2.54,64*2.54,3*2.54)-pnorm(61*2.54,64*2.54,3*2.54)



Exercise 5. Probability of 1 SD from average
# ===================================================================================

taller = 67
shorter = 61
pnorm(67,64,3)-pnorm(61,64,3)




Exercise 6. Distribution of male heights
# ===================================================================================

# Determine the height of a man in the 99th percentile of the distribution.
qnorm(0.99,69,3)



Exercise 7. Distribution of IQ scores
# ===================================================================================

B <- 1000

set.seed(1)

# Create an object called `highestIQ` that contains the highest IQ score from each random distribution of 10,000 people.
highestIQ = replicate(B,{
    v = max(rnorm(10000,100,15))
})

# Make a histogram of the highest IQ scores.
hist(highestIQ)


note: rnorm(size,avg,sd)
rnorm(5,0,1), 以N(0,1)的正态分布，分别列出5个值










*************************************************************************************
Random Variables and Sampling Models
*************************************************************************************


Exercise 1. American Roulette probabilities
# ===================================================================================

p_green = 2/38
p_green



Exercise 2. American Roulette payout
# ===================================================================================

# Create a model to predict the random variable `X`, your winnings from betting on green. Sample one time.
X=sample(c(17,-1),1,replace=TRUE,prob=c(p_green,p_not_green))

# Print the value of `X` to the console
X



Exercise 3. American Roulette expected value
# ===================================================================================

X = 17*p_green-1*p_not_green
X



Exercise 4. American Roulette standard error
# ===================================================================================

# Compute the standard error of the random variable
abs((17 - -1))*sqrt(p_green*p_not_green)

?????????



Exercise 5. American Roulette sum of winnings
# ===================================================================================

# Define the number of bets using the variable 'n'
n = 1000

# Create a vector called 'X' that contains the outcomes of 1000 samples
X = sample(c(17,-1),n,replace=TRUE,prob=c(p_green,p_not_green))
X

# Assign the sum of all 1000 outcomes to the variable 'S'
S=sum(X)

# Print the value of 'S' to the console
S

# 结果是-10



Exercise 6. American Roulette winnings expected value
# ===================================================================================

# Calculate the expected outcome of 1,000 spins if you win $17 when the ball lands on green and you lose $1 when the ball doesn't land on green
1000*(17*p_green-1*p_not_green)

note: The expected value of multiple spins equals 
the number of spins times the expected value of one spin




Exercise 7. American Roulette winnings expected value
# ===================================================================================

# Compute the standard error of the sum of 1,000 outcomes
sqrt(n) * abs((17 + 1))*sqrt(p_green*p_not_green)









*************************************************************************************
The Central Limit Theorem
*************************************************************************************


Exercise 1. American Roulette probability of winning money
# ===================================================================================

1-pnorm(0,avg,se)



Exercise 2. American Roulette Monte Carlo simulation
# ===================================================================================

p_green <- 2 / 38

p_not_green <- 1-p_green

n <- 100

B <- 10000

set.seed(1)

# Create an object called `S` that replicates the sample code for `B` iterations and sums the outcomes.
S=replicate(B,{
    X = sample(c(17,-1),n,replace=TRUE,prob=c(p_green,p_not_green))
    sum(X)
})

# Compute the average value for 'S'
mean(S)

# Calculate the standard deviation of 'S'
sd(S)



Exercise 3. American Roulette Monte Carlo vs CLT
# ===================================================================================

# Calculate the proportion of outcomes in the vector `S` that exceed $0
mean(S>0)


Exercise 4. American Roulette Monte Carlo vs CLT comparison
# ===================================================================================

B


Exercise 5. American Roulette average winnings per bet
# ===================================================================================

# Create a vector called `X` that contains the outcomes of `n` bets
X=sample(c(17,-1),n,replace=TRUE,prob=c(p_green,p_not_green))
X
# Define a variable `Y` that contains the mean outcome per bet. Print this mean to the console.
Y=mean(X)
Y



Exercise 6. American Roulette per bet expected value
# ===================================================================================

# Calculate the expected outcome of `Y`, the mean outcome per bet in 10,000 bets
17*p_green-1*p_not_green



Exercise 7. American Roulette per bet standard error
# ===================================================================================

# Compute the standard error of 'Y', the mean outcome per bet from 10,000 bets.
abs((17 - (-1))*sqrt(p_green*p_not_green) / sqrt(n))

???



Exercise 8. American Roulette winnings per game are positive
# ===================================================================================

1-pnorm(0,avg,se)



Exercise 9. American Roulette Monte Carlo again
# ===================================================================================

n <- 10000

B <- 10000

set.seed(1)

# Generate a vector `S` that contains the the average outcomes of 10,000 bets modeled 10,000 times
S = replicate(B,{
    X=sample(c(17,-1),n,replace=TRUE,prob=c(2/38,36/38))
    mean(X)
})

# Compute the average of `S`
mean(S)

# Compute the standard deviation of `S`
sd(S)





Exercise 10. American Roulette comparison
# ===================================================================================

mean(S>0)



Exercise 11. American Roulette comparison analysis
# ===================================================================================

题目：The Monte Carlo result and the CLT approximation are now much closer than 
when we calculated the probability of winning for 100 bets on green. 
What could account for this difference?

C：The CLT works better when the sample size is larger.







*************************************************************************************
The Big Short
*************************************************************************************


Exercise 1. Bank earnings
# ===================================================================================

# Assign the number of loans to the variable `n`
n <- 10000

# Assign the loss per foreclosure to the variable `loss_per_foreclosure`
loss_per_foreclosure <- -200000

p_default <- 0.03

set.seed(1)

# Generate a vector called `defaults` that contains the default outcomes of `n` loans
defaults = sample(c(0,1),n,replace=TRUE,prob=c(0.97,0.03))

# Generate `S`, the total amount of money lost across all foreclosures. Print the value to the console.
S = loss_per_foreclosure* sum(defaults)
S




Exercise 2. Bank earnings Monte Carlo
# ===================================================================================

# Generate a list of summed losses 'S'. Replicate the code from the previous exercise over 'B' iterations to generate a list of summed losses for 'n' loans.  Ignore any warnings for now.
S = replicate(B,{
    defaults = sample(c(0,1),n,replace=TRUE,prob=c(0.97,0.03))
    loss_per_foreclosure * sum(defaults)
})

# Plot a histogram of 'S'.  Ignore any warnings for now.
hist(S)




Exercise 3. Bank earnings expected value
# ===================================================================================

n*(p_default*loss_per_foreclosure + (1-p_default)*0)




Exercise 4. Bank earnings standard error
# ===================================================================================

# Compute the standard error of the sum of 10,000 loans
sqrt(n) * abs(loss_per_foreclosure) * sqrt(p_default*(1 - p_default))

？？？？？




Exercise 5. Bank earnings interest rate - 1
# ===================================================================================

# Assign a variable `x` as the total amount necessary to have an expected outcome of $0
x = -(loss_per_foreclosure*p_default) / (1 - p_default)

# Convert `x` to a rate, given that the loan amount is $180,000. Print this value to the console.
x/180000

?????


Exercise 6. Bank earnings interest rate - 2
# ===================================================================================

# Generate a variable `z` using the `qnorm` function
z = qnorm(0.05)

# Generate a variable `x` using `z`, `p_default`, `loss_per_foreclosure`, and `n`
x <- -loss_per_foreclosure*( n*p_default - z*sqrt(n*p_default*(1 - p_default)))/ ( n*(1 - p_default) + z*sqrt(n*p_default*(1 - p_default)))

# Convert `x` to an interest rate, given that the loan amount is $180,000. Print this value to the console.
x/180000



Exercise 7. Bank earnings - minimize money loss
# ===================================================================================

C
