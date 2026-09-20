import flet as ft
import icons as ic
import colors as cor
import measures as mea
import frontend.main_page as mainPG

import asyncio

class Home:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page_top()
        self.bottom_area()

    async def animation_button(self, pg_update = None, e = None):
        if pg_update is not None and e is not None:
            eve = e.control
            eve.scale = 0.76
            pg_update.update()
            await asyncio.sleep(0.2)
            eve.scale = 1
            pg_update.update()

    def page_top(self):
        async def animacao_bt(e):
            await self.animation_button(self.page, e)

        self.altura_theDOG = (self.page.width * 3/9) - 16
        self.dog_img = ft.Image(
            top = 8, right = 28,
            src = 'imgs/the_dog.png',
            height = self.page.width * 3/9 - 12
        )
        self.text_balance = ft.Column(
            spacing = 0,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            controls = [
                ft.Text(
                    value = 'Caixa de Hoje', font_family = 'wix',
                    size = mea.size_Text, color = cor.lilas_suave_BRANCO,
                    weight = ft.FontWeight.W_500
                ),
                
                ft.Text(
                    value = 'R$ 1.000,00', font_family = 'wix',
                    size = mea.size_TEXT / (4 / 7),
                    color = cor.lilas_suave_BRANCO,
                    weight = ft.FontWeight.W_600
                ),
            ],
            margin = ft.Margin(
                top = mea.heihgt_NavBar/3,
                left = mea.heihgt_NavBar/3
            ),
        )
        self.wallet_movements = ft.Container(
            border_radius = mea.radius,
            alignment = ft.Alignment.CENTER,
            height = ((self.page.height * 2/5)/3) * 4/5,
            bgcolor = ft.Colors.with_opacity(color = cor.lilas_suave_BRANCO, opacity = 0.2),
            margin = ft.Margin(left = mea.heihgt_NavBar/3, right = mea.heihgt_NavBar/3),

            content = ft.Row(
                spacing = 0,
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    ft.Container(
                        expand = 1,
                        bgcolor = cor.transparente,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            expand = True,
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.START,
                            controls = [
                                ft.Row(
                                    spacing = mea.margins,
                                    alignment = ft.MainAxisAlignment.START,
                                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                    controls = [
                                        ft.Text(
                                            value = 'Ganhos',
                                            size = mea.size_Text,
                                            font_family = 'wix',
                                            color = cor.lilas_suave_BRANCO,
                                            weight = ft.FontWeight.W_500
                                        ),

                                        ic.svg_icon(
                                            icon = 'arrow_up',
                                            size = mea.icons,
                                            color = cor.green
                                        ),
                                    ]
                                ),

                                ft.Text(
                                    value = 'R$ 1.090,00',
                                    size = mea.size_TEXT,
                                    font_family = 'wix',
                                    color = cor.lilas_suave_BRANCO,
                                    weight = ft.FontWeight.W_600
                                ),
                            ]
                        ),
                        margin = ft.Margin(
                            left = mea.heihgt_NavBar/5,
                            right = mea.heihgt_NavBar/10
                        )
                    ),
                    
                    ft.Container(
                        expand = 1,
                        bgcolor = cor.transparente,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            expand = True,
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.START,
                            controls = [
                                ft.Row(
                                    spacing = mea.margins,
                                    alignment = ft.MainAxisAlignment.START,
                                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                    controls = [
                                        ft.Text(
                                            value = 'Despesas',
                                            size = mea.size_Text,
                                            font_family = 'wix',
                                            color = cor.lilas_suave_BRANCO,
                                            weight = ft.FontWeight.W_500
                                        ),

                                        ic.svg_icon(
                                            icon = 'arrow_down',
                                            size = mea.icons,
                                            color = cor.red
                                        ),
                                    ]
                                ),

                                ft.Text(
                                    value = 'R$ 90,00',
                                    size = mea.size_TEXT,
                                    font_family = 'wix',
                                    color = cor.lilas_suave_BRANCO,
                                    weight = ft.FontWeight.W_600
                                ),
                            ]
                        ),
                        margin = ft.Margin(
                            left = mea.heihgt_NavBar/10,
                            right = mea.heihgt_NavBar/5
                        )
                    )
                ]
            )
        )
        def shortcuts_buttons(title = None, icon = None, action = True):
            if title and icon and action:
                return ft.Column(
                    expand = 1,
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        ft.Container(
                            width = ((self.page.height * 3/5)/3) * 2/5,
                            height = ((self.page.height * 3/5)/3) * 2/5,
                            border_radius = (((self.page.height * 2/5)/3) * 3/5)/2,
                            alignment = ft.Alignment.CENTER,
                            bgcolor = cor.lilas_suave_BRANCO,
                            content = ic.svg_icon(
                                icon = icon,
                                size = mea.icons,
                                color = cor.lilas_escuro
                            ),
                            on_click = animacao_bt,
                            ink = True, ink_color = cor.lilas_natural,
                            animate_scale = ft.Animation(curve = ft.AnimationCurve.EASE_IN_OUT, duration = 300)
                        ),

                        ft.Text(
                            value = title,
                            size = mea.size_text,
                            color = cor.lilas_suave_BRANCO,
                            font_family = 'wix', weight = ft.FontWeight.W_500
                        )
                    ]
                )
            
        self.shortcut_area = ft.Row(
            expand = True,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                shortcuts_buttons(title = 'Financeiro', icon = 'money_bag'),
                ft.Column(
                    expand = 2,
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.MainAxisAlignment.CENTER,
                    controls = [
                        ft.Container(
                            height = ((self.page.height * 3/5)/3) * 2/5,
                            border_radius = (((self.page.height * 2/5)/3) * 3/5)/2,
                            alignment = ft.Alignment.CENTER,
                            bgcolor = cor.lilas_suave_BRANCO,
                            content = ft.Icon(
                                icon = ft.CupertinoIcons.SCISSORS_ALT,
                                size = mea.icons,
                                color = cor.lilas_escuro
                            ),
                            on_click = animacao_bt,
                            ink = True, ink_color = cor.lilas_natural,
                            animate_scale = ft.Animation(curve = ft.AnimationCurve.EASE_IN_OUT, duration = 300)
                        ),

                        ft.Text(
                            value = 'Registrar Atendimento',
                            size = mea.size_text,
                            color = cor.lilas_suave_BRANCO,
                            font_family = 'wix', weight = ft.FontWeight.W_500
                        )
                    ]
                ),
                shortcuts_buttons(title = 'Ajustes', icon = 'settings'),
            ],
            margin = ft.Margin(left = mea.heihgt_NavBar/3, right = mea.heihgt_NavBar/3),
        )
        self.banner = ft.Container(
            left = 0,
            right = 0,
            bottom = 0,
            height = self.page.height * 2/5,
            gradient = ft.LinearGradient(
                begin = ft.Alignment.TOP_LEFT,
                end = ft.Alignment.BOTTOM_RIGHT,
                colors = [cor.lilas_escuro, cor.lilas_natural]
            ),
            border_radius = mea.heihgt_NavBar/2,
            margin = ft.Margin(left = mea.margins, right = mea.margins),

            content = ft.Stack(
                expand = True,
                controls = [
                    ft.Image(
                        expand = True,
                        src = 'imgs/bg_banner.png',
                        fit = ft.BoxFit.COVER,
                        top = 0, left = 0, right = 0, bottom = 0
                    ),
                    ft.Column(
                        expand = True,
                        alignment = ft.MainAxisAlignment.START,
                        horizontal_alignment = ft.CrossAxisAlignment.START,
                        controls = [
                            self.text_balance,
                            self.wallet_movements,
                            self.shortcut_area
                        ],
                        top = 0, left = 0, right = 0, bottom = 0
                    )
                ]
            )
        )
        self.icon_company = ft.Container(
            bgcolor = cor.lilas_escuro,
            width = mea.heihgt_NavBar,
            height = mea.heihgt_NavBar,
            border_radius = ft.BorderRadius(
                mea.heihgt_NavBar/2,
                mea.heihgt_NavBar/2,
                mea.heihgt_NavBar/2,
                mea.heihgt_NavBar/2
            ),
            alignment = ft.Alignment.CENTER,
            content = ic.svg_icon(
                icon = 'company',
                size = mea.icons,
                color = cor.lilas_suave_BRANCO
            ),
            margin = ft.Margin(left = mea.margins),
            ink = True, ink_color = cor.lilas_natural,
            animate_scale = ft.Animation(curve = ft.AnimationCurve.EASE_IN_OUT, duration = 300)
        )
        self.title_company = ft.Column(
            spacing = 0,
            height = mea.heihgt_NavBar,
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            controls = [
                ft.Text(
                    value = 'Barros',
                    style = ft.TextStyle(
                        size = 56,
                        height = 0.9,
                        color = cor.color_fonts,
                        font_family = 'tangerine',
                    ),
                ),
                
                ft.Text(
                    value = 'barbearia',
                    style = ft.TextStyle(
                        size = 18,
                        height = 1,
                        font_family = 'julius',
                        color = cor.color_fonts,
                        weight = ft.FontWeight.W_500
                    ),
                )
            ]
        )
        self.adm_company = ft.Row(
            left = 0,
            spacing = mea.margins,
            top = (self.altura_theDOG - mea.heihgt_NavBar)/2,
            height = mea.heihgt_NavBar,
            width = self.page.width - self.altura_theDOG,
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                self.icon_company,
                self.title_company,
            ]
        )

        self.juncao_top = ft.Stack(
            width = self.page.width,
            height = (self.page.height * 2/5 + self.page.width * 3/9) - 16,
            controls = [
                self.banner,
                self.dog_img,
                self.adm_company
            ]
        )

        self.icon_company.on_click = animacao_bt
    def bottom_area(self):
        self.title = ft.Row(
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Text(
                    value = 'Importantes', font_family = 'wix',
                    size = mea.size_TEXT, color = cor.lilas_escuro,
                    margin = ft.Margin(top = 12, left = mea.margins, bottom = 6),
                    weight = ft.FontWeight.W_500
                )
            ]
        )

        self.avisos = ft.Container(
            height = 108,
            expand = True,
            border_radius = mea.radius,
            bgcolor = cor.top_fundo_BRANCO,
            margin = ft.Margin(left = mea.margins, right = mea.margins)
        )
    
    def build_HOME(self):
        self.estrutura_HOME = ft.Column(
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                self.juncao_top,
                self.title,
                *[self.avisos for x in range(1, 4)],
                ft.Column(height = 164)
            ]
        )

        return self.estrutura_HOME