class: title

# Python the Swiss Army Knife:
## Sourcing, Analyzing, and Reporting Twitter Data Using Python

![PyRVA](pyrva-logo.png)

---

class: logo

# Authors:

| | |
|---|---|
| ![ProfilePic](mike-alfare.jpg) | Mike Alfare |
| ![ProfilePic](brian-cohan.jpg) | Brian Cohan |
| ![ProfilePic](stephen-lowery.png) | Stephen Lowery |
| ![ProfilePic](chris-may.jpg) | Chris May |

---

class: title

## Python is a unique language. It is powerful enough to used in places like NASA, Wall Street, and the Large Hadron Collider to do things like render the first image of a black hole and discover new particles.

## Yet it's syntax is simple enough that it is used in elementary schools to teach students to program.

## This imbalance of readability and power is one aspect that is contributing to python's rise in popularity. But how can that be, after all, Python is not as fast as C. It is not in all the same environments that JavaScript is in. It's too big to fit on board most embedded chips.

## And yet it beat out C developers in creating an online platform (YouTube). People are bringing it to the browser it's getting put on development boards (Circuit Playground Express).

---

class: title

# Why is this?

---

class: title

> Python is not the best language at doing any one thing. 
> But the moment you want to do more than one thing, Python quickly rises to the top.

<cite>~ Glyph Lefkowitz</cite>

---

class: title

The python ecosystem is large, and it gives anyone the ability to download software that can empower your project
to capture data, analyze and graph it, and deploy it to a web server, without having to change languages.

It is this attribute of python that we'd like to show you today.

---

# We're going to show you how to accomplish several different tasks, all from within python

--
* Get data from Twitter

--
* Produce a simple bar chart

--
* Use Streamlit to produce charts and graphics

--
* Use Podium to produce these slides

---

class: title

# Get data from Twitter

---

# Placeholder

---

class: title

# Produce a simple bar chart

---

# Placeholder

---
class: title

![streamlit logo](streamlit-logo.png)
# [Streamlit](https://www.streamlit.io/)

Open-source app framework for creating beautiful, performant apps in pure Python.

On June 16, 2020, Streamlit announced a [$21M Series A Investment](https://medium.com/streamlit/announcing-streamlits-21m-series-a-ae05daa6c885)

---

# Streamlit in a Nutshell

Streamlit will run your app from top to bottom like a python script

Work with any Python libraries you'd like

Easily add interactive widgets using only Python

Use `@st.cache` decorator to cache expensive functions

Easily deploy to [Streamlit for Teams](https://www.streamlit.io/for-teams) (beta) or other providers like [Heroku](https://pyrva-rvatech.herokuapp.com/)

---

# Graph PyRVA Attendance History - Code

```python
import altair, pandas, requests, streamlit

url = 'https://api.meetup.com/PyRVAUserGroup/events'
response = requests.get(url, params={'status': 'past'})
df = pandas.DataFrame(response.json())

streamlit.write(df)
streamlit.altair_chart(
    altair.Chart(df).mark_line().encode(
        x=altair.X('local_date:T', title='Date'),
        y=altair.Y('yes_rsvp_count:Q', title='RSVPs'),
    ),
    use_container_width=True
)
```

---

# Graph PyRVA Attendance History - Results

`streamlit run src/pyrva_talk/streamlit/pyrva-attendance.py`

![pyrva attendance](pyrva-attendance.png)

---

# Streamlit Works Well With The Following and More!

.left-column[

**Data Analysis / Machine Learning**

* Numpy
* Pandas
* Keras
* TensorFlow
* Scikit Learn
* OpenCV
]
.right-column[

**Visualization**

* Altair
* Bokeh
* matplotlib
* Seaborn
* Deck.GL
* Plotly
]

---

# Interactive Widgets!

.left-column[
![widgets](widgets1.png)
]
.right-column[
![widgets](widgets2.png)
]

---

# Streamlit Caching

.left-column[
```python
def bar(y):
  time.sleep(1)
  return y

@st.cache
def foo(x):
  time.sleep(1)
  return bar(x)

foo(1)
```
]
.right-column[

Streamlit will check 

* The input parameters that you called the function with
* The value of any external variable used in the function
* The body of the function
* The body of any function used inside the cached function 
]

---

# Deploy
```
web: sh setup.sh && streamlit run path/to/app.py
```

.left-column[

To deploy to Heroku, you need three files:

* Your application 
  * May be multiple files
* `Procfile` (above)
* `setup.sh` (right)

]
.right-column[
```
mkdir -p ~/.streamlit/

echo "[general]\nemail = author@example.com" > ~/.streamlit/credentials.toml

echo "[server]\nheadless = true\nenableCORS=false\nport = $PORT\n" > ~/.streamlit/config.toml
```
]

---

class: title

# Use Podium to produce these slides

---

# Placeholder

---

# Resources:

* PyRVA: https://www.pyrva.org/
* GitHub: https://www.github.com/pyrva/rvatech-2020-07-21/
* Streamlit app: https://pyrva-rvatech.herokuapp.com/
