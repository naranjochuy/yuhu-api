from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    description = models.TextField(verbose_name="Description")
    email = models.EmailField(max_length=50, verbose_name="Email")
    expiration_date = models.DateField("Expiration Date")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return (
            f"<{self.__class__.__name__} id={self.id} title={self.title}>"
        )

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} id={self.id} title={self.title}>"
        )
