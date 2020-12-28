

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


Data frames
# ===================================================================================

loading the dslabs library and loading the murders dataset using the data function:

library(dslabs)
data(murders)

class(murders)
#> [1] "data.frame"



Examining an object
# ===================================================================================

str is useful for finding out more about the structure of an object:

str(murders)

head(murders)



The accessor: $
# ===================================================================================

murders$population

names(murders)




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



time series plot
# ===================================================================================

geom_line()
ggplot automatically group by colours

geom_text()
theme()




transformations
# ===================================================================================

log transformations
log2 
log10 used in population


modes
local modes

bimodal

scale_x_continuous(trans="log2")
scale_y_continuous(trans="log2")





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





ecological fallacy
# ===================================================================================

limit参数 in scale_x_continuous

breaks参数



introduction to data visualisation principles
# ===================================================================================


encode data using visual cues
# ===================================================================================


know when to include zero
# ===================================================================================

do not distort quantatiles
# ===================================================================================

order by a meaningful value
# ===================================================================================

show the data
# ===================================================================================

add jitter
alpha blending


ease comparisons using common axes
# ===================================================================================

keep axes the same when comparing

align plots
横图纵向比较，纵图横向比较


consider transformations
# ===================================================================================

visual cues should be adjacent
# ===================================================================================

scale_color_manual(values=color_blind_friendly_cols)



slope charts
# ===================================================================================

geom_lines



encode a thrid variable
# ===================================================================================


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


avoid pseudo and gratuitous 3D plots
# ===================================================================================

gratuitous不必要的


avoid too many significant digits
# ===================================================================================

default show 7 significant digits

signif

round

options(digits=n)












Data Science: Probability


introduction to probability
# ===================================================================================

financial crisis 2008

event: 如pick a red bead

Pr(A)


monte carlo simulation
# ===================================================================================

random number generators
sample()

rep()
c()

replicate() # repeat same task any times we want

如：
B <- 10000
events <- replicate(B, sample(beads,1))

tab <- table(events) # see the distribution
prop.table(tab)


sample function by default without replacement
set replace = TRUE

eg.
events <- sample(beads, B, replace=TRUE)
prop.table(table(events))



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

