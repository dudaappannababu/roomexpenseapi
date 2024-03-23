# To deploy FastApi refer to this link
https://www.koyeb.com/docs/deploy/fastapi

# Deploying FastAPI on GitHub using Koyeb

To deploy your FastAPI application on GitHub using Koyeb, you can follow these steps:

1. Sign up for a Koyeb account at [https://www.koyeb.com](https://www.koyeb.com) if you haven't already.

2. Create a new application on Koyeb by clicking on the "Create Application" button.

3. Choose the GitHub repository where your FastAPI code is located.

4. Configure the deployment settings, such as the branch to deploy, the build command, and the runtime environment.

5. Once the configuration is set, click on the "Deploy" button to start the deployment process.

6. Koyeb will automatically build and deploy your FastAPI application from your GitHub repository.

7. After the deployment is complete, you will receive a URL where your FastAPI application is accessible.

8. You can now access your FastAPI application by visiting the provided URL.

For more detailed instructions and information, you can refer to the [Koyeb documentation](https://www.koyeb.com/docs/deploy/fastapi).

# Creating a Virtual Environment
To create a virtual environment, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the root directory of your project.
3. Run the following command to create a virtual environment named "venv":

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

# Installing FastAPI
To install FastAPI and its dependencies, run the following command:
    Run the command `pip install fastapi "uvicorn[standard]"`
