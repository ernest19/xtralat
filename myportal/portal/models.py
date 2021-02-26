# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db.models import GeometryField
# Create your models here.




class TblEvcTransactions(models.Model):
    ersreference = models.CharField(max_length=50, blank=True, null=True)
    originalersreference = models.CharField(max_length=50, blank=True, null=True)
    referredersreference = models.CharField(max_length=50, blank=True, null=True)
    isreversal = models.CharField(max_length=50, blank=True, null=True)
    clienttype = models.CharField(max_length=50, blank=True, null=True)
    transactiontype = models.CharField(max_length=50, blank=True, null=True)
    starttime = models.CharField(max_length=50, blank=True, null=True)
    endtime = models.CharField(max_length=50, blank=True, null=True)
    initiatorid = models.CharField(max_length=50, blank=True, null=True)
    initiatoridtype = models.CharField(max_length=50, blank=True, null=True)
    initiatortype = models.CharField(max_length=50, blank=True, null=True)
    transactionprofile = models.CharField(max_length=50, blank=True, null=True)
    resultcode = models.CharField(max_length=50, blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    initiatormsisdn = models.CharField(max_length=50, blank=True, null=True)
    initiatorresellerid = models.CharField(max_length=50, blank=True, null=True)
    initiatorcontractid = models.CharField(max_length=50, blank=True, null=True)
    initiatorresellerpath = models.CharField(max_length=50, blank=True, null=True)
    initiatorgroup = models.CharField(max_length=50, blank=True, null=True)
    initiatoruserid = models.CharField(max_length=50, blank=True, null=True)
    resultmessage = models.CharField(max_length=50, blank=True, null=True)
    extrafields = models.CharField(max_length=50, blank=True, null=True)
    requestamountvalue = models.CharField(max_length=50, blank=True, null=True)
    requestamountcurrency = models.CharField(max_length=50, blank=True, null=True)
    receiveraccountid = models.CharField(max_length=50, blank=True, null=True)
    receiveraccounttype = models.CharField(max_length=50, blank=True, null=True)
    receiverid = models.CharField(max_length=50, blank=True, null=True)
    receiveridtype = models.CharField(max_length=50, blank=True, null=True)
    receivertype = models.CharField(max_length=50, blank=True, null=True)
    receivermsisdn = models.CharField(max_length=50, blank=True, null=True)
    receiverresellerid = models.CharField(max_length=50, blank=True, null=True)
    receiverresellerpath = models.CharField(max_length=50, blank=True, null=True)
    receiverresellertype = models.CharField(max_length=50, blank=True, null=True)
    receiverbalancevaluebefore = models.CharField(max_length=50, blank=True, null=True)
    receiverbalancevalueafter = models.CharField(max_length=50, blank=True, null=True)
    senderid = models.CharField(max_length=50, blank=True, null=True)
    senderidtype = models.CharField(max_length=50, blank=True, null=True)
    sendertype = models.CharField(max_length=50, blank=True, null=True)
    sendermsisdn = models.CharField(max_length=50, blank=True, null=True)
    senderresellerid = models.CharField(max_length=50, blank=True, null=True)
    senderresellerpath = models.CharField(max_length=50, blank=True, null=True)
    senderresellertype = models.CharField(max_length=50, blank=True, null=True)
    senderuserid = models.CharField(max_length=50, blank=True, null=True)
    senderaccountid = models.CharField(max_length=50, blank=True, null=True)
    senderaccounttype = models.CharField(max_length=50, blank=True, null=True)
    senderbalancevaluebefore = models.CharField(max_length=50, blank=True, null=True)
    senderbalancevalueafter = models.CharField(max_length=50, blank=True, null=True)
    receiveraccountstatus = models.CharField(max_length=50, blank=True, null=True)
    receiveraccountlinktypeid = models.CharField(max_length=50, blank=True, null=True)
    receiveraccountclassid = models.CharField(max_length=50, blank=True, null=True)
    receiveramountvalue = models.CharField(max_length=50, blank=True, null=True)
    topuptype = models.CharField(max_length=50, blank=True, null=True)
    resellercommissionamount = models.CharField(max_length=50, blank=True, null=True)
    receiverbonusamount = models.CharField(max_length=50, blank=True, null=True)
    receivercommissionamount = models.CharField(max_length=50, blank=True, null=True)
    bonustype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_evc_transactions'





class Territories(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    territoryname = models.CharField( max_length=2000, blank=True, null=True)  # Field name made lowercase.
    territoryid = models.CharField(max_length=2000, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    altitudemode = models.CharField(db_column='altitudeMode', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tessellate = models.IntegerField(blank=True, null=True)
    extrude = models.IntegerField(blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    draworder = models.IntegerField(db_column='drawOrder', blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(max_length=2000, blank=True, null=True)
    source = models.CharField(db_column='Source', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    descriptio = models.CharField(max_length=2000, blank=True, null=True)
    altitudemo = models.CharField(db_column='altitudeMo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(db_column='COUNTY', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tsc_name = models.CharField(db_column='TSC_Name', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tsc_number = models.FloatField(db_column='TSC_Number', blank=True, null=True)  # Field name made lowercase.
    loc_rel = models.CharField(db_column='Loc_Rel', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    pos_count = models.FloatField(db_column='POS_Count', blank=True, null=True)  # Field name made lowercase.
    circuit_co = models.FloatField(db_column='Circuit_Co', blank=True, null=True)  # Field name made lowercase.
    cell_count = models.FloatField(db_column='Cell_Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territories'





class TblPos(models.Model):
    # id = models.BigAutoField(unique=True)
    pos = models.BigIntegerField(db_column='pos_id',primary_key=True)
    owner_first_name = models.CharField(max_length=255)
    owner_last_name = models.CharField(max_length=255)
    owner_telephone = models.CharField(max_length=20)
    business_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=20, decimal_places=9)
    latitude = models.DecimalField(max_digits=20, decimal_places=9)
    territory=models.ForeignKey(Territories, on_delete=models.CASCADE,default="")

    class Meta:
        managed = False
        db_table = 'tbl_pos'


# class TblPos(models.Model):
#     id = models.BigIntegerField()
#     pos_id = models.BigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'tbl_pos_'


class TblSessions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    access_token = models.CharField(unique=True, max_length=100)
    access_token_expiry = models.DateTimeField()
    refresh_token = models.CharField(unique=True, max_length=100)
    refresh_token_expiry = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_sessions'


class TblTerritories(models.Model):
    id = models.BigAutoField(primary_key=True)
    territoryid = models.BigIntegerField()
    territoryname = models.CharField(max_length=255)
    regionid = models.BigIntegerField()
    regionname = models.CharField(max_length=255)
    county = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_territories'


class TblUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=10, blank=True, null=True)
    is_admin = models.CharField(max_length=10, blank=True, null=True)
    territory =models.ForeignKey(Territories, on_delete=models.CASCADE,default="")
    created_by_user_id = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_users'


class TblTraining(models.Model):
    id = models.BigAutoField(primary_key=True)
    user=models.ForeignKey(TblUsers, on_delete=models.CASCADE,default="")
    pos=models.ForeignKey(TblPos, on_delete=models.CASCADE,default="")
    knowledge_of_service = models.FloatField()
    knowledge_of_selling_products = models.IntegerField()
    have_scratch_card = models.IntegerField()
    have_evd = models.IntegerField()
    data_package = models.IntegerField()
    plug = models.IntegerField()
    x5 = models.IntegerField()
    longitude = models.DecimalField(max_digits=20, decimal_places=9)
    latitude = models.DecimalField(max_digits=20, decimal_places=9)
    distance = models.DecimalField(max_digits=20, decimal_places=9)
    event_date = models.DateTimeField(blank=True, null=True)
    enter_agent_msisdn = models.CharField(max_length=30, blank=True, null=True)
    balance_momo = models.IntegerField(blank=True, null=True)
    momo_number = models.CharField(max_length=30, blank=True, null=True)
    momo_amount = models.CharField(max_length=100, blank=True, null=True)
    did_top_up_evd = models.IntegerField(blank=True, null=True)
    enter_evd_number = models.CharField(max_length=30, blank=True, null=True)
    enter_evd_amount = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_training'




class TblWeekdays(models.Model):
    id = models.BigIntegerField(primary_key=True)
    custom_id = models.BigIntegerField()
    weekday_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_weekdays'




# class Regions(models.Model):
#     geom = models.GeometryField(blank=True, null=True)
#     shape_leng = models.FloatField(blank=True, null=True)
#     shape_area = models.FloatField(blank=True, null=True)
#     adm1_en = models.CharField(max_length=50, blank=True, null=True)
#     adm1_pcode = models.CharField(max_length=50, blank=True, null=True)
#     adm1_ref = models.CharField(max_length=50, blank=True, null=True)
#     adm1alt1en = models.CharField(max_length=50, blank=True, null=True)
#     adm1alt2en = models.CharField(max_length=50, blank=True, null=True)
#     adm0_en = models.CharField(max_length=50, blank=True, null=True)
#     adm0_pcode = models.CharField(max_length=50, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     validon = models.DateField(blank=True, null=True)
#     validto = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'Regions'

# class County(models.Model):
#     geom = models.GeometryField(blank=True, null=True)
#     shape_leng = models.FloatField(blank=True, null=True)
#     shape_area = models.FloatField(blank=True, null=True)
#     adm2_en = models.CharField(max_length=50, blank=True, null=True)
#     adm2_pcode = models.CharField(max_length=50, blank=True, null=True)
#     adm2_ref = models.CharField(max_length=50, blank=True, null=True)
#     adm2alt1en = models.CharField(max_length=50, blank=True, null=True)
#     adm2alt2en = models.CharField(max_length=50, blank=True, null=True)
#     adm1_en = models.CharField(max_length=50, blank=True, null=True)
#     adm1_pcode = models.CharField(max_length=50, blank=True, null=True)
#     adm0_en = models.CharField(max_length=50, blank=True, null=True)
#     adm0_pcode = models.CharField(max_length=50, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     validon = models.DateField(blank=True, null=True)
#     validto = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'county'



# class Training4326(models.Model):
#     id = models.IntegerField(primary_key=True)
#     geom = models.GeometryField(blank=True, null=True)
#     user_id = models.IntegerField(blank=True, null=True)
#     pos_id = models.IntegerField(blank=True, null=True)
#     knowledge_of_service = models.IntegerField(blank=True, null=True)
#     knowledge_of_selling_products = models.IntegerField(blank=True, null=True)
#     have_scratch_card = models.IntegerField(blank=True, null=True)
#     have_evd = models.IntegerField(blank=True, null=True)
#     data_package = models.IntegerField(blank=True, null=True)
#     plug = models.IntegerField(blank=True, null=True)
#     x5 = models.IntegerField(blank=True, null=True)
#     longitude = models.FloatField(blank=True, null=True)
#     latitude = models.FloatField(blank=True, null=True)
#     distance = models.FloatField(blank=True, null=True)
#     event_date = models.CharField(max_length=50, blank=True, null=True)
#     event_date_field = models.DateTimeField(db_column='event_date_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     distince_field = models.CharField(db_column='distince_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     owner_first_name = models.CharField(max_length=50, blank=True, null=True)
#     owner_last_name = models.CharField(max_length=50, blank=True, null=True)
#     owner_telephone = models.IntegerField(blank=True, null=True)
#     business_name = models.CharField(max_length=50, blank=True, null=True)
#     category = models.CharField(max_length=50, blank=True, null=True)
#     status = models.CharField(max_length=50, blank=True, null=True)
#     territory_id = models.IntegerField(blank=True, null=True)
#     knowledge_of_selling_products_field = models.CharField(db_column='knowledge_of_selling_products_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     have_scratch_card_field = models.CharField(db_column='have_scratch_card_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     have_evd_field = models.CharField(db_column='have_evd_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     data_package_field = models.CharField(db_column='data_package_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     plug_field = models.CharField(db_column='plug_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     x5_field = models.CharField(db_column='x5_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
#     user_full_name = models.CharField(max_length=50, blank=True, null=True)
#     user_telephone = models.IntegerField(blank=True, null=True)
#     agent_msisdn = models.CharField(max_length=50, blank=True, null=True)
#     balance_momo = models.IntegerField(blank=True, null=True)
#     momo_amount = models.IntegerField(blank=True, null=True)
#     did_top_up_evd = models.IntegerField(blank=True, null=True)
#     evd_number = models.BigIntegerField(blank=True, null=True)
#     evd_amount = models.FloatField(blank=True, null=True)
    
#     class Meta:
#         managed = True
#         db_table = 'tbl_training'


# class TblTraining(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user_id = models.BigIntegerField()
#     pos_id = models.BigIntegerField()
#     knowledge_of_service = models.FloatField()
#     knowledge_of_selling_products = models.IntegerField()
#     have_scratch_card = models.IntegerField()
#     have_evd = models.IntegerField()
#     data_package = models.IntegerField()
#     plug = models.IntegerField()
#     x5 = models.IntegerField()
#     longitude = models.DecimalField(max_digits=20, decimal_places=9)
#     latitude = models.DecimalField(max_digits=20, decimal_places=9)
#     distance = models.DecimalField(max_digits=20, decimal_places=9)
#     event_date = models.DateTimeField(blank=True, null=True)
#     enter_agent_msisdn = models.CharField(max_length=30, blank=True, null=True)
#     balance_momo = models.IntegerField(blank=True, null=True)
#     momo_number = models.CharField(max_length=30, blank=True, null=True)
#     momo_amount = models.CharField(max_length=100, blank=True, null=True)
#     did_top_up_evd = models.IntegerField(blank=True, null=True)
#     enter_evd_number = models.CharField(max_length=30, blank=True, null=True)
#     enter_evd_amount = models.CharField(max_length=100, blank=True, null=True)
#     geom = models.GeometryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tbl_training'






class RegDist(models.Model):
    geom = models.GeometryField(blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=2000, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    altitudemode = models.CharField(db_column='altitudeMode', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tessellate = models.IntegerField(blank=True, null=True)
    extrude = models.IntegerField(blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    draworder = models.IntegerField(db_column='drawOrder', blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(max_length=2000, blank=True, null=True)
    descriptio = models.CharField(max_length=2000, blank=True, null=True)
    altitudemo = models.CharField(db_column='altitudeMo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    circuit_co = models.FloatField(db_column='Circuit_Co', blank=True, null=True)  # Field name made lowercase.
    pos_count = models.FloatField(db_column='POS_Count', blank=True, null=True)  # Field name made lowercase.
    shape_leng = models.FloatField(db_column='Shape_Leng', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reg_Dist'








        
