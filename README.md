# BuildYourOwnClassifier
Big Red Hacks Fall 2017

## Inspiration
I have worked in many projects in the past that I thought could be optimized with machine learning. However for me and most other developers, machine learning has too high of a barrier to entry to effectively use in our projects. Since then I focused on learning the basics of machine learning with scikit-learn and Tensorflow. The biggest challenge in applying machine learning to a project is training the model when you don't have data. There needs to be an easy way to build and train models.

## What it does
We built a web interface for developers to customize, build, and train their own machine learning classifiers. After manually training their models, the users can download them as pickle files to use in their python code without actually writing ML code.

## How I built it
This was built as Node.js/Express.js we application. The machine learning is done through a python script that communicates with the Node server.

## Challenges I ran into
Some challenges were in running Python in a javascript application and required reading into Node.js streams and multithreading. We also had trouble uploading JSON files from the browser and storing them in the server.

## Accomplishments that I'm proud of
The basic foundation is completed but will require a lot more work to fully develop.

## What I learned
Running Python in Node.js presented interesting challenges that I had not seen before. It was a valuable experience. Overall, this project lead me to think about how projects can scale in the long term.

## What's next for BuildYourOwnClassifier
This project is not completed due to lack of time and only two members in the hackathon team. We hope to further develop and deploy this application in the future.
