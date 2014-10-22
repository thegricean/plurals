setwd("~/cogsci/projects/plurals/results/")
source("rscripts/helpers.r")

r = read.table("data/results.tsv", sep="\t", header=T,quote="")
summary(r)
r$NounAdj = as.factor(paste(r$Noun,r$Adjective))
t = as.data.frame(table(r$NounAdj))
write.table(t[order(t[,c("Freq")],decreasing=T),],file="data/frequencies.txt",sep="\t",quote=F,row.names=F,col.names=F)
ordering = t[order(t[,c("Freq")],decreasing=T),]$Var1
str(ordering)

table(r$Match)
levels(r$NounAdj) = ordering

#r[r$Noun == "leaves" & r$Adjective == "long",]$Sentence
save(r, file="data/r.RData")
nrow(r)
