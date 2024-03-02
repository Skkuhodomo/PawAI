# PawAI 🐕 🐾

**PawAI (ResNet50)**: Designed to identify your pet's breed, this model is recommended for cases where you are unsure about your pet's breed.


**GPT-Vision (Prompt-Tuning)**: The GPT-Vision module has been fine-tuned with prompt-tuning capabilities. By uploading your pet's image, GPT will analyze both your pet's overall condition and accurately determine its breed.
## Cat vs Dog classifier

### ResNet50
: Residual Neural Network. I used pretrained model, ResNet50 for indenfifying pet's breed. 

<details>
<summary>Click for More Info</summary>
  
### PlainNet(Left) &rightarrow; ResNet(Right)
<div align = "center">
<img src="http://incredible.ai/assets/images/resnet_plain.png", width="35%", height="35%"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/ResBlock.png", width="50%", height="50%"/>
</div>

**"Is learning better networks as easy as stacking more layers?"**


ResNet was prompted by a pivotal question: does incorporating more layers consistently lead to superior models? PainNet's primary aim was to minimize H(x). However, this proves to be challenging when the value of x is not fixed and can be altered in models. Researchers posit that addressing this challenge becomes feasible when x is intricately linked to the output, expressed as F(x) + x. Consequently, in this context, H(x) is represented as F(x) + x. To minimize H(x), the emphasis shifts to ensuring that F(x) = -x. This underlying concept forms the essence of ResNet. Despite the dynamic nature of x in both models, ResNet redefines the role of F(x) to align with x. This shift in focus significantly enhances accuracy. 

[References](https://arxiv.org/pdf/1409.1556.pdf)

### Process of learning(ResNet50)
![preview](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*-JY0Nx8HXlNyJNijEyCWUg.jpeg)
https://jisuhan.tistory.com/71
<br/>
</details>

Data is from Tensorflow dataset.[Data resource](https://www.tensorflow.org/datasets/catalog/cats_vs_dogs)


## GPT-VISION
With **Langchain🦜⛓️** you can load openAI model. 

I modified a GPT prompt so that it can be a **veterinarian** who can identify the breed and condition of pets through images.

[OpenAI](https://platform.openai.com/docs/guides/vision)
![class-diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/Skkuhodomo/PawAI/main/diagram/langchain-gpt-vision.puml) 

## To Get Started 

Download Source code 
```
  git clone https://github.com/Skkuhodomo/PawAI.git
```
</pre>

Install library
```
  pip install -r requirements.txt
```
Run
```
  streamlit run main.py
```

## Examples: 
<div>
<img src="images/2.png" width="30%" height="30%"/>
<img src="images/3.png" width="30%" height="30%"/>
<img src="images/4.png" width="30%" height="30%"/>
</div>
