from django.apps import AppConfig

class MillenniumPanelConfig(AppConfig):
    name = 'millennium.panel'
    label = 'millenniumpanel'
    verbose_name = 'Millennium Panel'

    def ready(self):
        import millennium.panel.signals

default_app_config = 'millennium.panel.MillenniumPanelConfig'
