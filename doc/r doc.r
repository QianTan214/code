
*************************************************************************************
1. Data Science: R
*************************************************************************************


R basics
# ===================================================================================

help("log")
?log
args(log)

data # show datasets

Inf

rm
recommend save the workspace
save
save.image

recommend suffix .rda or RData

create and save a script

commment in R ##


class(a) # data type


library(dslabs)
data(murders) # load murders dataset
class(murders)
#> [1] "data.frame"

str(murders) # structure
head(murders) # first 6 rows

murders$population

autoc-complete
type murders$p then hit tab key

pop <- murders$population
length(pop)
#> [1] 51

turn numeric into integer:
as.integer()
class(1L)



factors
# ===================================================================================


levels(murders$region) # factor data type use levels function

R stores these levels as integers and keeps a map to keep track of the labels. This is more memory efficient than storing all the characters

reorder:
we want levels of the region by the total number of murders rather than alphabetical order

eg.
region <- murders$region
value <- murders$total
region <- reorder(region, value, FUN = sum)
levels(region)
#> [1] "Northeast"     "North Central" "West"          "South"



lists
# ===================================================================================


Data frames are a special case of lists
you can store any combination of different types

equivalent:
record$student_id
record[["student_id"]]
#> [1] 1234

lists without variable names
record2 <- list("John Doe", 1234)


If a list does not have names, you cannot extract the elements with $, 
but you can still use the brackets method and instead of providing the variable name, you provide the list index

eg. 
record2[[1]]
#> [1] "John Doe"



Matrices
# ===================================================================================


same data type

mat <- matrix(1:12, 4, 3) # 4 rows, 3 cols

convert matrices into data frames using the function as.data.frame

eg.
as.data.frame(mat)
#>   V1 V2 V3
#> 1  1  5  9
#> 2  2  6 10
#> 3  3  7 11
#> 4  4  8 12



Vectors
# ===================================================================================


create vectors using the function c, which stands for concatenate

eg.
codes <- c(380, 124, 818)
country <- c('italy', 'canada', 'egypt')


codes <- c(italy = 380, canada = 124, egypt = 818)
class(codes)
names(codes)




subsetting
# ===================================================================================


codes[c(1,3)]
codes[1:2]




Coercion
# ===================================================================================


x <- c(1, "canada", 3)
class(x)
#> [1] "character"


x <- 1:5
y <- as.character(x)


x <- c("1", "b", "3")
as.numeric(x)
#> Warning: NAs introduced by coercion
#> [1]  1 NA  3




Sort
# ===================================================================================


sort: sorts a vector in increasing order

order: returns the index that sorts input vector

eg.
x
#> [1] 31  4 15 92 65
order(x)
#> [1] 2 3 1 5 4



max: largest value
which.max: the index of the largest value

min
which.min


rank

eg.
x <- c(31, 4, 15, 92, 65)
rank(x)
#> [1] 3 1 2 5 4


eg.

original	sort	order	rank
31	        4	        2	    3
4	        15	        3	    1
15	        31	        1	    2
92	        65	        5	    5
65	        92	        4	    4



recycling(common error)
if the vectors don’t match in length, we don’t get an error

eg.
x <- c(1,2,3)
y <- c(10, 20, 30, 40, 50, 60, 70)
x+y
#> Warning in x + y: longer object length is not a multiple of shorter
#> object length
#> [1] 11 22 33 41 52 63 71





Vector arithmetics
# ===================================================================================


In R, arithmetic operations on vectors occur element-wise


Subsetting with logicals

eg.
ind <- murder_rate <= 0.71
murders$state[ind]

sum(ind)
#> [1] 5


& 
ind <- safe & west


which
convert vectors of logicals into indexes

eg.
ind <- which(murders$state == "California")
murder_rate[ind]
#> [1] 3.37



match
match tells us which indexes of a second vector match each of the entries of a first vector

eg.
ind <- match(c("New York", "Florida", "Texas"), murders$state)
ind
#> [1] 33 10 44



%in%
If rather than an index we want a logical that tells us whether or not each element of a first vector is in a second, 
we can use the function %in%

eg.
c("Boston", "Dakota", "Washington") %in% murders$state
#> [1] FALSE FALSE  TRUE



Advanced: There is a connection between match and %in% through which. To see this, 
notice that the following two lines produce the same index (although in different order):

eg.
match(c("New York", "Florida", "Texas"), murders$state)
#> [1] 33 10 44
which(murders$state%in%c("New York", "Florida", "Texas"))
#> [1] 10 33 44





Basic plots
# ===================================================================================


with
For a quick plot that avoids accessing variables twice, we can use the with function

eg.
with(murders, plot(population, total))


hist

eg.
x <- with(murders, total / population * 100000)
hist(x)


boxplot

eg.
murders$rate <- with(murders, total / population * 100000)
boxplot(rate~region, data = murders)


image

eg.
x <- matrix(1:120, 12, 10)
image(x)







Programming basics
# ===================================================================================



several functions that are widely used to program in R but that we will not cover in this book. 
These include split, cut, do.call, and Reduce, as well as the data.table package.



Conditional expressions
# ===================================================================================


if else`

eg.
a <- 0

if(a!=0){
  print(1/a)
} else{
  print("No reciprocal for 0.")
}
#> [1] "No reciprocal for 0."



ifelse

eg.

a <- 0
ifelse(a > 0, 1/a, NA)
#> [1] NA


no_nas <- ifelse(is.na(na_example), 0, na_example)


any()
all()



Defining functions
# ===================================================================================


eg.

avg <- function(x){
  s <- sum(x)
  n <- length(x)
  s/n
}


identical()

identical(mean(x), avg(x))

avg(1:10)

ifelse(arithmetic, sum(x)/n, prod(x)^(1/n)) #  arithmetic or geometric average


eg.

avg <- function(x, arithmetic = TRUE){
  n <- length(x)
  ifelse(arithmetic, sum(x)/n, prod(x)^(1/n))
}




Namespaces
# ===================================================================================


two packages use the same name for two different functions

both dplyr and the R-base stats package define a filter function

search()

stats::filter

dplyr::filter

Also note that if we want to use a function in a package without loading the entire package, we can use the double colon as well.





For-loops
# ===================================================================================


although R rarely uses for loops

eg.
compute_s_n <- function(n){
  x <- 1:n
  sum(x)
}


eg.
m <- 25
s_n <- vector(length = m) # create an empty vector
for(n in 1:m){
  s_n[n] <- compute_s_n(n)
}




Vectorization and functionals
# ===================================================================================


vectorization is preferred over for-loops


eg.
x <- 1:10
sqrt(x)
#>  [1] 1.00 1.41 1.73 2.00 2.24 2.45 2.65 2.83 3.00 3.16
y <- 1:10
x*y
#>  [1]   1   4   9  16  25  36  49  64  81 100


sapply
The function sapply permits us to perform element-wise operations on any function


Other functionals are apply, lapply, tapply, mapply, vapply, and replicate. We mostly use sapply, apply, and replicate in this book




The tidyverse
# ===================================================================================



the preferred unit for data storage is not the vector but the data frame

installing and loading the tidyverse package

dplyr package for manipulating data frames and the purrr package for working with functions

tidyverse also includes a graphing package, ggplot2


We say that a data table is in tidy format if each row represents one observation and columns represent the different variables 
for each of these observations



Manipulating data frames
# ===================================================================================

For the tidyverse packages to be optimally used, data need to be reshaped into tidy format

mutate: adding a column

eg.
library(dslabs)
data("murders")
murders <- mutate(murders, rate = total / population * 100000)


Although we have overwritten the original murders object, this does not change the object that loaded with data(murders). 
If we load the murders data again, the original will overwrite our mutated version.

filter

eg.
filter(murders, rate <= 0.71)

select
eg.
new_table <- select(murders, state, region, rate)
filter(new_table, rate <= 0.71)



pipe %>%
# ===================================================================================


eg.
murders %>% select(state, region, rate) %>% filter(rate <= 0.71)

eg.
16 %>% sqrt() %>% log2()

pipe %>%
In general, the pipe sends the result of the left side of the pipe to be the first argument of the function on the right side of the pipe
Therefore, we no longer need to specify the required first argument




Summarize
# ===================================================================================


summarize

eg. # a new summarised table
s <- heights %>% 
  filter(sex == "Female") %>%
  summarize(average = mean(height), standard_deviation = sd(height))
s
#>   average standard_deviation
#> 1    64.9               3.76


eg.
heights %>% 
  filter(sex == "Female") %>%
  summarize(median = median(height), minimum = min(height), 
            maximum = max(height))
#>   median minimum maximum
#> 1     65      51      79


quantile(x, c(0,0.5,1)) returns the min (0th percentile), median (50th percentile), and max (100th percentile)


eg. error because with function summarize, we can only call functions that return a single value.
heights %>% 
  filter(sex == "Female") %>%
  summarize(range = quantile(height, c(0, 0.5, 1)))




pull
# ===================================================================================


summarize always returns a data frame

pull: when a data object is piped that object and its columns 
can be accessed using the pull function

eg.
us_murder_rate %>% pull(rate)
#> [1] 3.03

equivalent:
us_murder_rate$rate


group_by
# ===================================================================================


first split data into groups and then summarise each group

eg.
heights %>% 
  group_by(sex) %>%
  summarize(average = mean(height), standard_deviation = sd(height))




arrange 
# ===================================================================================


arrange: order the entire table
we decide which column to sort by

eg. order the states by population size
murders %>% arrange(population) %>% head()

eg.
murders %>% arrange(desc(rate)) # in descending order




nested Sorting
# ===================================================================================

eg.
murders %>% arrange(region, rate) %>% head() # nested sorting




top_n
# ===================================================================================


show number of rows

eg.
murders %>% top_n(5, rate)

if the third argument left blank, top_n filters by the last column




dot operator .
# ===================================================================================


access the rate vector if the pull function not available

eg.
rates <- filter(murders, region == "South") %>% 
  mutate(rate = total / population * 10^5) %>% 
  .$rate
median(rates)
#> [1] 3.4



The purrr package
# ===================================================================================

similar to sapply

eg.
compute_s_n <- function(n){
  x <- 1:n
  sum(x)
}
n <- 1:25
s_n <- sapply(n, compute_s_n)



difference between sapply and purrr package:

sapply can return several different object types

purrr functions return objects of a specified type 
or return an error if this is not possible.

map returns a list

eg.
library(purrr)
s_n <- map(n, compute_s_n)
class(s_n)
#> [1] "list"


map_dbl: always returns a vector of numeric values

eg.
s_n <- map_dbl(n, compute_s_n)
class(s_n)
#> [1] "numeric"


map_df: always returns a tibble data frame




case_when
# ===================================================================================

case_when can output any values
ifelse can only output True and False

eg.
x <- c(-2, -1, 0, 1, 2)
case_when(x < 0 ~ "Negative", 
          x > 0 ~ "Positive", 
          TRUE  ~ "Zero")
#> [1] "Negative" "Negative" "Zero"     "Positive" "Positive"


eg.
murders %>% 
  mutate(group = case_when(
    abb %in% c("ME", "NH", "VT", "MA", "RI", "CT") ~ "New England",
    abb %in% c("WA", "OR", "CA") ~ "West Coast",
    region == "South" ~ "South",
    TRUE ~ "Other")) %>%
  group_by(group) %>%
  summarize(rate = sum(total) / sum(population) * 10^5) 
#> `summarise()` ungrouping output (override with `.groups` argument)
#> # A tibble: 4 x 2
#>   group        rate
#>   <chr>       <dbl>
#> 1 New England  1.72
#> 2 Other        2.71
#> 3 South        3.63
#> 4 West Coast   2.90



between
# ===================================================================================

x >= a & x <= b

equivalent:
between(x, a, b)



import data
# ===================================================================================

check notes online











*************************************************************************************
2. Data Science: Data Visualisation
*************************************************************************************

ggplot2 

main three components:
data, geometry, aesthetic mapping

geom_X where X is the name of the geometry. eg. geom_point, 
geom_bar, and geom_histogram





Aesthetic mappings
# ===================================================================================

whereas mappings use data from specific observations and need to be inside aes()

operations we want to affect all the points the same way 
do not need to be included inside aes


eg.
murders %>% ggplot() + 
  geom_point(aes(x = population/10^6, y = total))

eg.
p_test <- p + geom_text(aes(population/10^6, total, label = abb))





Global vs local aesthetic mappings
# ===================================================================================

define a mapping in ggplot, all the geometries that are added as layers 
will default to this mapping

eg.
p <- murders %>% ggplot(aes(population/10^6, total, label = abb))


we can override the global mapping by defining a new mapping within each layer
These local definitions override the global

eg.
p + geom_point(size = 3) +  
  geom_text(aes(x = 10, y = 800, label = "Hello there!"))


eg. log scale
p + geom_point(size = 3) +  
  geom_text(nudge_x = 0.05) + 
  scale_x_continuous(trans = "log10") +
  scale_y_continuous(trans = "log10") 

eg.
scale_x_log10() + scale_y_log10() 





Labels and titles
# ===================================================================================

xlab("Populations in millions (log scale)") + 
ylab("Total number of murders (log scale)") +
ggtitle("US Gun Murders in 2010")


p + geom_point(size = 3, color ="blue")


A nice default behavior of ggplot2 is that if we assign a categorical variable to color, 
it automatically assigns a different color to each category and also adds a legend.

p + geom_point(aes(col=region), size = 3)

To avoid automatically adding legend we set the geom_point argument show.legend = FALSE





Annotation, shapes, and adjustments
# ===================================================================================

geom_abline function. ggplot2 uses ab in the name to remind us of intercept (a) and slope (b). 

eg.
p + geom_point(aes(col=region), size = 3) + geom_abline(intercept = log10(r))





Add-on packages
# ===================================================================================

eg.
library(ggthemes)
p + theme_economist()


The add-on package ggrepel includes a geometry that adds labels while ensuring that they don’t fall on top of each other. 
We simply change geom_text with geom_text_repel.





Putting it all together
# ===================================================================================

eg.
library(ggthemes)
library(ggrepel)

r <- murders %>% 
  summarize(rate = sum(total) /  sum(population) * 10^6) %>%
  pull(rate)

murders %>% ggplot(aes(population/10^6, total, label = abb)) +   
  geom_abline(intercept = log10(r), lty = 2, color = "darkgrey") +
  geom_point(aes(col=region), size = 3) +
  geom_text_repel() + 
  scale_x_log10() +
  scale_y_log10() +
  xlab("Populations in millions (log scale)") + 
  ylab("Total number of murders (log scale)") +
  ggtitle("US Gun Murders in 2010") + 
  scale_color_discrete(name = "Region") +
  theme_economist()




qplot
# ===================================================================================

qplot: make a quick plot


eg.
qplot(x, y)




gridExtra 
# ===================================================================================

gridExtra: graph plots next to each other

eg.

library(gridExtra)
p1 <- qplot(x)
p2 <- qplot(x,y)
grid.arrange(p1, p2, ncol = 2)



Histograms
# ===================================================================================

histogram similar to barplot

but the histogram x-axis is numerical, not categorical






Smoothed density
# ===================================================================================

select degree of smoothness with care






The normal distribution
# ===================================================================================

mean: m <- sum(x) / length(x)
sd: s <- sqrt(sum((x-mu)^2) / length(x))




Standard units
# ===================================================================================

z <- scale(x)

how many men are within 2 SDs from the average

eg.
mean(abs(z) < 2)
#> [1] 0.95




Quantile-quantile plots
# ===================================================================================

QQ-plot

pnorm函数中的p表示Probability，它的功能是，在正态分布的PDF曲线上，
返回从负无穷到q的积分，其中这个q指的是一个Z-score

pnorm函数还能使用lower.tail参数，如果lower.tail设置为FALSE，
那么pnorm()函数返回的积分就是从q到正无穷区间的PDF下的曲线面积

eg.

pnorm(2)
# [1] 0.9772499

pnorm(2, mean = 5, sd = 3)
# [1] 0.1586553

pnorm(2, mean = 5, sd = 3, lower.tail = FALSE)
# [1] 0.8413447

1 - pnorm(2, mean = 5, sd = 3, lower.tail = FALSE)
# [1] 0.1586553


eg. inverse function

qnorm(0.975)
#> [1] 1.96

Note that these are for standard normal distribution by default (mean = 0, sd = 1), 
but we can also define these for any normal distribution

eg.
qnorm(0.975, mean = 5, sd = 2)
#> [1] 8.92

eg.
mean(x <= 69.5)
#> [1] 0.515

So about 50% are shorter or equal to 69 inches
This implies that if  p = 0.50 then q = 69.5


eg. ???
sample_quantiles <- quantile(z, p)
theoretical_quantiles <- qnorm(p) 
qplot(theoretical_quantiles, sample_quantiles) + geom_abline()


in practice it is easier to use the ggplot2

eg.
heights %>% filter(sex == "Male") %>%
  ggplot(aes(sample = scale(height))) + 
  geom_qq() +
  geom_abline()





Percentiles
# ===================================================================================

median: percentile 50 th

For normal distribution median and average are the same



Boxplots and stratification
# ===================================================================================

没什么内容




ggplot2 geometries
# ===================================================================================

如geom_bar等



Barplots
# ===================================================================================

eg. 
murders %>% ggplot(aes(region)) + geom_bar()

eg.
data(murders)
tab <- murders %>% 
  count(region) %>% 
  mutate(proportion = n/sum(n))
tab
#>          region  n proportion
#> 1     Northeast  9      0.176
#> 2         South 17      0.333
#> 3 North Central 12      0.235
#> 4          West 13      0.255


eg.
tab %>% ggplot(aes(region, proportion)) + geom_bar(stat = "identity")






Histograms
# ===================================================================================

eg.
heights %>% 
  filter(sex == "Female") %>% 
  ggplot(aes(height)) + 
  geom_histogram()

eg.
geom_histogram(binwidth = 1, fill = "blue", col = "black")




Density plots
# ===================================================================================

eg.
heights %>% 
  filter(sex == "Female") %>%
  ggplot(aes(height)) +
  geom_density()

eg. adjust bandwidth to be twice
geom_density(fill="blue", adjust = 2)





QQ-plots
# ===================================================================================

eg.
heights %>% filter(sex=="Male") %>%
  ggplot(aes(sample = height)) +
  geom_qq()


eg.
params <- heights %>% filter(sex=="Male") %>%
  summarize(mean = mean(height), sd = sd(height))

heights %>% filter(sex=="Male") %>%
  ggplot(aes(sample = height)) +
  geom_qq(dparams = params) +
  geom_abline()


Another option here is to scale the data first 
and then make a qqplot against the standard normal.

eg.
heights %>% 
  filter(sex=="Male") %>%
  ggplot(aes(sample = scale(height))) + 
  geom_qq() +
  geom_abline()





Images
# ===================================================================================

eg.
x <- expand.grid(x = 1:12, y = 1:10) %>% 
  mutate(z = 1:120) 

eg.
x %>% ggplot(aes(x, y, fill = z)) + 
  geom_raster() + 
  scale_fill_gradientn(colors =  terrain.colors(10))



Quick plots
# ===================================================================================

qplot permits us to make a plot with a short snippet of code

eg.
qplot(x)

eg.
qplot(sample = scale(x)) + geom_abline()


Note that in the code below we are using the data argument. 
Because the data frame is not the first argument in qplot, 
we have to use the dot operator.

eg.
heights %>% qplot(sex, height, data = .)


convert the plot above to a boxplot, use following code:

eg.
heights %>% qplot(sex, height, data = ., geom = "boxplot")


use the geom argument to generate a density plot instead of a histogram:

eg.
qplot(x, geom = "density")


eg.
qplot(x, bins=15, color = I("black"), xlab = "Population")
# the function I is used in R to say “keep it as it is”





Hans Rosling’s quiz
# ===================================================================================

eg.
gapminder %>% 
  filter(year == 2015 & country %in% c("Sri Lanka","Turkey")) %>% 
  select(country, infant_mortality)
#>     country infant_mortality
#> 1 Sri Lanka              8.4
#> 2    Turkey             11.6



eg. use colour to represent continent
filter(gapminder, year == 1962) %>%
  ggplot(aes(fertility, life_expectancy, color = continent)) +
  geom_point() 





Faceting
# ===================================================================================

facet：stratify the data by some variable and make the same plot for each strata

facet_grid
facet by up to two variables

facet function expects the row and column variables to be separated by a ~

. means we are not using one of the variables

eg.
filter(gapminder, year%in%c(1962, 2012)) %>%
  ggplot(aes(fertility, life_expectancy, col = continent)) +
  geom_point() +
  facet_grid(. ~ year)




facet_wrap
# ===================================================================================

we  want to use multiple rows and columns. 

facet_wrap permits us to do this by automatically wrapping the series of plots 
so that each display has viewable dimensions

eg.
years <- c(1962, 1980, 1990, 2000, 2012)
continents <- c("Europe", "Asia")
gapminder %>% 
  filter(year %in% years & continent %in% continents) %>%
  ggplot( aes(fertility, life_expectancy, col = continent)) +
  geom_point() +
  facet_wrap(~year) 






Fixed scales for better comparisons
# ===================================================================================

eg.
filter(gapminder, year%in%c(1962, 2012)) %>%
  ggplot(aes(fertility, life_expectancy, col = continent)) +
  geom_point() +
  facet_wrap(. ~ year, scales = "free")





Time series plots
# ===================================================================================

geom_line

eg.
gapminder %>% 
  filter(country == "United States") %>% 
  ggplot(aes(year, fertility)) +
  geom_line()


A useful effect of using color argument is that the data is automatically grouped

eg.
countries <- c("South Korea","Germany")

gapminder %>% filter(country %in% countries & !is.na(fertility)) %>% 
  ggplot(aes(year,fertility, col = country)) +
  geom_line()





Labels instead of legends
# ===================================================================================

eg.
labels <- data.frame(country = countries, x = c(1975,1965), y = c(60,72))

gapminder %>% 
  filter(country %in% countries) %>% 
  ggplot(aes(year, life_expectancy, col = country)) +
  geom_line() +
  geom_text(data = labels, aes(x, y, label = country), size = 5) +
  theme(legend.position = "none")





Log transformation
# ===================================================================================

eg.
gapminder %>% 
  filter(year == past_year & !is.na(gdp)) %>%
  ggplot(aes(log2(dollars_per_day))) + 
  geom_histogram(binwidth = 1, color = "black")


scale_x_continuous(trans = "log2")

trans argument: sqrt, logit, reverse





multimodal distributions
# ===================================================================================

mode of a distribution: value with the highest frequency






Comparing multiple distributions with boxplots and ridge plots
# ===================================================================================

eg.
gapminder <- gapminder %>% 
  mutate(group = case_when(
    region %in% c("Western Europe", "Northern Europe","Southern Europe", 
                    "Northern America", 
                  "Australia and New Zealand") ~ "West",
    region %in% c("Eastern Asia", "South-Eastern Asia") ~ "East Asia",
    region %in% c("Caribbean", "Central America", 
                  "South America") ~ "Latin America",
    continent == "Africa" & 
      region != "Northern Africa" ~ "Sub-Saharan",
    TRUE ~ "Others"))



turn this group variable into a factor to control the order of the levels

eg.
gapminder <- gapminder %>% 
  mutate(group = factor(group, levels = c("Others", "Latin America", 
                                          "East Asia", "Sub-Saharan",
                                          "West")))



turn the group labels vertical

eg.
theme(axis.text.x = element_text(angle = 90, hjust = 1))


show data in boxplot

eg.
p + geom_point(alpha = 0.5)






ridge plots
# ===================================================================================

ridge plots: stacked smooth densities or histograms

ggridges package

eg.
library(ggridges)
p <- gapminder %>% 
  filter(year == past_year & !is.na(dollars_per_day)) %>%
  ggplot(aes(dollars_per_day, group)) + 
  scale_x_continuous(trans = "log2") 
p  + geom_density_ridges() 


A useful geom_density_ridges parameter is scale, 
which lets you determine the amount of overlap, 
with scale = 1 meaning no overlap 
and larger values resulting in more overlap.


If the number of data points is small enough, we can add them to the ridge plot

eg.
p + geom_density_ridges(jittered_points = TRUE)


rug representation of the data

eg.
p + geom_density_ridges(jittered_points = TRUE, 
                        position = position_points_jitter(height = 0),
                        point_shape = '|', point_size = 3, 
                        point_alpha = 1, alpha = 0.7)





intersect function

eg.
country_list_1 <- gapminder %>% 
  filter(year == past_year & !is.na(dollars_per_day)) %>% 
  pull(country)

country_list_2 <- gapminder %>% 
  filter(year == present_year & !is.na(dollars_per_day)) %>% 
  pull(country)
      
country_list <- intersect(country_list_1, country_list_2)


eg.
gapminder %>% 
  filter(year %in% years & country %in% country_list) %>%
  ggplot(aes(group, dollars_per_day)) +
  geom_boxplot() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  scale_y_continuous(trans = "log2") +
  xlab("") +
  facet_grid(. ~ year)



note: year is a number, turn it into a factor since ggplot2 automatically 
assigns a color to each category of a factor.

eg.
mutate(year = factor(year))


eg. access variables by surrounding the name with two dots
aes(x = dollars_per_day, y = ..count..)


eg.
p <- gapminder %>% 
  filter(year %in% years & country %in% country_list) %>%
  mutate(group = ifelse(group == "West", "West", "Developing")) %>%
  ggplot(aes(dollars_per_day, y = ..count.., fill = group)) +
  scale_x_continuous(trans = "log2", limit = c(0.125, 300))

p + geom_density(alpha = 0.2) + 
  facet_grid(year ~ .)


eg. bw argument densities to be smoother
p + geom_density(alpha = 0.2, bw = 0.75) + facet_grid(year ~ .)


eg. stacking the densities on top of each other

eg.
gapminder %>% 
    filter(year %in% years & country %in% country_list) %>%
  group_by(year) %>%
  mutate(weight = population/sum(population)*2) %>%
  ungroup() %>%
  ggplot(aes(dollars_per_day, fill = group)) +
  scale_x_continuous(trans = "log2", limit = c(0.125, 300)) + 
  geom_density(alpha = 0.2, bw = 0.75, position = "stack") + 
  facet_grid(year ~ .) 


Weighted densities
We can weight the smooth densities using the weight mapping argument






The ecological fallacy and importance of showing the data
# ===================================================================================

logistic or logit transformation
log(p/(1-p))

ecological fallacy:
occurs when inferences about the nature of individuals are deduced 
from inferences about the group to which those individuals belong





Data visualization principles
# ===================================================================================

coord_flip()

reorder function

eg.
heights %>% 
  ggplot(aes(sex, height)) +
  geom_jitter(width = 0.1, alpha = 0.2) 


Align plots vertically to see horizontal changes and 
horizontally to see vertical changes

eg.
heights %>% 
  ggplot(aes(height, ..density..)) +
  geom_histogram(binwidth = 1, color="black") +
  facet_grid(sex~.)



eg.
west <- c("Western Europe","Northern Europe","Southern Europe",
          "Northern America","Australia and New Zealand")

dat <- gapminder %>% 
  filter(year%in% c(2010, 2015) & region %in% west & 
           !is.na(life_expectancy) & population > 10^7) 

dat %>%
  mutate(location = ifelse(year == 2010, 1, 2), 
         location = ifelse(year == 2015 & 
                             country %in% c("United Kingdom", "Portugal"),
                           location+0.22, location),
         hjust = ifelse(year == 2010, 1, 0)) %>%
  mutate(year = as.factor(year)) %>%
  ggplot(aes(year, life_expectancy, group = country)) +
  geom_line(aes(color = country), show.legend = FALSE) +
  geom_text(aes(x = location, label = country, hjust = hjust), 
            show.legend = FALSE) +
  xlab("") + ylab("Life Expectancy")





Bland-Altman plot
# ===================================================================================

eg.
library(ggrepel)
dat %>% 
  mutate(year = paste0("life_expectancy_", year)) %>%
  select(country, year, life_expectancy) %>% 
  spread(year, life_expectancy) %>% 
  mutate(average = (life_expectancy_2015 + life_expectancy_2010)/2,
         difference = life_expectancy_2015 - life_expectancy_2010) %>%
  ggplot(aes(average, difference, label = country)) + 
  geom_point() +
  geom_text_repel() +
  geom_abline(lty = 2) +
  xlab("Average of 2010 and 2015") + 
  ylab("Difference between 2015 and 2010")





Encoding a third variable
# ===================================================================================


shape argument

sequential and diverging

Sequential colors are suited for data that goes from high to low
Diverging colors are used to represent values that diverge from a center

eg.
library(RColorBrewer)
display.brewer.all(type="seq")

eg.
library(RColorBrewer)
display.brewer.all(type="div")

An example of when we would use a divergent pattern would be 
if we were to show height in standard deviations away from the average





Case study: vaccines and infectious diseases
# ===================================================================================

eg.
geom_vline(xintercept=1963, col = "blue")


eg.
dat %>% ggplot(aes(year, state, fill = rate)) +
  geom_tile(color = "grey50") +
  scale_x_continuous(expand=c(0,0)) +
  scale_fill_gradientn(colors = brewer.pal(9, "Reds"), trans = "sqrt") +
  geom_vline(xintercept=1963, col = "blue") +
  theme_minimal() +  
  theme(panel.grid = element_blank(), 
        legend.position="bottom", 
        text = element_text(size = 8)) +
  ggtitle(the_disease) + 
  ylab("") + xlab("")

square root transformation is to avoid having the really high counts dominate the plot



eg.
dat %>% 
  filter(!is.na(rate)) %>%
    ggplot() +
  geom_line(aes(year, rate, group = state),  color = "grey50", 
            show.legend = FALSE, alpha = 0.2, size = 1) +
  geom_line(mapping = aes(year, us_rate),  data = avg, size = 1) +
  scale_y_continuous(trans = "sqrt", breaks = c(5, 25, 125, 300)) + 
  ggtitle("Cases per 10,000 by state") + 
  xlab("") + ylab("") +
  geom_text(data = data.frame(x = 1955, y = 50), 
            mapping = aes(x, y, label="US average"), 
            color="black") + 
  geom_vline(xintercept=1963, col = "blue")





summary
# ===================================================================================

IQR = inter quartile range

The difference between the 3rd and 1st quartile (or 75th and 25th percentiles)

eg. outlier
q3 <- qnorm(0.75)
q1 <- qnorm(0.25)
iqr <- q3 - q1
r <- c(q1 - 1.5*iqr, q3 + 1.5*iqr)
r
#> [1] -2.7  2.7


eg.
max_height <- quantile(outlier_example, 0.75) + 3*IQR(outlier_example)
max_height
#>  75% 
#> 6.91




Median absolute deviation
# ===================================================================================

median absolute deviation (MAD)

eg.
mad(outlier_example)
#> [1] 0.237











*************************************************************************************
3. Data Science: Statistics with R
*************************************************************************************

case studies: financial crisis, forecasting election results, 
understanding heredity, building a baseball team




Probability
# ===================================================================================

rep: generate urn
sample: pick bead at random

eg.
beads <- rep(c("red", "blue"), times = c(2,3))

eg.
sample(beads, 1)





Monte Carlo simulation
# ===================================================================================

We want to repeat this experiment an infinite number of times, 
but it is impossible to repeat forever.

Monte Carlo simulation
we repeat the experiment a large enough number of times to 
make the results practically equivalent to repeating forever. 


replicate: perform monte carlo simulation
permits us to repeat the same task any number of times


eg.
B <- 10000
events <- replicate(B, sample(beads, 1))


table: see the distribution

eg.
tab <- table(events)


prop.table: gives us the proportions

eg.
prop.table(tab)


use Monte Carlo simulations to estimate probabilities 
when it is hard to compute the exact ones




Set the random seed
# ===================================================================================

set.seed(1986)
编号设定可以随意

> set.seed(1)
> runif(5)
[1] 0.2655087 0.3721239 0.5728534 0.9082078 0.2016819
> set.seed(2)
> runif(5)
[1] 0.1848823 0.7023740 0.5733263 0.1680519 0.9438393
> set.seed(1)
> runif(5)
[1] 0.2655087 0.3721239 0.5728534 0.9082078 0.2016819


With and without replacement
# ===================================================================================

by default, select without replacement

sample function can be used without the use of replicate

eg.
events <- sample(beads, B, replace = TRUE)
prop.table(table(events))





Combination and permutation
# ===================================================================================

construct a deck of cards, use expand.grid and paste


paste: create strings by joining smaller strings

eg.
number <- "Three"
suit <- "Hearts"
paste(number, suit)
#> [1] "Three Hearts"


paste: also work on pairs of vectors element-wise

eg.
paste(letters[1:5], as.character(1:5))
#> [1] "a 1" "b 2" "c 3" "d 4" "e 5"



expand.grid: give us all the combinations of entries of two vectors

eg.
expand.grid(pants = c("blue", "black"), shirt = c("white", "grey", "plaid"))


eg. generate a deck of cards

suits <- c("Diamonds", "Clubs", "Hearts", "Spades")
numbers <- c("Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", 
             "Eight", "Nine", "Ten", "Jack", "Queen", "King")
deck <- expand.grid(number=numbers, suit=suits)
deck <- paste(deck$number, deck$suit)





permutation
# ===================================================================================

permutations (from gtools package)
C10,7

eg.
library(gtools)
permutations(3, 2)
#>      [,1] [,2]
#> [1,]    1    2
#> [2,]    1    3
#> [3,]    2    1
#> [4,]    2    3
#> [5,]    3    1
#> [6,]    3    2


eg.
all_phone_numbers <- permutations(10, 7, v = 0:9)
n <- nrow(all_phone_numbers)
index <- sample(n, 5)
all_phone_numbers[index,]
#>      [,1] [,2] [,3] [,4] [,5] [,6] [,7]
#> [1,]    1    3    8    0    6    7    5
#> [2,]    2    9    1    6    4    8    0
#> [3,]    5    1    6    0    9    8    2
#> [4,]    7    4    6    0    2    8    1
#> [5,]    4    6    5    9    2    8    0

v argument: 0和9之间的数

nrow function





combination
# ===================================================================================

如21点, 用combinations, 顺序不重要
1/13 * 16/51 = 0.02


eg.
combinations(3,2)
#>      [,1] [,2]
#> [1,]    1    2
#> [2,]    1    3
#> [3,]    2    3


eg. probability of a Natural 21 in Blackjack

aces <- paste("Ace", suits)

facecard <- c("King", "Queen", "Jack", "Ten")
facecard <- expand.grid(number = facecard, suit = suits)
facecard <- paste(facecard$number, facecard$suit)

hands <- combinations(52, 2, v = deck)
mean(hands[,1] %in% aces & hands[,2] %in% facecard)
#> [1] 0.0483




Monte Carlo Natural 21
# ===================================================================================

eg.

blackjack <- function(){
   hand <- sample(deck, 2)
  (hand[1] %in% aces & hand[2] %in% facecard) | 
    (hand[2] %in% aces & hand[1] %in% facecard)
}

B <- 10000
results <- replicate(B, blackjack())
mean(results)
#> [1] 0.0475





Monty Hall problem
# ===================================================================================

eg.
B <- 10000
monty_hall <- function(strategy){
  doors <- as.character(1:3)
  prize <- sample(c("car", "goat", "goat"))
  prize_door <- doors[prize == "car"]
  my_pick  <- sample(doors, 1)
  show <- sample(doors[!doors %in% c(my_pick, prize_door)],1)
  stick <- my_pick
  stick == prize_door
  switch <- doors[!doors%in%c(my_pick, show)]
  choice <- ifelse(strategy == "stick", stick, switch)
  choice == prize_door
}
stick <- replicate(B, monty_hall("stick"))
mean(stick)
#> [1] 0.342
switch <- replicate(B, monty_hall("switch"))
mean(switch)
#> [1] 0.668






Birthday problem
# ===================================================================================

生日问题，可replacement

duplicated: returns TRUE whenever an element of a vector is a duplicate

eg.
duplicated(c(1,2,3,1,4,3,5))

eg.
n <- 50
bdays <- sample(1:365, n, replace = TRUE)


eg.
B <- 10000
same_birthday <- function(n){
  bdays <- sample(1:365, n, replace=TRUE)
  any(duplicated(bdays))
}
results <- replicate(B, same_birthday(50))
mean(results)
#> [1] 0.969



eg.create a look-up table

compute_prob <- function(n, B=10000){
  results <- replicate(B, same_birthday(n))
  mean(results)
}

n <- seq(1,60)
prob <- sapply(n, compute_prob)

library(tidyverse)
prob <- sapply(n, compute_prob)
qplot(n, prob)



eg. calculate exact probability not monte carlo
exact_prob <- function(n){
  prob_unique <- seq(365,365-n+1)/365 
  1 - prod( prob_unique)
}
eprob <- sapply(n, exact_prob)
qplot(n, prob) + geom_line(aes(n, eprob), col = "red")






Infinity in practice
# ===================================================================================

eg.
B <- 10^seq(1, 5, len = 100)
compute_prob <- function(B, n=25){
  same_day <- replicate(B, same_birthday(n))
  mean(same_day)
}
prob <- sapply(B, compute_prob)
qplot(log10(B), prob, geom = "line")





Theoretical distributions as approximations
# ===================================================================================

For example, it does not make sense to ask what is the probability 
that a normally distributed value is 70. 
Instead, we define probabilities for intervals. 
We thus could ask what is the probability that someone is between 69.5 and 70.5.

intervals that include exactly one round number


dnorm: probability density for the normal distribution

rnorm: 生成随机数

eg.
n <- length(x)
m <- mean(x)
s <- sd(x)
simulated_heights <- rnorm(n, m, s)


eg.
x <- seq(-4, 4, length.out = 100) # length.out：向量中元素数目
qplot(x, f, geom = "line", data = data.frame(x, f = dnorm(x)))




14 Random variables
# ===================================================================================

eg.
beads <- rep( c("red", "blue"), times = c(2,3))
X <- ifelse(sample(beads, 1) == "blue", 1, 0)






15 Statistical Inference
# ===================================================================================

15.2.1 The sample average
# ===================================================================================

15.2.3 Polling versus forecasting
# ===================================================================================


15.2.4 Properties of our estimate: expected value and standard error
# ===================================================================================

X¯ is a random variable

expected value of the average X¯ is:
E(X¯) = p

standard error of the average X¯ is:
SE(X¯) = sqrt(p*(1-p)/N)

we can make the standard error as small as we want by increasing N


We can also use other random variable equations to determine
expected value of the sum of draws E(S) and standard error of the sum of draws SE(S)
E(S)=Np 
SE(S)=sqrt(Np(1−p))




15.4 Central Limit Theorem in practice
# ===================================================================================

estimate of the standard error:

SE^(X¯)=sqrt(X¯(1−X¯)/N) # little hat denotes estimates


Code: Computing the probability of  X¯ being within 0.01 of p:
x_hat <- 0.48
se <- sqrt(x_hat*(1-x_hat)/25)
se
#> [1] 0.0999
pnorm(0.01/se) - pnorm(-0.01/se)
#> [1] 0.0797

margin of error：
defined as 2 times the standard error of the estimate  X¯ 
1.96*se
#> [1] 0.196

pnorm(1.96)-pnorm(-1.96)
#> [1] 0.95

There is about 95% chance that  X¯ will be within two standard errors 
of the actual parameter  p
在定义margin of error时，95%是最常用的数





15.4.1 A Monte Carlo simulation
# ===================================================================================

p <- 0.45    # unknown p to estimate
N <- 1000

# simulate one poll of size N and determine x_hat
x <- sample(c(0,1), size = N, replace = TRUE, prob = c(1-p, p))
x_hat <- mean(x)

# simulate B polls of size N and determine average x_hat
B <- 10000    # number of replicates
N <- 1000    # sample size per replicate
x_hat <- replicate(B, {
    x <- sample(c(0,1), size = N, replace = TRUE, prob = c(1-p, p))
    mean(x)
})

mean(x_hat)
#> [1] 0.45
sd(x_hat)
#> [1] 0.0157



Code: Histogram and QQ-plot of Monte Carlo results

library(tidyverse)
library(gridExtra)
p1 <- data.frame(x_hat = x_hat) %>%
    ggplot(aes(x_hat)) +
    geom_histogram(binwidth = 0.005, color = "black")
p2 <- data.frame(x_hat = x_hat) %>%
    ggplot(aes(sample = x_hat)) +
    stat_qq(dparams = list(mean = mean(x_hat), sd = sd(x_hat))) +
    geom_abline() +
    ylab("X_hat") +
    xlab("Theoretical normal")
grid.arrange(p1, p2, nrow=1)




15.4.2 The spread
# ===================================================================================
2 * p- 1




15.4.3 Bias: why not run a very large poll?
# ===================================================================================

systematic errors in polling are called bias


Code: Plotting margin of error in an extremely large poll over a range of values of p

library(tidyverse)
N <- 100000
p <- seq(0.35, 0.65, length = 100)
SE <- sapply(p, function(x) 2*sqrt(x*(1-x)/N))
data.frame(p = p, SE = SE) %>%
    ggplot(aes(p, SE)) +
    geom_line()




15.6 Confidence intervals
# ===================================================================================











library() 查看安装了哪些包

help(package="base")
help(package="car")

install.packages("car")

使用car包里的函数
加载car包
library(car)
some 调用car包里的some函数

head(mtcars) 前六条
lm(mpg~wt, data=mtcars) 线性回归

保存结果
result <- lm(mpg~wt, data=mtcars) 保存到result里
summary(result)
plot(result)



R与大数据处理平台的结合，如rhadoop，rhive，rhipe


<- assign values to variables
=
ls() # list variables

install.packages

library

ls

help("log")

?log

log function: 
For example, the base of the function log 
defaults to base = exp(1) making log the natural log by default.

log(8, base = 2) # 3
log(8,2) # 3


data() # see all the available datasets

Inf+1 # Inf

save
save.image # assign the workspace a specific name

load

rda / RData # save a workplace

## comment sign

n <- 1000
x <- seq(1, n)
sum(x)


rep
sample


Data types
# ===================================================================================


class(1) # numeric
as.integer(class(1)) # integer

或者在数字后面加L
class(1L) # integer





Vectors: numerics, characters, and logical
# ===================================================================================

?Comparison # 查看logical operator





factors
# ===================================================================================

In the background, R stores these levels as integers and keeps a map to 
keep track of the labels. 
This is more memory efficient than storing all the characters.


Factors are useful for storing categorical data
class(murders$region) # factor
levels(murders$region) # 用levels查看



list
# ===================================================================================

list function：

record <- list(name = "John Doe",
             student_id = 1234,
             grades = c(95, 82, 91, 97, 93), # function c
             final_grade = "A")

record$student_id 或者 record[["student_id"]]


lists without variable names:
record2 <- list("John Doe", 1234)

If a list does not have names, you cannot extract the elements with $, 
but you can still use the brackets method and instead of providing the variable name, 
you provide the list index, like this:

record2[[1]]
#> [1] "John Doe"



matrix
# ===================================================================================

define a matrix using the matrix function

mat <- matrix(1:12, 4, 3)

mat[2, 3] # 10

mat[2, ] # 2 6 10

mat[, 3] # 9 10 11 12

mat[, 2:3]

mat[1:2, 2:3]


convert matrices into data frames using the function as.data.frame:
as.data.frame(mat)



vectors
# ===================================================================================


create vectors using the function c (concatenate)

codes <- c(380, 124, 818)

create character vectors:
country <- c("italy", "canada", "egypt") # ''也可以

name the entries of a vector：
codes <- c(italy = 380, canada = 124, egypt = 818)
class(codes) # numeric
names(codes) # "italy"  "canada" "egypt"

和上面一样效果
codes <- c("italy" = 380, "canada" = 124, "egypt" = 818)


seq(1, 10)
seq(1, 10, 2) # 1 3 5 7 9

codes[2]
#> canada 
#>    124

codes[c(1,3)]
#> italy egypt 
#>   380   818

codes[1:2]
#>  italy canada 
#>    380    124

codes["canada"]
#> canada 
#>    124

codes[c("egypt","italy")]
#> egypt italy 
#>   818   380





Coercion
# ===================================================================================

x <- c(1, "canada", 3)
class(x) # [1] "character"

R consdier 1 and 3 as "1" and “3”

as.character
as.numeric

NA:
x <- c("1", "b", "3")
as.numeric(x)
#> Warning: NAs introduced by coercion
#> [1]  1 NA  3






Sorting
# ===================================================================================



















faceting
# ===================================================================================

facet_grid(row~col)
facet_grid(.~col) # no rows

facet_wrap(~col)












stratify and boxplot
# ===================================================================================

goem_boxplot() 无参数

theme(axis.text.x = element_text(angle=90, hjust=1))
x 轴坐标竖着显示

reorder(fac, value, FUN=mean)

fill颜色参数

geom_point(show.legend=False)





comparing distributions
# ===================================================================================

ifelse语句in mutate

geom_histogram(binwidth=1, color="black")

intersect()

fill=factor(year)参数，把数字year转化为factor，ggplot自动按颜色分类




density plot 
# ===================================================================================

geom_density()
position="stack"参数

?geom_density()

y = ..count.. 参数in ggplot

case_when()

weight参数in ggplot






case study vaccine
# ===================================================================================

sequential
divergent

geom_tile(color="grey50")

scale_fill_gradientn(colors=brewr.pal(9,"Reds"), trans="sqrt")

geom_vline()

theme_minimal()

theme(panel.grid=element_blank())

ggtitle()

ylab("")
xlab("")




avoid too many significant digits
# ===================================================================================

default show 7 significant digits

signif

round

options(digits=n)












Data Science: Probability





probability distribution
# ===================================================================================

continuous variables
discrete variables

independence
flip a coin

x[2:5]

conditional probability
given that or conditional on

blackjack 21点

1/13 * 16/51 = 0.02



combinations and permutations
# ===================================================================================

permutation: select r out of n
combination: order does not matter

suit: heart ...

expand.grid() # gives all combinations
paste() # 连接两个string

如：
number <- "three"
suit <- "heart"
paste(number, suit)

paste(letters[1:5], as.characters(1:5))
# "a 1" "b 2" "c 3" "d 4" "e 5"

expand.grid(pants=c("blue", "black"), shirt=c("white","grey","plaid"))

eg.
use expand.grid and paste to create a deck of cards

eg. king probability in a deck of cards
kings <- paste("King", suits)
mean(deck %in% kings)
# 0.07692308


library(gtools)
permutations(5,2)
permutations(10,7,v=0.9)
permutations(52,2,v=deck)


conditional probability:
sum(first_card %in% kings & second_card %in% kings) / sum(first_card %in% kings)
mean(first_card %in% kings & second_card %in% kings) / mean(first_card %in% kings)


try:
combinations(3,2)
permutations(3,2)


要review抽牌概率问题的代码




生日问题
# ===================================================================================

eg. 50 people, 2 people have the same birthday

n <- 50
bdays <- sample(1:365,n,replace=TRUE)

duplicated() # return T/F

monte carlto simulation:
B <- 10000
results <- replicate(B,{
    bdays <- sample(1:365,n,replace=TRUE)
    any(duplicated(bdays))
})

mean(results) # 0.977




sapply
# ===================================================================================

sapply() # element-wise operation on any functions

monte carlto simulation:

compute_prob <- function(n, B = 10000){
    same_day <- replicate(B,{
    bdays <- sample(1:365,n,replace=TRUE)
    any(duplicated(bdays))
})
    mean(results) # 0.977
}

n <- seq(1,60)


for loop rarely used in R

sapply():
x <- 1:10
sapply(x, sqrt) # 当然sqrt不需要这样做，只是举例

对于上例: use sapply
prob <- sapply(n, compute_prob)
plot(n, prob)


生日问题可以用1 - 没发生概率
review代码

plot(n, prob)
lines(n, eprob, col="red")

不能准确求概率时，可能可以用monte carlo


需要多少次monte carlo？
让B成为一个sequence，看prob什么时候趋近稳定



Addition rule: A or B
P(A or B) = P(A) + P(B) - P(A and B)




monte hall problem
# ===================================================================================

stick to same door: 1/3
switch door: 2/3

use monte carlo:

review代码



cotinuous probability
# ===================================================================================

cumulative distribution probability (CDF)
empirical cumulative distribution probability (eCDF)

eg. someone taller than 70
F <- function(a) mean(x<=a)
1 - F(70)


normal distribution
F(a) = pnorm(a, avg, s)

eg.
1 - pnorm(70.5, mean(x), sd(x))

probability for intervals

discretization:
no integer interval involved such as 70.1 - 70.9


probability density for normal distribution
dnorm()


rnorm(size,avg,sd)

d: density
q: quantatiles
p: probability density function
r: random
dnorm
pnorm
rnorm
qnorm


t-distribution
dt
pt
rt
qt



random variables
# ===================================================================================

random variable - capital letter

rep
sample

X <- sample(c(-1,1),n,replace=TRUE,prob=c(9/19,10/19))
S <- sum(X)
S is a random variable

random variable distribution function
F(a) = Pr(S<=a)

expected value: average
standard error: standard deviation

binominal distribution
central limit theorem(CLT)

X <= x
X: number on a die roll
x: actual value we see


E[X]=u
SE[X]



the big short
# ===================================================================================










*************************************************************************************
4. Data Science: Inference and Modeling
*************************************************************************************

statistical inference：the process of deducing characteristics of a population 
using data from a random sample
通过样本推断总体特征

pollster民意调查者
opinion polls


proportion of blue beads: p 
proportion of red beads: 1−p  
spread: 2*p−1

spread: The spread of a poll is the estimated difference 
between support two candidates or options.

take_poll(25) # draw 25 beads


p hat的标准差 = sqrt(p*(1-p)/n) # n是样本数量
p hat的标准误 = sqrt(p hat*(1-p hat)/n) 
# n是样本数量
# population proportion p
# sample proportion p hat




标准误standard error
# ===================================================================================


标准误 SE = sigma/sqrt(n)

标准误是sample对population平均值做估计时，对这个估计结果误差程度的表示方法

样本数越大，标准误越小

标准误：SE[X−(1−X)] = SE[2X−1] = 2SE[X] = 2sqrt(p(1−p)/N)


p hat的标准差 = sqrt(p*(1-p)/n)
p hat的标准误 = sqrt(p hat*(1-p hat)/n) 

例子：????????????????????????????????????????????
Again, consider the random variable S, 
which is the total number of Democrats in your sample of 25 voters. 
The variable  describes the proportion of Democrats in the sample, 
whereas  describes the proportion of Republicans.

What is the standard error of S?

答案:sqrt(25*p*(1-p))





Central Limit Theorem
# ===================================================================================

dividing a normally distributed random variable by a nonrandom constant,
the reuslting random variable is also normally distributed

hat denotes estimate

pnorm()



margin of error
# ===================================================================================


margin of error = critical value * standard error

例子：
900 students surveyed. GPA average 2.7 with standard deviation of 0.4.
calculate margin of error for a 90% confidence level.

答案:
对于90% confidence level，critical value = 1.645
SE = 0.4 / sqrt（900）= 0.013
margin of error = 1.645 * 0.013 = 0.021385


p hat的标准误 = sqrt(p hat*(1-p hat)/n) 
如果SE p hat为0.05，p hat为0.54，那么置信区间为0.44 - 0.64 （我们考虑95%confidence，即两个SE）
置信水平如果是95%，在两个标准差sigma范围内，标准误是0.05. margin of error就是 2 * 0.05 = 0.1



spread
# ===================================================================================

mean()
sd()

spread = p - (1-p) = 2*p−1

expected value of the spread is  2X¯−1

standard error of the spread is  2SE^ (X¯)

margin of error of the spread is 2 times the margin of error of  X¯




confidence interval
# ===================================================================================

the probability that a given interval contains the true parameter p

geom_smooth()
qnorm()

95% refers to the probability that the random interval falls on top of  p 



power
# ===================================================================================

Power is the probability of detecting an effect when there is a true effect to find. 
Power increases as sample size increases, 
because larger sample size means smaller standard error.




























*************************************************************************************
5. Data Science: Productivity Tools
*************************************************************************************

unix shell

r markdown

knitr package

git bash: a piece of software that emulates Unix on Windows machines


Ctrl+Shift+N

use tidyverse and dslabs packages for this course

install.packages("pkg_name")
install.packages(c("tidyverse", "dslabs")) # install multiple
library("pkg_name") # load a package
installed.packages() # see the list of all installed packages


Run an entire script:  Ctrl+Shift+Enter
Run a single line of script: Ctrl+Enter

.Rproj

The project name will appear in the upper left corner or the upper right corner, 
depending on your operating system. 
When you start an RStudio session with no project, it will display "Project: (None)".



git
# ===================================================================================

Git is most effectively used with Unix, but it can also interface with RStudio.

change the Rstudio preference so that you are using 
Git bash as the terminal (only for Windows user)

To avoid typing our GitHub password every time, we create a SSH/RSA key automatically 
through RStudio with the create RSA key button.

连接Rstudio和github

In terminal: configure git 
git config --global user.name "Your Name"
git config --global user.email "your@email.com"





Unix
# ===================================================================================

Absolute path vs. relative path
A full path specifies the location of a file from the root directory. It is independent of your present directory, and must begin with either a “/” or a “~”. In this example, the full path to our “project-1” file is: 

/home/projects/project-1

A relative path is the path relative to your present working directory. If our present working directory is the “projects” folder, then the relative path to our “project-1” file is simply: 

project-1



More path examples
1. Your current working directory is ~/projects and you want to move to the figs directory in the project-1 folder

Solution 2: cd ~/projects/project-1/figs (absolute)
Solution 2:  cd project-1/figs (relative)

2. Your current working directory is ~/projects and you want to move to the reports folder in the docs directory

Solution 1: cd ~/dos/reports (absolute)
Solution 2: cd ../docs/reports (relative)

3. Your current working directory is ~/projects/project-1/figs and you want to move to the project-2 folder in the projects directory

Solution 1: cd ~/projects/project-2 (absolute)
Solution 2: cd ../../project-2 (relative)


unix is operating system in data Science

in git bash, type in echo "hello world"

Note for Windows Users: 
The typical R installation will make your Documents directory your home directory in R. 
This will likely be different from your home directory in Git Bash. Generally, 
when we discuss home directories, we refer to the Unix home directory which for Windows, 
in this book, is the Git Bash Unix directory.


pwd - print working directory

"~" : home directory
"/" : at the beginning of the path stands for the root directory

When a path starts with "/", 
it is a "full path", which finds the current directory from the root directory




unix command
# ===================================================================================

tab # auto-complete

ls #list dir content
mkdir folder_name #create directory called "folder_name"
rmdir folder_name  #remove an empty directory as long as it is empty
rm -r folder_name  #remove dir that is not empty, "r" stands for recursive
../ # two dots represents parent dir
. # current working dir 

cd ~/projects # concatenate with forward slashes
cd ../.. # change to two parent layer beyond
cd -  # whatever dir you were before
cd  # return to the home dir

pwd 

mv # overwrite a file
mv path-to-file path-to-destination-directory
mv也可以改名

mv ~/docs/resumes ~/docs/reports/ # move resumes dir into reports dir, 最后的/不可少
如果没有/就变成改名了

cp # copy

rm # permanent

less # allows you to quickly look at the content of a file
Use q to exit the less page
use the arrows to navigate in the less page
eg. less cv.tex

initially called less
then called more
because less is more


In a project, we prefer relative paths (path relative to the default workin
instead of the full path so that code can run smoothly on other computers.
so dont use ~ in your code, cause it is full path


########## In RStudio ########
getwd()    # to confirm current working directory
save()    # save into .rda file, .RData is also fine but less preferred
ggsave("figs/barplot.png")    # save a plot generated by ggplot2 to a dir called "figs"




R Markdown
# ===================================================================================

knitr compiles R markdown Documents

Features of Rmarkdown: code and text can be combined to the same document 
and figures and tables are automatically added to the file.

R markdown
literate programming

.rmd

快捷键key binding： control + alt + I


# When echo=FALSE, code will be hided in output file
```{r echo=FALSE}
summary(pressure)
```

# use a descriptive name for each chunk for debugging purpose
```{r pressure-summary}
summary(pressure)
```

knitr:
to convert an r markdown file into a document, use knitr package




git and GitHub
# ===================================================================================

working dir
staging area
local repo
upstream repo （github repo）


不用写git add，直接在git commit -m "message" 后面加文件名即可

1. clone an existing repo

git fetch # update local repository to  be like the upstream repository, 
from upstream to local

git merge # make the updated local sync with the working directory and staging area

git pull # To change everything in one shot (from upstream to working dir), 
# use git pull (equivalent to combining git fetch + git merge)


2. initialise a new repo

cd ~/projects/murders
git init
git add README.txt
git commit -m "First commit. Adding README.txt file just to get started"
git remote add origin "https://github.com/rairizarry/murders.git"
git push # you may need to add these arguments the first time: --set-upstream origin master


连接rstudio和github

echo "a new repo with my scripts and data" > README.txt # 在README.txt里加这句话




Advanced Unix: Arguments
# ===================================================================================

Arguments
Arguments typically are defined using a dash (-) or two dashes (--) 
followed by a letter of a word.

rm -r name # recursive
-f # force, can remove protected file
rm -rf

ls -a
ls -l # l for long, more info about a file
ls -t # chronological order, with the most recent files at the top
ls -r # reverse order
ls -lart # more info, for all files, in reverse chronological order



man ls # man not available on git bash
command --help # on git bash
如ls --help

man ls | less # pipe
ls --help | less # on git bash

ls -lart | less

eg. command displays only the first 6 lines of a manual for the ls command
man ls| head -6

wild cards
* means any number of any combination of characters. 
ls *.html # list all html files
rm *.html # remove all html files

? means any single character




Envrionment variables
# ===================================================================================

Unix has settings that affect your command line environment. 
These are called environment variables.


In Unix, variables are distinguished from other entities by adding a $ in front. 
For example, the home directory is stored in $HOME.

$HOME # This command prints the path, or location, of the home directory. 
# For you, that might look something like /User/your_user_name/.

echo # in unix it is print
env # See all environment variables

echo $SHELL # See what shell is being used:  (most common shell is bash)

once you kown the shell, you can change environment variables

export variable value # change environment variable in bash shell

export PATH = /usr/bin/ # change path
# (Don’t actually run this command though!) 


There is a program that is run before each terminal starts 
where you can edit variables so they change whenever you call the terminal. 
This changes in different implementations, but if using bash, 
ou can create a file called .bashrc, .bash_profile,.bash_login, or .profile. 
You might already have one.



Executables
# ===================================================================================

In Unix, all programs are files. 
They are called executables. So, ls, mv, and git are all executable files.

which git # To find where these program files are, use which. 
# For example,  would return /usr/bin/git.

ls /usr/bin # see several executable files.

echo $PATH

ls -l # 可查看permission of each file
# you will see a series of symbols like this -rw-r--r--

-: regular file
d: directory
x: executable




Advanced Unix: Commands You Should Learn
# ===================================================================================

note commands are case-sensitive

open/start # figure out the right application of the filename and open it with that application
open # on Mac
start # on windows

On Git Bash, you can try start filename.


nano # A bare-bones text editor.

ln # create a symbolic link. do not recommend its use, but should be familiar

tar # archive files and subdirectories of a directory into one file

ssh # connect to another computer

grep # search for patterns in a file

awk/sed # These are two very powerful commands that permit you to 
# find specific strings in files and change them.


commands in R:

We can also perform file management from within R. 
?files # look at the help file 
Another useful function is unlink.

system # note that you can run Unix commands in R using system, but not recommended

