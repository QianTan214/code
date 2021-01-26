

*************************************************************************************
Data Types
*************************************************************************************

Exercise 1. Variable names
# ===================================================================================

names(heights)


Exercise 2. Variable type
# ===================================================================================

B

Exercise 3. Numerical values
# ===================================================================================

length(unique(heights$height))


Exercise 4. Tables
# ===================================================================================

Use the table function to compute the frequencies of each unique height value

x <- heights$height
tab=table(x)
tab


Exercise 5. Indicator variables
# ===================================================================================

sum(tab==1)


Exercise 6. Data types - heights
# ===================================================================================

A








*************************************************************************************
Quantiles, Percentiles, and Boxplots
*************************************************************************************


Exercise 1. Vector lengths
# ===================================================================================

length(male)
length(female)


Exercise 2. Percentiles
# ===================================================================================

library(dslabs)
data(heights)

male <- heights$height[heights$sex=="Male"]
female <- heights$height[heights$sex=="Female"]

female_percentiles = quantile(heights$height[heights$sex=="Female"],seq(0.1,1,0.2))
male_percentiles = quantile(heights$height[heights$sex=="Male"],seq(0.1,1,0.2))

df = data.frame(female=female_percentiles,male=male_percentiles)
df


Exercise 3. Interpreting Boxplots - 1
# ===================================================================================

C


Exercise 4. Interpreting Boxplots - 2
# ===================================================================================

A

Exercise 5. Interpreting Boxplots - 3
# ===================================================================================

C

Exercise 6. Low quantiles
# ===================================================================================

A

Exercise 7. Interquantile Range (IQR)
# ===================================================================================

B







*************************************************************************************
Distributions
*************************************************************************************


Exercise 1. Distributions - 1
# ===================================================================================

C


Exercise 2. Distributions - 2
# ===================================================================================

B

Exercise 3. Empirical Cumulative Distribution Function (eCDF)
# ===================================================================================

B

Exercise 4. eCDF Male Heights
# ===================================================================================

C

Exercise 5. eCDF of Murder Rates
# ===================================================================================

A

Exercise 6. eCDF of Murder Rates - 2
# ===================================================================================

D


Exercise 7. Histograms
# ===================================================================================

C

Exercise 8. Histograms - 2
# ===================================================================================

A

Exercise 9. Density plots
# ===================================================================================

B = 0.15
?????


Exercise 10. Density plots - 2
# ===================================================================================

D
?????








*************************************************************************************
Normal Distributions
*************************************************************************************

Exercise 1. Proportions
# ===================================================================================

mean(x>69 & x<=72)


Exercise 2. Averages and Standard Deviations
# ===================================================================================

pnorm(72,avg,stdev) - pnorm(69,avg,stdev)


Exercise 3. Approximations
# ===================================================================================

exact <- mean(x > 79 & x <= 81)
approx = pnorm(81) - pnorm(79)
exact/approx


Exercise 4. Seven footers and the NBA
# ===================================================================================

1-pnorm(84,69,3)


Exercise 5. Estimating the number seven footers
# ===================================================================================

p = 1-pnorm(84,69,3)
round(p*10^9)


Exercise 6. How many seven footers are in the NBA?
# ===================================================================================

p = 1-pnorm(84,69,3)
N=round(p*10^9)
10/N


Exercise 7. Lebron James height
# ===================================================================================

## Change the solution to previous answer
p <- 1 - pnorm(80, 69, 3)
N <- round(p * 10^9)
150/N


Exercise 8. Interpretation
# ===================================================================================

C






*************************************************************************************
Robust Summaries with Outliers
*************************************************************************************

Exercise 1. Exploring the Galton Dataset - Average and Median
# ===================================================================================

x <- Galton$child
mean(x)
median(x)


Exercise 2. Exploring the Galton Dataset - SD and MAD
# ===================================================================================

x <- Galton$child
sd(x)
mad(x) 

note: 
mad - median absolute deviation


Exercise 3. Error impact on average
# ===================================================================================

mean(x_with_error)-mean(x) 



Exercise 4. Error impact on SD
# ===================================================================================

sd(x_with_error)-sd(x)


Exercise 5. Error impact on median
# ===================================================================================

median(x_with_error)-median(x)


Exercise 6. Error impact on MAD
# ===================================================================================

mad(x_with_error)-mad(x)


Exercise 7. Usefulness of EDA
# ===================================================================================

C


Exercise 8. Using EDA to explore changes
# ===================================================================================

x <- Galton$child
error_avg <- function(k){
    x[1]=k
    mean(x)
}
error_avg(10000)
error_avg(-10000)







*************************************************************************************
Introduction to ggplot2
*************************************************************************************


Exercise 1. ggplot2 basics
# ===================================================================================

class(p)

Exercise 2. Printing
# ===================================================================================

B

Exercise 3. Pipes
# ===================================================================================

p = heights %>% ggplot()


Exercise 4. Layers
# ===================================================================================

C


Exercise 5. geom_point 1
# ===================================================================================

## Fill in the blanks
murders %>% ggplot(aes(x =population , y = total)) + geom_point()


Exercise 6. geom_point 2
# ===================================================================================

murders %>% ggplot(aes(total,population)) + geom_point()


Exercise 7. geom_point text
# ===================================================================================

A

Exercise 8. geom_point text
# ===================================================================================

## edit the next line to add the label
murders %>% ggplot(aes(population, total,label=abb)) + geom_label()


Exercise 9. geom_point colors
# ===================================================================================

D: By using the color argument in geom_label 
because we want all colors to be blue so we do not need to map colors


Exercise 10. geom_point colors 2
# ===================================================================================

murders %>% ggplot(aes(population, total,label= abb)) + geom_label(color='blue')


Exercise 11. geom_labels by region
# ===================================================================================

B: Mapping the colors through the color argument of aes because 
each label needs a different color


Exercise 12. geom_label colors
# ===================================================================================

## edit this code
murders %>% ggplot(aes(population, total, label = abb, color=region)) +
  geom_label()


Exercise 13. Log-scale
# ===================================================================================

## add layers to p here
p +  scale_x_log10() + scale_y_log10()


Exercise 14. Titles
# ===================================================================================

# add a layer to add title to the next line
p + scale_x_log10() + 
    scale_y_log10() + ggtitle( "Gun murder data")


Exercise 15. Histograms
# ===================================================================================

C

Exercise 16. A second example
# ===================================================================================

p <- heights %>% ggplot(aes(x=height))


Exercise 17. Histograms 2
# ===================================================================================

## add a layer to p
p + geom_histogram()


Exercise 18. Histogram binwidth
# ===================================================================================

## add the geom_histogram layer but with the requested argument
p + geom_histogram(binwidth=1)


Exercise 19. Smooth density plot
# ===================================================================================

## add the correct layer using +
heights %>% 
  ggplot(aes(height)) + geom_density()


Exercise 20. Two smooth density plots
# ===================================================================================

## add the group argument then a layer with +
heights %>% 
  ggplot(aes(height,group=sex)) + geom_density()



Exercise 21. Two smooth density plots 2
# ===================================================================================

## edit the next line to use color instead of group then add a density layer
heights %>% 
  ggplot(aes(height, color = sex)) + geom_density()



Exercise 22. Two smooth density plots 3
# ===================================================================================

heights %>% ggplot(aes(height,fill=sex)) + geom_density(alpha=0.2)










*************************************************************************************
Summarizing with dplyr
*************************************************************************************


Exercise 1. Blood pressure 1
# ===================================================================================

tab <- NHANES %>% 
filter(Gender == 'female'& AgeDecade ==" 20-29")


Exercise 2. Blood pressure 2
# ===================================================================================

## complete this line of code.
ref <- NHANES %>% 
filter(AgeDecade == " 20-29" & Gender == "female") %>% 
summarize(average = mean(BPSysAve,na.rm = TRUE), ref=sd(BPSysAve,na.rm = TRUE))


Exercise 3. Summarizing averages
# ===================================================================================

For this exercise, review how to use the . or pull function

## modify the code we wrote for previous exercise.
ref_avg <- NHANES %>%
filter(AgeDecade == " 20-29" & Gender == "female") %>%
summarize(average = mean(BPSysAve, na.rm = TRUE), 
standard_deviation = sd(BPSysAve, na.rm=TRUE)) %>% 
pull(average)


Exercise 4. Min and max
# ===================================================================================

## complete the line
NHANES %>%
filter(AgeDecade == " 20-29"  & Gender == "female") %>% 
summarise(minbp=min(BPSysAve,na.rm=TRUE),maxbp=max(BPSysAve,na.rm=TRUE))


Exercise 5. group_by
# ===================================================================================

##complete the line with group_by and summarize
NHANES %>%
filter(Gender == "female") %>% 
group_by(AgeDecade) %>% 
summarise(average=mean(BPSysAve,na.rm=TRUE),
standard_deviation=sd(BPSysAve,na.rm=TRUE))


Exercise 6. group_by example 2
# ===================================================================================

NHANES %>% 
filter(Gender == "male") %>% 
group_by(AgeDecade) %>% 
summarise(average=mean(BPSysAve,na.rm=TRUE),
standard_deviation=sd(BPSysAve,na.rm=TRUE))



Exercise 7. group_by example 3
# ===================================================================================

NHANES %>% 
group_by(AgeDecade,Gender) %>% 
summarise(average=mean(BPSysAve,na.rm=TRUE),
standard_deviation=sd(BPSysAve,na.rm=TRUE))


Exercise 8. Arrange
# ===================================================================================

NHANES %>% filter(Gender=="male", AgeDecade == " 40-49") %>% 
group_by(Race1) %>% 
summarise(average = mean(BPSysAve,na.rm=TRUE),
standard_deviation=sd(BPSysAve,na.rm=TRUE)) %>% 
arrange(average)










*************************************************************************************
Exploring the gapminder dataset
*************************************************************************************

Exercise 1. Life expectancy vs fertility - part 1
# ===================================================================================

## fill out the missing parts in filter and aes
gapminder %>% filter(continent == 'Africa' & year == '2012') %>%
  ggplot(aes(fertility,life_expectancy)) +
  geom_point()


Exercise 2. Life expectancy vs fertility - part 2 - coloring your plot
# ===================================================================================

gapminder %>% 
filter(continent == 'Africa' & year == '2012') %>% 
ggplot(aes(fertility,life_expectancy,color=region)) + 
geom_point()



Exercise 3. Life expectancy vs fertility - part 3 - selecting country and region
# ===================================================================================

df = gapminder %>% 
filter(continent == 'Africa' & year == '2012') %>% 
filter(fertility<=3 & life_expectancy >=70) %>% 
select(country, region) 



Exercise 4. Life expectancy and the Vietnam War - part 1
# ===================================================================================

tab = gapminder %>% 
filter(year>=1960 & year <= 2010 & country %in% 
c("Vietnam","United States"))


Exercise 5. Life expectancy and the Vietnam War - part 2
# ===================================================================================

p = tab %>% ggplot(aes(year,life_expectancy,color=country)) + geom_line()



Exercise 6. Life expectancy in Cambodia
# ===================================================================================

gapminder %>% 
filter(year>=1960 & year <=2010 & country == 'Cambodia') %>% 
ggplot(aes(year,life_expectancy)) + 
geom_line()



Exercise 7. Dollars per day - part 1
# ===================================================================================

daydollars = gapminder %>% 
mutate(dollars_per_day = gdp/population/365) %>%  
filter(continent=="Africa" & year == 2010 & !is.na(dollars_per_day))

note: 
is.na(...)



Exercise 8. Dollars per day - part 2
# ===================================================================================

daydollars %>% 
ggplot(aes(dollars_per_day)) + 
geom_density() + 
scale_x_continuous(trans = "log2")


Exercise 9. Dollars per day - part 3 - multiple density plots
# ===================================================================================

daydollars = gapminder %>% 
mutate(dollars_per_day = gdp/population/365) %>% 
filter(continent=="Africa" & year %in% 
c(1970,2010) & !is.na(dollars_per_day))


daydollars %>% 
ggplot(aes(dollars_per_day)) + 
geom_density() + 
scale_x_continuous(trans = "log2") + 
facet_grid()




Exercise 10. Dollars per day - part 4 - stacked density plot
# ===================================================================================

daydollars = gapminder %>% 
mutate(dollars_per_day = gdp/population/365) %>% 
filter(continent=="Africa" & year %in% 
c(1970,2010) & !is.na(dollars_per_day))


daydollars %>% 
ggplot(aes(dollars_per_day,fill=region)) + 
geom_density(bw=0.5,position="stack") + 
scale_x_continuous(trans = "log2") + 
facet_grid()


note: 
geom_density(bw=0.5,position="stack")




Exercise 11. Infant mortality scatter plot - part 1
# ===================================================================================


gapminder_Africa_2010 = gapminder %>% 
mutate(dollars_per_day = gdp/population/365) %>% 
filter(continent=="Africa" & year == 2010 & !is.na(dollars_per_day))

gapminder_Africa_2010 %>% 
ggplot(aes(dollars_per_day,infant_mortality, color = region)) + 
geom_point()



Exercise 12. Infant mortality scatter plot - part 2 - logarithmic axis
# ===================================================================================

gapminder_Africa_2010 %>% 
ggplot(aes(dollars_per_day,infant_mortality, color = region)) + 
geom_point() + scale_x_continuous(trans="log2")



Exercise 13. Infant mortality scatter plot - part 3 - adding labels
# ===================================================================================

gapminder_Africa_2010 %>% 
ggplot(aes(dollars_per_day,infant_mortality, color = region, label=country)) + 
geom_point() + scale_x_continuous(trans="log2") + geom_text()


note: 
geom_text()里没有东西，在aes里加label = country




Exercise 14. Infant mortality scatter plot - part 4 - comparison of scatter plots
# ===================================================================================

daydollars = gapminder %>% 
mutate(dollars_per_day = gdp/population/365) %>% 
filter(continent=="Africa" & year %in% c(1970,2010) & !is.na(dollars_per_day) & !is.na(infant_mortality))

daydollars %>% 
ggplot(aes(dollars_per_day,infant_mortality, color = region, label=country)) + 
geom_point() + 
scale_x_continuous(trans="log2") + 
geom_text() + 
facet_grid(year~.)


note: 
!is.na(infant_mortality)
facet_grid(year~.)









*************************************************************************************
Data Visualization Principles - Part 1
*************************************************************************************

Exercise 1: Customizing plots - Pie charts
# ===================================================================================

D


Exercise 2. Customizing plots - Whats wrong?
# ===================================================================================

B


Exercise 3: Customizing plots - Whats wrong 2?
# ===================================================================================

C










*************************************************************************************
Data Visualization Principles - Part 2
*************************************************************************************


Exercise 1: Customizing plots - watch and learn
# ===================================================================================

state = reorder(state,rate)
levels(state)

note:
state = reorder(state,rate)



Exercise 2: Customizing plots - redefining
# ===================================================================================

dat = us_contagious_diseases %>% 
filter(year == 1967 & disease=="Measles" & count>0 & !is.na(population)) %>%
mutate(rate = count / population * 10000 * 52 / weeks_reporting) %>% 
mutate(state = reorder(state,rate))

dat %>% 
ggplot(aes(state, rate)) +
geom_bar(stat="identity") +
coord_flip()

note:
又加了这个mutate(state = reorder(state,rate))，使state按rate排序




Exercise 3: Showing the data and customizing plots
# ===================================================================================

C


Exercise 4: Making a box plot
# ===================================================================================

murders %>% 
mutate(rate = total/population*100000) %>% 
mutate(region=reorder(region,rate,FUN=median)) %>% 
ggplot(aes(region,rate)) + 
geom_boxplot() + 
geom_point()


note:
mutate(region=reorder(region,rate,FUN=median))











*************************************************************************************
Data Visualization Principles - Part 3
*************************************************************************************


Exercise 1: Tile plot - measles and smallpox
# ===================================================================================

library(dplyr)
library(ggplot2)
library(RColorBrewer)
library(dslabs)
data(us_contagious_diseases)

the_disease = "Smallpox"
dat <- us_contagious_diseases %>% 
   filter(!state%in%c("Hawaii","Alaska") & disease == the_disease & !weeks_reporting < 10) %>% 
   mutate(rate = count / population * 10000) %>% 
   mutate(state = reorder(state, rate))

dat %>% ggplot(aes(year, state, fill = rate)) + 
  geom_tile(color = "grey50") + 
  scale_x_continuous(expand=c(0,0)) + 
  scale_fill_gradientn(colors = brewer.pal(9, "Reds"), trans = "sqrt") + 
  theme_minimal() + 
  theme(panel.grid = element_blank()) + 
  ggtitle(the_disease) + 
  ylab("") + 
  xlab("")


note: 
tile plot: geom_tile()
geom_tile(color = "grey50") + 
scale_fill_gradientn(colors = brewer.pal(9, "Reds"), trans = "sqrt")
theme_minimal()
theme(panel.grid = element_blank()





Exercise 2. Time series plot - measles and smallpox
# ===================================================================================

data(us_contagious_diseases)

the_disease = "Smallpox"
dat <- us_contagious_diseases %>%
   filter(!state%in%c("Hawaii","Alaska") & disease == the_disease    & weeks_reporting >= 10) %>%
   mutate(rate = count / population * 10000) %>%
   mutate(state = reorder(state, rate))

avg <- us_contagious_diseases %>%
  filter(disease==the_disease & weeks_reporting >= 10) %>% group_by(year) %>%
  summarize(us_rate = sum(count, na.rm=TRUE)/sum(population, na.rm=TRUE)*10000)

dat %>% ggplot() +
  geom_line(aes(year, rate, group = state),  color = "grey50", 
            show.legend = FALSE, alpha = 0.2, size = 1) +
  geom_line(mapping = aes(year, us_rate),  data = avg, size = 1, color = "black") +
  scale_y_continuous(trans = "sqrt", breaks = c(5,25,125,300)) + 
  ggtitle("Cases per 10,000 by state") + 
  xlab("") + 
  ylab("") +
  geom_text(data = data.frame(x=1955, y=50), mapping = aes(x, y, label="US average"), color="black") + 
  geom_vline(xintercept=1963, col = "blue")



note: 
time series plot: geom_line()
geom_line(aes(year, rate, group = state),  color = "grey50", 
        show.legend = FALSE, alpha = 0.2, size = 1)
geom_line(mapping = aes(year, us_rate),  data = avg, size = 1, color = "black")
scale_y_continuous(trans = "sqrt", breaks = c(5,25,125,300))
geom_vline(xintercept=1963, col = "blue")





Exercise 3: Time series plot - all diseases in California
# ===================================================================================

us_contagious_diseases %>% 
filter(state=="California" &weeks_reporting >=10) %>% 
group_by(year, disease) %>%
summarize(rate = sum(count)/sum(population)*10000) %>%
ggplot(aes(year, rate, color=disease)) + 
geom_line()




Exercise 4: Time series plot - all diseases in the United States
# ===================================================================================

us_contagious_diseases %>% 
group_by(year,disease) %>% 
filter(!is.na(population)) %>% 
summarise(rate=sum(count)/sum(population)*10000) %>% 
ggplot(aes(year,rate,color=disease)) + 
geom_line()



