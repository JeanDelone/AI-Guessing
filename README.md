# AI vs. Real Image Quiz Webapp

This project is a web-based application designed to quiz users on whether they can distinguish between AI-generated images and real photos. The webapp an image, and users must guess whether it's AI or real. The goal is to collect user responses and analyze which image features and AI models tend to fool users, and which aspects of real photos make users believe they are AI-generated. In order for users to willingfully participate in quizes, there will be added features and mechanics like gamification in the future.

## Features

- **Quiz Interface**: Users are presented with a random image and must choose whether the image is AI-generated or real.
- **Data Storage**: User responses and image metadata are stored in a database for future analysis.
- **Analytics**: The stored data will allow to analyze which photo features, AI models, and other factors impact users' ability to distinguish AI-generated images from real ones.

## Technology Stack

- **Backend**: 
  - [FastAPI](https://fastapi.tiangolo.com/) for building the RESTful API.
  - [SQLAlchemy](https://www.sqlalchemy.org/) for ORM and database management.
  - [SQLite](https://www.sqlite.org/index.html) as the database for storing images, user responses, and metadata.
  
- **Frontend**: 
  - Plain HTML, CSS, and JavaScript for the user interface (currently basic, can be expanded later).
  
- **Database**:
  - Stores image data (AI-generated vs. real), user responses, and additional metadata like AI models, image features, and timestamps.


## TODO

- Display photos that matches user's display ratio. For example to users on phone, display only vertical images
- Add tinder-like mechanic to swipe left or right photos to vote and load next ones instead of clicking a respective vote button
- Make UI somewhat good lol