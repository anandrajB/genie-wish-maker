from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRectangleFlatButton , MDFlatButton
from kivymd.font_definitions import theme_font_styles
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog








class ScfApp(MDApp):

    screen = Screen()


    def close_dialog(self,obj):
        self.dialog.dismiss()


    def show_data(self,obj):
        if self.username.text is None :
            check_string = "Please enter username"
        else:
            close = MDFlatButton(text = 'close' , on_release = self.close_dialog)
            self.dialog = MDDialog(text=f'Welcome {self.username.text}!' , buttons = [close])
            self.dialog.open()

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        # self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        # label = MDLabel(
        #     text="hello", 
        #     halign="center",
        #     theme_text_color="Custom",
        #     text_color=(0, 1, 0, 1),
        #     font_style="Subtitle1",
        # )
        # icon_label = MDIcon(icon="language-python", halign="center")
        btn_flat = MDRectangleFlatButton(text="SUBMIT",  pos_hint={"center_x": 0.5, "center_y": 0.4} ,
                    on_release = self.show_data )
        self.username  = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(btn_flat)
        return screen


ScfApp().run()
