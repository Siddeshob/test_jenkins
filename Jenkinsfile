pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                echo "cloning repo....."
                checkout scm
            }
        }

        stage('Setup'){
            steps{
                echo 'installing dependancies....'
                sh'''
                python3 -m venv myenv
                . myenv/bin/activate
                pip install -r requirements.txt
                 '''
            }
        }

        stage('Test'){
            steps{
                echo 'Running test....'
                sh""" 
                . myenv/bin/activate
                python3 -m pytest --html=report.html
                """
            }
        }
    }
    post{
        success{
            echo 'build success'
        }
        failure{
            echo 'build failed'
        }
    }
}