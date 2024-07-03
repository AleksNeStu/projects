---
source: https://medium.com/thelorry-product-tech-data/aws-lambda-fastapi-ci-cd-pipeline-with-github-actions-c414866b2d48

created: 2024-07-03T15:09:44 (UTC +02:00)

tags: []

author: Azzan Amin

---
# AWS Lambda + FastAPI (Serverless Deployment): Complete CI/CD Pipeline Using GitHub Actions | TheLorry Data, Tech & Product | TheLorry Data, Tech & Product
---
[

![Azzan Amin](https://miro.medium.com/v2/resize:fill:88:88/1*NArVUZMGHGHZHayN8CAA5A.jpeg)



](https://medium.com/@ibnuamin97?source=post_page-----c414866b2d48--------------------------------)[

![TheLorry Data, Tech & Product](https://miro.medium.com/v2/resize:fill:48:48/1*CSMcx6ufOb6fm35GAD-iLQ.jpeg)



](https://medium.com/thelorry-product-tech-data?source=post_page-----c414866b2d48--------------------------------)

_Let’s build a complete CI/CD workflow using GitHub Actions, FastAPI, AWS Lambda (Serverless Deployment) and AWS S3._

![](https://miro.medium.com/v2/resize:fit:689/0*GUsTjzpO_0AHSxm9)

Photo by [Manasvita S](https://unsplash.com/@manasvita?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Are you burdened with mundane boring and repetitive tasks that delays bringing your magical software product to production? As software/devops engineers focused on bringing our code to life, we all face the same problems where we need to perform tasks that are boring, repetitive and sometimes a total waste of time. For instance, one of them is the process of running the unit tests on various environments and then deploying our software to various delivery platform. The processes takes longer than they should and surely makes our day at work inefficient and unproductive. Have you ever wondered:

-   How can I automate all these boring repetitive testing and deployment processes?
-   Do we have any kind of method that could solve these problems?

Don't worry you’re not alone.

> I thought about it all the time, till I realized that there is a simple solution to these problems. It is an amazing method in software development world called **Continuous Integration and Continuous Deployment(CI/CD).**

CI/CD is one of the best practices in software development as it reduces the repetitive process of unit testing and the deployment of the software.

This practice undeniably will help the developers in efficiently automating all the steps required for running the automated tests on the server. Plus, it can continuously deploy the application to the deployment platform once it has passed the automated tests. And yes, it is fully automated.

The good news is, all of these processes can be achieved by using a new feature on **Github** called **GitHub Actions!**

In this article, we’ll demonstrate you a simple walkthrough on building a complete CI/CD workflow of FastAPI using GitHub Actions and we’ll deploy the API to AWS Lambda.

Let’s Dive in!

## **Table of Contents:**

1.  Create a GitHub Repository
2.  Clone your repository to local machine
3.  Setup Virtual Environment
4.  Install the Required Dependencies
5.  Run the API in Local Machine
6.  Run Unit Test in Local Machine
7.  Update requirements.txt
8.  Create GitHub Actions Workflow Directory
9.  The Components of GitHub Actions
10.  Continuous Integration (CI): Build Automated Test
11.  Configuring GitHub Secrets, Amazon S3 and AWS Lambda
12.  Continuous Deployment (CD): Deploy Lambda
13.  Running the GitHub workflow

## 1\. Create a GitHub Repository

Create a new repository in GitHub for the project.

![](https://miro.medium.com/v2/resize:fit:689/1*wIcdHlhuz4A3OPbOrRmj0A.png)

Setup repository in GitHub

In this part, assign a relevant repository name and you’ll also need to add a `.gitignore` file. You can select the `.gitignore` template and since we are using Python (FastAPI), go ahead select the Python `.gitignore` template.

## 2\. Clone your repository to your local machine

In order to clone the your repository, you’ll need to have the link of your GitHub repository.

![](https://miro.medium.com/v2/resize:fit:689/1*ow07rBWi7q8-Zb9usOwTdg.png)

Clone GitHub Repository

From your repository page on GitHub, click the green button labeled **Code**, and in the “Clone with HTTPs” section, copy the URL for your repository. Once you have copied the link, you can now clone the project to your local machine.

Open your bash shell and you can change your current working directory to the location that you want to clone your repository. To clone your repository is simple, you can use:

```
<span id="b606" data-selectable-paragraph="">git clone <a href="https://github.com/URL-TO-REPO-HERE" rel="noopener ugc nofollow" target="_blank">https://github.com/URL-TO-REPO-HERE</a></span>
```

Nice! you have successfully cloned your github repository.

## 3\. Setup Virtual Environment

To follow these steps below, you are required to install Python in your machine. If you do not have it install yet, please check this out: [Python 3 Installation & Setup Guide — Real Python](https://realpython.com/installing-python/)

Once you have Python 3 installed, create a virtual environment inside your local project directory. Open a terminal on your local machine and run the following commands:

1.  **Install the virtualenv package**

You can install the package by using pip.

```
<span id="08e7" data-selectable-paragraph="">pip install virtualenv</span>
```

**2\. Create the virtual environment**

To create a virtual environment, you must specify a path for that. For example to create one in the local directory called `venv`, type the following:

```
<span id="c31f" data-selectable-paragraph="">virtualenv venv</span>
```

**3\. Activate the virtual environment**

You can activate the python virtualenv by running the following command:

-   Mac OS / Linux

```
<span id="b829" data-selectable-paragraph="">source venv/bin/activate</span>
```

-   Windows

```
<span id="f905" data-selectable-paragraph="">venv\Scripts\activate</span>
```

## 4\. Install the Required Dependencies

If you want to follow along the walkthrough, [this GitHub repository](https://github.com/azzan-amin-97/aws-serverless-fastapi-cicd-pipeline) contains the code for this project. Please feel free to use and follow the codes there.

To install all the libraries for the project, make sure you are in the root of the project and run the following command:

```
<span id="2ff7" data-selectable-paragraph="">pip<em> </em>install -r requirements.txt</span>
```

## 5\. Run the API in Local Machine

The sample project we created in this walkthrough tutorial is based on FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. If, you’re interested in learning more about this cool framework, you can read [this](https://medium.com/@tiangolo/introducing-fastapi-fdc1206d453f) article written by its awesome author, [Sebastián Ramírez](https://medium.com/u/963974981597?source=post_page-----c414866b2d48--------------------------------). Take it from us, FastAPI 🤩 is the most efficient way of creating api’s in python.

In order to run the FastAPI app, we can use Uvicorn ASGI server to start the app in our terminal. If you downloaded or cloned the code [from GitHub](https://github.com/azzan-amin-97/aws-serverless-fastapi-cicd-pipeline) (as mentioned in Point 4), you can follow the commands below.

Alright, let’s change our current working directory to `app` folder. Then, start our uvicorn server (hypercorn is another alternative):

```
<span id="d706" data-selectable-paragraph="">cd app &amp;&amp; uvicorn main:app --reload</span>
```

Once we run it, we should be able to access the Swagger UI in our browser. Visit the link:

```
<span id="dfe0" data-selectable-paragraph=""><a href="http://localhost:8000/docs" rel="noopener ugc nofollow" target="_blank">http://localhost:8000/docs</a></span>
```

![](https://miro.medium.com/v2/resize:fit:689/1*8E7-IeVRN3IFF4qUi4vOzQ.png)

Simple FastAPI app CI/CD workflow using GitHub Actions

## 6\. Run Unit Tests in Local Machine

In the project, we have few unit tests that will check the endpoints whether they are working fine or not. The unit tests file is inside `app/tests` folder named `test_main.py`. To know more about why unit tests are important and how to write them, you may follow our other article [here](https://medium.com/thelorry-product-tech-data/unit-testing-and-continues-integration-ci-in-github-action-for-python-programming-c8ad57fae3a1).

```
<span id="7adc" data-selectable-paragraph="">from fastapi.testclient import TestClient<br>from main import app</span><span id="24fe" data-selectable-paragraph="">client = TestClient(app)<br></span><span id="9bef" data-selectable-paragraph="">def test_main_resource():<br>    response_auth = client.get("/")<br>    assert response_auth.status_code == 200<br></span><span id="7a88" data-selectable-paragraph="">def test_child_resource():<br>    response_auth = client.get("/api/v1/test")<br>    assert response_auth.status_code == 200</span>
```

To run the unit tests, open the terminal and type:

```
<span id="8da0" data-selectable-paragraph="">pytest</span>
```

Output in console:

![](https://miro.medium.com/v2/resize:fit:689/1*mJBVFpqx8UdASyEnfJixsg.png)

Great, we have passed all the unit tests! Please note that the Pytest library is required to run the test.

## 7\. Update requirements.txt

Incase if you have installed any new libraries or packages to the project, its a good practice to update your requirements.txt by typing the following _freeze_ command:

```
<span id="e720" data-selectable-paragraph="">pip freeze &gt; requirements.txt</span>
```

This is just to ensure we have the latest updated packages inside our `requirements.txt` file so that we can avoid complications when running the projects on the server or any other machine.

## 8\. Create GitHub Actions Workflow Directory

To create the CI/CD workflow in GitHub Actions, we need to create a .yml file in our repository. From our application root, create a folder named `.github/workflows` that will contain the GitHub action workflows.

Then, create `main.yml` (just an example, we can put any name that you like for the .yml file) inside the created folder as this file will contain all the instructions for our automated tests and deployment process to AWS Lambda through our code on GitHub repository. You can use the code below in the terminal as the guide to achieve this process.

```
<span id="cb55" data-selectable-paragraph="">cd path/to/root_repo<br>mkdir .github/workflows<br>touch .github/workflows/main.yml</span>
```

Cool! Now we have the directory for GitHub Actions workflow.

## 9\. Understanding the GitHub Actions Workflow

There are six main components in GitHub Actions:

-   **Workflow** — The automated procedure that we add to our repository and can be triggered or scheduled by an event.
-   **Events** — It is a specific activity that will trigger a workflow. For example, an event triggers when someone pushes a commit to a repository or a pull request is created.
-   **Jobs** —Series of steps that execute on the same runner. It can run parallelly or sequentially depends on our workflow objectives.
-   **Steps** — It is an individual task that will run commands in a job.
-   **Actions** — An action is a set of standalone commands that gets executed on the runner and it is combined into steps to create a job.
-   **Runners** — A server that hosted virtual operating systems by GitHub or your own (self-hosted) that can run commands to perform a build process. Hosted runners by GitHub are based on Microsoft Windows, Ubuntu Linux and macOS.

The workflow that we are going to build will consist of **two main jobs**:

-   **Continuous Integration (CI)**

The CI will run the automated test, package our FastAPI into Lambda and upload the lambda artifact in the GitHub server in order to enable the other jobs (in our case, the Continuous Deployment Job) to use it.

-   **Continuous Deployment (CD)**

This job will only be executed when the CI job is successfully completed. CD job needs to be dependent on the status of the CI build job in order to make sure that we can only deploy the application once we have passed the CI part. Basically, this job will download the lambda artifact that has been uploaded during the CI job and deploy it to AWS Lambda by linking it with AWS S3.

So our workflow will look like this in the .yml file.

```
<span id="a589" data-selectable-paragraph="">name: CI/CD Pipeline<br><br>on:<br>  push:<br>    branches: [ main ]<br>jobs:<br><br>  continuous-integration:<br>  ....<br>  <br>  continuous-deployment:<br>  .....</span>
```

For the detailing part of the steps and commands inside each job, please stay along with me okay!

Alright, let’s get our hands dirty by creating the workflow using GitHub Actions.

## 10\. Continuous Integration (CI): Build Automated Test and Package Lambda

Here is the complete CI workflow in our main.yml file.

```
<span id="4fad" data-selectable-paragraph="">name: CI/CD Pipeline<br><br>on:<br>  push:<br>    branches: [ main ]<br><br><br>jobs:<br><br>  continuous-integration:<br>    runs-on: ubuntu-latest<br><br>    steps:</span><span id="39a1" data-selectable-paragraph="">      # Step 1      <br>      - uses: actions/checkout@v2<br>      <br>      # Step 2<br>      - name: Set up Python <br>        uses: actions/setup-python@v2<br>        with:<br>          python-version: 3.7<br>          architecture: x64<br>      # Step 3<br>      - name: Install Python Virtual ENV<br>        run: pip3 install virtualenv<br>      # Step 4<br>      - name:  Setup Virtual env<br>        uses: actions/cache@v2<br>        id: cache-venv<br>        with:<br>          path: venv<br>          key: ${{ runner.os }}-venv-${{ hashFiles('**/requirements*.txt') }}<br>          restore-keys: |<br>            ${{ runner.os }}-venv-<br>      # Step 5<br>      - name: Activate and Install Depencies into Virtual env<br>        run: python -m venv venv &amp;&amp; source venv/bin/activate &amp;&amp;<br>          pip3 install -r requirements.txt<br>        if: steps.cache-venv.outputs.cache-hit != 'true'</span><span id="e2c0" data-selectable-paragraph="">      # Step 6     <br>      - name: Activate venv and Run Test        <br>        run: . venv/bin/activate &amp;&amp; pytest<br>      <br>      # Step 7<br>      - name: Create Zipfile archive of Dependencies<br>        run: |<br>          cd ./venv/lib/python3.7/site-packages<br>          zip -r9 ../../../../api.zip .<br>      <br>      # Step 8<br>      - name: Add App to Zip file<br>        run: cd ./app &amp;&amp; zip -g ../api.zip -r .<br>      <br>      # Step 9<br>      - name: Upload zip file artifact<br>        uses: actions/upload-artifact@v2<br>        with:<br>          name: api<br>          path: api.zip</span>
```

Let us break it down and have a look at each part of the workflow:

-   The name assigned to this workflow is `CI/CD Pipeline`
-   The workflow will be triggered when commit codes pushed to the `main` branch in the repository.
-   The job defined in this workflow is `continuous-integration`.
-   The runner used in the workflow is `ubuntu-latest` (Ubuntu Linux Operating Systems)

These are the sequential series of steps defined in the CI workflow:

-   **Step 1:** Perform `actions/checkout@v2` that will checkout to our repository and downloads it to the runner.
-   **Step 2:** Setup python 3.7 by using actions - `actions/setup-python@v2`
-   **Step 3:** Install Python Virtual Environment (`virtualenv`) package
-   **Step 4:** Caching Dependencies using `actions/cache@v2`. This step will increase the performance of the project workflow that consists of many large dependencies by efficiently reduce the time required for downloading. For further explanation, please read the [GitHub Actions Documentations](https://docs.github.com/en/free-pro-team@latest/actions/guides/building-and-testing-python).
-   **Step 5:** Activate the virtualenv and install all the dependencies that consist inside`requirements.txt`
-   **Step 6:** Run Unit Tests. By the way, we need to activate again the virtualenv before running the test as GitHub Actions doesn’t preserve the environment.
-   **Step 7:** Package our Lambda by zipping all the dependencies in the `venv` site-packages and place it in our root directory. The zip file is named `api.zip`
-   **Step 8:** Add the contents of our app folder into `api.zip`
-   **Step 9:** Upload the `api.zip` to GitHub server as an artifact using `actions/upload-artifact@v2` . This will enable the next job to retrieve back the artifact file for the deployment of our lambda package which is our `api.zip` file.

Phew! We have completed our CI workflow using GitHub Actions. Let’s make some minor changes in our code and try to push our code to the main branch. Make sure you’re using the CI code above in the `main.yml` file to test the CI workflow. This is how the result will look like when we have trigger the workflow by our code push event.

![](https://miro.medium.com/v2/resize:fit:689/1*FbCskgfNsNMUSysOyq9JUQ.png)

CI workflow GitHub Actions Result

You will see this output by going inside the Actions tab in your repository.

![](https://miro.medium.com/v2/resize:fit:689/1*CGLi5mJC0J2Rh7RKEXzpMQ.png)

GitHub Actions Tab

> Continous Integration (CI) Done! ✔️

Let’s quickly move onto the Continuous Deployment part now. We are almost there!

## 11\. Configuring GitHub Secrets, Amazon S3 and AWS Lambda

Before we create the CD workflow for our project, **FIVE** things that need to be done:

-   Add GitHub Secrets
-   Create S3 Bucket
-   Create a Lambda Function
-   Implement Mangum Handler
-   Update Lambda handler

1.  **Add GitHub Secrets**

GitHub Secrets is used to store confidential information. In our case, we need to store our AWS\_SECRET\_ACCESS\_KEY\_ID, AWS\_SECRET\_ACCESS\_KEY, and AWS\_DEFAULT\_REGION.

To add the secrets, click on Settings from the repository page, then select secrets from the left menu-list. We will see a button named New Repository Secrets on the top right and click on that Button. This is the example output in GitHub after we have added the secrets.

![](https://miro.medium.com/v2/resize:fit:689/1*C96HGpXPg25AOgXpAZ_DTw.png)

GitHub Secrets

After we have added the secrets in our GitHub repository, we can now use the secrets variable in our `main.yml` workflow file.

**2\. Create Amazon S3 Bucket**

Go to AWS Management Console and log in using our AWS Account. Then, proceed to Amazon S3 in the console and Click on **Create bucket.**

![](https://miro.medium.com/v2/resize:fit:689/1*YpLOVy6YFelTGi7FEWdzmg.png)

AWS S3

Just give the bucket any name and click on **Create bucket.** The diagram below shows how to create the S3 bucket:

Done, you have successfully created the S3 bucket. Let’s create our Lambda function then.

**3\. Create a Lambda Function**

Go to AWS Management Console and log in using our AWS Account. Then, proceed to AWS Lambda in the console and click on the **Create function.**

![](https://miro.medium.com/v2/resize:fit:689/1*3OvPuQd2znMjr2Srpup2HQ.png)

AWS Lambda

Then, choose **author from scratch**, select **python 3.7** as runtime. You will need to **choose or create an execution role** before creating the function. Once it is done, click on the **Create function.**

**4\. Implement Mangum Handler**

In order to enable our FastAPI to be deployed as a Lambda function in AWS, we will need to use the [Mangum](https://pypi.org/project/mangum/) library to wrap our API. Why we need Mangum? It is because:

-   Mangum will manage the responses back from the Lambda function to the API Gateway and it acts as an adapter to handle the API Gateway routes requests to our Lambda function.

To apply Mangum in our code, we just need to add the following code:

```
<span id="6e9a" data-selectable-paragraph="">from mangum import Mangum<br>...<br>handler = Mangum(app=app)</span>
```

In our `main.py` , this is how we implement the Mangum which is the Amazon lambda handler:

```
<span id="a633" data-selectable-paragraph="">from fastapi import FastAPI<br>from mangum import Mangum  # &lt;---------- import Mangum library<br><br>from api.v1.api import router as api_router<br><br>app = FastAPI(title='Serverless Lambda FastAPI')<br><br>app.include_router(api_router, prefix="/api/v1")<br><br><br>@app.get("/",  tags=["Endpoint Test"])<br>def main_endpoint_test():<br>    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}<br><br>handler = Mangum(app=app) # &lt;----------- wrap the API with Mangum</span>
```

**5\. Update Lambda Handler**

For this part, we need to update the lambda handler in AWS Lambda **Runtime settings.**

By default we will see the handler is set to `lambda_function.lambda_handler` and we need to update this handler value to match with our FastAPI handler.

![](https://miro.medium.com/v2/resize:fit:689/1*wpyJh6CH-8QZWHo5eEOSgw.png)

AWS Lambda Runtime Settings

Under **Runtime Settings** click on **Edit**. Then, update the handler to `main.handler` (it means that we retrieve the `handler` variable which is the Mangum handler inside `main.py`)

![](https://miro.medium.com/v2/resize:fit:689/1*5YvCY7oydHn3yQeIkp_kwg.png)

Update Lambda handler

## 12\. Continuous Deployment (CD): Deploy Lambda

Let’s continue with our GitHub Actions workflow. So, here is the complete CD workflow in our `main.yml` file.

```
<span id="c5a8" data-selectable-paragraph="">...</span><span id="1d69" data-selectable-paragraph="">continuous-deployment:<br>  runs-on: ubuntu-latest<br>  needs: [continuous-integration]<br>  if: github.ref == 'refs/heads/main'<br>  steps:</span><span id="61c2" data-selectable-paragraph="">    # Step 1<br>    - name: Install AWS CLI<br>      uses: unfor19/install-aws-cli-action@v1<br>      with:<br>        version: 1<br>      env:<br>        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}<br>        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}<br>        AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}</span><span id="7add" data-selectable-paragraph="">    # Step 2<br>    - name: Download Lambda api.zip<br>      uses: actions/download-artifact@v2<br>      with:<br>        name: api</span><span id="1c3e" data-selectable-paragraph=""># Step 3<br>    - name: Upload to S3<br>      run: aws s3 cp api.zip s3://&lt;YOUR_S3_BUCKET_NAME&gt;/api.zip<br>      env:<br>        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}<br>        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}<br>        AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}</span><span id="79c2" data-selectable-paragraph=""># Step 4<br>    - name: Deploy new Lambda<br>      run: aws lambda update-function-code --function-name &lt;YOUR_LAMBDA_FUNCTION_NAME&gt; --s3-bucket &lt;YOUR_S3_BUCKET_NAME&gt; --s3-key api.zip<br>      env:<br>        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}<br>        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}<br>        AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}</span>
```

Here is the explanation:

-   The job defined in this workflow is `continuous-deployment`.
-   The runner used in the workflow is `ubuntu-latest` (Ubuntu Linux Operating Systems)
-   This job will only run when the `continuous-integration` build is succeeded. This process can be achieved by using the command `needs:[continuous-integration]` after the runner has been defined.
-   Check if current branch is `main` by using the command `if: github.ref == ‘refs/heads/main’`

These are the sequential series of steps defined in the CD workflow:

-   **Step 1:** Install AWS CLI in the runner using `unfor19/install-aws-cli-action@v1`
-   **Step 2:** Download `api.zip` artifact from GitHub server using `actions/download-artifact@v2` . The artifact name defines in this step must the same as the name used during the step of uploading the artifact. In our case, the artifact name is `api`
-   **Step 3:** Upload `api.zip` to our Amazon S3 bucket name that we have defined.
-   **Step 4:** Deploy the `api.zip` as uploaded in S3 to our AWS Lambda function name that we have defined.

P/s: For each of the steps that use AWS CLI, we need to include the environment variables of AWS secret keys inside it. The AWS secret keys will be the GitHub Secrets that we store earlier. This is how it can be done in GitHub Actions .yml file:

```
<span id="658d" data-selectable-paragraph="">env:<br>        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}<br>        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}<br>        AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}</span>
```

So, this is how the build succeeded result will look like for the CD workflow when we have triggered it by any push event.

![](https://miro.medium.com/v2/resize:fit:689/1*IJEpEgkC2rzk7OGeKyWM3A.png)

CD workflow GitHub Actions

> Continuous Deployment (CD) workflow is done! ✔️

## 13\. Running the GitHub Actions CI/CD workflow

Here is the complete CI/CD workflow in our `main.yml` file:

```
<span id="b061" data-selectable-paragraph="">name: CI/CD Pipeline<br><br>on:<br>  push:<br>    branches: [ main ]<br><br><br>jobs:<br><br>  continuous-integration:<br>    runs-on: ubuntu-latest<br><br>    steps:<br>      - uses: actions/checkout@v2<br><br>      - name: Set up Python all python version<br>        uses: actions/setup-python@v2<br>        with:<br>          python-version: 3.7<br>          architecture: x64<br><br>      - name: Install Python Virtual ENV<br>        run: pip3 install virtualenv<br><br>      - name:  Setup Virtual env<br>        uses: actions/cache@v2<br>        id: cache-venv<br>        with:<br>          path: venv<br>          key: ${{ runner.os }}-venv-${{ hashFiles('**/requirements*.txt') }}<br>          restore-keys: |<br>            ${{ runner.os }}-venv-<br><br>      - name: Activate and Install Depencies into Virtual env<br>        run: python -m venv venv &amp;&amp; source venv/bin/activate &amp;&amp;<br>          pip3 install -r requirements.txt<br>        if: steps.cache-venv.outputs.cache-hit != 'true'<br><br><br>      <em># Install all the app dependencies<br>      </em>- name: Install dependencies<br>        run: pip3 install -r requirements.txt<br><br><br>      <em># Build the app and run tests<br>      </em>- name: Build and Run Test<br>        run: . venv/bin/activate &amp;&amp; pytest<br><br>      - name: Create Zipfile archive of Dependencies<br>        run: |<br>          cd ./venv/lib/python3.7/site-packages<br>          zip -r9 ../../../../api.zip .<br><br>      - name: Add App to Zipfile<br>        run: cd ./app &amp;&amp; zip -g ../api.zip -r .<br><br>      - name: Upload zip file artifact<br>        uses: actions/upload-artifact@v2<br>        with:<br>          name: api<br>          path: api.zip<br><br><br>  continuous-deployment:<br>    runs-on: ubuntu-latest<br>    needs: [continuous-integration]<br>    if: github.ref == 'refs/heads/main'<br>    steps:<br><br>      - name: Install AWS CLI<br>        uses: unfor19/install-aws-cli-action@v1<br>        with:<br>          version: 1<br>        env:<br>          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}<br>          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}<br>          AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}<br><br>      - name: Download Lambda api.zip<br>        uses: actions/download-artifact@v2<br>        with:<br>          name: api<br><br>      - name: Upload to S3<br>        run: aws s3 cp api.zip s3://&lt;YOUR_S3_BUCKET_NAME&gt;/api.zip<br>        env:<br>          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}<br>          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}<br>          AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}<br><br>      - name: Deploy new Lambda<br>        run: aws lambda update-function-code --function-name &lt;YOUR_LAMBDA_FUNCTION_NAME&gt; --s3-bucket &lt;YOUR_S3_BUCKET_NAME&gt; --s3-key api.zip<br>        env:<br>          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}<br>          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}<br>          AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}</span>
```

Now, let’s push some changes to our main branch to see the result of our CI/CD workflow in GitHub Actions. We should see something like this in our GitHub Actions for the latest build workflow result.

![](https://miro.medium.com/v2/resize:fit:689/1*z_xz2XaM38svgev8Dtp3NQ.png)

CI/CD Detailed Build Succeeded

Awesome! All jobs succeeded. All jobs succeeded. This means we have completed the full workflow of our CI/CD Pipeline for FastAPI to AWS Lambda.

This is extremely powerful. We can now deploy our API, bug fixes and any new feature requests to production in minutes rather than days, without any human dependency. Congratulations!

## Summary

Implementing a CI/CD Pipeline in our API development projects is incredibly powerful. IT helps us increase our productivity and confidence without having to spend a lot of time handling the tasks and commands to run these mundane processes manually.

In this article, we discussed the complete CI/CD workflow starting from creating a GitHub Repository until building a complete CI/CD workflow using GitHub Actions. Along the way, we also learned about running ASGI APIs, performing unit tests in our local machine, packaging our FastAPI to Lambda using Mangum, and configuring AWS Lambda and AWS S3 Services for our deployment.

We hope this article will help you build your own customized CI/CD Pipelines for your own awesome FastAPI projects.

Peace! ✌️
