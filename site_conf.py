import os


class SiteConfig:
    home = os.path.abspath("./").replace("\\", "/")
site_config = SiteConfig()
