from datetime import datetime

from rest_framework.renderers import BrowsableAPIRenderer


class BrowsableAPIRendererWithoutForms(BrowsableAPIRenderer):
    """Renders the browsable api, but excludes the forms."""

    def get_context(self, *args, **kwargs):
        ctx = super().get_context(*args, **kwargs)

        ctx['display_edit_forms'] = False

        return ctx

    def show_form_for_method(self, view, method, request, obj):
        """We never want to do this! So just return False."""
        return False

    def get_rendered_html_form(self, data, view, method, request):
        """Why render _any_ forms at all. This method should return
        rendered HTML, so let's simply return an empty string.
        """
        return ""


def format_date(date_from, date_to):
    """
    Formats the starting/ending dates

    :param str date_from: Start Date
    :param str date_to: End Date

    :return: str
    """

    start_date = datetime.strptime(str(date_from), "%Y-%m-%d")

    end_date = datetime.strptime(str(date_to), "%Y-%m-%d")

    if str(start_date) == str(end_date):
        return '%s, %s' % (
            start_date.strftime('%B %d'),
            end_date.strftime('%Y')
        )
    elif str(start_date.strftime('%m')) > str(end_date.strftime('%m')):
        return '%s - %s' % (
            start_date.strftime('%B %d, %Y'),
            end_date.strftime('%B %d, %Y')
        )
    elif str(start_date.strftime('%d')) > str(end_date.strftime('%d')):
        return '%s - %s' % (
            start_date.strftime('%B %d'),
            end_date.strftime('%B %d, %Y')
        )
    else:
        return '%s - %s' % (
            start_date.strftime('%B %d'),
            end_date.strftime('%d, %Y')
        )


def format_xpl(xpl):
    """
    Formats the students experience

    :param str xpl: Experience

    :return: str
    """

    if xpl == 'none':
        return 'None'
    elif xpl == 'some':
        return 'Some but a long time ago'
    elif xpl == '1_6':
        return '1 to 6 months'
    elif xpl == '6_12':
        return '6 to 12 months'
    elif xpl == 'more':
        return 'More than one year'
    elif xpl == 'dirt':
        return 'Dirt bike only'
    else:
        return 'Unknown'
