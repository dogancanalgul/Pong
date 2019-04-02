import kivy

kivy.require("1.0.6")


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.graphics import Ellipse
from kivy.graphics import Rectangle

class Screen(Widget):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
    def on_touch_down(self, touch):
       with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)
        touch.ud["ellipse"] = Ellipse(Rectangle(pos=(10, 10), size=(500, 500)))
        with self.canvas:
            Ellipse(pos=(touch.x - 15, touch.y - 15), size = (30,30))

class Pong(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    Pong().run()