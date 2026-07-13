workspace = "D:/RSEAT/EVTG/VegMapping/L5_Forest"
ModelData = "D:/RSEAT/EVTG/VegMapping/L5_Forest/Model_Dataset.csv"
ApplyData = "D:/RSEAT/EVTG/VegMapping/L5_Forest/Apply_Dataset.csv"
zonalstats = "D:/RSEAT/EVTG/Data_for_Exercise/ZonalStats/ZonalStatsConstrained.txt"
outputtxt = "D:/RSEAT/EVTG/VegMapping/L5_Forest/Level5_responses.csv"
##########################################################################
#Install and load libraries
##########################################################################
install.packages("randomForest", repos='http://cran.us.r-project.org')
library(randomForest)
##########################################################################
# Turns off scientific notation
##########################################################################
options(scipen=999)
##########################################################################
#set the workspace
##########################################################################
setwd(workspace)
rm(workspace)
##########################################################################
#Load the reference points
##########################################################################
ReferenceData = read.csv(ModelData,header=T)
#rm(points)
##########################################################################
#Load the Zonal Stats
##########################################################################
AllZonalStats = read.table(zonalstats,header=TRUE)
#rm(zonalstats)
##########################################################################
#Load the Apply dataset FIDs
##########################################################################
applyData = read.csv(ApplyData, header = TRUE)
##########################################################################
#Get the Zonal Statistics for the Model Dataset (Make sure that the right column names are specified)
##########################################################################
Model_Dataset = merge(x = ReferenceData, y = AllZonalStats, by.x = 'FID_Model', by.y = 'FID')
######################################################################################
# Get the Zonal Statistics for the Apply Dataset (Make sure that the right column names are specified)
######################################################################################
applyDataset = merge(x = applyData, y = AllZonalStats, by.x = 'FID_Model', by.y = 'FID')
######################################################################################
# Run randomForest
######################################################################################
lastColumn = dim(Model_Dataset)[2]
RF_Model = randomForest(Model_Dataset[,3:lastColumn],Model_Dataset[,2], data=Model_Dataset,importance=TRUE,ntree=4000)
print(RF_Model)
######################################################################################
#  Create Predictions 
######################################################################################
Predictions = predict(RF_Model,applyDataset,type="response")
Predictions_Vector = as.vector(Predictions)
######################################################################################
#  output text file
######################################################################################
ApplyFID = as.numeric(applyDataset[,1])
ApplyPredictions = as.factor(Predictions_Vector)
output = as.data.frame(ApplyFID)
output = cbind(output,ApplyPredictions)

colnames(output)[2] = "responses"
colnames(output)[1] = "FID"

TrainingData = ReferenceData[,1]
TrainingData = as.data.frame(TrainingData)
TrainingData = cbind(TrainingData,as.factor(ReferenceData[,2]))
colnames(TrainingData)[2] = "responses"
colnames(TrainingData)[1] = "FID"

output = rbind(output,TrainingData)

write.csv(output, outputtxt,row.names=FALSE)






