import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, RoundedRectangle


Window.size = (1000,650)



# DATA

ingredients_menu = {
	"Shrimp":["Fried Shrimp","Grilled Shrimp"],
	"Chicken":["Fried Chicken","Roasted Chicken"],
	"Pork":["Grilled Pork","Stir Fried Pork"],
	"Egg":["Omelette","Fried Egg"]
}

all_food = [
	"Arepas",
	"Japanese Curry",
	"Fried Chicken",
	"Koshari",
	"Tonkatsu",
	"Sushi",
	"Ramen",
	"Okonomiyaki",
	"Pizza"
]

food_images = {
	"Arepas": "images/Arepas.jpg",
	"Japanese Curry": "images/Japanese Curry.webp",
	"Fried Chicken": "images/Fried Chicken.webp",
	"Koshari": "images/Koshari.jpg",
	"Okonomiyaki": "images/Okonomiyaki.jpg",
	"Sushi": "images/Sushi.webp",
	"Ramen": "images/Ramen.webp",
	"Tonkatsu": "images/Tonkatsu.webp",
	"Pizza": "images/pizza.jpg"
}


# ROUND BUTTON

class RoundButton(Button):
	def __init__(self,color=(1,0.6,0.2,1), **kwargs):
		super().__init__(**kwargs)

		self.background_normal=""
		self.background_color=(0,0,0,0)
		self.color=(1,1,1,1)

		with self.canvas.before:

			Color(*color)

			self.rect=RoundedRectangle(
				pos=self.pos,
				size=self.size,
				radius=[30]
			)

		self.bind(pos=self.update)
		self.bind(size=self.update)

	def update(self,*args):
		self.rect.pos=self.pos
		self.rect.size=self.size


# BACKGROUND

class Background(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		with self.canvas.before:
			self.bg=Rectangle(
				source="images/bg.png",
				pos=self.pos,
				size=Window.size
			)

		self.bind(pos=self.update_bg)
		self.bind(size=self.update_bg)

	def update_bg(self,*args):
		self.bg.pos=self.pos
		self.bg.size=self.size



# CARD

class Card(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		with self.canvas.before:
			Color(1,1,1,1)
			self.rect=RoundedRectangle(
				pos=self.pos,
				size=self.size,
				radius=[25]
			)
		self.bind(pos=self.update)
		self.bind(size=self.update)

	def update(self,*args):
		self.rect.pos=self.pos
		self.rect.size=self.size


# HOME

class HomeScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		root=Background()
		container=BoxLayout(
			padding=[200,120],
		)

		card=Card(
			orientation="vertical",
			spacing=40,
			padding=60,
			size_hint=(1,1)
		)

		title=Label(
			text="Random Food Picker",
			font_size=42,
			color=(0,0,0,1)
		)

		btn_food=RoundButton(
			text="Random Food",
			size_hint=(None,None),
			size=(280,80),
			pos_hint={"center_x":0.5},
			color=(1,0.5,0.2,1)
		)

		btn_ing=RoundButton(
			text="Random Ingredient",
			size_hint=(None,None),
			size=(280,80),
			pos_hint={"center_x":0.5},
			color=(0.2,0.6,1,1)
		)

		btn_food.bind(on_press=lambda x:setattr(self.manager,"current","random"))
		btn_ing.bind(on_press=lambda x:setattr(self.manager,"current","ingredient"))

		card.add_widget(title)
		card.add_widget(btn_food)
		card.add_widget(btn_ing)

		container.add_widget(card)
		root.add_widget(container)

		self.add_widget(root)



# RANDOM FOOD

class RandomFood(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		root=Background(orientation="vertical")

		top=BoxLayout(
			size_hint=(1,None),
			height=70,
			padding=[20,10]
		)

		top.add_widget(Label())

		btn_list=RoundButton(
			text="List Menu",
			size_hint=(None,None),
			size=(160,50),
			color=(0.4,0.7,1,1)
		)

		btn_list.bind(on_press=lambda x:setattr(self.manager,"current","list"))

		top.add_widget(btn_list)

		layout=BoxLayout(
			orientation="horizontal",
			spacing=60,
			padding=[80,40]
		)

		title=Label(
			text="Random Food",
			font_size=40,
			size_hint=(1,None),
			height=60,
			color=(0,0,0,1)
		)

		self.food_image=Image(
			source="food.png",
			size_hint=(0.65,1)
		)

		right=BoxLayout(
			orientation="vertical",
			spacing=25,
			padding=[40,10,40,200],  #ซ้าย ล่าง ขวา บน
			size_hint=(0.45,1)
		)

		result_box = BoxLayout(
			size_hint=(1,None),
			height=120,
			padding=10,
		)

		with result_box.canvas.before:
			Color(1,1,1,1)
			self.result_bg = RoundedRectangle(radius=[15])

		def update_result_bg(*args):
			self.result_bg.pos = result_box.pos
			self.result_bg.size = result_box.size

		result_box.bind(pos=update_result_bg, size=update_result_bg)

		self.result = Label(
			text="Press Random",
			font_size=40,
			color=(0,0,0,1)
		)

		result_box.add_widget(self.result)

		buttons=BoxLayout(
			orientation="vertical",
			spacing=20,
			size_hint=(1,None),
			height=150
		)

		btn_random=RoundButton(
			text="Random",
			size_hint=(None,None),
			size=(260,70),
			pos_hint={"center_x":0.5},
			color=(1,0.5,0.2,1)
		)

		btn_home=RoundButton(
			text="Home",
			size_hint=(None,None),
			size=(200,60),
			pos_hint={"center_x":0.5},
			color=(0.5,0.5,0.5,1)
		)

		btn_random.bind(on_press=self.start_animation)
		btn_home.bind(on_press=lambda x:setattr(self.manager,"current","home"))

		buttons.add_widget(btn_random)
		buttons.add_widget(btn_home)

		right.add_widget(title)
		right.add_widget(result_box)
		right.add_widget(buttons)

		layout.add_widget(self.food_image)
		layout.add_widget(right)

		root.add_widget(top)
		root.add_widget(layout)

		self.add_widget(root)

	def start_animation(self,instance):
		self.count=0
		Clock.schedule_interval(self.animate,0.1)

	def animate(self,dt):
		food=random.choice(all_food)
		self.result.text=food
		if food in food_images:
			self.food_image.source = food_images[food]
			self.food_image.reload()
		self.count += 1

		if self.count > 15:
			Clock.unschedule(self.animate)
			food = random.choice(all_food)
			self.result.text = food

		if food in food_images:
			self.food_image.source = food_images[food]
			self.food_image.reload()



# INGREDIENT
class IngredientScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		root=Background(
			orientation="vertical",
			padding=[200,100],
			spacing=40
		)

		title=Label(
			text="Choose Ingredient",
			font_size=36,
			color=(0,0,0,1)
		)

		result_box = BoxLayout(
			size_hint=(1,None),
			height=100,
			padding=10
		)

		with result_box.canvas.before:
			Color(1,1,1,1)
			self.result_bg = RoundedRectangle(radius=[15])

			Color(0,0,0,0) #สีพื้นกล่องขาว
			self.result_border = RoundedRectangle(radius=[15])

		def update_result_bg(*args):
			self.result_bg.pos = result_box.pos
			self.result_bg.size = result_box.size

			self.result_border.pos = result_box.pos
			self.result_border.size = result_box.size

		result_box.bind(pos=update_result_bg, size=update_result_bg)

		self.result = Label(
			text="",
			font_size=32,
			color=(0,0,0,1)
		)

		result_box.add_widget(self.result)

		grid=GridLayout(
			cols=2,
			spacing=30,
			size_hint=(1,None),
			height=180
		)

		colors=[
		(1,0.4,0.4,1),
		(0.4,0.8,0.4,1),
		(0.4,0.6,1,1),
		(1,0.7,0.3,1)
		]

		i=0

		for ing in ingredients_menu:
			btn=RoundButton(
				text=ing,
				size_hint=(1,None),
				height=70,
				color=colors[i]
			)

			btn.bind(on_press=self.random_menu)
			grid.add_widget(btn)
			i+=1

		btn_home=RoundButton(
			text="Home",
			size_hint=(None,None),
			size=(200,60),
			pos_hint={"center_x":0.5},
			color=(0.6,0.6,0.6,1)
		)

		btn_home.bind(on_press=lambda x:setattr(self.manager,"current","home"))

		root.add_widget(title)
		root.add_widget(result_box)
		root.add_widget(grid)
		root.add_widget(btn_home)

		self.add_widget(root)

	def random_menu(self,instance):
		self.current_ing = instance.text
		self.count = 0

		Clock.schedule_interval(self.animate_ing,0.1)

	def animate_ing(self,dt):
		menu = random.choice(ingredients_menu[self.current_ing])
		self.result.text = menu
		self.count += 1

		if self.count > 15:
			Clock.unschedule(self.animate_ing)
			menu = random.choice(ingredients_menu[self.current_ing])
			self.result.text = menu

# LIST MENU

class ListMenu(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		root=Background()
		container = BoxLayout(
			padding=[200,120]
		)

		card = Card(
			orientation="vertical",
			spacing=15,
			padding=40
		)

		title=Label(
			text="Menu List",
			font_size=36,
			color=(0,0,0,1)
		)

		card.add_widget(title)

		for food in all_food:
			card.add_widget(Label(
				text=food,
				color=(0,0,0,1),
				font_size=24
			))

		btn=RoundButton(
			text="Back",
			size_hint=(None,None),
            		size=(200,60),
            		pos_hint={"center_x":0.5},
            		color=(0.5,0.5,0.5,1)
        	)
		btn.bind(on_press=lambda x:setattr(self.manager,"current","random"))
		card.add_widget(btn)
		self.add_widget(root)
		container.add_widget(card)
		root.add_widget(container)


# APP

class RandomFoodApp(App):
	def build(self):
		sm=ScreenManager()
		sm.add_widget(HomeScreen(name="home"))
		sm.add_widget(RandomFood(name="random"))
		sm.add_widget(IngredientScreen(name="ingredient"))
		sm.add_widget(ListMenu(name="list"))

		return sm

RandomFoodApp().run()