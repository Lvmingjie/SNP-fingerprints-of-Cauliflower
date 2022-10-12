setwd("D:\\代码\\DNA_Fingerprint")
library(RColorBrewer)

df3 <- read.table('snp.p.3.Q.reformat')
df4 <- read.table('snp.p.4.Q.reformat')
df5 <- read.table('snp.p.5.Q.reformat')
df6 <- read.table('snp.p.6.Q.reformat')
df7 <- read.table('snp.p.7.Q.reformat')
df8 <- read.table('snp.p.8.Q.reformat')
df9 <- read.table('snp.p.9.Q.reformat')

color1 = rgb(158, 1, 66, maxColorValue = 255)
color2 = rgb(213, 62, 79, maxColorValue = 255)
color3 = rgb(244, 109, 67, maxColorValue = 255)
color4 = rgb(252, 141, 89, maxColorValue = 255)
color5 = rgb(254, 224, 139, maxColorValue = 255)
color6 = rgb(255, 255, 191, maxColorValue = 255)
color7 = rgb(230, 245, 152, maxColorValue = 255)
color8 = rgb(171, 221, 164, maxColorValue = 255)
color9 = rgb(102, 194, 165, maxColorValue = 255)
color10 = rgb(50, 136, 189, maxColorValue = 255)
color11 = rgb(94, 79, 162, maxColorValue = 255)
spectral <- c(color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11)

pdf('admixture_Q3.reformat.pdf', width = 15, height = 3)
barplot(t(as.matrix(df3)), 
				col = spectral[1:3], 
				xlab = 'Individual', ylab = 'Ancestry', 
				border = NA, 
				space = 0)
dev.off()

pdf('admixture_Q4.reformat.pdf', width = 15, height = 3)
barplot(t(as.matrix(df4)), 
				col = spectral[1:4], 
				xlab = 'Individual', ylab = 'Ancestry', 
				border = NA, 
				space = 0)
dev.off()

pdf('admixture_Q5.reformat.pdf', width = 15, height = 3)
barplot(t(as.matrix(df5)), 
				col = spectral[1:5], 
				xlab = 'Individual', ylab = 'Ancestry', 
				border = NA, 
				space = 0)
dev.off()

pdf('admixture_Q6.reformat.pdf', width = 15, height = 3)
barplot(t(as.matrix(df6)), 
				col = spectral[1:6], 
				xlab = 'Individual', ylab = 'Ancestry', 
				border = NA, 
				space = 0)
dev.off()

pdf('admixture_Q7.reformat.pdf', width = 15, height = 3)
barplot(t(as.matrix(df7)), 
				col = spectral[1:7], 
				xlab = 'Individual', ylab = 'Ancestry', 
				border = NA, 
				space = 0)
dev.off()

pdf('admixture_Q8.reformat.pdf', width = 15, height = 3)
barplot(t(as.matrix(df8)), 
				col = spectral[1:8], 
				xlab = 'Individual', ylab = 'Ancestry', 
				border = NA, 
				space = 0)
dev.off()

pdf('admixture_Q9.reformat.pdf', width = 15, height = 3)
barplot(t(as.matrix(df9)), 
				col = spectral[1:9], 
				xlab = 'Individual', ylab = 'Ancestry', 
				border = NA, 
				space = 0)
dev.off()

