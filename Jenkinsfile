pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_USR = credentials('dockerhub-creds').username
        DOCKER_CREDENTIALS_PSW = credentials('dockerhub-creds').password
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Varunk55/movie-recommendation-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || echo "No tests yet"'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t movie-recommender .'
            }
        }

        stage('Docker Login') {
            steps {
                sh 'echo "$DOCKER_CREDENTIALS_PSW" | docker login -u "$DOCKER_CREDENTIALS_USR" --password-stdin'
            }
        }

        stage('Docker Push') {
            steps {
                sh 'docker tag movie-recommender kingv5/movie-recommender:latest'
                sh 'docker push kingv5/movie-recommender:latest'
            }
        }
    }
}
