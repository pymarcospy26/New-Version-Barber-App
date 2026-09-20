import flet as ft
import colors as cor
import measures as mea
import icons as ic
import asyncio

class Main_PAGE:
    def __init__(self, page: ft.Page):
        self.page = page
        self.navegation_bar()

    async def animation_button(self, pg_update = None, e = None):
        if pg_update is not None and e is not None:
            eve = e.control
            eve.scale = 0.76
            pg_update.update()
            await asyncio.sleep(0.2)
            eve.scale = 1
            pg_update.update()

    def navegation_bar(self):
        async def clicks_btn_NavBar(e):
            for x in self.button_bakground.content.controls:
                x.bgcolor = cor.transparente
                x.content.color = cor.lilas_suave_BRANCO

            eve = e.control
            eve.bgcolor = cor.lilas_suave_BRANCO
            eve.content.color = cor.lilas_escuro
            await self.animation_button(self.button_bakground, e)

            self.button_bakground.update()

        def buttons_NavBar(icon = None, page = True):
            if icon is not None and page is not None:
                return ft.Container(
                    width = mea.heihgt_NavBar - (2 * mea.margins),
                    height = mea.heihgt_NavBar - (2 * mea.margins),
                    margin = ft.Margin(top = mea.margins, bottom = mea.margins),
                    border_radius = (mea.heihgt_NavBar - (2 * mea.margins))/2,
                    alignment = ft.Alignment.CENTER, content = icon,
                    bgcolor = cor.transparente, ink = True, ink_color = cor.lilas_suave_BRANCO,
                    on_click = clicks_btn_NavBar,

                    animate_scale = ft.Animation(curve = ft.AnimationCurve.EASE_IN_OUT, duration = 300)
                )
            
        self.button_bakground = ft.Container(
            expand = True,
            height = mea.heihgt_NavBar,
            bgcolor = cor.lilas_escuro,
            border_radius = mea.heihgt_NavBar/2,

            left = mea.margins_NavBar,
            right = mea.margins_NavBar,
            bottom = mea.margins_NavBar + 10,

            content = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,
                margin = ft.Margin(left = mea.margins, right = mea.margins),
                controls = [
                    buttons_NavBar(
                        icon = ic.svg_icon(
                            icon = 'home',
                            size = mea.icons,
                            color = cor.lilas_suave_BRANCO
                        )
                    ),

                    buttons_NavBar(
                        icon = ic.svg_icon(
                            icon = 'agenda',
                            size = mea.icons,
                            color = cor.lilas_suave_BRANCO
                        )
                    ),

                    buttons_NavBar(
                        icon = ic.svg_icon(
                            icon = 'chart',
                            size = mea.icons,
                            color = cor.lilas_suave_BRANCO
                        )
                    ),

                    buttons_NavBar(
                        icon = ic.svg_icon(
                            icon = 'menu',
                            size = mea.icons,
                            color = cor.lilas_suave_BRANCO
                        )
                    )
                ]
            )
        )

        self.button_bakground.content.controls[0].bgcolor = cor.lilas_suave_BRANCO
        self.button_bakground.content.controls[0].content.color = cor.lilas_escuro

    def page_ADM(self, control_now = None):
        self.estrutura_page = ft.Column(
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [control_now]
        )
        
        self.safe = ft.SafeArea(
            content = self.estrutura_page
        )

        self.layout = ft.Stack(
            expand = True,
            controls = [
                self.safe,
                self.button_bakground
            ]
        )

        return self.layout