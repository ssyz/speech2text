# Google Cloud AI: TEXT-TO-SPEECH

Artificial Intelligence (AI) and machine learning are some of the biggest buzz words in 21st century computing. Google's Cloud AI provides modern machine learning services, with pre-trained models and a service to generate your own tailored models. In this project, I integrate [CLOUD TEXT-TO-SPEECH](https://cloud.google.com/text-to-speech/) and present a trivial sample project. The idea is for you to utilize the abstracted code and make something cool! Definitely let me know if there is any additional functionality you would find useful.

It may be important to note that any meaningful project based on Cloud AI probably requires prior experience with Python or another coding language.

See all DIY Resources [here](https://emory.instructure.com/courses/48119/modules#module_80184).

## Prerequisites

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* Your choice of a Python IDE, I recommend [Atom](https://atom.io/)
* A [Google Cloud Account](https://console.cloud.google.com)

## Setup in 3 Steps

1. [Enable](https://console.cloud.google.com/flows/enableapi?apiid=texttospeech.googleapis.com) the Cloud Text-to-Speech API on your [console](https://console.cloud.google.com), making sure that [billing](https://cloud.google.com/billing/docs/how-to/modify-project) is enabled
2. Set up [authentication](https://console.cloud.google.com/apis/credentials/serviceaccountkey)
3. Intall and initialize the [Cloud SDK](https://cloud.google.com/sdk/docs/)



## Making the project work

One of the hardest parts of programming applications is getting various services to work together. In general, it is best practice to refer to the provided [documentation](https://cloud.google.com/text-to-speech/docs/). Below are a few critical components and examples. I will continue to add to this section as questions come up.

### Remember to set application credentials!

Verification and security is required by most API calls. For this project, before you run your code, you must set the environment variables in the terminal.

```
> set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\Jay\Documents\Emory\Fall Semester 2018\Appcology\GCP\GCP-1-02d8b5cb2fcd.json
```

### Call the API!

I've modified the original file to allow for easy calling of the API, this means you can ignore the behind the scenes code.

```
import speech2text as st
text = "Welcome to Appcology! I can't wait to see what you all create."
fileName = "hi.mp3"
st.outputSpeech(text, fileName)
```



## Deployment

To submit your completed project for a grade, please upload all code and output files as a ZIP onto Canvas.

## Authors

* **Jay Syz** - *Initial work* - [ssyz](https://github.com/ssyz)
* **Quickstart Guide** - *Reference* - [Google](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries#client-libraries-install-python)

