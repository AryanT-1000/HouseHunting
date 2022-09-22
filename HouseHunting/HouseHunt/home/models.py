from email.policy import default
from django.db import models

# Create your models here.

class Property(models.Model):

    # NOT migrated yet
    b0 = 'unknown'
    b1 = '1 BHK'
    b2 = '2 BHK'
    b3 = '3 BHK'
    b4 = '4 BHK'

    room_type = [
        (b0, 'unknown'),
        (b1, '1 BHK'),
        (b2, '2 BHK'),
        (b3, '3 BHK'),
        (b4, '4 BHK'),
    ]
    # -------------------------------------------------------
    unknown_state = 'unknown'
    rtm = 'Ready to move'
    undercon = 'Under Construction'
    fur = 'Furnished'
    semifur = 'Semi-Furnished'
    unfur = 'Unfurnished'

    state = [
        (unknown_state, 'unknown'),
        (rtm, 'Ready To Move'),
        (undercon, 'Under Construction'),
        (fur, 'Furnished'),
        (semifur, 'Semi-Furnished'),
        (unfur,'Unfurnished'),
    ]
    # ------------------------------------------------------------
    unknown_type = 'Type Unknown'
    flat = 'Flat'
    house = 'House'
    shop = 'Shop'
    warehouse = 'Warehouse'
    land = 'Land(Plot)'

    type_of_estate = [
        (unknown_type,'Type Unknown'),
        (flat ,'Flat'),
        (house ,'House'),
        (shop,'Shop'),
        (warehouse ,'Warehouse'),
        (land, 'Land(Plot)'),
    ]

    # -------------------------------------------------------------
    unknown_purpose = 'unknown'
    for_sell = 'SELL'
    for_buy = 'BUY'
    for_rent = 'RENT'

    for_purpose = [
        (unknown_purpose,'unknown'),
        (for_sell, 'SELL'),
        (for_buy, 'BUY'),
        (for_rent, 'RENT')
    ]

    user_mail = models.ForeignKey("loging.TenentUser", on_delete=models.CASCADE)
    mobile = models.IntegerField()
    price = models.IntegerField()
    BHK = models.CharField(choices=room_type, max_length=7, default=b0)
    location = models.CharField(max_length=100)
    status = models.CharField(choices=state, max_length=20, default=unknown_state)
    prop_type = models.CharField(choices=type_of_estate, max_length=20, default=unknown_type)
    city =  models.CharField(max_length=30)
    for_sell_or_rent =  models.CharField(choices=for_purpose,default= unknown_purpose, max_length=20)
    image = models.ImageField(upload_to='User_Images/')
    prop_number = models.CharField(max_length=30)

    def __str__(self):
        return self.location
