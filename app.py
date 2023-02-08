import tkinter as tk
import customtkinter as ctk

from PIL import Image, ImageTk

from authtoken import auth_token

import torch
from torch import autocast

from diffusers import StableDiffusionPipeline

# create the app
app = tk.Tk()
app.geometry("532*622")
app.title("Stable Diffusion App")
ctk.set_appearance_mode("dark")

# input text box
prompt = ctk.CTkEntry(height= 40, width = 512, text_font = ("Arial", 20), text_color = "black", fg_color = "white")
prompt.place(x = 10, y = 10)

# place holder for output image
lmain = ctk.CTkLabel(height = 512, width = 512)
lmain.place(x = 10, y = 110)

# specify model name
model_id = "CompVis/stable-diffusion-v1-4"

# create the pipeline
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision = "fp16", torch_dtypes = torch.float16, use_auth_token = auth_token)

# send this pipe to gPU
device = "cuda"
pipe.to(device)



def generate():
    pass

# button to generate image
trigger = ctk.CTkButton(text = "Generate", height = 40, width = 512, text_font = ("Arial", 20), text_color = "white", fg_color = "blue",  command=generate)
trigger.configure(text="Generate")
trigger.place(x=206, y = 60)

app.mainloop()

