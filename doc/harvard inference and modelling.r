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
？？？？


Exercise 13. Estimating the probability of a specific error size
# ===================================================================================

N <-100
X_hat <- 0.51

# Define `se_hat` as the standard error of the sample average
se_hat = sqrt(X_hat*(1-X_hat)/N)

# Calculate the probability that the error is 0.01 or larger
1 - (pnorm(0.01/se_hat) - pnorm(-0.01/se_hat))










*************************************************************************************
Assessment 3.1: Confidence Intervals and p-Values
*************************************************************************************


Exercise 1. Confidence interval for p
# ===================================================================================

# Load the data
data(polls_us_election_2016)

# Generate an object `polls` that contains data filtered for polls that ended on or after October 31, 2016 in the United States
polls = polls_us_election_2016 %>% filter(state=="U.S." & enddate>='2016-10-31')

# How many rows does `polls` contain? Print this value to the console.
nrow(polls)

# Assign the sample size of the first poll in `polls` to a variable called `N`. Print this value to the console.

N = head(polls$samplesize,1)
N

# For the first poll in `polls`, assign the estimated percentage of Clinton voters to a variable called `X_hat`. Print this value to the console.
X_hat = head(polls$rawpoll_clinton,1)/100
X_hat

# Calculate the standard error of `X_hat` and save it to a variable called `se_hat`. Print this value to the console.
se_hat = sqrt(X_hat*(1-X_hat)/N)
se_hat

# Use `qnorm` to calculate the 95% confidence interval for the proportion of Clinton voters. Save the lower and then the upper confidence interval to a variable called `ci`.
qnorm(0.975)
ci = c(X_hat - qnorm(0.975)*se_hat, X_hat + qnorm(0.975)*se_hat)
ci



note: 
If 95% of the area lies between −z and z, then 5% of the area must lie 
outside of this range. since normal curves are symmetric, 
half of this amount 2.5% must lie before −z. 
Then the area under the curve before z must be:

0.025+0.95=0.975.

Hence z is actually the 97.5th percentile of the standard normal distribution, 
and we can find it as follows:

qnorm(0.975,mean=0,sd=1)
## [1] 1.959964




Exercise 2. Pollster results for p
# ===================================================================================

# The `polls` object that filtered all the data by date and nation has already been loaded. Examine it using the `head` function.
head(polls)

# Create a new object called `pollster_results` that contains columns for pollster name, end date, X_hat, se_hat, lower confidence interval, and upper confidence interval for each poll.

polls = mutate (polls, X_hat = polls$rawpoll_clinton/100, 
se_hat = sqrt(X_hat*(1-X_hat)/polls$samplesize), 
lower= X_hat - qnorm(0.975)*se_hat, 
upper= X_hat + qnorm(0.975)*se_hat)

pollster_results = select (polls, pollster, enddate, X_hat, se_hat,lower, upper)
pollster_results




Exercise 3. Comparing to actual results - p
# ===================================================================================

# The `pollster_results` object has already been loaded. Examine it using the `head` function.
head(pollster_results)

# Add a logical variable called `hit` that indicates whether the actual value exists within the confidence interval of each poll. Summarize the average `hit` result to determine the proportion of polls with confidence intervals include the actual value. Save the result as an object called `avg_hit`.

pollster_results = mutate(pollster_results, hit=(lower<=0.482 & upper>=0.482))
avg_hit <- pollster_results %>% summarize(mean(hit))
avg_hit




Exercise 4. Theory of confidence intervals
# ===================================================================================

D


Exercise 5. Confidence interval for d
# ===================================================================================

# Add a statement to this line of code that will add a new column named `d_hat` to `polls`. The new column should contain the difference in the proportion of voters.
polls <- polls_us_election_2016 %>% filter(enddate >= "2016-10-31" & state == "U.S.") %>% mutate(d_hat = (rawpoll_clinton - rawpoll_trump)/100)

# Assign the sample size of the first poll in `polls` to a variable called `N`. Print this value to the console.
N = head(polls$samplesize,1)
N

# Assign the difference `d_hat` of the first poll in `polls` to a variable called `d_hat`. Print this value to the console.
d_hat = head(polls$d_hat,1)
d_hat

# Assign proportion of votes for Clinton to the variable `X_hat`.
X_hat = (1+d_hat)/2
X_hat

# Calculate the standard error of the spread and save it to a variable called `se_hat`. Print this value to the console.
se_hat = 2*sqrt(X_hat*(1-X_hat)/N)
se_hat

# Use `qnorm` to calculate the 95% confidence interval for the difference in the proportions of voters. Save the lower and then the upper confidence interval to a variable called `ci`.
ci = c(d_hat - qnorm(0.975)*se_hat,d_hat + qnorm(0.975)*se_hat)
ci




Exercise 6. Pollster results for d
# ===================================================================================

# The subset `polls` data with 'd_hat' already calculated has been loaded. Examine it using the `head` function.
head(polls)

# Create a new object called `pollster_results` that contains columns for pollster name, end date, d_hat, lower confidence interval of d_hat, and upper confidence interval of d_hat for each poll.

polls = polls %>% mutate(X_hat=(d_hat+1)/2, se_hat=2*sqrt(X_hat*(1-X_hat)/samplesize), lower=d_hat-qnorm(0.975)*se_hat,upper=d_hat+qnorm(0.975)*se_hat)

pollster_results = polls %>% select(pollster, enddate, d_hat, lower, upper)

pollster_results




Exercise 7. Comparing to actual results - d
# ===================================================================================

# The `pollster_results` object has already been loaded. Examine it using the `head` function.
head(pollster_results)

# Add a logical variable called `hit` that indicates whether the actual value (0.021) exists within the confidence interval of each poll. Summarize the average `hit` result to determine the proportion of polls with confidence intervals include the actual value. Save the result as an object called `avg_hit`.

avg_hit = pollster_results %>% mutate(hit = lower<=0.021 & upper >= 0.021) %>% summarize(mean(hit))
avg_hit




Exercise 8. Comparing to actual results by pollster
# ===================================================================================

# The `polls` object has already been loaded. Examine it using the `head` function.
head(polls)

# Add variable called `error` to the object `polls` that contains the difference between d_hat and the actual difference on election day. Then make a plot of the error stratified by pollster.

polls %>% mutate(error= d_hat-0.021) %>% ggplot(aes(x=pollster,y=error)) + geom_point() + theme(axis.text.x = element_text(angle =90, hjust=1))





Exercise 9. Comparing to actual results by pollster - multiple polls
# ===================================================================================

# The `polls` object has already been loaded. Examine it using the `head` function.
head(polls)

# Add variable called `error` to the object `polls` that contains the difference between d_hat and the actual difference on election day. Then make a plot of the error stratified by pollster, but only for pollsters who took 5 or more polls.

polls %>% mutate(error=(d_hat-0.021)) %>% group_by(pollster) %>% filter(n() >=5) %>% ggplot(aes(x=pollster,y=error)) + geom_point() +theme(axis.text.x = element_text(angle=90, hjust=1))










*************************************************************************************
Assessment 4.1: Statistical Models
*************************************************************************************


Exercise 1 - Heights Revisited
# ===================================================================================

mean(x)
sd(x)




Exercise 2 - Sample the population of heights
# ===================================================================================

X = sample(x,N,replace=TRUE)
mean(X)
sd(X)



Exercise 3 - Sample and Population Averages
# ===================================================================================

B


Exercise 4 - Confidence Interval Calculation
# ===================================================================================

# Define `se` as the standard error of the estimate. Print this value to the console.
se = sd(X)/sqrt(N)
se

# Construct a 95% confidence interval for the population average based on our sample. Save the lower and then the upper confidence interval to a variable called `ci`.
ci = c(qnorm(0.025, mean(X), se), qnorm(0.975, mean(X), se))






Exercise 5 - Monte Carlo Simulation for Heights
# ===================================================================================

# Define an object `res` that contains a logical vector for simulated intervals that contain mu
res = replicate(B,{
    X=sample(x,N,replace=TRUE)
    interval=c(qnorm(0.025,mean(X),sd(X)/sqrt(N)),qnorm(0.975,mean(X),sd(X)/sqrt(N)))
    between(mean(x),interval[1],interval[2])
})

note: interval[1] 从1开始，不是0

# Calculate the proportion of results in `res` that include mu. Print this value to the console.
mean(res)




Exercise 6 - Visualizing Polling Bias
# ===================================================================================

polls %>% ggplot(aes(pollster, spread)) + geom_boxplot() + geom_point()




Exercise 7 - Defining Pollster Bias
# ===================================================================================

C


Exercise 8 - Derive Expected Value
# ===================================================================================

A


Exercise 9 - Expected Value and Standard Error of Poll 1
# ===================================================================================

C


Exercise 10 - Expected Value and Standard Error of Poll 2
# ===================================================================================

C


Exercise 11 - Difference in Expected Values Between Polls
# ===================================================================================

D


Exercise 12 - Standard Error of the Difference Between Polls
# ===================================================================================

A



Exercise 13 - Compute the Estimates
# ===================================================================================

# Create an object called `sigma` that contains a column for `pollster` and a column for `s`, the standard deviation of the spread
sigma = polls %>% group_by(pollster) %>% summarize(s=sd(spread))

# Print the contents of sigma to the console
sigma



Exercise 14 - Probability Distribution of the Spread
# ===================================================================================

C


Exercise 15 - Calculate the 95% Confidence Interval of the Spreads
# ===================================================================================

# The `polls` data have already been loaded for you. Use the `head` function to examine them.
head(polls)

# Create an object called `res` that summarizes the average, standard deviation, and number of polls for the two pollsters.
res = polls %>% group_by(pollster) %>% summarize(avg=mean(spread),s=sd(spread), N=n())
res

# Store the difference between the larger average and the smaller in a variable called `estimate`. Print this value to the console.
estimate = max(res$avg) - min(res$avg)
estimate

# Store the standard error of the estimates as a variable called `se_hat`. Print this value to the console.
se_hat = sqrt(res$s[2]^2/res$N[2] + res$s[1]^2/res$N[1])
se_hat

# Calculate the 95% confidence interval of the spreads. Save the lower and then the upper confidence interval to a variable called `ci`.
ci = c(qnorm(0.025,estimate,se_hat),qnorm(0.975,estimate,se_hat))
ci




Exercise 16 - Calculate the P-value
# ===================================================================================

？？？？？？？？？？？？？

# Calculate the p-value
2*(1-pnorm(estimate/se_hat,0,1))




Exercise 17 - Comparing Within-Poll and Between-Poll Variability
# ===================================================================================

var = polls %>% group_by(pollster) %>% summarize(avg=mean(spread),s=sd(spread))
var








*************************************************************************************
Assessment 5.1: Bayesian Statistics
*************************************************************************************


Exercise 1 - Statistics in the Courtroom
# ===================================================================================

A


Exercise 2 - Recalculating the SIDS Statistics
# ===================================================================================

# Calculate the probability of both sons dying of SIDS. Print this value to the console.
Pr_1 * 1/100



Exercise 3 - Bayes Rule in the Courtroom
# ===================================================================================

C


Exercise 4 - Calculate the Probability
# ===================================================================================

Pr_AB = Pr_BA * Pr_A / Pr_B
Pr_AB


Exercise 5 - Misuse of Statistics in the Courts
# ===================================================================================

B


Exercise 6 - Back to Election Polls
# ===================================================================================


# Create an object called `results` that has two columns containing the average spread (`avg`) and the standard error (`se`). Print the results to the console.
results = polls %>% summarize(avg=mean(spread),se=sd(spread)/sqrt(n()))
results





Exercise 7 - The Prior Distribution
# ===================================================================================

B


Exercise 8 - Estimate the Posterior Distribution
# ===================================================================================

# The results` object has already been loaded. Examine the values stored: `avg` and `se` of the spread
results

# Define `mu` and `tau`
mu <- 0
tau <- 0.01

# Define a variable called `sigma` that contains the standard error in the object `results`
sigma = results$se

# Define a variable called `Y` that contains the average in the object `results`
Y = results$avg

# Define a variable `B` using `sigma` and `tau`. Print this value to the console.
tau <- 0.01
miu <- 0
B = sigma^2 / (sigma^2 + tau^2)

# Calculate the expected value of the posterior distribution
miu + (1-B)*(Y-miu)




Exercise 9 - Standard Error of the Posterior Distribution
# ===================================================================================

# Here are the variables we have defined
mu <- 0
tau <- 0.01
sigma <- results$se
Y <- results$avg
B <- sigma^2 / (sigma^2 + tau^2)

# Compute the standard error of the posterior distribution. Print this value to the console.
sqrt(1 / (1 / sigma ^2 + 1 / tau ^2))



Exercise 10- Constructing a Credible Interval
# ===================================================================================

# Construct the 95% credible interval. Save the lower and then the upper confidence interval to a variable called `ci`.
est = B * mu + (1 - B) * Y
ci = c(est - qnorm(0.975) * se, est + qnorm(0.975) * se)
ci




Exercise 11 - Odds of Winning Florida
# ===================================================================================

# Using the `pnorm` function, calculate the probability that the actual spread was less than 0 (in Trump's favor). Print this value to the console.
pnorm(0, exp_value, se)



Exercise 12 - Change the Priors
# ===================================================================================

# Define the variables from previous exercises
mu <- 0
sigma <- results$se
Y <- results$avg

# Define a variable `taus` as different values of tau
taus <- seq(0.005, 0.05, len = 100)

# Create a function called `p_calc` that generates `B` and calculates the probability of the spread being less than 0
p_calc = function(tau){
    B <- sigma ^ 2 / (sigma^2 + tau^2)
    se <- sqrt(1 / (1/sigma^2 + 1/tau^2))
    exp_value <- B * mu + (1 - B) * Y
    pnorm(0, exp_value, se)
}

# Create a vector called `ps` by applying the function `p_calc` across values in `taus`
ps = p_calc(taus)

# Plot `taus` on the x-axis and `ps` on the y-axis
plot(taus, ps)







*************************************************************************************
Assessment 6.1: Election Forecasting
*************************************************************************************


Exercise 1 - Confidence Intervals of Polling Data
# ===================================================================================

# Create an object called `cis` that has the columns indicated in the instructions
cis = polls %>% 
mutate(X_hat = (spread+1)/2, se = 2*sqrt(X_hat*(1-X_hat)/samplesize), 
lower=spread-qnorm(0.975)*se, upper = spread + qnorm(0.975)*se) %>% 
select(state,startdate,enddate,pollster,grade,spread,lower,upper)




Exercise 2 - Compare to Actual Results
# ===================================================================================

# Create an object called `p_hits` that summarizes the proportion of confidence intervals that contain the actual value. Print this object to the console.
p_hits = ci_data %>% 
mutate(hit=actual_spread>=lower & actual_spread<=upper) %>% 
summarise(mean(hit))




Exercise 3 - Stratify by Pollster and Grade
# ===================================================================================

# Create an object called `p_hits` that summarizes the proportion of hits for each pollster that has at least 5 polls.
p_hits = ci_data %>% 
mutate(hit=actual_spread>=lower & actual_spread <= upper) %>% 
group_by(pollster) %>% 
filter(n()>=5) %>% 
summarise(proportion_hits = mean(hit), n=n(), grade = head(grade,1)) %>% 
arrange(desc(proportion_hits))

或者grade=grade[1]



Exercise 4 - Stratify by State
# ===================================================================================

# Create an object called `p_hits` that summarizes the proportion of hits for each state that has more than 5 polls.
p_hits = ci_data %>% 
mutate(hit=actual_spread>=lower &actual_spread <= upper) %>% 
group_by(state) %>% 
filter(n()>=5) %>% 
summarise(proportion_hits = mean(hit), n=n()) %>% 
arrange(desc(proportion_hits))




Exercise 5- Plotting Prediction Results
# ===================================================================================

# Make a barplot of the proportion of hits for each state
p_hits %>% arrange(proportion_hits) %>% 
ggplot(aes(x=state,y=proportion_hits)) + 
geom_bar(stat="identity") +
coord_flip()




Exercise 6 - Predicting the Winner
# ===================================================================================

# Create an object called `errors` that calculates the difference between the predicted and actual spread and indicates if the correct winner was predicted
errors = cis %>% 
mutate(error = spread - actual_spread, hit = sign(actual_spread) == sign(spread))

# Examine the last 6 rows of `errors`
tail(errors)

note：sign函数的用法




Exercise 7 - Plotting Prediction Results
# ===================================================================================

# Create an object called `p_hits` that summarizes the proportion of hits for each state that has 5 or more polls
p_hits = errors %>% 
group_by(state) %>% 
filter(n()>=5) %>% 
summarise(proportion_hits = mean(hit),n=n()) %>% 
arrange(proportion_hits) 

# Make a barplot of the proportion of hits for each state
p_hits %>% 
ggplot(aes(x=state,y=proportion_hits)) + 
geom_bar(stat="identity") + 
coord_flip()




Exercise 8 - Plotting the Errors
# ===================================================================================

# Generate a histogram of the error
hist(errors$error)
# Calculate the median of the errors. Print this value to the console.
median(errors$error)

note: 还有个geom_histogram()




Exercise 9- Plot Bias by State
# ===================================================================================

# Create a boxplot showing the errors by state for polls with grades B+ or higher
errors %>% 
filter(grade %in% c("A+","A","A-","B+")) %>% 
ggplot(aes(x=reorder(state,error),y=error)) + 
theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
geom_boxplot() + 
geom_point()


以下也可以：
errors %>% 
filter(grade %in% c("A+","A","A-","B+") | is.na(grade)) %>%
mutate(state = reorder(state, error)) %>%
ggplot(aes(state, error)) + 
theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
geom_boxplot() + 
geom_point()





Exercise 10 - Filter Error Plot
# ===================================================================================

# Create a boxplot showing the errors by state for states with at least 5 polls with grades B+ or higher
errors %>% 
filter(grade %in% c("A+","A","A-","B+")) %>% 
group_by(state) %>%
filter(n()>=5) %>%
ungroup() %>%
ggplot(aes(x=reorder(state,error),y=error)) + 
theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
geom_boxplot() + 
geom_point()










*************************************************************************************
Assessment 6.2: The t-Distribution
*************************************************************************************


Exercise 1 - Using the t-Distribution
# ===================================================================================

# Calculate the probability of seeing t-distributed random variables being more than 2 in absolute value when 'df = 3'.
1 - pt(2, 3) + pt(-2, 3)

note: pt函数



Exercise 2 - Plotting the t-distribution
# ===================================================================================

# Generate a vector 'df' that contains a sequence of numbers from 3 to 50
df = seq(3,50)

# Make a function called 'pt_func' that calculates the probability that a value is more than |2| for any degrees of freedom 
pt_func = function(n){
    1 - pt(2,n) + pt(-2,n)
}

# Generate a vector 'probs' that uses the `pt_func` function to calculate the probabilities
probs = sapply(df,pt_func)

# Plot 'df' on the x-axis and 'probs' on the y-axis
plot(df,probs)




Exercise 3 - Sampling From the Normal Distribution
# ===================================================================================

# Generate a logical vector 'res' that contains the results of the simulations
res = replicate(B,{
    X = sample(x,N,replace=TRUE)
    interval = mean(X)+c(-1,1)*qnorm(0.975)*sd(X)/sqrt(N)
    between (mu,interval[1],interval[2])
})

# Calculate the proportion of times the simulation produced values within the 95% confidence interval. Print this value to the console.
mean(res)




Exercise 4 - Sampling from the t-Distribution
# ===================================================================================

# Generate a logical vector 'res' that contains the results of the simulations using the t-distribution
res = replicate(B,{
    X = sample(x,N,replace=TRUE)
    interval=mean(X) + c(-1,1)*qt(0.975, N - 1) * sd(X)/sqrt(N)
    between(mu,interval[1],interval[2])
})

# Calculate the proportion of times the simulation produced values within the 95% confidence interval. Print this value to the console.
mean(res)



Exercise 5 - Why the t-Distribution?
# ===================================================================================

A









*************************************************************************************
Assessment 7.1: Association and Chi-Squared Tests
*************************************************************************************

Exercise 1 - Comparing Proportions of Hits
# ===================================================================================

# The 'errors' data have already been loaded. Examine them using the `head` function.
head(errors)

# Generate an object called 'totals' that contains the numbers of good and bad predictions for polls rated A- and C-
totals = errors %>% filter(grade %in% c("A-","C-")) %>% group_by(grade,hit) %>% summarise(num=n()) %>% spread(grade,num)

# Print the proportion of hits for grade A- polls to the console
totals[[2,3]]/sum(totals[[3]])

# Print the proportion of hits for grade C- polls to the console
totals[[2,2]]/sum(totals[[2]])




Exercise 2 - Chi-squared Test
# ===================================================================================

# The 'totals' data have already been loaded. Examine them using the `head` function.
head(totals)

# Perform a chi-squared test on the hit data. Save the results as an object called 'chisq_test'.
chisq_test = totals %>% select(-hit) %>% chisq.test()
chisq_test

# Print the p-value of the chi-squared test to the console
chisq_test$p.value




Exercise 3 - Odds Ratio Calculation
# ===================================================================================

# The 'totals' data have already been loaded. Examine them using the `head` function.
head(totals)

# Generate a variable called `odds_C` that contains the odds of getting the prediction right for grade C- polls
odds_C <- (totals[[2,2]] / sum(totals[[2]])) / (totals[[1,2]] / sum(totals[[2]]))

# Generate a variable called `odds_A` that contains the odds of getting the prediction right for grade A- polls
odds_A = (totals[[2,3]] / sum(totals[[3]])) / (totals[[1,3]] / sum(totals[[3]]))

# Calculate the odds ratio to determine how many times larger the odds ratio is for grade A- polls than grade C- polls
odds_A/odds_C




Exercise 4 - Significance
# ===================================================================================

C