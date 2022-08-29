import os


class ServerItem:
    def __init__(self, name, icon) -> None:
        self.name = name
        self.icon = icon


class Servers:
    def __init__(self) -> None:
        path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(path, "flags")
        self.global_servers = [
            ServerItem(name="Kenya", icon=f'{icon_path}\kenya.png'),
            ServerItem(name="Brazil", icon=f'{icon_path}\\brazil-flag.png'),
            ServerItem(name="Korea", icon=f'{icon_path}\south-korea.png'),
            ServerItem(name="United States", icon=f'{icon_path}\\usa.png'),
            ServerItem(name="London", icon=f'{icon_path}\\uk.png'),
            ServerItem(name="South Africa", icon=f'{icon_path}\sa.png'),
            ServerItem(name="Rusia", icon=f'{icon_path}\\rusia.png'),
            ServerItem(name="India", icon=f'{icon_path}\india.png'),
            ServerItem(name="Germany", icon=f'{icon_path}\germany.png'),
            ServerItem(name="Peru", icon=f'{icon_path}\peru.png'),
            ServerItem(name="Egypt", icon=f'{icon_path}\egypt.png'),
            ServerItem(name="Kenya", icon=f'{icon_path}\kenya.png'),
            ServerItem(name="Brazil", icon=f'{icon_path}\\brazil-flag.png'),
            ServerItem(name="Korea", icon=f'{icon_path}\south-korea.png'),
            ServerItem(name="United States", icon=f'{icon_path}\\usa.png'),
            ServerItem(name="London", icon=f'{icon_path}\\uk.png'),
            ServerItem(name="Germany", icon=f'{icon_path}\germany.png'),
            ServerItem(name="Peru", icon=f'{icon_path}\peru.png'),
            ServerItem(name="Egypt", icon=f'{icon_path}\egypt.png'),
        ]
        self.special_servers = [
            ServerItem(name="South Africa", icon=f'{icon_path}\sa.png'),
            ServerItem(name="Rusia", icon=f'{icon_path}\\rusia.png'),
            ServerItem(name="India", icon=f'{icon_path}\india.png'),
            ServerItem(name="Germany", icon=f'{icon_path}\germany.png'),
            ServerItem(name="Peru", icon=f'{icon_path}\peru.png'),
            ServerItem(name="Egypt", icon=f'{icon_path}\egypt.png'),
            ServerItem(name="Kenya", icon=f'{icon_path}\kenya.png'),
            ServerItem(name="Brazil", icon=f'{icon_path}\\brazil-flag.png'),
            ServerItem(name="Korea", icon=f'{icon_path}\south-korea.png'),
            ServerItem(name="United States", icon=f'{icon_path}\\usa.png'),
            ServerItem(name="London", icon=f'{icon_path}\\uk.png'),
            ServerItem(name="Germany", icon=f'{icon_path}\germany.png'),
            ServerItem(name="Peru", icon=f'{icon_path}\peru.png'),
            ServerItem(name="Egypt", icon=f'{icon_path}\egypt.png'),
            ServerItem(name="Kenya", icon=f'{icon_path}\kenya.png'),
            ServerItem(name="Brazil", icon=f'{icon_path}\\brazil-flag.png'),
            ServerItem(name="Korea", icon=f'{icon_path}\south-korea.png'),
            ServerItem(name="United States", icon=f'{icon_path}\\usa.png'),
            ServerItem(name="London", icon=f'{icon_path}\\uk.png'),
        ]

