import configparser

class ThemeManager:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.load_config()
        self.themes = {
            'default': {
                'bg': '#f0f0f0',
                'button_bg': '#e1e1e1',
                'button_fg': '#000000',
                'button_active_bg': '#d1d1d1',
                'button_active_fg': '#000000',
                'entry_bg': '#ffffff',
                'entry_fg': '#000000'
            },
            'dark': {
                'bg': '#2c2c2c',
                'button_bg': '#3c3c3c',
                'button_fg': '#ffffff',
                'button_active_bg': '#4c4c4c',
                'button_active_fg': '#ffffff',
                'entry_bg': '#1c1c1c',
                'entry_fg': '#ffffff'
            },
            'light': {
                'bg': '#ffffff',
                'button_bg': '#f0f0f0',
                'button_fg': '#000000',
                'button_active_bg': '#e0e0e0',
                'button_active_fg': '#000000',
                'entry_bg': '#ffffff',
                'entry_fg': '#000000'
            },
            'blue': {
                'bg': '#e6f2ff',
                'button_bg': '#b3d9ff',
                'button_fg': '#000000',
                'button_active_bg': '#80bfff',
                'button_active_fg': '#000000',
                'entry_bg': '#ffffff',
                'entry_fg': '#000000'
            }
        }
        self.current_theme = self.config.get('Theme', 'current', fallback='default')

    def load_config(self):
        self.config.read(self.config_file)
        if not self.config.has_section('Theme'):
            self.config.add_section('Theme')
            self.config.set('Theme', 'current', 'default')
            self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def get_current_theme(self):
        return self.themes[self.current_theme]

    def next_theme(self):
        themes = list(self.themes.keys())
        current_index = themes.index(self.current_theme)
        next_index = (current_index + 1) % len(themes)
        self.current_theme = themes[next_index]
        self.config.set('Theme', 'current', self.current_theme)
        self.save_config()
