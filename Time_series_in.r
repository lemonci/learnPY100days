#Finished Characteristics of Time Series and Time Series Regression and Exploratory Data Analysis
par(mfrow=c(2,1))
plot(arima.sim(list(order=c(1,0,0), ar=.9), n=100), ylab="x", main=(expression(AR(1)~~~phi==+.9)))
plot(arima.sim(list(order=c(1,0,0), ar=-.9), n=100), ylab="x", main=(expression(AR(1)~~~phi==-.9)))
par(mfrow=c(2,1))
plot(arima.sim(list(order=c(0,0,1), ma=.9), n=100), ylab="x", main=(expression(MA(1)~~~theta==+.5)))
plot(arima.sim(list(order=c(0,0,1), ma=-.9), n=100), ylab="x", main=(expression(MA(1)~~~theta==-.5)))
plot(arima.sim(list(order=c(0,0,1), ma=5), n=100), ylab="x", main=(expression(MA(1)~~~theta==5)))
plot(arima.sim(list(order=c(0,0,1), ma=1/5), n=100), ylab="x", main=(expression(MA(1)~~~theta==1/5)))
plot(arima.sim(list(order=c(0,0,1), ma=-.9), n=100), ylab="x", main=(expression(MA(1)~~~theta==5)))
plot(arima.sim(list(order=c(0,0,1), ma=-.9), n=100), ylab="x", main=(expression(MA(1)~~~theta==0.2)))
set.seed(8575309)
x = rnorm(150, mean=5)
arima(x, order=c(1, 0, 1))
ARMAtoMA(ar =.9, ma = .5, 10) # first 10 psi-weights
ARMAtoMA(ar=-.5, ma=-.9, 10)
z = c(1, -1.5, .75)
(a = polyroot(z)[1])
arg = Arg(a)/(2*pi)
1/arg
set.seed(8675309)
ar2 = arima.sim(list(order=c(2,0,0), ar=c(1.5, -.75)), n = 144)
plot(ar2, axes=FALSE, xlab="Time")
axis(2); axis(1, at=seq(0, 144, by=12)); box()
abline(v=seq(0, 144, by=12), lty=2)
ACF = ARMAacf(ar=c(1.5, -.75), ma=2, 50)
plot(ACF, type="h", xlab="lag")
abline(h=0)
ARMAtoMA(ar=.9, ma=.5, 50) # for a list
plot(ARMAtoMA(ar=.9, ma=.5, 50))
# finish 3.2 Difference Equations
ACF = ARMAacf(ar=c(1.5, -.75), ma=0, 24)[-1]
PACF = ARMAacf(ar=c(1.5, -.75), ma=0, 24, pacf=TRUE)
par(mfrow=c(1,2))
plot(ACF, type="h", xlab="lag", ylim=c(-.8, 1)); abline(h=0)
plot(PACF, type="h", xlab="lag", ylim=c(-.8,1)); abline(h=0)
library(astsa)
acf2(rec, 48)
(regr = ar.ols(rec, order=2, demean = FALSE, intercept=TRUE))
regr$asy.se.coef # standard errors of the estimates
# finish Autocorrelation and Partial Autocorrelation