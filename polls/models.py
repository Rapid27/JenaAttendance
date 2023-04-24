from django.db import models
from datetime import datetime



class Employee(models.Model):

    name = models.CharField(max_length= 255)
    surname = models.CharField(max_length = 255)
    pub_date = models.DateTimeField('Date created' , auto_now = True)
    
    class department(models.TextChoices):
        mining = "Mining"
        engineering = "Engineering"
        admin = "Adminstration"
        
    Department = models.CharField(max_length=20,
                                  choices = department.choices,
                                  default = department.mining
                                  )
    phone_number = models.IntegerField(default=222,) 
    mine_number = models.IntegerField(default = 222,)
   
    
    class Meta:
        db_table = 'Employee'
        
    def __str__(self):
        return self.name
    
class FingerprintIdentity(models.Model):
    received_value = models.IntegerField(default=0 , editable=False)
    Jena_Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    Reg_Date = models.DateTimeField('Date registered', auto_now_add= True)
    entry_time = models.TimeField('Time of entry' , blank=True , null= True)
    exit_time = models.TimeField('Time of Exit' , blank=True , null = True)
    
    def update_entry_time(self):
        now1 = datetime.now()
        now_str = now1.strftime("%H:%M:%S")
        self.entry_time = now_str
        
    
    def update_exit_time(self):
        now2 = datetime.now()
        now2_str = now2.strftime("%H:%M:%S")
        self.exit_time = now2_str
        
        
    def reset_exit_time(self):
        self.exit_time = None
        
    class Meta:
        db_table = 'FingerprintIdentity'
        
    def __str__(self):
        return self.Jena_Employee.name
    
class DailyAttendance(models.Model): #this is an automatically created model which is created every 24hours starting at 6am
    
    daily_attendee = models.ManyToManyField(FingerprintIdentity, blank=True)
    
    date_created = models.DateTimeField('Entry Date ', auto_now_add = True)
    
    
    def __str__(self):
        date_string = str(self.date_created)
        return date_string
        