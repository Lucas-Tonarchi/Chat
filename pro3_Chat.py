#                              Flet library
import flet as ft          

def main(page):
    
    title = ft.Text("Calling")
    
    def broadcast_bridge(message):
        chat.controls.append(ft.Text(message))
        page.update()
                                                
    page.pubsub.subscribe(broadcast_bridge) # creates communication tunnel 
    
    welcome = ft.Text("Bem vindo ao Calling")  
    username = ft.TextField(label="Seu Nome... ")

    def send_message(event):
        text = f"{username.value}: {text_report.value}"
        page.pubsub.send_all(text) 
        text_report.value = ""
        page.update()
    
    text_report = ft.TextField(label="Digite algo...", on_submit=send_message)
    send_button = ft.ElevatedButton("Enviar", on_click=send_message)   
    
    chat = ft.Column()                                             

    chat_line = ft.Row([text_report, send_button])    
    
    def enter_chat(event):
        page.remove(title)
        page.remove(start_button) 
        alert.open = False   
        page.add(chat)
        page.add(chat_line)

        gotIn_chat = f"{username.value} entrou no chat"
        page.pubsub.send_all(gotIn_chat)
        page.update()
    
    enter_button = ft.ElevatedButton("Entrar no chat", on_click=enter_chat)
    alert = ft.AlertDialog(title=welcome, content=username, actions=[enter_button])

    def appear(event):                                        
        page.dialog = alert
        alert.open = True
        page.update()
   
    start_button = ft.ElevatedButton("Iniciar Chat", on_click=appear)

    page.add(title)
    page.add(start_button)    

ft.app(main, view=ft.WEB_BROWSER)
# To stop the execution of the program, press Ctrl+C at the end of the terminal text!