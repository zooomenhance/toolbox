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

###################plot data#####################
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

## Plot - change xlim to 0,100 for canopy cover or 0,50 for chm
plot(Obsrv_Vals, Pred_Vals, pch=19, cex = .1, xlim=c(0,30), ylim=c(0,30))
##Plot a 'heatmap' of the data
smoothScatter(Obsrv_Vals, Pred_Vals, xlim=c(0,100), ylim=c(0,100))
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
