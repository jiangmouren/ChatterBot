from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    A Django management command for calling a
    chat bot's training method.
    """

    help = 'Trains the database used by the chat bot'
    can_import_settings = True

    def handle(self, *args, **options):
        from chatterbot import ChatBot
        from chatterbot.ext.django_chatterbot import settings
        from chatterbot.trainers import ChatterBotCorpusTrainer

        chatterbot = ChatBot(**settings.CHATTERBOT)

        trainer = ChatterBotCorpusTrainer(chatterbot)

        trainer.train(*settings.CHATTERBOT['training_data'])

        # Django 1.8 does not define SUCCESS
        if hasattr(self.style, 'SUCCESS'):
            style = self.style.SUCCESS
        else:
            style = self.style.NOTICE

        self.stdout.write(style('Starting training...'))
        training_class = trainer.__class__.__name__
        self.stdout.write(style('ChatterBot trained using "%s"' % training_class))