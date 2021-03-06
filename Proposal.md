# Project Redacted

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
| Institute | 2nd Year B.Tech Student<br>Computer Science and Engineering<br>National Institute of Technology Kurukshetra |
| Email     | [ratin.kumar.2k@gmail.com](mailto:ratin.kumar.2k@gmail.com)[ratin_11822004@nitkkr.ac.in](mailto:ratin_11822004@nitkkr.ac.in) |
| Phone     | +91-9896225424                                               |
| Blog      | [https://medium.com/@ratin.kumar.2k](https://medium.com/@ratin.kumar.2k) |
| Github    | [https://github.com/DumbMachine](https://github.com/DumbMachine) |
| Skype     | RatinKumar                                                   |
| IRC Nick  | DumbMachine (Freenode)                                       |
| Timezone  | Indian Standard Time (GMT +0530)                             |
| Address   | 208, Hostel-6, NIT campus<br>National Institute of Technology Kurukshetra<br>Kurukshetra, Haryana, India 136119 |
## About Me

I am Ratin Kumar, a 2nd year undergraduate Computer Engineering student at National Institute of Technology Kurukshetra. I have experience in programming with multiple languages such as Python, C/C++, Java, JavaScript, with Python being my favorite. My major interests lie in the field of machine learning. My most significant work to date is a machine learning algorithm that extracts key frames from long videos and uses object locations from each key frame as a means to search frames from database of videos. A research paper detailing the specifics of this approach will be released soon. _Project Autonate_ is a tool I have been working on which will provide the world with an open source solution that helps bring automation to the mundane task of data annotation by actively learning from annotated data.

Besides programming, road cycling and stalking stocks are the hobbies that tack up most of my time.Project `redacted`

### Preparation I have done:

- Completed the qualification task. I will help ccextractor migrate their wiki website to the desired platform.
- I have run extensive tests to help me understand the project better and determine best techniques to employ iterative/active learners to help manual annotators.

## Abstract

The field of Artificial Intelligence is helping advancement of many fields. AI is relevant to any intellectual task. Modern artificial intelligence techniques are pervasive and are too numerous to list here. Some of the prominent examples range from `something `autonomous vehicles to life saving by helping in medical diagnosis. Apart from the aforementioned serious, AI is used in entertainment industry whether it maybe using AI to create articles or create deepfakes. The world has also seen AI being used to detect the wrongs in our society, like fake news and also to detect the wrongs by AI itself (eg deepfakes).

At the heart of most AI solutions lies requirement of **labeled data**. The lack of  labeled data makes impossible for the algorithm to learn the regularities and patterns in data. Labeling data, manually, is cumbersome and time consuming. Datasets can be divided in two categories:

- Derivatives: These would be datasets, whose base or parent object (in the tree of object types) have already trained models. For example consider the dataset of `Ferarri Cars` , the parent object type `car` had already been trained in pre-trained models on ImageNet. These pre-trained models will help us to improve the quality of annotations.
- Non Derivatives: Datasets like images of`microchip`, have previously not been trained for and thus would require training from scratch. 

Project `redacted` aims at providing a platform to simplify and speedup the process of data labeling by making use of automation tools and pre-trained machine learning models. This project will provide a simple gui to users for annotating data required by various machine learning tasks (computer vision based, nlp based or audio based) and make use of pre-trained models and some techniques (mentioned in implementation details section)  to allow automation of annotation to as far extent as possible. The gui will be supported by a `python-backend` responsible for all preprocessing/recommendation for annotation and also storage of annotations received by the frontend.

## Background

CCExtractor, initially a small project, has now embedded itself firmly into large corporations and prestigious universities where it is used for many educational feats. This project will help fuel the fire of AI boom. It will introduce a tool to all the machine learning practitioners, which will allow them to annotate data a lot faster than before.

## Motivation

World of Artificial Intelligence has made big leaps in providing humans the power to find patterns in data. It will be the basis of most of the automation in the coming century, to keep this field expanding it requires data. Data, in its raw form, is available readily. This data accompanied with the right tool, which should focus on automatic and fast annotation, will improve efficiency of practitioners. Reduction of time spent annotating data implies increase in the time spent on finding solutions of real world problems.

## Project `redacted`

To accomplish this project's aims, a simple gui and a powerful backend which learns from past annotations are required. The gui will be simple and only expose those functions that are required and allow for usage of keyboard shortcuts to allow for reaching peak of efficiency of the manual annotators. The accompanying backend will actively learn from the annotations to suggest the annotations to users passively. This passive suggestion for manual annotators will mean no amount will be spend on annotation for correct suggestion and ignoring the incorrect suggestion, if wrong hence being a **passive suggestion**. Currently the benefits that will served from this project can be condensed to:

- Increase in speed and efficiency of manual annotators.
- Increase the amount of annotated data, as annotation tasks' difficulty and time investment decreases.

`redacted` will allow institutes, professional or any interested party to annotate data fast and easily, leaving the party with more time for implementation of solution.

## Detailed Working And Implementation

![image-20200315061224704](image-20200315061224704.png)

The project can be divided into the following components:

- **React based frontend**: The frontend webapp, will be the component most users see and use. 
- **Python based backend**: The server responsible for providing data to react app and taking annotation data from it. The iterative learning model, which will give real time suggestions of annotations, will also be backend's responsibility. To increase the modularity of backend's components, the following division is recommended:
  - **Docker Container**: Machine Learning frameworks have a lot of dependencies and can be hard to locally setup. To overcome this, all the functioning related to inference and learning will be done from the container.
  - **Datastore**: Making use of local file-system to store the annotations. The annotations will have option to be exported into contemporary formats and then be saved on the local fs.
  - **Server**: To listen and respond to requests of react app, while also controlling the above to components. 

Let's look at the components in more detail:

### React-based Frontend:

(Mockups of the proposed homepage)

![image-20200315162227548](image-20200315162227548.png)

![image-20200315162508401](image-20200315162508401.png)

(mockup for audio and video under process)

The project will come bundled together. The python server will come with a cli tool to startup all the necesarry. Starting all the necessary components will be as easy as:

```bash
# Registering a new dataset
$ project-redacted create --dataset <dataset_name> --data_directory <directory>
# Starting the server
$ project-redacted start --config <config_file>
```

A config file will be essential in providing information necessary for the functioning, a default config will look like:

```yaml
# config.yaml
version: 1 # tag to help in versioning of data

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

active_learner_params:
    train_size: "1000" # max samples from each class for training model
    train_split: "0.1"  # At what proportions of train_size to retrain
    augmentation: "True" # prevent overftting and increase robustness of model
    train_framework: "sklearn" # ∈ ['sklearn', 'tensorflow/pytorch']
    train_acc_threshold: 0.4 # Only serve suggestions if model is able to achive this accuracy 


# Miscellaneous options
user_name: "dumbmachine"
frontend_theme: "dark" # ∈ ['light', 'dark']
```

Using the config all the necessary variables will be initialized and allow for proper communication between frontend and backend.

Once started, the frontend will greet the user with types of annotations available unless stated in the `config_file` . After choosing the necessary task, the `react-app`will request data from `python-backend` which serve the request by fetching data from `data_directory` field in the `config_file`. Upon successful annotation of data, `react-app` will `post` the annotation metadata to `python-backend`and request for further data. This cycle will continue until `train_split` percentage of data points are not annotated.

(mockup, circular saving)

When `train_split` percent of data points have become annotated, `python-backend` will start learning annotations to provide _suggestions_. After training, the cycle of data annotation will change: when `react-app` asks for `data` for annotation it receives `(data, prediction)` where `data` is the data requested and `prediction` is the suggestion. On each multiple of `train_split`, the model will train with the new data to update its knowledge of annotations and increase accuracy.

The primary component will execute `fn` `getIniData()` when the component mounts 

```javascript
# home_component: Details left out to maintain brevity.
import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

class home_demo extends React.Component {
    # initially all state vars dummy
    state = {
        dataset_name: "default_dataset" # name of the current working dataset
        iter: 0, # index of data to be asked for 
        data: [], # data to be received from python-server for annotation
        annotations: "", # annotation of the above mentioned data
        suggestion: "" # suggestion for the data
    }

	componentDidMount(){
        axios.get(`<localhost>/dataset/${this.state.dataset_name}?id=${this.state.iter}`)
        	.then(res => {
            const data = res.data.data;
            const suggestion = res.data.suggestion;
            this.setState({data, suggestion});
        });
    }

	sendAnnotations(){
        axios.post(
        `<localhost>/dataset/${this.state.dataset_name}`,
        {iter, annotations})
            .then(res => console.log(res))
        	.catch(err => console.log(err))
    }
	......
    ......
}
```



## Python-based Backend:

I propose the following structure for python-related code:

```bash
# NOTE: Some details are left out to maintain brevity.
. <source_dir>
  |-react_app
  | |-public
  | |-src
  | | |-components
  | | | | App.js
  | | | | App.css
  |-python-server
  | |-server
  | | |-server.py
  | | |-server_utils.py
  | |-cli
  | | |-cli.py
  | | |-cli_utils.py      
  | |-active_learning
  | | |-server.py
  | | |-server_utils.py      
```

`Python` on the backend will be responsible for:

- `server`:  The module will be responsible for catering to the requests of `react-app` and calling the `active_learning` module for learning patterns from annotated data. Main responsibilities are:

  - serving requests of data of `react-app`.
  - saving `annotations` in the required `export_format`.
  - giving data to `docker container` for actively learning from annotations.

  

  ```python
  # flask_server: Details left out to maintain brevity.
  from ml_algorithms import suggestion
  
  # Register a new dataset        
  @app.route('/create', methods=['GET'])
  def register_dataset_handler():
      ....
  # Endpoint for `getting` data or `putting` annotations 
  @app.route('/dataset/<dataset_name>', methods=['GET', 'POST'])
  def annotation_handler():
      # react-app is asking for data
      if request.method == "GET": 
          return (dataset_generator(dataset_name, idx), suggestion(dataset_name, idx))
      # react-app is giving the annotation
     	else:
          idx = request.form.get('iter')
          annotation = request.form.get('annotation')
          save_annotation(
              dataset_name.
              annotation, idx
          )
          
  def train_model(...):
  ```

  

- `cli_tools`: This module will implement the `cli` for starting and controlling the service.

  ```bash
  # cli will support the following functions:
  
  # Registering a new dataset
  $ project-redacted create --dataset <dataset_name> --data_directory <directory>
  # Starting the processes
  $ project-redacted start --config <config_file>
  # Continue from previous work
  $ project-redacted continue --config <config_file>
  # Create a config file
  $ project-redacted create_config 
  ```

- `active_learning`: This module holds the responsibilities of training a model in the background to produce confident suggestions for annotations on new data. Following methods will be employed for learning:

  - Algorithmic: These do not employ machine learning based solutions. Making use of general algorithms, that are many times used in conjunction with ml techniques. Further details are provided below, where I mention in details about the techniques for each individual  task of annotations.
  - Machine Learning: These employ machine learning solutions to directly learn trends in data or by using representations of data to learn trends.

Currently the following are tasks that support iterative or active learning:

###    Computer Vision Tasks:

- **Image Classification**:  Two methods will supported for actively learning annotations:

  1. *Simple classifier (or simple classifier on top of pre-trained model):* Here a model will be trained in background on each iteration where number of samples for each class reaches a multiple of `train_split`threshold. Even distribution inhibits the suggestion model from overfitting or biasing. Advantages of this approach are better suggestion and lighter on resource usage. But disdvantages of this approach is :

     - Only trains model when each category has enough samples, this might not happend uniformly in real world cases.
     - Dataset might have a skewed distribution.

     These issues can be tackled by intensive augmentation to try and balance class distributions or allow user to submit a model for usage in *iterative learning*. This might have the benefit of prior knowledge if user has a model catering to the dataset. 

     A sample for this model can be found in [this notebook](https://www.kaggle.com/ratinkumar/poc-iteration/edit). Where a model is trained in iterations of 100 samples per class for a total of 5 cycles. This implies that model was trained only on 3000(6 classes x 500 images each) images out of 25k images,

     ![img](Sun, 15 Mar 2020 212901.png)

     (There is a spelling mistake on this graph)

  2. *OneVsAllClassifier*:  `n` models will be trained, where `n` corresponds to the number of classes in the classification problem. This will require more resources for inference and training but has the advantage of allowing support for skewed classes.

     (I will link the poc here)

- Object Detection: 

  - Making use of pre-trained models to train on subset of data for which annotations become available. The benefit of using a pre-trained model can be seen with the below examples:

    Note: The below images are result of training tensorflow object detection api using mobilenet on only a set of 20 images, for reference look at [this notebooks](https://colab.research.google.com/drive/15xa-RS3jerXLB3Yw223woppIYN9epO-4#scrollTo=SFQYOYMFmm1n)

    First image displays that models help reduce the total number of annotations to be manually done.

    ![image](76706748-fd4be000-670f-11ea-9f63-fa809cf3427b.png)

    Second image displays that even if suggested annotation is wrong, the model correctly drew the bounding box. Weak Object Detectors will help get boundaries and once Object Detectors get trained with enough data they start suggestion correct boundaries and annotations.

    ![image](76706755-089f0b80-6710-11ea-9d0b-970d16c71fa1.png)

  - Instance Segmentation and Key Points: These will also take an approach similar to above, i.e they will make use of iterative: training on pre-trained models. 

    - The user will also have a choice to use a custom tool which can isolate object using their colors. This tools converts the image colors to `HSV` and tries to isolate specific colors by setting `low,high` ranges.

      ![image-20200316000953611](image-20200316000953611.png)

    For reference : https://colab.research.google.com/drive/1wDoeNGxZOI0Q0YlhFVTe0pI8hi7TuWc9

###    Natural Language Processing:

- Full Support:

  - NER, Classification, Sentiment Analysis: Two option will available to the user, initially: either make use of tfidf transformers and learn occurrences of works. Or make use of `word2vec` or `bert` to get representations of words and treat it like a normal classification problem.

    By making use of tfidf vectors, a model can learn what category of words are more probable of occurring as a particular category in NERs. An example showcasing a method of using TFIDF counts to find important annotations from each type, can be found here : https://github.com/DumbMachine/POC/blob/master/src/text/NER/Untitled.ipynb

    ![img](Tue, 17 Mar 2020 143028.png)

    For datasets that require more contextual approach in finding appropriate suggestions, a `word2vec` model will be used to obtain a `vector` representation of each word. The vectors. learnt from large corpus of data, have repsentations of words to understand relationships. 
    
    
    
    ![img](download-1584437543542.jpeg)
    
    For classification and sentiment analysis, users will have two options at their disposal:
    
    - Sklearn-based Solution: This will employ the, resource friendly, 
    
      ```python
      # The arguments for significant functions can be passed via config.yaml
      vec_tdidf = TfidfVectorizer(**args)
      clf = XGBClassifier(**args)
      
      # Training on the documents where:
      #  - X_train: Are feature vectors of each document using TfidfVectorizer.
      # - Y_train: Label for documents.
      clf.fit(X_train, y_train)
      ```
    
    - Deep Learning-based Solution: Using `word2vec` representation to generate vectors for documents and use them for classification.
    
    (I will update the POC for this soon)

- Partial Support:

  - Paraphrase detection and other similar tasks: Weak suggestions can be made in other nlp task by learning trends of occurrences of words in data. But these 	may not offer any real world advantage. This is still under testing

###    Audio Tasks:

- Classification, Segmentation and Tagging: By either making use of pre-trained vectors to obtain vectors from irregular length audio clips for use as features for regression models or generating own features by analyzing the audio wave histogram.

  Using the python library `librosa`, we obtain [Mel-frequency cepstrum](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum) features of each audio clip. The following code snippet will display the method:

  ```python
  #returns mfcc features with mean and standard deviation along time
  def get_mfcc(path):
      b, _ = librosa.core.load(path, sr = SAMPLE_RATE)
      assert _ == SAMPLE_RATE
      try:
          ft1 = librosa.feature.mfcc(b, sr = SAMPLE_RATE, n_mfcc=20)
          ft2 = librosa.feature.zero_crossing_rate(b)[0]
          ft3 = librosa.feature.spectral_rolloff(b)[0]
          ft4 = librosa.feature.spectral_centroid(b)[0]
          ft5 = librosa.feature.spectral_contrast(b)[0]
          ft6 = librosa.feature.spectral_bandwidth(b)[0]
          ft1_trunc = np.hstack((np.mean(ft1, axis=1), np.std(ft1, axis=1), skew(ft1, axis = 1), np.max(ft1, axis = 1), np.min(ft1, axis = 1)))
          ft2_trunc = np.hstack((np.mean(ft2), np.std(ft2), skew(ft2), np.max(ft2), np.min(ft2)))
          ft3_trunc = np.hstack((np.mean(ft3), np.std(ft3), skew(ft3), np.max(ft3), np.min(ft3)))
          ft4_trunc = np.hstack((np.mean(ft4), np.std(ft4), skew(ft4), np.max(ft4), np.min(ft4)))
          ft5_trunc = np.hstack((np.mean(ft5), np.std(ft5), skew(ft5), np.max(ft5), np.min(ft5)))
          ft6_trunc = np.hstack((np.mean(ft6), np.std(ft6), skew(ft6), np.max(ft6), np.m(ft6)))
          return pd.Series(np.hstack((ft1_trunc, ft2_trunc, ft3_trunc, ft4_trunc, ft5_trunc, ft6_trunc)))
      except:
          logging.error(f'bad file {path}')
          return pd.Series([0]*125)
  ```

  This will generate features for all the audio clips. Example is following 

  | Id   | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | ...  | 117  | 118  | 119  | 120  | 121  | 122  | 123  | 124  | path         | label        |
  | ---- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :----------- | ------------ |
  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 00044347.wav | Hi-hat       |
  | 1    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 001ca53d.wav | Saxophone    |
  | 2    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 002d256b.wav | Trumpet      |
  | 3    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0033e230.wav | Glockenspiel |
  | 4    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 00353774.wav | Cello        |

  We combine the `mfcc`  features with another feature generator which analyses the distributions among each audio sample

  ```python
  def extract_features(files, path):
      features = {}
  
      cnt = 0
      for f in tqdm(files):
          features[f] = {}
  
          fs, data = scipy.io.wavfile.read(os.path.join(path, f))
  
          abs_data = np.abs(data)
          diff_data = np.diff(data)
  
          def calc_part_features(data, n=2, prefix=''):
              f_i = 1
              for i in range(0, len(data), len(data)//n):
                  features[f]['{}mean_{}_{}'.format(prefix, f_i, n)] = np.mean(data[i:i + len(data)//n])
                  features[f]['{}std_{}_{}'.format(prefix, f_i, n)] = np.std(data[i:i + len(data)//n])
                  features[f]['{}min_{}_{}'.format(prefix, f_i, n)] = np.min(data[i:i + len(data)//n])
                  features[f]['{}max_{}_{}'.format(prefix, f_i, n)] = np.max(data[i:i + len(data)//n])
  
          features[f]['len'] = len(data)
          if features[f]['len'] > 0:
              n = 1
              calc_part_features(data, n=n)
              calc_part_features(abs_data, n=n, prefix='abs_')
              calc_part_features(diff_data, n=n, prefix='diff_')
  
              n = 2
              calc_part_features(data, n=n)
              calc_part_features(abs_data, n=n, prefix='abs_')
              calc_part_features(diff_data, n=n, prefix='diff_')
  
              n = 3
              calc_part_features(data, n=n)
              calc_part_features(abs_data, n=n, prefix='abs_')
              calc_part_features(diff_data, n=n, prefix='diff_')
  
  
          cnt += 1
  
          # if cnt >= 1000:
          #     break
  
      features = pd.DataFrame(features).T.reset_index()
      features.rename(columns={'index': 'fname'}, inplace=True)
      
      return features
  ```

  This will generate robust features for each audio sample:

  | Id   | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | ...  | max_1_3 | mean_1_1  | mean_1_2  | mean_1_3  | min_1_1  | min_1_2 | min_1_3 | std_1_1     | std_1_2     | std_1_3     | label        |
  | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :------ | :-------- | :-------- | :-------- | :------- | :------ | :------ | :---------- | :---------- | ----------- | ------------ |
  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 97.0    | -0.931367 | -0.838818 | -0.757430 | -18601.0 | -221.0  | -126.0  | 1206.881456 | 28.793127   | 14.249761   | Hi-hat       |
  | 1    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 15701.0 | -0.495702 | -0.327620 | -0.344328 | -12593.0 | -9359.0 | -7484.0 | 3196.572491 | 2866.174942 | 2887.041732 | Saxophone    |
  | 2    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 35.0    | -1.156308 | -1.077098 | -1.173006 | -636.0   | -53.0   | -33.0   | 65.608624   | 13.855835   | 13.421382   | Trumpet      |
  | 3    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 4.0     | -0.817937 | -0.637596 | -0.496497 | -8345.0  | -25.0   | -5.0    | 259.141991  | 4.846361    | 1.041946    | Glockenspiel |
  | 4    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 0    | ...  | 5157.0  | -0.038102 | 22.482221 | 38.551893 | -12829.0 | -8860.0 | -5577.0 | 3005.821294 | 1701.234020 | 905.514833  | Cello        |

  Now these features will be used to train a classifier. Depending upon the resources available to user and size of dataset, one of the two methods will be employed for learning annotations:

  - Tree based Classifier: Making use of robust tree classifiers such as `LightGBM` or `XGBoost` imply that we can train on data fast.
  - Deep Learning based Classifier: Making use of Neural Networks to learn on annotated data. This would require more

- Refer to this document (will be updated soon) for a demo showing the accuracy of a tree classifer on audio data. 

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

      - QnA datasets

      - Machine Translation

      - Sentiment Analysis 

      - Custom tasks ( like transliteration )

   3. Audio based datasets for:

      - Audio Transcription
      - Audio Segmentation
      - Audio Classification
2. A robust backend which will take care of:

   - Sending data for annotation to frontend.
   - Saving annotations received from frontend.
   - Export annotations to formats allowing for direct ingestion.
   - An active learning model, which will improve with each annotation and also provide suggestions for annotations.
   - Maintain metrics to log the statistics of resources used and latency of requests served.
3. Full test-suite of `unittests` and `integration`.
4. Detailed documentation; for users as well as developers.
5. Fortnightly blogs on developmental advances and milestones. 
6. Simple pipeline for training to allow users to train standard models with the data annotated by them. Possible integration with CCExtractor's project Rekognition.

#### Major Dependencies

- **ReactJs**
- **Sklearn**
- **Tensorflow**/**Pytorch**
- **Docker**
- **Flask**
- **Travis** **CI**

#  Timeline

| Duration              | Task                                                         |
| --------------------- | :----------------------------------------------------------- |
| March 31              | **Deadline for submitting Project Proposal**                 |
| March 31 - April 27   | **Application Review Period**                                |
| April 27 - May 18     | **Official Community Bonding Period**                        |
| May 18 - June 12      | **Official Coding Period Start** <br>**Begin Task 1:**<br>Finish implementation of `react-app` and a simple data loading `python-server`. <br>Test `react-app` on samples using local backend server.<br>Perform UI tests and fix bugs. |
| June 12 - June 15     | Time period for any unexpected delay.<br>**Finish Task 1**   |
| June 15 - June 19     | **Phase 1 evaluation**<br>Submit git repository of Code with documentation for Task 1 |
| June 19 - July 10     | **Begin Task 2 : Implement Active Learning**<br/>Implement functionality for integrating active/iterative learning and dataloaders<br>Ask for feedbacks from the users and implement suggestions. |
| July 10 - July 13     | Time period for any unexpected delay.<br/>**Finish Task 2**  |
| July 13 - July 17     | **Phase 2 evaluation**<br/>Submit git repository of Code with documentation for Task 2 |
| July 17 - August 7    | **Begin Task 3 : Complete Integration**<br/>Complete the integration of `react-app` and `python-server`.<br>Implement basic pipeline to allows users to train on data using standard models.<br>Ask feedback from the users and implement suggestions. |
| August 7 - August 10  | **Phase 3 evaluation**<br/>Submit git repository of Code with documentation for Task 3 |
| August 10 - August 17 | **Finish Task 3** **Final Submission<br/>**Submit git repository of final code with complete documentation. |

## Additional Information Regarding Timeline

- The timeline gives a rough idea of my planned project work. Best efforts will be made to follow the proposed schedule. I believe that I will be able to achieve all the milestones for this as it aligns with my interest and trying to do something innovative. 
- I’ve no other commitments during summer and hence, will be able to dedicate 48 hours to 60 hours a week. During the last month of the project, my college will begin and I’ll be denoting around 28-30 hours a week.
- Each week, time will be divided for implementation of features and documentation of these features. All the features and documentation will be written simultaneously (in the same week). I would like to spend weekdays on implementation and use weekends for testing, writing documentation and researching about the next weeks implementation.
- Weekends will be mostly dedicated to testing, bug fixing, and blog writing. Fortnightly blogs will be maintained at https://medium.com/@ratin.kumar.2k and will include highlights of the development process and also methods used to overcome hurdles.

## Requirements

- **Remote High-Processing Server**: A machine capable of servicing gpu loads of contemporary machine learning tasks. Getting access to this would be appreciated but is not a necessity for successful execution of this project. 

## Previous Contributions

- [Swag lyrics](https://github.com/SwagLyrics/autosynch/issues/30#issuecomment-592868099)
- Generating script to help migration of CCExtractor wiki page to `fastpages`. Link to [repo](https://github.com/DumbMachine/migrate-ccextractor), link to wip [hosted site]([https://dumbmachine.github.io/ccextractor-wiki-test/_pages/Gsoc%20start%20here.html](https://dumbmachine.github.io/ccextractor-wiki-test/_pages/Gsoc start here.html)). If, in future, a decision is made to not choose `fastpages` but any other framework, I'll be willing to work on it.

## Working Environment And Schedule

I’ll be working full-time on the code on weekdays. On weekends, I’ll be focusing on documentation, testing and bug fixing. My awake hours would usually be in between 6:30 AM IST (1:00 AM UTC) to 2 AM IST the next day (8:30 PM UTC) and I’m comfortable working anytime during this period but I can easily tune my working hours if circumstances ask for it. Except for a few days of traveling (which I’ll be informing in advance to my mentor), I’ll be having no other absences. In case of emergencies, I'll be informing my mentor.

I'll be working from either my house or hostel, both the places have access to good internet. 

I’m very flexible with my schedule and timezone variation (with my mentor) won’t be an issue. I’m comfortable with any form of communication that suits my mentor.

## Future Prospects:

- Building a extension to this project to bring support for training models using state of the art models.
- Build a complete pipeline to allow laymen to train machine learning models and then export in standard forms.
- Add support for cloud backend to data source.
- Add support to allow usage cloud services as the processing backend.c

![image-20200315092713162](image-20200315092713162.png)

(this chart needs updation to slow preprocessors and dataloaders)

# **References**:

This is a work in progress.