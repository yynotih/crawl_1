from django.db import models


class HouseProject(models.Model):
    id = models.IntegerField()
    projectName = models.CharField(max_length=255)
    avgPrice = models.CharField(max_length=63)
    presaleLicence = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    houseNum = models.CharField(max_length=31)
    landArea = models.CharField(max_length=63)
    buildingArea = models.CharField(max_length=63)
    presaleDate = models.CharField(max_length=31)
    presaleEndDate = models.CharField(max_length=31)
    addDate = models.DateField()
    modifyDate = models.DateField()
