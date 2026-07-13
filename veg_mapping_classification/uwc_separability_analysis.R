# Load library packages
install.packages("ggplot2")
install.packages("geomnet")
install.packages("plyr")
install.packages("ape")

library(ggplot2)
library(geomnet)
library(plyr)
library(ape)

# Set working directory
setwd('\\\\166.2.126.25\\R4_VegMaps\\Uinta_Wasatch_Cache\\Mapping\\01_Veg_Type\\SeparabilityAnalysis')

# Functions (http://stats.stackexchange.com/questions/106325/jeffries-matusita-distance-for-14-variables)

# Compute the Mahalanobis distance between two vectors.
mahalanobis <- function(m1, m2, sigma) {m <- m1 - m2; m %*% solve(sigma, m)}

# Compute the Bhattacharyya distance between two multivariate normal distributions
# given by their means and covariance matrices.
bhattacharyya <- function(m1, s1, m2, s2) {
  d <- function(u) determinant(u, logarithm=TRUE)$modulus # Log determinant of matrix u
  s <- (s1 + s2)/2                                        # mean covariance matrix
  mahalanobis(m1, m2, s)/8 + (d(s) - d(s1)/2 - d(s2)/2)/2
}

# Re-express the Bhattacharyya distance as the Jeffries-Matusita distance.
jeffries.matusita <- function(...) sqrt(2*(1-exp(-bhattacharyya(...))))

# Load CSV data as data frame
filepath <- 'UWC_Separability_ZonalStats.csv'
class_data <- read.table(filepath,header=TRUE,sep=",",stringsAsFactors=FALSE)

# Remove unwanted column(s) in the data
class_data$FID <- NULL
# class_data$uwc_ned_slopeaspect_cos_transformation1_MEAN <- NULL
# class_data$uwc_ned_slopeaspect_sin_transformation1_MEAN <- NULL
# class_data$uwc_ned_slope_degrees1_MEAN <- NULL

# Remove BLSB and PP obs
class_data <- class_data[!(class_data$Class %in% c('BLSB','PP')),]

# Combine BSB and WSB obs as WSB/BSB
class_data$Class[class_data$Class %in% c('BSB','WSB')] <- 'WSB/BSB'
class_data$Class <- as.factor(class_data$Class)

# Select predictors
# pred_list <- c('dixie_elevation1_MEAN','dx_slope_degrees1_MEAN','dx_slp_asp_cos1_MEAN',
#                'dx_slp_asp_sin1_MEAN','dx_10m_naip1_MEAN','dx_10m_naip2_MEAN',
#                'dx_10m_naip3_MEAN','dx_10m_naip4_MEAN','dx_landsat_summer_bands2_8_10m1_MEAN',
#                'dx_landsat_summer_bands2_8_10m2_MEAN','dx_landsat_summer_bands2_8_10m3_MEAN',
#                'dx_landsat_summer_bands2_8_10m4_MEAN','dx_landsat_summer_bands2_8_10m5_MEAN',
#                'dx_landsat_summer_bands2_8_10m6_MEAN','dx_landsat_summer_bands2_8_10m7_MEAN',
#                'dx_landsat_summer_bands2_8_10m1_MEAN','Class')
# 
# # pred_list <- c('dixie_elevation1_MEAN','dx_slope_degrees1_MEAN','dx_slp_asp_cos1_MEAN',
# #                'dx_slp_asp_sin1_MEAN','dx_10m_naip1_MEAN','dx_10m_naip2_MEAN',
# #                'dx_10m_naip3_MEAN','dx_10m_naip4_MEAN','dx_landsat_fall_bands2_8_10m1_MEAN',
# #                'dx_landsat_fall_bands2_8_10m2_MEAN','dx_landsat_fall_bands2_8_10m3_MEAN',
# #                'dx_landsat_fall_bands2_8_10m4_MEAN','dx_landsat_fall_bands2_8_10m5_MEAN',
# #                'dx_landsat_fall_bands2_8_10m6_MEAN','dx_landsat_fall_bands2_8_10m7_MEAN',
# #                'dx_landsat_fall_bands2_8_10m1_MEAN','Class')

freq <- count(class_data,'Class')
sortfreq <- freq[with(freq,order(-freq)),]
sortfreq

# subset <- class_data[,pred_list]
subset <- class_data

subset$Class <- NULL
pca <- princomp(subset)
pca_data <- as.data.frame(pca$scores)
pca_data$Class <- class_data$Class

class_levels <- levels(class_data$Class)
l <- length(class_levels)

D <- matrix(data=NA, nrow=l, ncol=l)
for(i in 1:l){
  pca_i <- pca_data[which(pca_data$Class==class_levels[i]),c(1:8)]
  pca_i$Class <- NULL
  pmat_i <- as.matrix(pca_i)
  m1 <- colMeans(pmat_i)
  s1 <- cov(pmat_i)
  for(j in 1:l){
    if (i == j) {
      D[i,j] <- 0
    } else if (i > j) {
      D[i,j] <- D[j,i]
    } else {
      pca_j <- pca_data[which(pca_data$Class==class_levels[j]),c(1:8)]
      pca_j$Class <- NULL
      pmat_j <- as.matrix(pca_j)
      m2 <- colMeans(pmat_j)
      s2 <- cov(pmat_j)
      jm <- jeffries.matusita(m1,s1,m2,s2)
      D[i,j] <- jm[1,1]*100/sqrt(2)
    }
  }
}
colnames(D) <- rownames(D) <- class_levels
D <- as.dist(D)
hc <- hclust(D)
plot(hc,xlab=null,main="Cluster Dendrogram")
plot(hc,hang=-1,xlab=null)

hcd <- as.dendrogram(hc)
plot(hcd,horiz=TRUE)
plot(as.phylo(hc), type = "unrooted")
plot(as.phylo(hc), type = "fan")
