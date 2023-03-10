from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineIconListItem , MDList , IconLeftWidget
from kivymd.uix.scrollview import ScrollView
from kivy.lang import Builder
from helpers import INBOX_HELPER


# class ScfApp(MDApp):

   
#     def build(self):
#         screen = Screen()

#         scroller = ScrollView()
#         main_list_views = MDList()
#         scroller.add_widget(main_list_views)

#         for i in range(1,20):
#             icon = IconLeftWidget(icon = 'language-python')
#             items = OneLineIconListItem(text=f'item {i}')
#             items.add_widget(icon)
#             main_list_views.add_widget(items)

#         screen.add_widget(scroller)
#         return screen


# ScfApp().run()



class ScfApp(MDApp):

   
    def build(self):
        screen = Builder.load_file(INBOX_HELPER)
        return screen


ScfApp().run()