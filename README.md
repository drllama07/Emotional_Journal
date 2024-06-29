# Emotional_Journal

A minimalistic Python app for tracking 12 emotions (personally chosen) and using historical data stored in the database to generate an image based on the last 28 days.

## Technologies Used in This Project
- [Tkinter]
- [SQLAlchemy]
- [Pillow]
- [NumPy]

## Features of This App

The Tkinter library allows us to design a simple, single-paged app. The app depicts the 12 main emotions and their scales (to rate the intensity of the emotion from 0 to 10). Each emotion has an assigned color shown on a widget, and with the intensity of each emotion, we create a monthly (28 days) image of the stored daily entries. Additionally, there is a widget that shows the average color of the last 3 days and labels it as calculated momentum.

## Role of Each Library in This App

As mentioned earlier, Tkinter is the GUI library and the frontend of the project. On the backend side, SQLAlchemy and SQLite are the database components because they are easy to use and better fit for a small project like this. NumPy is used to manipulate large arrays efficiently, and after processing the arrays, we use Pillow to create an image to visualize the historical data for the user.

## How to Use This App

The number of daily entries is limited to one. If you do not have enough entries for the monthly (28 days) image, the app will give you an error stating that, and this also applies to multiple daily entries. If you want to test the app with random data, there is a dedicated file (`test.py`) for generating a custom number of entries.

## Installation

To use this app, you need Python set up on your local machine, and you have to install the mentioned libraries as well.

Install the required libraries:

'pip install tkinter sqlalchemy pillow numpy'

## Extra Notes
The main concept of this project came from one of my good friends, so if you like the idea, you can thank her.

My main goal with this project was to get started with databases and a bit of object-oriented programming.

The app itself is just a conceptual demo, so in the future I might add more features to it or even design a real-world application.
