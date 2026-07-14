install.packages("data.table")
library("data.table", lib.loc="~/R/R-3.3.2/library")

##set workspace where all csvs are located
setwd("J:/zonalstats_cor/output")

## read in all csvs from GDAL zonal script
chm = fread("J:/zonalstats_cor/output/2017_02_02_combine_cor_nf_chm_6m_null.csv") 
l8fall = fread("J:/zonalstats_cor/output/cor_fall16_l8_bands2_8_6m_img.csv") 
coeff = fread("J:/zonalstats_cor/output/cor_ndvi_2014_2016_6m.csv") 
l8sum = fread("J:/zonalstats_cor/output/cor_sum16_l8_z12_bands2_8_6m.csv") 
naip = fread("J:/zonalstats_cor/output/Coronado_NF_10m_NAIP2015_mosaic.csv") 
naip_ndvi = fread("J:/zonalstats_cor/output/Coronado_NF_10m_NAIP2015_mosaic1_NDVI.csv") 
ned = fread("J:/zonalstats_cor/output_topo/Cor_NF_5m_NED.csv") 
nedslope = fread("J:/zonalstats_cor/output_topo/Cor_NF_5m_NED_slope.csv")
resource = fread("J:/zonalstats_cor/output_resource/cor_resource_2011_4band_6m.csv")
resourcendvi = fread("J:/zonalstats_cor/output_resource/cor_resource_2011_4band_6m_ndvi1.csv")

blank = fread("J:/zonalstats_cor/output/2017_03_23_cor_nf_seg_working_nfborder_clip_elim40.csv")


##pick out only the columns you want to keep

chm<-chm[,c("FeatureId","Mean","Std")]
naip_ndvi<-naip_ndvi[,c("FeatureId","Mean","Std")]
ned<-ned[,c("FeatureId","Mean","Std")]
nedslope<-nedslope[,c("FeatureId","Mean","Std")]
resourcendvi<-resourcendvi[,c("FeatureId","Mean","Std")]
# 
# l8fall<-l8fall[,c("FeatureId","Mean","Std")]
# coeff<-coeff[,c("FeatureId","Mean","Std")]
# l8sum<-l8sum[,c("FeatureId","Mean","Std")]
# naip<-naip[,c("FeatureId","Mean","Std")]



##rename columns according to raster
colnames(chm) <- c("chmFeatureId","chmMean","chmStd")
colnames(naip_ndvi) <- c("naip_ndviFeatureId","naip_ndviMean","naip_ndviStd")
colnames(ned) <- c("nedFeatureId","nedMean","nedStd")
colnames(nedslope) <- c("nedslopeFeatureId","nedslopeMean","nedslopeStd")
colnames(resourcendvi) <- c("resndviFeatureId","resndvislopeMean","resndvislopeStd")

# colnames(l8fall) <- c("l8fallFeatureId","l8fallMean","l8fallStd")
# colnames(coeff) <- c("coeffFeatureId","coeffMean","coeffStd")
# colnames(l8sum) <- c("l8sumFeatureId","l8sumMean","l8sumStd")
# colnames(naip) <- c("naipFeatureId","naipMean","naipStd")
# 

##break out rasters with multiple bands into each band
res1 <- subset(resource, resource$RasterBand =='1', select=c(FeatureId,Mean,Std))
res2 <- subset(resource, resource$RasterBand =='2', select=c(FeatureId,Mean,Std))
res3 <- subset(resource, resource$RasterBand =='3', select=c(FeatureId,Mean,Std))
res4 <- subset(resource, resource$RasterBand =='4', select=c(FeatureId,Mean,Std))


naip1 <- subset(naip, naip$RasterBand =='1', select=c(FeatureId,Mean,Std))
naip2 <- subset(naip, naip$RasterBand =='2', select=c(FeatureId,Mean,Std))
naip3 <- subset(naip, naip$RasterBand =='3', select=c(FeatureId,Mean,Std))
naip4 <- subset(naip, naip$RasterBand =='4', select=c(FeatureId,Mean,Std))

l8fall1 <- subset(l8fall, l8fall$RasterBand =='1', select=c(FeatureId,Mean,Std))
l8fall2 <- subset(l8fall, l8fall$RasterBand =='2', select=c(FeatureId,Mean,Std))
l8fall3 <- subset(l8fall, l8fall$RasterBand =='3', select=c(FeatureId,Mean,Std))
l8fall4 <- subset(l8fall, l8fall$RasterBand =='4', select=c(FeatureId,Mean,Std))
l8fall5 <- subset(l8fall, l8fall$RasterBand =='5', select=c(FeatureId,Mean,Std))
l8fall6 <- subset(l8fall, l8fall$RasterBand =='6', select=c(FeatureId,Mean,Std))
l8fall7 <- subset(l8fall, l8fall$RasterBand =='7', select=c(FeatureId,Mean,Std))

l8sum1 <- subset(l8sum, l8sum$RasterBand =='1', select=c(FeatureId,Mean,Std))
l8sum2 <- subset(l8sum, l8sum$RasterBand =='2', select=c(FeatureId,Mean,Std))
l8sum3 <- subset(l8sum, l8sum$RasterBand =='3', select=c(FeatureId,Mean,Std))
l8sum4 <- subset(l8sum, l8sum$RasterBand =='4', select=c(FeatureId,Mean,Std))
l8sum5 <- subset(l8sum, l8sum$RasterBand =='5', select=c(FeatureId,Mean,Std))
l8sum6 <- subset(l8sum, l8sum$RasterBand =='6', select=c(FeatureId,Mean,Std))
l8sum7 <- subset(l8sum, l8sum$RasterBand =='7', select=c(FeatureId,Mean,Std))

coeff1 <- subset(coeff, coeff$RasterBand =='1', select=c(FeatureId,Mean,Std))
coeff2 <- subset(coeff, coeff$RasterBand =='2', select=c(FeatureId,Mean,Std))
coeff3 <- subset(coeff, coeff$RasterBand =='3', select=c(FeatureId,Mean,Std))
coeff4 <- subset(coeff, coeff$RasterBand =='4', select=c(FeatureId,Mean,Std))

##rename columns from raster with multiple bands
colnames(coeff1) <- c("coeff1FeatureId","coeff1Mean","coeff1Std")
colnames(coeff2) <- c("coeff2FeatureId","coeff2Mean","coeff2Std")
colnames(coeff3) <- c("coeff3FeatureId","coeff3Mean","coeff3Std")
colnames(coeff4) <- c("coeff4FeatureId","coeff4Mean","coeff4Std")

colnames(l8fall1) <- c("l8fall1FeatureId","l8fall1Mean","l8fall1Std")
colnames(l8fall2) <- c("l8fall2FeatureId","l8fall2Mean","l8fall2Std")
colnames(l8fall3) <- c("l8fall3FeatureId","l8fall3Mean","l8fall3Std")
colnames(l8fall4) <- c("l8fall4FeatureId","l8fall4Mean","l8fall4Std")
colnames(l8fall5) <- c("l8fall5FeatureId","l8fall5Mean","l8fall5Std")
colnames(l8fall6) <- c("l8fall6FeatureId","l8fall6Mean","l8fall6Std")
colnames(l8fall7) <- c("l8fall7FeatureId","l8fall7Mean","l8fall7Std")

colnames(l8sum1) <- c("l8sum1FeatureId","l8sum1Mean","l8sum1Std")
colnames(l8sum2) <- c("l8sum2FeatureId","l8sum2Mean","l8sum2Std")
colnames(l8sum3) <- c("l8sum3FeatureId","l8sum3Mean","l8sum3Std")
colnames(l8sum4) <- c("l8sum4FeatureId","l8sum4Mean","l8sum4Std")
colnames(l8sum5) <- c("l8sum5FeatureId","l8sum5Mean","l8sum5Std")
colnames(l8sum6) <- c("l8sum6FeatureId","l8sum6Mean","l8sum6Std")
colnames(l8sum7) <- c("l8sum7FeatureId","l8sum7Mean","l8sum7Std")

colnames(naip1) <- c("naip1FeatureId","naip1Mean","naip1Std")
colnames(naip2) <- c("naip2FeatureId","naip2Mean","naip2Std")
colnames(naip3) <- c("naip3FeatureId","naip3Mean","naip3Std")
colnames(naip4) <- c("naip4FeatureId","naip4Mean","naip4Std")

colnames(res1) <- c("res1FeatureId","res1Mean","res1Std")
colnames(res2) <- c("res2FeatureId","res2Mean","res2Std")
colnames(res3) <- c("res3FeatureId","res3Mean","res3Std")
colnames(res4) <- c("res4FeatureId","res4Mean","res4Std")

##merge all datasets together keeping ones that don't match and creating NA value. I saved each step as a seperate data frame to keep track in
##case something went wrong, more data intensive, but I wanted to make sure it worked right. Could easily just rewrite over the same dataframe with each merge if needed
blank1 <- merge(blank,chm, by.x = "model_fid", by.y = "chmFeatureId",all = TRUE)
blank2 <- merge(blank1,naip_ndvi, by.x = "model_fid", by.y = "naip_ndviFeatureId",all = TRUE)
blank3 <- merge(blank2,coeff1, by.x = "model_fid", by.y = "coeff1FeatureId",all = TRUE)
blank4 <- merge(blank3,coeff2, by.x = "model_fid", by.y = "coeff2FeatureId",all = TRUE)
blank5 <- merge(blank4,coeff3, by.x = "model_fid", by.y = "coeff3FeatureId",all = TRUE)
blank6 <- merge(blank5,coeff4, by.x = "model_fid", by.y = "coeff4FeatureId",all = TRUE)
blank7 <- merge(blank6,l8fall1, by.x = "model_fid", by.y = "l8fall1FeatureId",all = TRUE)
blank8 <- merge(blank7,l8fall2, by.x = "model_fid", by.y = "l8fall2FeatureId",all = TRUE)
blank9 <- merge(blank8,l8fall3, by.x = "model_fid", by.y = "l8fall3FeatureId",all = TRUE)
blank10 <- merge(blank9,l8fall4, by.x = "model_fid", by.y = "l8fall4FeatureId",all = TRUE)
blank11 <- merge(blank10,l8fall5, by.x = "model_fid", by.y = "l8fall5FeatureId",all = TRUE)
blank12 <- merge(blank11,l8fall6, by.x = "model_fid", by.y = "l8fall6FeatureId",all = TRUE)
blank13 <- merge(blank12,l8fall7, by.x = "model_fid", by.y = "l8fall7FeatureId",all = TRUE)
blank14 <- merge(blank13,l8sum1, by.x = "model_fid", by.y = "l8sum1FeatureId",all = TRUE)
blank15 <- merge(blank14,l8sum2, by.x = "model_fid", by.y = "l8sum2FeatureId",all = TRUE)
blank16 <- merge(blank15,l8sum3, by.x = "model_fid", by.y = "l8sum3FeatureId",all = TRUE)
blank17 <- merge(blank16,l8sum4, by.x = "model_fid", by.y = "l8sum4FeatureId",all = TRUE)
blank18 <- merge(blank17,l8sum5, by.x = "model_fid", by.y = "l8sum5FeatureId",all = TRUE)
blank19 <- merge(blank18,l8sum6, by.x = "model_fid", by.y = "l8sum6FeatureId",all = TRUE)
blank20 <- merge(blank19,l8sum7, by.x = "model_fid", by.y = "l8sum7FeatureId",all = TRUE)
blank21 <- merge(blank20,naip1, by.x = "model_fid", by.y = "naip1FeatureId",all = TRUE)
blank22 <- merge(blank21,naip2, by.x = "model_fid", by.y = "naip2FeatureId",all = TRUE)
blank23 <- merge(blank22,naip3, by.x = "model_fid", by.y = "naip3FeatureId",all = TRUE)
blank24 <- merge(blank23,naip4, by.x = "model_fid", by.y = "naip4FeatureId",all = TRUE)
blank25 <- merge(blank24,ned, by.x = "model_fid", by.y = "nedFeatureId",all = TRUE)
blank26 <- merge(blank25,nedslope, by.x = "model_fid", by.y = "nedslopeFeatureId",all = TRUE)
blank27 <- merge(blank26,res1, by.x = "model_fid", by.y = "res1FeatureId",all = TRUE)
blank28 <- merge(blank27,res2, by.x = "model_fid", by.y = "res2FeatureId",all = TRUE)
blank29 <- merge(blank28,res3, by.x = "model_fid", by.y = "res3FeatureId",all = TRUE)
blank30 <- merge(blank29,res4, by.x = "model_fid", by.y = "res4FeatureId",all = TRUE)
blank31 <- merge(blank30,resourcendvi, by.x = "model_fid", by.y = "resndviFeatureId",all = TRUE)


##Remove all NA and put as -999 and write resulting dataframe as a csv ,na="-999"
write.csv(blank31, file = "allmerged_topo_res_nona.csv",na="-999")
##read csv back into R to review
##allmergereview = read.csv("J:/zonalstats_aps/output/backup/allmerged.csv") 