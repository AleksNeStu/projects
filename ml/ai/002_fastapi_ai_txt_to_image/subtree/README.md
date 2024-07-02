

<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" 
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">FastAPI for Stable Diffusion LLMs Demo</h1>

This repository contains the files to build your very own AI image generation web application! Outlined are the core components of the FastAPI web framework, and application leverage the newly-released Stable Diffusion text-to-image deep learning model.

📺 You can checkout the full video [here](https://www.youtube.com/watch?v=_BZGtifh_gw)!

![Screenshot 2022-12-15 at 11 34 39 AM](https://user-images.githubusercontent.com/37101144/207929696-886ccfe3-6d86-4674-8aca-0844fb795727.png)

![Screenshot 2022-12-15 at 11 35 51 AM](https://user-images.githubusercontent.com/37101144/207929748-afafc036-cbf6-48aa-a7b2-b64d66c32b75.png)

![image-generated.jpg](image-generated.jpg)![image.png]


**Local run example**
```
INFO:     127.0.0.1:59428 - "GET /openapi.json HTTP/1.1" 200 OK
Using device: cpu
100%|██████████| 50/50 [06:08<00:00,  7.37s/it]
INFO:     127.0.0.1:55088 - "GET /generate?prompt=Monkey%20Fish&num_inference_steps=50&guidance_scale=7.5 HTTP/1.1" 200 OK
```