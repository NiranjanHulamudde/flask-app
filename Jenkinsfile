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
                
                withCredentials([usernamePassword(credentialsId: 'docker-pass',
                                                  usernameVariable: 'HUB_USER',
                                                  passwordVariable: 'HUB_PASS')]) {
                    
                    sh "echo \${HUB_PASS} | docker login -u \${HUB_USER} --password-stdin"
                    sh "docker push ${DOCKER_USER}/${DOCKER_IMAGE}:${IMAGE_TAG}"
                }
            }
        }

        stage('Infrastructure provisioning') {
            environment {
                AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
            }
            steps {
                dir('terraform') {
                    sh 'terraform init'
                    sh 'terraform apply --auto-approve'
                }
            }
        }
    } 
    
    post {
        success {
            echo "Image uploaded successfully"
        }
        failure {
            echo "failed to upload Image"
        }
    }
}
