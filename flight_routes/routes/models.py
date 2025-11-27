from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    def __lt__(self, other):
        # Compare airports by their code for heapq
        return self.code < other.code

class Route(models.Model):
    DIRECTION_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]
    
    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departing_routes')
    to_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arriving_routes')
    direction = models.CharField(max_length=5, choices=DIRECTION_CHOICES)
    duration = models.IntegerField(help_text="Duration in minutes")
    position = models.IntegerField(help_text="Order/position in route")
    
    # class Meta:
    #     unique_together = ['from_airport', 'to_airport', 'direction']
    
    def __str__(self):
        return f"{self.from_airport.code} -> {self.to_airport.code} ({self.direction}) - {self.duration}min"