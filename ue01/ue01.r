## @knitr read-ue01-3-data
diff <- read.csv(file="piresult_diff.csv", head=TRUE, sep=";")
time <- read.csv(file="piresult_time.csv", head=TRUE, sep=";")

## @knitr plot-ue01-3-data-diff
boxplot(diff, xlab="Anzahl generierter Punkte", ylab="Differenz zu PI")

## @knitr plot-ue01-3-data-time
boxplot(time, xlab="Anzahl generierter Punkte", ylab="Ausführungszeit in sec", log="y")
