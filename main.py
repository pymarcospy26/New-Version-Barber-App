import flet as ft
import colors as cor
import shares as shay
import frontend.main_page as mainPG
from frontend.pages import home as hm

class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.expand = True
        self.page.bgcolor = cor.lilas_suave_BRANCO

        self.page.fonts = {
            'wix': 'fonts/wix.ttf',
            'julius': 'fonts/julius.ttf',
            'tangerine': 'fonts/tangerine.ttf',
        }

        self.page.theme = ft.Theme(
            system_overlay_style = ft.SystemOverlayStyle(
                status_bar_icon_brightness = ft.Brightness.DARK,
                status_bar_brightness = ft.Brightness.DARK,
                status_bar_color = cor.transparente,

                system_navigation_bar_icon_brightness = ft.Brightness.DARK,
                system_navigation_bar_color = cor.transparente
            )
        )

        self.tela_HOME = hm.Home(page).build_HOME()
        shay.telas['HOME'] = self.tela_HOME

        self.page.add(mainPG.Main_PAGE(self.page).page_ADM(control_now = self.tela_HOME))

def run(page: ft.Page):
    Main(page)

ft.run(main = run, assets_dir = 'assets',  view = ft.AppView.WEB_BROWSER, host = '0.0.0.0')

