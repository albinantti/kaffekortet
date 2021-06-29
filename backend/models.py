from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class card(models.Model):
    identifier = models.CharField(
        max_length=128,
        verbose_name=_('Unique identifier'),
        help_text=_("Unique identifier for the given card,"
                    " the result of 'blipping' it."),
        unique=True,
    )
    owner = models.CharField(
        max_length=128,
        verbose_name=_("Owner"),
        help_text=_("Who the card belongs to"),
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_("Phone number"),
        help_text=_("Phone number belonging to the card's owner.")
    )
    created = models.DateTimeField(
        verbose_name=_("Creation date"),
        help_text=_("When the card was added."
                    " This value is automatically updated."),
    )
    modified = models.DateTimeField(
        verbose_name=_("Last modified"),
        help_text=_('''When the card was last modified in some way.
         This value is automatically updated.'''),
    )
    valid_subscription = models.BooleanField(
        verbose_name=_("Subscription valid"),
        help_text=_("Whether or not the card has an activate subscription.")
    )
    subscription_end = models.DateTimeField(
        verbose_name=_("Subscription end"),
        help_text=_("When the subscription ends."),
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        ''' On save, update timestamps. '''
        if not self.id:
            self.created = now()
        self.modified = now()
        return super(card, self).save(*args, **kwargs)

    def __str__(self):
        return self.owner + " - " + self.identifier


class uses(models.Model):
    card = models.ForeignKey(
        to="card",
        on_delete=models.CASCADE,
        verbose_name=_("Card identifier"),
        help_text=_("The card used.")
    )
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' Automatically set timestamp. '''
        self.timestamp = now()
        return super(card, self).save(*args, **kwargs)
