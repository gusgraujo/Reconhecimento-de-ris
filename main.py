from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color , Ellipse,Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.factory import Factory



from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

from kivy.uix.image import AsyncImage

from plyer import filechooser
from kivy.properties import ListProperty
from kivy.uix.button import Button



import json
from user import Usuario


usuarios = []
file =''


class Menu(Screen):
    def on_pre_enter(self):
        Window.bind(on_request_close = self.confirmacao)

    def confirmacao(self,*args,**kwargs):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10,spacing=10)

        pop = Popup(title='Deseja mesmo sair?',content=box,size_hint=(None,None),
                    size=(150,150))

        sim = Botao(text='Sim',on_release=App.get_running_app().stop)
        nao = Botao(text='Não',on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        box.add_widget(botoes)
        
        animText = Animation(color=(0,0,0,1))+ Animation(color = (1,1,1,1))
        animText.repeat = True
        animText.start(sim)
        anim = Animation(size =(300,180),duration = 0.2,t='out_back')
        anim.start(pop)
        pop.open()

        return True


class Botao(ButtonBehavior,Label):

    cor = ListProperty([0.4,0.5,0.7,1])
    cor2 = ListProperty([0.5,0.5,0.1,1])
    def __init__(self,**kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self,*args):
        self.atualizar()
    def on_press(self, *args):
        self.cor,self.cor2 = self.cor2 , self.cor

    def on_release(self,*args):
        self.cor = self.cor2
    def on_cor(self,*args):
        self.atualizar()

    def atualizar(self,*args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba =self.cor)
            Ellipse(size = (self.height, self.height),pos=self.pos)
            Ellipse(size = (self.height,self.height),pos = (self.x+self.width-self.height,self.y))
            Rectangle(size = (self.width -self.height , self.height), pos = (self.x+self.height/2.0,self.y) )



class Cadastro(Screen):
    def __init__(self,**kwargs):
        #chama construtor do grid layout
        super(Cadastro,self).__init__(**kwargs)

        
    
       
        #layout

        grid_layout = GridLayout(rows = 10 ,cols = 2,spacing = 2,row_force_default = True, row_default_height = 70, padding =20)
        
        self.add_widget(CanvasWidget())

        self.add_widget(grid_layout)
        #widgets
        # 1st row
        grid_layout.add_widget(Label(text = 'Cadastro de Dados ',color = [.56,.229,.229,1]))
        grid_layout.add_widget(Label(text = 'Nome:'))
        self.nome = TextInput(multiline = True,height = 30)  
        grid_layout.add_widget(self.nome)  
        # 2st row
        grid_layout.add_widget(Label(text = 'Idade:'))
        self.idade = TextInput(multiline = True,height = 30)  
        grid_layout.add_widget(self.idade)   
        # 3st row
        grid_layout.add_widget(Label(text = 'Dia de registro:'))
        self.data = TextInput(multiline = True,height = 30)  
        grid_layout.add_widget(self.data)   
        # 4st row
        button = Botao(text ='Cadastrar')
        button.bind(on_press=self.cadPessoa,on_release =self.clear_txt )
        grid_layout.add_widget(button) 

        buttonFile = Botao(text ='Arquivo Iris')
        buttonFile.bind(on_press=self.telaFile)
        grid_layout.add_widget(buttonFile) 
        
        

    def cadPessoa(self,*args,**kwargs):
        getId = len(usuarios) +1
        new_user = Usuario(getId,self.nome.text,self.idade.text,self.data.text,None)
        app_program.screen_manager.current = 'menu'
        try:
            usuarios.append(new_user)
            print(usuarios)
            
            
        except:
            
            print("An exception occurred")

    def telaFile(self,*args,**kwargs):
        app_program.screen_manager.current = 'arquivo'

    def clear_txt(self, instance):
        self.nome.text = ''
        self.idade.text = ''
        self.data.text = ''

        

        

    

class CanvasWidget(Widget):
      
    def __init__(self, **kwargs):
  
        super(CanvasWidget, self).__init__(**kwargs)
  
        # Arranging Canvas
        with self.canvas:
  
            Color(.163 ,.176, .159 , 1)  # set the colour 
  
            # Seting the size and position of canvas
            self.rect = Rectangle(pos = self.center,
                                  size =(self.width / 2.,
                                        self.height / 2.))
  
            # Update the canvas as the screen size change
            self.bind(pos = self.update_rect,
                  size = self.update_rect)
  
    # update function which makes the canvas adjustable.
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

        

class Arquivo(Widget):
    selection = ListProperty([])

   

    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)

    def choose_d(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.choose_dir(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection
        #print(str(selection))

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        self.b_t.ii = self.selection[0]
         
class Test(App):
    def build(self):
        # We are going to use screen manager, so we can add multiple screens
        # and switch between them
        self.screen_manager = ScreenManager()


        
        self.menu_page = Menu()
        screen = Screen(name='menu')
        screen.add_widget(self.menu_page)
        self.screen_manager.add_widget(screen)

        # Initial, connection screen (we use passed in name to activate screen)
        # First create a page, then a new screen, add page to screen and screen to screen manager
        self.cadastro_page = Cadastro()
        screen = Screen(name='cadastro')
        screen.add_widget(self.cadastro_page)
        self.screen_manager.add_widget(screen)


        self.file_page = Arquivo()
        screen = Screen(name='arquivo')
        screen.add_widget(self.file_page)
        self.screen_manager.add_widget(screen)

       

        return self.screen_manager


if __name__ == "__main__":
    app_program = Test()
    app_program.run()


