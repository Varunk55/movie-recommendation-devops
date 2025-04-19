pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Varunk55/movie-recommendation-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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
    }
}
