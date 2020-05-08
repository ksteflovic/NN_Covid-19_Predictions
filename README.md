# NEURAL NETWORK for COVID-19
  > **Note:** This repository is written in *slovak* language.

### *What is Covid 19?*

Coronavirus disease (**COVID-19**) is an *infectious disease* caused by a newly discovered coronavirus.
Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.

### *How does it spreads?*

The virus that causes *COVID-19* is mainly transmitted through **droplets** generated when an infected person coughs, sneezes, or exhales. These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces.

You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19, or by touching a contaminated surface and then your *eyes*, *nose* or *mouth*.

  > The virus caused a big pandemia, which started in China, in whe end of the year 2019. In the beggining of 2020 COVID-19 started spreading the whole world rapidly fast. See the map below.
  
![world](docs/images/COVID-19-outbreak-timeline.gif)
<p align="right"><sup><strong>Image <a href="https://commons.wikimedia.org/wiki/File:COVID-19-outbreak-timeline.gif" target="_blank">source</a>.</strong></sup></p>

### How to protect yourself?
- *wash* your *hands* often 👏🧼
- maintain a *safe distance* from anyone who is *coughing* or *sneezing* 🤧
- wear *face mask* in public 😷
- stay *home* if you feel unwell 🤒

### Positive cases



### Or...
Help flatten the Coronavirus curve by self-isolating!

![spreading](docs/images/Covid-19-curves-graphic2-stopthespread-v2.gif)

Think twice, do you really need to go outside?

![transmission](docs/images/Covid-19-Transmission-graphic-01.gif)  

### Famous quotes „“
---
  <img align="right" src="docs/images/people/trump.jpg" width="80px" height="80px">

  > *"And then I see the disinfectant where it knocks it out in a minute. One minute. And is there a way we can do something like that, by injection inside or almost a cleaning? So it'd be interesting to check that."*
  
  > **Donald J. Trump,** ***24.4.2020***
  
  <p align="right"><sup><strong>Image <a href="https://dribbble.com/shots/5567286-US-President-Donald-Trump-vector-portrait" target="_blank">source</a>.</strong></sup></p>

 ---
 <img align="right" src="docs/images/people/bolsonaro.png" width="90px" height="90px">

  > *"So what? What do you want me to do? My name's Messiah but I can't work miracles."*
  
  > **Jair Messias Bolsonaro,** ***29.4.2020***
  
  <br>
  <p align="right"><sup><strong>Image <a href="https://www.shutterstock.com/image-vector/west-nusa-tenggara-indonesia-april-09-1698476086" target="_blank">source</a>.</strong></sup></p>
  
---
  <img align="right" src="docs/images/people/babis.png" width="90px" height="80px">

  > *"Zítra jdou děti do školy. Bylo by dobré, aby se učitelé zeptali, nebo spolužáci, jestli někdo ze spolužáků nebyl, i když u dětí samozřejmě ten výskyt není, ale v každém případě aby se zeptali, jestli nebyli na prázdninách v těch oblastech, které jsou vlastně nakaženy, a samozřejmě ten virus se šíří z Itálie. V Itálii to nezvládli..."*
  
  > **Andrej Babiš,** ***1.3.2020***
  
  <p align="right"><sup><strong>Image <a href="https://www.shutterstock.com/image-vector/andrej-czech-entrepreneur-businessman-politician-vector-746499280" target="_blank">source</a>.</strong></sup></p>
  
---
<img align="right" src="docs/images/people/johnson.jpg" width="78px" height="90px">

  > *"I shook hands with everybody."*
  
  > **Boris Johnson,** ***3.3.2020***
  
  <br>
  <p align="right"><sup><strong>Image <a href="https://www.dreamstime.com/march-secretary-state-foreign-commonwealth-affairs-boris-johnson-editorial-use-march-secretary-state-image112524424" target="_blank">source</a>.</strong></sup></p>

---


### Interesting websites 🌐
- Coronavirus Map -> https://covid19.health/

---
# About this repository

This work represents **Jupyter python project** to predict the spread of COVID19 per given country for the next days.

### Folder structure
<pre><code>📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/data">data</a>
 └──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/data/models">models</a> - contains <em>.csv</em> datasets
     ├──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/data/models/by-days">by-days</a> - used for data visualization
     ├──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/data/models/c19-week-1">c19-week-1</a> - <em>not used</em>
     ├──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/data/models/c19-week-4">c19-week-4</a> - used for <em>neural network</em>
     ├──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/data/models/c19-week-5">c19-week-5</a> - newest data, but <em>not used</em>
     └──📃README.md
📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/docs">docs</a>
 ├──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/docs/custom">custom</a>
 │   └──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/docs/custom/conavirus_disease_presentation.pptx">coronavirus_disease_presentation.pptx</a> - main powerpoint <strong>presentaton</strong>
 └──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/docs/images">images</a> - contains images for README files
📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src">src</a>
 ├──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks">notebooks</a>
 │   ├──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks/neural_network">neural_network</a>
 │   │   ├──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks/neural_network/__init__.py">__init__.py</a>
 │   │   └──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks/neural_network/notebook_covid-19.ipynb">notebook_covid-19.ipynb</a> - <strong>Neural network for Covid-19 predictions</strong>
 │   └──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/visualization">visualization</a>
 │       ├──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks/visualization/__init__.py">__init__.py</a>
 │       ├──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks/visualization/data_curve_visualization.ipynb">data_curve_visualization.ipynb</a>
 │       ├──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks/visualization/data_visualization_europe.ipynb">data_visualization_europe.ipynb</a>
 │       └──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/notebooks/visualization/map_visualization.ipynb">map_visualization.ipynb</a>
 └──📁<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/python">python</a>
     └──📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/src/python/country_utils.py">country_utils.py</a>
📃<a href="https://github.com/pajka-js/Steflovicova_NS2019/tree/master/.gitignore">.gitignore</a> - nothing important
📃README.md - file you are reading right now
</code></pre>

## Working with data




![world](docs/images/covid_world.jpeg)

**Keep strong, world! Stay safe.**
