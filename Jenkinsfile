pipeline {
    agent any

    stages {
        stage('Install Python Tools') {
            steps {
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}
