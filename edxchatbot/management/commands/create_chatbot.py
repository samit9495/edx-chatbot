from django.core.management.base import BaseCommand
from edxchatbot.models import CourseChatbot

log = getLogger(__name__)

class Command(BaseCommand):
    help = """
    This command creates chatbot for a given course

    example:
        manage.py ... create_chatbot -n chatbotname -c edX/Open_DemoX/edx_demo_course -u livechatboturl
    """
    
    def add_arguments(self, parser):
        parser.add_argument('-n', '--name',
                            metavar='CHATBOT_NAME',
                            help='Chatbotname',
                            required=True)
        parser.add_argument('-c', '--course',
                            metavar='COURSE_ID',
                            help='Course ID',
                            required=True)
        parser.add_argument('-u', '--url',
                            metavar='CHATBOT_URL',
                            help='Chatbot URL',
                            required=True)

    def handle(self, *args, **options):
        course_chatbot = CourseChatbot.objects.create(
                             chatbot_name = options['name'],
                             course_id = options['course_id'],
                             chatbot_url = options['url']
                                   )
        course_chatbot.save()
        log.info("Chatbot created")


        
