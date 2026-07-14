install.packages("data.table")
library("data.table", lib.loc="C:/Program Files/R/R-3.5.1/library")

##set workspace where all csvs are located
setwd("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables")

## read in all crosswalk txt file - created from shapefile dbf
black_kettle_04_05 = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables/black_kettle_04_05.txt") 
black_kettle_05 = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables/black_kettle_05.txt") 
kiowa_rb_east_e = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables/kiowa_rb_east_e.txt") 
kiowa_rb_nm_west = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables/kiowa_rb_nm_west.txt") 
mcclellen_creek = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables/mcclellen_creek.txt") 
ng = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables/ng.txt") 
nf_lidar = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/segmentation/output/crosswalk_tables/nf_lidar.txt") 
#nf_mag = read.delim("nf_phodar_mag.txt")
#nf_san = read.delim("nf_phodar_san.txt")
#ng_nf_phodar = read.delim("ng_nf_phodar.txt")


black_kettle_04_05_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_black_kettle_0405_v2.txt") 
black_kettle_05_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_black_kettle_05_v2.txt") 
kiowa_rb_east_e_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_rb_kiowa_east_e_v2.txt") 
kiowa_rb_nm_west_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_rb_kiowa_nm_west_v2.txt") 
mcclellen_creek_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_mcclellan_creek_v2.txt") 
nf_lidar_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_nf_l8_naip_lidar_dem_nona.txt")
nf_lidar_vh_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_lidar_reclass_zs.txt")

#nf_mag_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_nf_mag_l8_naip_phodar_dem.txt")
#nf_san_zs = read.delim("//166.2.126.25/R4_VegMaps/R3_RiparianMapping/2018_forests/cibola/mapping/zonal_stats/cib_nf_san_l8_naip_phodar_dem.txt")
##pick out only the columns you want to keep
##chm<-chm[,c("FeatureId","Mean","Std")]



##rename columns so they are all identical 

colnames(black_kettle_04_05_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","phoav","phomd","phosd","elevav","elevmd","elevsd","slopeav","slopemd","slopesd")
colnames(black_kettle_05_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","phoav","phomd","phosd","elevav","elevmd","elevsd","slopeav","slopemd","slopesd")
colnames(kiowa_rb_east_e_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","phoav","phomd","phosd","elevav","elevmd","elevsd","slopeav","slopemd","slopesd")
colnames(kiowa_rb_nm_west_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","phoav","phomd","phosd","elevav","elevmd","elevsd","slopeav","slopemd","slopesd")
colnames(mcclellen_creek_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","phoav","phomd","phosd","elevav","elevmd","elevsd","slopeav","slopemd","slopesd")
#colnames(nf_mag_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","phoav","phomd","phosd","elevav","elevmd","elevsd","slopeav","slopemd","slopesd")
#colnames(nf_san_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","phoav","phomd","phosd","elevav","elevmd","elevsd","slopeav","slopemd","slopesd")
colnames(nf_lidar_zs) <- c("fid","l81av","l81md","l81sd","l82av","l82md","l82sd","l83av","l83md","l83sd","l84av","l84md","l84sd","l85av","l85md","l85sd","l86av","l86md","l86sd","ndviav","ndvimd","ndvisd","naip1av","naip1md","naip1sd","naip2av","naip2md","naip2sd","naip3av","naip3md","naip3sd","naip4av","naip4md","naip4sd","lidreclsav","lidreclsmd","lidreclssd","lidcovav","lidcovmd","lidcovsd","lidav","lidmd","lidsd","slopeav","slopemd","slopesd","elevav","elevmd","elevsd")


##break out rasters with multiple bands into each band
##res1 <- subset(resource, resource$RasterBand =='1', select=c(FeatureId,Mean,Std))

##join zonal stats with table that crosswalks model fid and master fid to be able to connect to main master fid file

black_kettle_04_05_zs_id <- merge(black_kettle_04_05,black_kettle_04_05_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
kiowa_rb_nm_west_zs_id <- merge(kiowa_rb_nm_west,kiowa_rb_nm_west_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
kiowa_rb_east_e_zs_id <- merge(kiowa_rb_east_e,kiowa_rb_east_e_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
mcclellen_creek_zs_id <- merge(mcclellen_creek,mcclellen_creek_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
black_kettle_05_zs_id <- merge(black_kettle_05,black_kettle_05_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
#nf_mag_zs_id <- merge(nf_mag,nf_mag_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
#nf_san_zs_id <- merge(nf_san,nf_san_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
nf_lidar_zs_id <- merge(nf_lidar,nf_lidar_zs, by.x = "model_fid", by.y = "FID",all = TRUE)
nf_lidar_vh_zs_id <- merge(nf_lidar,nf_lidar_vh_zs, by.x = "model_fid", by.y = "FID",all = TRUE)

##remove the model_fid field
black_kettle_04_05_zs_id$model_fid <- NULL
kiowa_rb_nm_west_zs_id$model_fid <- NULL
kiowa_rb_east_e_zs_id$model_fid <- NULL
mcclellen_creek_zs_id$model_fid <- NULL
black_kettle_05_zs_id$model_fid <- NULL
#nf_mag_zs_id$model_fid <- NULL
#nf_san_zs_id$model_fid <- NULL
nf_lidar_zs_id$model_fid <- NULL

##join all together by using the master fid
rbind1 <- rbind(black_kettle_04_05_zs_id,kiowa_rb_nm_west_zs_id)
rbind2 <- rbind(rbind1,kiowa_rb_east_e_zs_id)
rbind3 <- rbind(rbind2,mcclellen_creek_zs_id)
rbind4 <- rbind(rbind3,black_kettle_05_zs_id)
#rbind5 <- rbind(rbind4,nf_mag_zs_id)
#rbind6 <- rbind(rbind5,nf_san_zs_id)

rbind4_order <- rbind4[order(rbind4$master_fid),]
#rbind6_order <- rbind6[order(rbind6$master_fid),]

#remove(rbind21)

###################################Review##########################################
#picking the first row of each zonal stats and comparing the master id to main file to make sure
#the correct data is in both

#reconnecting original zonal stats to master table to recover model fid
black_kettle_04_05_zs_id1 <- merge(black_kettle_04_05,black_kettle_04_05_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
kiowa_rb_nm_west_zs_id1 <- merge(kiowa_rb_nm_west,kiowa_rb_nm_west_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
kiowa_rb_east_e_zs_id1 <- merge(kiowa_rb_east_e,kiowa_rb_east_e_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
mcclellen_creek_zs_id1 <- merge(mcclellen_creek,mcclellen_creek_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
black_kettle_05_zs_id1 <- merge(black_kettle_05,black_kettle_05_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
#nf_mag_zs_id1 <- merge(nf_mag,nf_mag_zs, by.x = "model_fid", by.y = "fid",all = TRUE)
#nf_san_zs_id1 <- merge(nf_san,nf_san_zs, by.x = "model_fid", by.y = "fid",all = TRUE)


##function that will pull the data from original zonal stats and compare to main master file, returning the first line of data to compare
review = function(zs_id, master_zs)
{
sample1 <- zs_id[1,1:44]
sample1$model_fid <- NULL
master_id <- sample1[1,1]
sample2 <- subset(master_zs, master_zs$master_fid == master_id)
review_df <-rbind(sample1, sample2)
return(review_df)
}
review(black_kettle_05_zs_id1,rbind4_order)
review(black_kettle_04_05_zs_id1,rbind4_order)
review(kiowa_rb_nm_west_zs_id1,rbind4_order)
review(kiowa_rb_east_e_zs_id1,rbind4_order)
review(mcclellen_creek_zs_id1,rbind4_order)
#review(nf_mag_zs_id1,rbind6_order)
#review(nf_san_zs_id1,rbind6_order)
###################################Review##########################################


##Remove all NA and put as -999 and write resulting dataframe as a csv ,na="-999" I had to edit the fid field in excel. Seems like the column header got shifted over one for some reason. Easiest to just fix in excel
#write.csv(rbind6_order, file = "cib_ng_zs1.csv")
write.table(nf_lidar_vh_zs_id, file = "nf_lidar_vh_zs_id.txt",sep="\t",na="-999")
write.table(rbind4_order, file = "cib_ng_zs_nona_v2.txt",sep="\t",na="-999")
write.table(nf_lidar_zs_id, file = "cib_nf_l8_naip_lidar_dem_nona_v2.txt",sep="\t",na="-999")
##read csv back into R to review
##allmergereview = read.csv("J:/zonalstats_aps/output/backup/allmerged.csv") 
zs_readin = read.delim("cib_phodar_zs_nona_v2.txt")
