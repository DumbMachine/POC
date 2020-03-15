![img](download.jpeg)



Mentors:

- Carlos Fernandez

Ratin Kumar
Email: [ratin.kumar.2k@gmail.com](mailto:ratin.kumar.2k@gmail.com)  
Phone: +91-9896225424

## Index

1. [Introduction](#introduction)
2. [Synopsis](#synopsis)
3. [Project Goals](#project-goals)
4. [Timeline](#timeline)
5. [Deliverables](#deliverables)
6. [References](#references)

## Introduction


## Personal Information
|           |                                                              |
| --------- | ------------------------------------------------------------ |
| Full Name | Ratin Kumar                                                  |
| Institute | 2nd Year B.Tech StudentComputer Science and EngineeringNational Institute of Technology Kurukshetra |
| Email     | [ratin.kumar.2k@gmail.com](mailto:ratin.kumar.2k@gmail.com)[ratin_11822004@nitkkr.ac.in](mailto:ratin_11822004@nitkkr.ac.in) |
| Phone     | +91-9896225424                                               |
| Blog      | [https://medium.com/@ratin.kumar.2k](https://medium.com/@ratin.kumar.2k) |
| Github    | [https://github.com/DumbMachine](https://github.com/DumbMachine) |
| Skype     | RatinKumar                                                   |
| IRC Nick  | DumbMachine (Freenode)                                       |
| Timezone  | Indian Standard Time (GMT +0530)                             |
| Address   | 317, Abhimanyu Bhavan Hostel-6, NIT campus,National Institute of Technology Kurukshetra, Kurukshetra, Haryana, India 136119 |
## About Me
I am Ratin Kumar, a 2nd-year undergraduate Computer Engineering student at National Institute of Technology Kurukshetra. I have good experience of using Python and Javascript for creating applications or just some hacky scripts to get things done. I really enjoy coding all the time, because of which I have numerous small projects on my Github.


Riding cycle, stalking stock market trends and competitive FPS games are some of my interests outside of the world of programming.


### Open Source
I am part of many organizations on Github and have made multiple minor and a few major contributions. I love the spirit of Open Source, promoting universal access to code, and thus have become the part of this amazing community. Being a part of the Open Source group at my College, I have organized workshops on GIT and using Machine Learning for Image Captioning and continually help colleagues.


### Skills
* Good knowledge of using Python and some knowledge of the internals of Python.
* Knowledge of Data Science.
* Good background in Mathematics; Calculus and Linear Algebra.
* Comfortable with using GIT or any other similar service.

Project `redacted`**

## Abstract

The field of Artificial Intelligence is helping advancement of many fields. AI is relevant to any intellectual task. Modern artificial intelligence techniques are pervasive and are too numerous to list here. Some of the prominent examples range from `something `autonomous vehicles to life saving by helping in medical diagnosis. Apart from the aforementioned serious, AI is used in entertainment industry whether it maybe using AI to create articles or create deepfakes. The world has also seen AI being used to detect the wrongs in our society, like fake news and also to detect the wrongs by AI itself (eg deepfakes).

At the heart of most AI solutions lies requirement of **labeled data**. The lack of  labeled data makes impossible for the algorithm to learn the regularities and patterns in data. Labeling data, manually, is cumbersome and time consuming. AI solutions can be divided in two categories:

- Totally new
- Derivative of something 

Project `redacted` aims at providing a platform to simplify and speedup the process of data labeling by making use of automation tools and pre-trained machine learning models. This project will provide a simple gui to users for annotating data required by various machine learning tasks (computer vision based, nlp based or audio based) and make use of pre-trained models and some techniques (mentioned in implementation details section)  to allow automation of annotation to as far extent as possible. The gui will be supported by a `python` backend responsible for all preprocessing/recommendation for annotation and also storage of annotations received by the frontend.

## Background

CCExtractor, initially a small project, has now embedded itself firmly into large corporations and prestigious universities where it is used for many educational feats. This project will help fuel the fire of AI boom. It will introduce a tool to all the machine learning practitioners, which will allow them to annotate data a lot faster than before.

## Motivation

World of Artificial Intelligence has made big leaps in providing humans the power to find patterns in data. It will be the basis of most of the automation in the coming century, to keep this field expanding it requires data. Data, in its raw form, is available readily. This data accompanied with the right tool, which should focus on automatic and fast annotation, will improve efficiency of practitioners. Reduction of time spent annotating data implies increase in the time spent on finding solutions of real world problems.

## Project `redacted`

To accomplish this project's aims, a simple gui and a powerful backend which learns from past annotations are required. The gui will be simple and only expose those functions that are required and allow for usage of keyboard shortcuts to allow for reaching peak of efficiency of the manual annotators. The accompanying backend will actively learn from the annotations to suggest the annotations to users passively. This passive suggestion for manual annotators will mean no amount will be spend on annotation for correct suggestion and ignoring the suggestion, if wrong hence being a **passive suggestion**. Currently the benefits that will served from this project can be condensed to:

- Increase in speed and efficiency of manual annotators.
- Increase the amount of annotated data, as annotation tasks' difficulty and time investment decreases.
- Any more points?

`redacted` will allow institutes, professional or any interested party to annotate data fast and easily, leaving the party with more time for implementation of solution.

## Why do I want to Build `redacted`?

#### Why `redacted`?

Make the world more productive.

#### Why CCExtractor?

Mentor gave me the opportunity.



## Proposed Deliverables for GSOC

1. A simple react-based frontend, allowing for ingestion of the following:

   1. Computer-Vision based datasets for:

      - Image/Video Classification
      - Image Key points
      - Object Detection
      - Instance Segmentation
      - Action Recognition
      - Video Segmentation

   2. Natural-Language Processing based datasets for:

      - Classification

      - Named Entity Recognition

      - QnA

      - Machine Translation

      - Sentiment Analysis (sentiment slider)

      - Custom tasks ( like transliteration )

   3. Audio based datasets for:

      - Audio Transcription
      - Audio Segmentation
      - Audio Classification

2. A robust backend which will take care of:

   - Send data for annotation to frontend
   - Saving annotations received from frontend 
   - Export annotations to format allowing for ingestion from AutoML things, Detectron2 and Tensorflow Object Detection API and Our custom thing.
   - An active learning model, which will improve with each annotation and also provide suggestions for annotations.
   - Maintain metrics

3. Tests and Continuous Integration tools.

4. Detailed documentation; for users as well as developers.

5. Fortnightly blogs on developmental advances and milestones.

6. Setting the ground for a Model Zoo things, to allow ingestion of Annotations and train models. Possible integration with Rekognition.

## Brief Tentative Working

Brief show of the workflow

## Detailed Working And Implementation

![image-20200315061224704](image-20200315061224704.png)

The project can be divided into the following components:

- **React based frontend**: The frontend webapp, will be the component most users see and use. 
- **Python based backend**: The server responsible for providing data to react app and taking annotation data from it. The iterative learning model, which will give real time suggestions of annotations, will also be backend's responsiblity. To increase the modularity of backend's components, the following division is recommended:
  - **Docker Container**: Machine Learning frameworks have alot of dependencies and can be hard to locally setup. To overcome this, all the functioning related to inference and learning will be done from the container.
  - **Datastore**: Making use of local filesystem to store the annotations. The annotations will have option to be exported into contemporary formats and then be saved on the local fs.
  - **Server**: To listen and respond to requests of react app, while also controling the above to components. 

Let's look at the components in more detail:

### React-based Frontend:

(Mockups of the proposed frontend)

![image-20200315162227548](image-20200315162227548.png)

![image-20200315162508401](image-20200315162508401.png)

(mockup for audio and video under process)

The project will come bundled together. The python server will come with a cli tool to startup all the necesarry. Currently the cli is planned to come with the following features:

```bash
# Registering a new dataset
$ project-redacted create --dataset <dataset_name> --data_directory <directory>
# Starting the processes
$ project-redacted start --config <config_file>
# Continue from previous work
$ project-redacted continue --config <config_file>
# Create a config file
$ project-redacted create_config 
```

A config file will be essential in providing information necessary for the functioning, a default config will look like:

```yaml
# config.yaml
init: False # flag to initialize new dataset repo
dataset_name: "default_dataset"

# data related options
data_directory: <current_directory>
annotation_directory: <current_directory>/annotations
export_format: "detectron2" # support for standard format from the industry

# Problem related options
problem_field: "computer-vision"
problem_sub_field: "classification"
classification_categories:
	- aeroplane
	- airport personnel
	- shuttle bus
	- luggage carrier

# Iterative Learning related options
train: "true"
training_approach: "iterative_learning" # ∈ ["iterative_learning", "multi_onevsall_classifiers"]
train_split: "0.1"  # At what proportions to retrain
train_framework: "sklearn" # ∈ ['sklearn', 'tensorflow/pytorch']
train_acc_threshold: 0.4 # Only serve suggestions if model is able to achive this accuracy 

# Miscellaneous options
user_name: "dumbmachine"
frontend_theme: "dark" # ∈ ['light', 'dark']
```

Using the config all the necassary variables will be initialized and allow for proper communitcation between frontend and backend.

Once started, the frontend will greet the user with types of annotations available unless stated in the `config_file` . After choosing the necessary task, the `react-app`will request data from `python-backend` which serve the request by fetching data from `data_directory` field in the `config_file`. Upon successful annotation of data, `react-app` will `post` the annotation metadata to `python-backend`and request for further data. This cycle will continue until `train_split` precentage of data points are not annotated.

(mockup, circular saving )

When `train_split` percent of data points have become annotated, `python-backend` will start learning annotations to provide _suggestions_. After training, the cycle of data annotation will change: when `react-app` asks for `data` for annotation it recieves `(data, prediction)` where `data` is the data requested and `prediction` is the suggestion. On each multiple of `train_split`, the model will train with the new data to update its knowledge of annotations and increase accuracy.

## Python-based Backend:

A `flask app` on the backend will be responsible for:

- serving requests of data of `react-app`.
- saving `annotations` in the required `export_format`.
- giving data to `docker container` for actively learning from annotations.



# Timeline

| Duration              | Task                                                         |
| --------------------- | ------------------------------------------------------------ |
| March 31              | **Deadline for submitting Project Proposal**                 |
| March 31 - April 27   | Application Review Period                                    |
| April 27 - May 18     | **Official Community Bonding Period**                        |
| May 18 - August       | **Official Coding Period Start**Finish implementation of pluginTest the plugin to some sample jobs on local backend server.Perform UI tests and fix bugs. |
| June 6 - June 11      | Time period for any unexpected delay.**Finish Task 1**       |
| June 11 - June 15     | **Phase 1 evaluation**Submit git repository of Code with documentation for Task 1 |
| June 15 - July 4      | **Begin Task 2 : Integrate plugin with HTCondor**Implement functionality for integrating HTCondor as backend.Test plugin for real batch jobs at CERN.Ask for feedbacks from the users and implement suggestions. |
| July 4 - July 9       | Time period for any unexpected delay.**Finish Task 2**       |
| July 9 - July 13      | **Phase 2 evaluation**Submit git repository of Code with documentation for Task 2 |
| July 13 - August 10   | **Begin Task 3 : Deploy plugin to CERN IT Infrastructure**Test plugin on CERN’s batch infrastructure.Integrate plugin to SWAN Notebook service.Ask feedback from the users and implement suggestions. |
| August 10 - August 10 | **Finish Task 3** **Final Submission**Submit git repository of final code with complete documentation. |



## Additional Information Regarding Timeline

- The timeline gives a rough idea of my planned project work. Best efforts will be made to follow the proposed schedule. I believe that I will be able to achieve all the milestones for this project, as it aligns with my interest and trying to do something innovative. 
- I’ve no other commitments during summer and hence, will be able to dedicate 48 hours to 60 hours a week. During the last month of the project, my college will begin and I’ll be denoting around 28-30 hours a week. `this might be for testing and polishing`.
- Each week, time will be divided (according to workload) amongst planning, learning, coding, documenting and testing features. Except for the developer’s guide, all documentation will go hand in hand with the development. This will help to keep a profound grasp over the code implementation and working, minimizing bugs in the later stages.
- Weekends will be mostly dedicated to testing, bug fixing, and blog writing. Fortnightly blogs will be maintained at https://medium.com/@ratin.kumar.2k and will include highlights of the development process and also methods used to overcome hurdles.
- I’m very enthusiastic about working on this project as it has been on my mind for a long time. It has potential to help in `thing of AI`. 

## Requirements

- **Remote High-Processing Server**: A machine capable of servicing gpu loads of contemporary machine learning tasks. Getting access to this would be appreciated but is not a necessity for successful execution of this project. 

## Contributions (till 26 March 2018)

- Swag lyrics
- Moving the site from thing to `fastpages` or anything else, that they would prefer.

### Deliverables

- A functional frontend.
- Fully modular and feature-rich backend which learns annotations while users perform actions.
- Simple pipeline for training `Classification` and `Object Detection`. Making the base for an extension to allow for training.
- Full test-suite of `unittests` and `integration`.
- Detailed documentation of the whole tool.
- Samples for using the tool.

## Working Environment And Schedule

I’ll be working full-time on the code on weekdays. On weekends, I’ll be focusing on documentation, testing and bug fixing. My awake hours would usually be in between 6:30 AM IST (1:00 AM UTC) to 2 AM IST the next day (8:30 PM UTC) and I’m comfortable working anytime during this period but I can easily tune my working hours if circumstances ask for it. Except for a few days of traveling (which I’ll be informing in advance to my mentor), I’ll be having no other absences. In case of emergencies, I'll be informing my mentor.

I'll be working from either my house or hostel, both the places have access to good internet. 

I’m very flexible with my schedule and already have the habit of working at night and hence timezone variation (with my mentor) won’t be an issue. I’m comfortable with any form of communication that suits my mentor.

## Future Prospects:

- Building a extension to this project to bring support for training models using standard or sota models.
- Build a complete pipeline to allow laymen to train machine learning models and then export in standard forms.
- I want to, through this project, provide the technical/non-technical audience a means to easily make datasets or train practical models on them.
- Add support for cloud backend to data source.
- Add support to allow usage cloud services as the processing backend.

![image-20200315092713162](image-20200315092713162.png)

# **References**:

This is a work in progress.