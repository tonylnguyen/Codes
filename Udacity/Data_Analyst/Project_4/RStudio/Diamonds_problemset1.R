library(ggplot2) #must load the ggplot package first 
data(diamonds)

summary(diamonds)

?diamonds

summary(diamonds$price)

sum(diamonds$price < 500)
sum(diamonds$price < 250)
sum(diamonds$price >= 15000)


qplot(x = price, data = diamonds, binwidth = 50) +
  scale_x_continuous(breaks = seq(250, 15000, 500), limits = c(0,15000)) +
  facet_wrap(~cut, ncol = 2)
# ggsave('priceHistogram.png') saving the histogram

by(diamonds$price, diamonds$cut, summary, digits = max(getOption('digits')))
# r rounded the values, to compenstate we added a digits command (not sure what digits actually does)

qplot(x = price, data = diamonds) + facet_wrap(~cut)
# the y axsis are fixed, each graph uses the same count measurements
qplot(x = price, data = diamonds) + facet_wrap(~cut,  scales = "free")
# the y axsis are proprtioned to it's own individual data

qplot(x = log10(price/carat), data = diamonds, geom="histogram", binwidth = 0.25) +
  facet_wrap(~cut, scales = 'free_y')


qplot(x = clarity, y = price, data = diamonds, geom="boxplot", color = clarity) 
ggsave('price_clarity_box.png')

by(diamonds$price, diamonds$color, summary)

IQR(subset(diamonds, price)$color) 
?diamonds

IQR(subset(diamonds, color == 'D')$price) 

qplot(x = color, y = (price/carat), data = diamonds, geom="boxplot", color = color) +coord_cartesian(ylim = c(1000,6000))
ggsave('price_carat_color.png')

qplot(x = carat, data = diamonds, geom="freqpoly", bins = 300) +
  scale_x_continuous(limits= c(.15,2), breaks = seq(.2,2,.10)) 
install.packages("lubridate")
