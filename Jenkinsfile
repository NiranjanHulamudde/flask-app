pipeline {
    agent any

    environment {
        DOCKER_USER  = 'niranjanhulamudde'
        DOCKER_IMAGE = 'flask-app'
        IMAGE_TAG    = 'latest'
    }

    stages {
        stage('Code checking') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Installing dependencies and running unit tests...'
                // Run pytest using Python. If a test fails, the pipeline stops immediately.
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest test_app.py
                '''
            }
        }
        
        stage('Building the image') {
            steps {
                sh "docker build -t ${DOCKER_USER}/${DOCKER_IMAGE}:${IMAGE_TAG} ." 
            }
        }
        stage('Pushing the image to dockerhub') {
            steps {
                withCredentials([(usernamePassword(credentialsId: 'docker-pass',
                                                  usernameVariable: '$DOCKER_USER',
                                                  passwordVariable: '$DOCKER_PASSWORD'  ))])  {
                    echo "docker \${DOCKER_PASSWORD} | docker login -u \${DOCKER_USER} --password-stdin"
                    sh "docker push ${DOCKER_USER}/${DOCKER_IMAGE}:${IMAGE_TAG}"
                }
        }
        }
    }
    post {
        success {
            echo "Image uploaded successfully"
        }
        failure {
            echo "failed to uploade Image"
        }
    }
}
