############################### Load your packages ###################

# package to convert rasters for analysis

library(raster);library(maptools);library(sp)

## Example data 
  dataDir = "\\\\166.2.126.25\\R10_VegMaps\\ChugachNF\\CNF_Structure_Pilot\\Analysis\\KP_Structure_Eval\\"
  setwd(dataDir)

#######################lidar data#############################

ifsarString = "KPse1_IfSAR_CHM.tif"
ifsarRaster = raster(ifsarString)
las1String = "KPse1_las1m_CHM.tif"
las1Raster= raster(las1String)
las3String = "KPse1_las3m_CHM.tif"
las3Raster= raster(las3String)
phodarString = "KPse1_orthoCHM.tif"
phodarRaster= raster(phodarString)
sa = readShapePoly("\\\\166.2.126.25\\R10_VegMaps\\ChugachNF\\Kenai_Peninsula\\Boundary\\KP_Structure_Evaluation\\KP_Structure_Eval1.shp")
# lidString = "lidar_2p5m_clip.img"
# lidRaster = raster(lidString)
# 
# pholidString = "Pholid_2p5m_clip.img"
# pholidRaster = raster(pholidString)
#   
# filtString = "filt_2p5m_clip.img"
# filtRaster= raster(filtString)
# 
# filString = "Fill_2p5m_clip.img"
# filRaster = raster(filString)
###################grid metrics data#################
# lidCovs = "1st_cover_above3_20METERS.asc"
# lidCovr = raster(lidCovs)
# 
# pholidCovs = "all_cover_above3_20METERS_pholid_chm.asc"
# pholidCovr = raster(pholidCovs)
# 
# ##Jeremy method for getting CC
# phoCovs = "canopy_cover_est_mosaic.tif"
# phoCovr = raster(phoCovs)
# 
# lidp95s = "elev_P95_2plus_20METERS_lid_chm.asc"
# lidp95r = raster(lidp95s)
# 
# pholidp95s = "elev_P95_2plus_20METERS_pholid_chm.asc"
# pholidp95r = raster(pholidp95s)
# 
# lidSlopes = "Lidar_dtm_slope_2p5m_clip_mask.img"
# lidSloper = raster(lidSlopes)
# 

###################plot lidar#####################
plot(ifsarRaster)
plot(las1Raster)
plot(las3Raster)
plot(phodarRaster)

############################### MAKE SOME FUNCTIONS ###################

## function to convert raster to Vector for fun in R
rtv = function(input){
  rast = as.vector(as.array(raster(input)))
}
# Function that returns Root Mean Squared Error
rmse = function(observed, predicted)
{
  error = observed - predicted
  output = sqrt(mean(error^2))
}
# Function that returns Mean Absolute Error
mae = function(observed, predicted)
{
  error = observed - predicted
  mean(abs(error))
}


comparison = function(observed, predicted, StudyRegion, min, max)
{
  points = spsample(StudyRegion, n = 100000, "random")
## Extract the values using the point locations from each of the rasters
##change the raster of Pred_Vals to for different comparisons to lidar
Pred_Vals = extract(predicted, points)
Obsrv_Vals = extract(observed, points)
##using values to stratify by canopy cover values
# strata = extract(cc, points)
# Obsrv_Vals[strata<min] = NA
# Obsrv_Vals[strata>max] = NA

## Plot - change xlim to 0,100 for canopy cover or 0,50 for chm
plot(Obsrv_Vals, Pred_Vals, pch=19, cex = .1, xlim=c(0,30), ylim=c(0,30))
##Plot a 'heatmap' of the data
##smoothScatter(Obsrv_Vals, Pred_Vals, xlim=c(0,100), ylim=c(0,100))
##add 1:1 line
abline(0,1,lty=2, col="blue")
##add linear regression line
abline(lm(Pred_Vals~Obsrv_Vals), col="red")
##summarize the linear regression
summary = summary(lm(Pred_Vals~Obsrv_Vals))
print(summary)
##put the data together
bothVals = cbind(Obsrv_Vals, Pred_Vals)
## Get rid of rows with NA's
bothVals = bothVals[complete.cases(bothVals),]
##compute RMSE
error = bothVals[,1]- bothVals[,2]
output = sqrt(mean(error^2))
print("RMSE")
print(output)}

## Get rid of rows with NA's
bothVals = bothVals[complete.cases(bothVals),]

comparison(ifsarRaster, phodarRaster,sa ,0 ,100)
comparison(las1Raster, las3Raster,sa,0 ,100)
comparison(las1Raster, phodarRaster,sa,0 ,100)
comparison(las1Raster, ifsarRaster,sa,0 ,100)

# comparison(lidCovr, phoCovr, readShapePoly("lidar_area_mask.shp"), lidCovr, 0, 100)
# comparison(lidCovr, phoCovr, readShapePoly("lidar_area_mask.shp"), lidCovr, 0, 20)
# comparison(lidCovr, phoCovr, readShapePoly("lidar_area_mask.shp"), lidCovr, 20, 40)
# comparison(lidCovr, phoCovr, readShapePoly("lidar_area_mask.shp"), lidCovr, 40, 60)
# comparison(lidCovr, phoCovr, readShapePoly("lidar_area_mask.shp"), lidCovr, 60, 80)
# comparison(lidCovr, phoCovr, readShapePoly("lidar_area_mask.shp"), lidCovr, 80, 100)
# 
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidCovr, 0, 100)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidCovr, 0, 20)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidCovr, 20, 40)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidCovr, 40, 60)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidCovr, 60, 80)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidCovr, 80, 100)
# 
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidSloper, 0, 100)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidSloper, 0, 10)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidSloper, 10, 20)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidSloper, 20, 30)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidSloper, 30, 40)
# comparison(lidp95r, pholidp95r, readShapePoly("lidar_area_mask.shp"), lidSloper, 40, 90)
# 
# 
# 
# 
