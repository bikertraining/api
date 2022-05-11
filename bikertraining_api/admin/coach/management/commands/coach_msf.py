from datetime import date

from django.core.mail import send_mail
from django.core.management import base
from django.template import loader

from admin.coach import serializers
from utils import worker


class Command(base.BaseCommand):
    help = 'Coach: MSF Expiration Notification'

    def handle(self, *args, **options):
        serializer = serializers.MsfExpirationSerializer(data={})

        if serializer.is_valid():
            serializer.save()

            current_month = date.today().strftime('%m')
            current_year = date.today().strftime('%Y')

            for item in serializer.instance:
                msf_month = item.date_to.strftime('%m')
                msf_year = item.date_to.strftime('%Y')

                months = int(msf_month) - int(current_month) + (12 * (int(msf_year) - int(current_year)))

                if months >= 6:
                    self.stdout.write(f"Coach: {item.name} is current.")
                elif 6 > months >= 0:
                    # Send email
                    html_message = loader.render_to_string(
                        'coach/expiring.html',
                        {
                            'month': months,
                            'name': item.name
                        }
                    )

                    # Email coach
                    send_mail(
                        from_email='noreply@bikertraining.net',
                        recipient_list=[
                            item.email
                        ],
                        subject='MSF Certification Expiring Soon',
                        html_message=html_message,
                        message=None
                    )

                    self.stdout.write(f"Coach: {item.name} is going to expire soon.")
                elif months <= 0:
                    # Send email
                    html_message = loader.render_to_string(
                        'coach/expired.html',
                        {
                            'name': item.name
                        }
                    )

                    # Email coach
                    send_mail(
                        from_email='noreply@bikertraining.net',
                        recipient_list=[
                            item.email
                        ],
                        subject='MSF Certification has Expired',
                        html_message=html_message,
                        message=None
                    )

                    self.stdout.write(f"Coach: {item.name} has expired.")
        else:
            self.stdout.write(worker.error_to_human_readable(serializer.errors))
