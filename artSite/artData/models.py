from django.db import models

class CustomerModel(models.Model):
   # customer_id = models.IntegerField()
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()
    preferred_style = models.CharField(max_length = 50)
    preferred_medium = models.CharField(max_length = 50)
    phone_num = models.CharField(max_length = 25)
    artist_id = models.IntegerField()

class ArtWorkModel(models.Model):
    title = models.CharField(max_length = 100)
    year = models.IntegerField()
    style = models.CharField(max_length = 50)
    medium = models.CharField(max_length = 50)
    #type = models.CharField(max_length=50)
    asking_price = models.DecimalField(max_digits=8, decimal_places=2)
    artist_id = models.IntegerField()
    collector_id = models.IntegerField()

class ArtistModel(models.Model):
    artist_id = models.IntegerField()
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()
    age = models.IntegerField()
    art_medium = models.CharField(max_length = 50)
    art_style = models.CharField(max_length = 50)
    art_type = models.CharField(max_length = 50)

class CollectorModel(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    #collector_id = models.IntegerField()
    collection_type = models.CharField(max_length = 50)
    collection_style = models.CharField(max_length = 50)
    collection_medium = models.CharField(max_length = 50)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()
    phone_num = models.CharField(max_length = 50)
    artist_id_id = models.IntegerField()

class ArtShowModel(models.Model):
    show_name = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()

class RentModel(models.Model):
   invoice_num = models.IntegerField()
   start_date = models.DateField()
   return_date = models.DateField()
   duration = models.IntegerField()
   rent_fee = models.DecimalField(max_digits=8, decimal_places=2)
   artist_percentage = models.IntegerField()
   renter_id = models.IntegerField()

class SaleModel(models.Model):
   sale_date = models.DateField()
   invoice_num = models.IntegerField()
   sale_price = models.DecimalField(max_digits=8, decimal_places=2)
   artist_percentage = models.IntegerField()
   buyer_id = models.IntegerField()

class RenterModel(models.Model):
    renter_id = models.IntegerField()
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()
    phone_num = models.CharField(max_length = 25)
    num_rents = models.IntegerField()

class BuyerModel(models.Model):
    buyer_id = models.IntegerField()
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()
    phone_num = models.CharField(max_length = 25)
    num_purchase = models.IntegerField()

class query1(models.Model):
    show_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    count = models.IntegerField()

class query2(models.Model):
    avg_cost_to_buy = models.DecimalField(max_digits = 10, decimal_places=2)

class query3(models.Model):
    buyer_id = models.IntegerField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()

class query4(models.Model):
    title = models.CharField(max_length = 50)
    artist_id = models.IntegerField()

class query5(models.Model):
    buyer_id = models.IntegerField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_num = models.IntegerField()

class query6(models.Model):
    buyer_id = models.IntegerField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)


class DisplayedModel(models.Model):
    show_name = models.ForeignKey(ArtShowModel, on_delete=models.CASCADE, null=True, blank=True)
    # art_title = models.ForeignKey(ArtWorkModel, on_delete=models.CASCADE, null=True, blank=True)
    # artist_id_display = models.ForeignKey(ArtWorkModel, on_delete=models.CASCADE, null=True, blank=True)
class RentedModel(models.Model):
    # invoice_num_rent = models.ForeignKey(RentModel, on_delete=models.CASCADE, null=True, blank=True)
    title_rent = models.ForeignKey(ArtWorkModel, on_delete=models.CASCADE, null=True, blank=True,)
    # artist_id_rent = models.ForeignKey(ArtWorkModel, on_delete=models.CASCADE, null=True, blank=True)
class SoldModel(models.Model):
    # invoice_num_sale = models.ForeignKey(SaleModel, on_delete=models.CASCADE, null=True, blank=True)
    # title_sold = models.ForeignKey(ArtWorkModel, on_delete=models.CASCADE, null=True, blank=True)
    artist_id_sold = models.ForeignKey(ArtWorkModel, on_delete=models.CASCADE, null=True, blank=True)





